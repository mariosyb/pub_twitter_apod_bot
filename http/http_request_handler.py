import requests
import json
import enum


class HttpMethods(enum.Enum):
    get = 'GET'
    post = 'POST'


def makeApiCall(url, params, method):
    """make simple Http  call

    Args:
        url (String): api url
        params (Dict): api query params
        method (String): http method

    Returns:
        Dict: custom response of api call
    """
    if 'GET' == method:
        data = requests.get(url, params)
    elif 'POST' == method:
        data = requests.post(url, params)
    else:
        print(f'ERROR: not supported method: {method}')
        return

    custonResponse = getCustomResponse(data, url, params)

    return custonResponse


def printApiResponse(custonResponse):
    """Print custom api response

    Args:
        custonResponse (Dict): custom response returned by
        makeApiCall(url, params, method)
    """
    print('\nURL:')
    print(custonResponse['url'])
    print('\nParametros usados:')
    print(custonResponse['request_params_pretty'])
    print('\nRespuesta del api:')
    print(custonResponse['response_data_pretty'])
    print('\n=======================')


def getCustomResponse(responseData, url, params):
    """convert requests lib response data to my custom
        response dictionary

    Args:
        responseData (Response): response class returned from requests lib
        url (String): requests uri
        params (Dict): params used

    Returns:
        Dict: custom response
    """
    custonResponse = dict()
    custonResponse['url'] = url
    custonResponse['status_code'] = responseData.status_code
    custonResponse['request_params_raw'] = params
    custonResponse['request_params_pretty'] = json.dumps(params, indent=4)  # convierte el python(dic) a json
    custonResponse['response_data_raw'] = json.loads(responseData.content)  # convierte el json a python(dic)
    custonResponse['response_data_pretty'] = json.dumps(custonResponse['response_data_raw'], indent=4)

    return custonResponse

