from tweetapodbot.twitter.twitter_upload_handler import getTwitterApi
from tweetapodbot.twitter.twitter_upload_handler import tweetImage
from tweetapodbot.twitter.twitter_upload_handler import responseToTweet
from tweetapodbot.twitter.twitter_upload_handler import getExplanationChunkSize
from tweetapodbot.twitter.twitter_upload_handler import chunkString
from tweepy import TweepError

TEST_FILE_ABSOLUTE_PATH = '<YOUR_PATH>'
EXPLANATION = str(
        'How long would it take to drive to the Sun? Brittany age 7, and D.J. age 12,'
        'ponder this question over dinner one evening. James also age 7, suggests taking a really fast'
        'racing car while Christopher age 4, eagerly agrees. Jerry, a really old guy who is used to estimating'
        'driving time on family trips based on distance divided by speed, offers to do the numbers.'
        )


def testAuthentication():
    api = getTwitterApi()

    isOk = None
    try:
        api.verify_credentials()
        isOk = True
    except TweepError as ex:
        isOk = False
        print(ex)

    assert isOk


def testTweetImage():
    tweetId = None
    try:
        tweetId = tweetImage(TEST_FILE_ABSOLUTE_PATH, 'Hello world!' + "\U00002604")  # 1310736058162782210 id de este tweet
        print(f'mediaId is: {tweetId}')
    except TweepError as ex:
        print('error: ', ex)

    assert tweetId is not None


def testResponseToTweet():
    isOk = None
    try:
        responseToTweet('1311440718058131457', 'hello 3')
        isOk = True
    except TweepError as ex:
        isOk = False
        print('error: ', ex)

    assert isOk


def testGetExplanationChunkSize():
    chunkSize = getExplanationChunkSize(EXPLANATION)

    print('chunk size: ', chunkSize)

    assert chunkSize is not None


def testSplitExplanation():
    chunks = list(chunkString(EXPLANATION, 180))

    print('expla chunks: ', len(chunks))

    assert chunks is not None
