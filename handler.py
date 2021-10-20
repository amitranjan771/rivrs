import json

def rivr(event, context):
    body = {
        "message": "This is a test for cicd pipeline from github to aws lambda function from src"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
