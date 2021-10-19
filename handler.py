import json


def get_joke(event, context):
    body = {
        "message": "This is a test for cicd pipeline from github to aws lambda function"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
