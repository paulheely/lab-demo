import os
import json
import boto3


def lambda_handler(event, context):
    msg = event["msg"]
    srcLang = event["SrcLang"]
    tgtLang = event["TgtLang"]
    outVoice = event[OutVoice"]

    translate = boto3.client(service_name='translate')

    result = translate.translate_text(
        Text=msg, SourceLanguageCode=srcLang, TargetLanguageCode=tgtLang)

    polly_client = boto3.client('polly')

    response = polly_client.synthesize_speech(VoiceId=outVoice,
                                              OutputFormat='mp3',
                                              Text=result)

    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()

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
