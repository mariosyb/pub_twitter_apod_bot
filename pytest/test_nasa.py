from tweetapodbot.app import HttpMethods
from tweetapodbot.nasa.nasa_info_handler import getNasaInfo
from tweetapodbot.http.http_request_handler import makeApiCall
from tweetapodbot.nasa.nasa_param_handler import getApodEndpointParams
from tweetapodbot.nasa.nasa_response_handler import getImageCopyright
from tweetapodbot.nasa.nasa_response_handler import getImageExplanation
from tweetapodbot.nasa.nasa_response_handler import getImageTitle
from tweetapodbot.nasa.nasa_response_handler import validateMedia
from tweetapodbot.nasa.nasa_response_handler import NasaMediaType
from tweetapodbot.nasa.nasa_response_handler import subtractDaysFromCurrentDate


def testNasaApodApiCall():
    response = callNasaApi()
    assert response['status_code'] == 200


def testGetImageCopyright():
    copyright = getImageCopyright(callNasaApi())

    print(f'copyrisht is: {copyright}')

    assert copyright is not None


def testGetImageExplanation():
    explanation = getImageExplanation(callNasaApi())

    print(f'explanation is: {explanation}')

    assert explanation is not None


def testGetImageTitle():
    title = getImageTitle(callNasaApi())

    print(f'title is: {title}')

    assert title is not None


def testValidateMediaInResponse():
    mediaType = NasaMediaType.image.value

    isOkMedia = validateMedia(mediaType, callNasaApi())

    print(f'is media of type {mediaType} ?', isOkMedia)

    assert isOkMedia


def testDaysSubtraction():
    date = subtractDaysFromCurrentDate(1)

    print(f'subtracted date: {date}')

    assert date is not None


def callNasaApi():
    nasaInfo = getNasaInfo()
    url = nasaInfo['nasa_apod_api_uri']
    params = getApodEndpointParams('True')
    response = makeApiCall(url, params, HttpMethods.get.value)

    return response
