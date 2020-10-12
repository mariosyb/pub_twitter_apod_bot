import os
import requests
import tempfile
import pathlib
import mimetypes


NASA_IMAGES_TMP_DIR = 'nasa_images'


def getMimeType(pathToFile):
    """returns mime type

    Args:
        pathToFile (String): absolute path

    Returns:
        String: mime type
    """
    mime = mimetypes.guess_type(pathToFile, strict=True)

    return mime[0]


def getTotalBytes(pathToFile):
    """returns file size in bytes

    Args:
        pathToFile (String): path absolute path

    Returns:
        [int]: size in bytes
    """
    return os.path.getsize(pathToFile)


def getMediaType(nasaApiResponse):
    mediaType = nasaApiResponse['response_data_raw']['media_type']

    return mediaType


def deleteImage(imageAbsolutePath):
    pathlib.Path(imageAbsolutePath).unlink()


def downloadImage(url):
    """downloads nasa photo from url

    Args:
        url (String): photo url

    Returns:
        String: local path where the photo was downloaded
    """
    print(f'starting image download form: "{url}"')

    imageName = url.rsplit('/', 1)[1]
    localImageAbsolutePath = getDownloadTempDirectory() + os.path.sep + imageName

    createDirectory(getDownloadTempDirectory())

    print(f'image name is: "{imageName}"')
    print(f'image local path is: "{localImageAbsolutePath}"')

    print('downloading image...')
    imageBinaryData = requests.get(url)
    with open(localImageAbsolutePath, 'wb') as f:
        f.write(imageBinaryData.content)

    print('download finished')
    return localImageAbsolutePath


def splitImage(imageAbsolutePath, extension):
    """split the image in chunks

    Args:
        imageAbsolutePath (String): absolute path to image
        extension (String): extension for chunks
    """
    CHUNK_SIZE = 500000  # 1/2 mb
    file_number = 1
    pathWithoutBasename = os.path.dirname(imageAbsolutePath)

    with open(imageAbsolutePath, 'rb') as infile:
        while True:
            # Read 500000byte chunks of the image
            chunk = infile.read(CHUNK_SIZE)
            if not chunk:
                break

            # Do what you want with each chunk
            with open(pathWithoutBasename + os.path.sep + 'image_part_' + str(file_number) +
                      extension, 'wb+') as chunk_file:
                chunk_file.write(chunk)
                chunk_file.close()

            file_number += 1


def getDownloadTempDirectory():
    return tempfile.gettempdir() + os.path.sep + NASA_IMAGES_TMP_DIR


def existFile(filePath):
    return os.path.exists(filePath)


def createDirectory(directoryPath):
    pathlib.Path(directoryPath).mkdir(parents=True, exist_ok=True)
