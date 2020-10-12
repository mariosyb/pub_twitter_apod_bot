import enum
from datetime import date, timedelta

COPYRIGHT_PARAMETER = 'copyright'  # this will be in response if the image is not public domain
TITLE_PARAMETER = 'title'
EXPLANATION_PARAMETER = 'explanation'
MEDIA_TYPE_PARAMETER = 'media_type'
HD_URL_PARAMETER = 'hdurl'
DATE_FORMAT = '%Y-%m-%d'


class NasaMediaType(enum.Enum):
    image = 'IMAGE'
    video = 'VIDEO'


def getImageUrl(response):
    """gets photo url

    Args:
        response (Dict): Custom response from NASA APOD API

    Returns:
        String: image url
    """
    url = response['response_data_raw'][HD_URL_PARAMETER]

    return url


def getImageExplanation(response):
    """gets photo explanation

    Args:
        response (Dict): Custom response from NASA APOD API

    Returns:
        String: image explanation
    """
    explanation = response['response_data_raw'][EXPLANATION_PARAMETER]

    return explanation


def getImageTitle(response):
    """gets image title

    Args:
        response (Dict): Custom response from NASA APOD API

    Returns:
        String: image title
    """
    return response['response_data_raw'][TITLE_PARAMETER]


def getImageCopyright(response):
    """checks if the image has copyright or not

    Args:
        response (Dict): Custom response from NASA APOD API

    Returns:
        String: copyright value or 'public domain' if the image has no copyright
    """
    copyright = None

    if COPYRIGHT_PARAMETER in response['response_data_raw']:
        copyright = response['response_data_raw'][COPYRIGHT_PARAMETER]
    else:
        copyright = 'public domain'

    return copyright


def validateMedia(mediaType, response):
    """validates media type os NASA response

    Args:
        mediaType (NasaMediaType): desire media type from enum
        response (Dict): cusntom service response

    Returns:
        Boolean: True if media type in resonse is the same passed as argument False otherwise
    """
    isMediaType = None
    responseMediaType = response['response_data_raw'][MEDIA_TYPE_PARAMETER]

    if 'IMAGE' == mediaType:
        isMediaType = NasaMediaType.image.value == responseMediaType.upper()
    elif 'VIDEO' == mediaType:
        isMediaType = NasaMediaType.video.value == responseMediaType.upper()
    else:
        print(f'ERROR: not supported media type: {mediaType}')
        return

    return isMediaType


def subtractDaysFromCurrentDate(days):
    """subtracts a quantity of days from today's date

    Args:
        days (integer): number of days to subtract

    Returns:
        String: formatted YYYY-MM-DD substracted date
    """
    today = date.today()

    subtractedDate = today - timedelta(days=days)

    strFormattedDate = subtractedDate.strftime(DATE_FORMAT)

    return strFormattedDate
