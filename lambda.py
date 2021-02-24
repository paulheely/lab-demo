import os
import json
import boto3


def lambda_handler(event, context):
    msg = event["msg"]
    srcLang = event["SrcLang"]
    tgtLang = event["TgtLang"]

    translate = boto3.client(service_name='translate')

    result = translate.translate_text(
        Text=msg, SourceLanguageCode=srcLang, TargetLanguageCode=tgtLang)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "SrcLang": srcLang,
            "SrcMsg": msg,
            "TgtLang": tgtLang,
            "TgtMsg": result.get('TranslatedText')
        })
    }
