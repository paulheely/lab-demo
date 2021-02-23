import os
import json


def lambda_handler(event, context):
    msg = event["msg"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Msg": msg
        })
    }
