from tweetapodbot.app import HttpMethods
from tweetapodbot.http.http_request_handler import makeApiCall
from tweetapodbot.nasa.nasa_info_handler import getNasaInfo
from tweetapodbot.nasa.nasa_param_handler import getApodEndpointParams
from tweetapodbot.media.media_handler import getMediaType
from tweetapodbot.media.media_handler import downloadImage
from tweetapodbot.media.media_handler import deleteImage
from tweetapodbot.media.media_handler import existFile
from tweetapodbot.media.media_handler import splitImage
from tweetapodbot.media.media_handler import getMimeType
from tweetapodbot.media.media_handler import getTotalBytes

TEST_FILE_ABSOLUTE_PATH = '<YOUR_PATH>'


def testGetTotalSize():
    size = getTotalBytes(TEST_FILE_ABSOLUTE_PATH)

    print(f'size: "{size}"')

    assert size is not None


def testGetMimeType():
    mime = getMimeType(TEST_FILE_ABSOLUTE_PATH)

    print(mime)

    assert mime is not None


def testGetMediaType():
    response = callNasaApi()
    mediaType = getMediaType(response)

    assert mediaType == 'image' or mediaType == 'video'


def testDownloadImage():
    url = 'https://apod.nasa.gov/apod/image/2008/CygnusVeil_Symon_2000.jpg'
    localImagePath = downloadImage(url)

    assert existFile(localImagePath)


def testDeleteImage():
    pathToFile = TEST_FILE_ABSOLUTE_PATH
    deleteImage(pathToFile)

    assert not existFile(pathToFile)


def testSplitImage():
    pathToFile = TEST_FILE_ABSOLUTE_PATH
    splitImage(pathToFile, '.jpg')

    assert 1 == 1


def callNasaApi():
    nasaInfo = getNasaInfo()
    url = nasaInfo['nasa_apod_api_uri']
    params = getApodEndpointParams('True')
    response = makeApiCall(url, params, HttpMethods.get.value)

    return response
