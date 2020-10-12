import random
from .http.http_request_handler import HttpMethods
from .http.http_request_handler import makeApiCall
from .http.http_request_handler import printApiResponse

from .nasa.nasa_info_handler import getNasaInfo
from .nasa.nasa_param_handler import getApodEndpointParams
from .nasa.nasa_emoji_handler import getSpaceEmojis
from .nasa.nasa_response_handler import validateMedia
from .nasa.nasa_response_handler import NasaMediaType
from .nasa.nasa_response_handler import subtractDaysFromCurrentDate
from .nasa.nasa_response_handler import getImageUrl
from .nasa.nasa_response_handler import getImageTitle
from .nasa.nasa_response_handler import getImageExplanation
from .nasa.nasa_response_handler import getImageCopyright

from .media.media_handler import downloadImage
from .media.media_handler import existFile
from .media.media_handler import deleteImage

from .twitter.twitter_upload_handler import tweetImage
from .twitter.twitter_upload_handler import getExplanationChunkSize
from .twitter.twitter_upload_handler import chunkString
from .twitter.twitter_upload_handler import responseToTweet


nasaInfo = getNasaInfo()
spaceEmojis = getSpaceEmojis()


def run():
    print('Starting Job...')

    print('STEP 1 - Calling NASA API')

    nasaApiResponse = callNasaApi()
    printApiResponse(nasaApiResponse)

    isData = validateData(nasaApiResponse)

    if not isData:
        nasaApiResponse = callNasaApiUntilImageIsReturned()

    print('validating NASA mediatype.')
    isImage = validateMedia(NasaMediaType.image.value, nasaApiResponse)

    print(f'is media from NASA an image?: {isImage}')

    if not isImage:
        nasaApiResponse = callNasaApiUntilImageIsReturned()

    print('STEP 2 - Donwload photo')

    nasaImageUrl = getImageUrl(nasaApiResponse)

    imageLocalPath = downloadImage(nasaImageUrl)

    print('validating download...')

    if not existFile(imageLocalPath):
        print('ERROR - photo was not downloaded, ending process.')
        return

    print('download validation successful')
    print('STEP 3 - Tweet Image')

    imageTitle = getImageTitle(nasaApiResponse)
    titleEmoji = random.choice(list(spaceEmojis.values()))  # getting random emoji
    mainTweetId = tweetImage(imageLocalPath, titleEmoji + ' ' + imageTitle)

    print('STEP 4 - Add Tweet Explanation and CopyRight')

    nasaExplanation = getImageExplanation(nasaApiResponse)

    lastTweetId = tweetExplanation(mainTweetId, nasaExplanation)

    copyright = getImageCopyright(nasaApiResponse)
    if copyright != 'public domain':
        print('adding copyright...')
        responseToTweet(lastTweetId, 'Copyright: ' + copyright)

    print('STEP 5 - Delete Photo')

    deleteImage(imageLocalPath)

    print('Job Finished.')


def validateData(response):
    """validates that NASA API response returned data

    Args:
        response (Dict): custom response from API

    Returns:
        Boolean: True is data was returned False otherwise
    """
    """ this is NASA's service response when they have no data for the day {
    "code": 404,
    "msg": "No data available for date: 2020-10-04",
    "service_version": "v1"
    } """

    NO_DATA_MSG = 'No data available for date'
    MSG_RESPONSE_PARAMETER = 'msg'

    if MSG_RESPONSE_PARAMETER in response['response_data_raw']:
        msg = response['response_data_raw']['msg']

        if response['status_code'] == 404 and NO_DATA_MSG in msg:
            return False
    else:
        if response['status_code'] == 200:
            return True


def tweetExplanation(mainTweetId, explanation):
    """response to the original image tweet with its explanation

    Args:
        mainTweetId (String): tweet id of the image main tweet
        explanation (String): explanation text

    Returns:
        String: last tweet id of the created twitter thread
    """
    chukSize = getExplanationChunkSize(explanation)

    print(f'chunk size is:{chukSize}')

    print('starting response secuence')
    tweetId = mainTweetId
    for chunk in chunkString(explanation, chukSize):  # iterating generator
        tweetId = responseToTweet(tweetId, chunk)

    print('explanation tweets finished')
    # tweetId del ultimo twwt creado en el thread de twitter
    return tweetId


def callNasaApiUntilImageIsReturned():
    """calls NASA API until image is returned, subtracting N(random) days from today each
    iteration

    Returns:
        Dict: custom response from NASA's API
    """

    print('first NASA call did not return an image, looking for image...')

    response = None
    count = random.randint(60, 100)  # una imagen de minimo 2 meses atras(60 dias)

    while True:
        date = subtractDaysFromCurrentDate(count)
        response = callNasaApi(date)

        isMediaOk = validateMedia(NasaMediaType.image.value, response)

        if isMediaOk:
            break

        count += 1

    print('image finded, printing response...')
    printApiResponse(response)

    print('image search is finished.')
    return response


def callNasaApi(date='empty'):
    """calls NASA APIS

    Args:
        date (str, optional): date for nasa APOD API. Defaults to 'empty'.

    Returns:
        Dict: custom API response
    """
    print('calling nasa APOD API...')
    url = nasaInfo['nasa_apod_api_uri']

    if date != 'empty':
        params = getApodEndpointParams('True', date)
    else:
        params = getApodEndpointParams('True')

    response = makeApiCall(url, params, HttpMethods.get.value)

    return response
