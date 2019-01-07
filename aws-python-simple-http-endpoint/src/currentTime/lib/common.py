import json

def response_builder(status, body):
    """Builds a response with the given status code and message body

    Arguments:
    status {int} -- an HTTP status code
    body {dict} -- a response body

    Returns:
    {dict} -- a response object including status code
    """
    response = {
        "statusCode": status,
        "body": json.dumps(body)
    }
    return response
