NASA_API_KEY = '<YOUR_NASA_API_KEY>'
NASA_BASIC_DOMAIN = 'https://api.nasa.gov'


def getNasaInfo():
    nasaInfo = dict()
    nasaInfo['nasa_api_key'] = NASA_API_KEY
    nasaInfo['nasa_apod_api_uri'] = NASA_BASIC_DOMAIN + '/planetary/apod'

    return nasaInfo
