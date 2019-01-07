from lib.common import response_builder
import datetime
import os


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    cwd = os.getcwd()
    body = {
        "message": "Hello, the current time is " + str(current_time),
        "cwd": str(cwd)
    }
    response = response_builder(200, body)

    return response
