from .nasa_info_handler import getNasaInfo

nasaInfo = getNasaInfo()


def getApodEndpointParams(hd, date='empty'):
    """Get query APOD NASA endpoint query paramas

    Args:
        hd (String): True of False in order to get hd picture url

    Returns:
        Dict: endpoint query params
    """
    # https://api.nasa.gov/planetary/apod?hd=True&api_key=Z02aer...

    params = dict()

    if date != 'empty':
        params['date'] = date

    params['hd'] = hd
    params['api_key'] = nasaInfo['nasa_api_key']

    return params
