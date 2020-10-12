import tweepy
import math
from .twitter_info_handler import getTwitterInfo

TW_INFO = getTwitterInfo()


def getTwitterApi():
    """autenticates to twitter API

    Returns:
        API: tweepy API object
    """
    access_token = TW_INFO['twitter_access_token']
    access_token_secret = TW_INFO['twitter_access_secret_token']
    consumer_key = TW_INFO['twitter_api_key']
    consumer_secret = TW_INFO['twitter_api_secret_key']

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def tweetImage(pathToFile, message):
    """create a tweet with image

    Args:
        pathToFile (String): path to photo
        message (String): text of the tweet

    Returns:
        String: tweet id
    """
    api = getTwitterApi()

    print('uploading photo...')
    # responseStatusObj = api.update_with_media(pathToFile, status=message)  # tweepy.models.Status
    responseObj = api.media_upload(pathToFile)  # subiendo foto twitter
    print('photo uploaded.')

    mediaId = responseObj.media_id

    media_ids = []
    media_ids.append(mediaId)
    tweetId = tweetMedia(message, media_ids, api)

    return tweetId


def tweetMedia(message, mediaIds, api):
    """creates a tweet with previously uploaded media using the mediaId

    Args:
        message (String): tweet text
        mediaIds (List): list of media ids for the tweet
        api (API Tweetpy Object): twitter api object with authentication

    Returns:
        String: created tweetId
    """

    print('tweeting media...')
    responseStatusObj = api.update_status(status=message, media_ids=mediaIds)
    print('media tweeted.')

    tweetId = responseStatusObj.id_str

    return tweetId


def responseToTweet(tweetId, message):
    """response to a existing tweet

    Args:
        tweetId (String): id of target tweet
        message (String): content of the response tweet
    Returns:
        String: id of the tweetcreated as response
    """
    print('authenticating to twitter...')
    api = getTwitterApi()

    print('tweeting response.')
    responseStatusObj = api.update_status(message, tweetId)
    print('response created.')

    tweetId = responseStatusObj.id_str
    return tweetId


def getExplanationChunkSize(explanation):
    """returns the chunk size for this explanation String

    Args:
        explanation (String): NASA explanation from API

    Returns:
        int: chunks size
    """
    explanationLength = len(explanation)

    print(f'explanation total length is: {explanationLength}')

    chunkSize = None
    if explanationLength > 280:
        # obtengo el total de chunks que haran falta
        totalChunks = math.ceil(explanationLength / 280)  # redondea el sesultado a entero superior, ej: 4,5 a 5
        # obtengo cuantos caracteres necesito por chunk
        chunkSize = math.floor(explanationLength / totalChunks)
    else:
        chunkSize = explanationLength

    return chunkSize


def chunkString(string, length):
    """This function returns a generator, using a generator comprehension.
        The generator returns the string sliced, from 0 + a multiple of the length of the chunks,
        to the length of the chunks + a multiple of the length of the chunks.

    Args:
        string (String): string to be splitted
        length (int): chunk size

    Returns:
        Generator: generator with chunks
    """
    return (string[0+i:length+i] for i in range(0, len(string), length))
