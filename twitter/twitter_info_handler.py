# keys
TWITTER_API_KEY = '<YOUR_API_KEY>'
TWITTER_API_SECRET_KEY = '<YOUR_API_SECRET_KEY>'
TWITTER_ACCESS_TOKEN = '<YOUR_ACCESS_TOKEN>'
TWITTER_ACCESS_SECRET_TOKEN = '<YOUR_ACCESS_SECRET_TOKEN>'
# uris
TWITTER_UPDATE_BASE_URI = 'https://api.twitter.com/1.1/statuses/update.json'
TWITTER_UPLOAD_BASE_URI = 'https://upload.twitter.com/1.1/media/upload.json'


def getTwitterInfo():
    twitterInfo = dict()
    twitterInfo['twitter_api_key'] = TWITTER_API_KEY
    twitterInfo['twitter_api_secret_key'] = TWITTER_API_SECRET_KEY
    twitterInfo['twitter_access_token'] = TWITTER_ACCESS_TOKEN
    twitterInfo['twitter_access_secret_token'] = TWITTER_ACCESS_SECRET_TOKEN
    twitterInfo['twitter_update_base_uri'] = TWITTER_UPDATE_BASE_URI
    twitterInfo['twitter_upload_base_uri'] = TWITTER_UPLOAD_BASE_URI

    return twitterInfo
