import os
import json
import boto3


def lambda_handler(event, context):
    msg = event["msg"]
    srcLang = event["SrcLang"]
    tgtLang = event["TgtLang"]
    outVoice = event["OutVoice"]
    outBucket = event["OutBucket"]

    translate = boto3.client(service_name='translate')

    result = translate.translate_text(
        Text=msg, SourceLanguageCode=srcLang, TargetLanguageCode=tgtLang)

    polly_client = boto3.client('polly')

    response = polly_client.start_speech_synthesis_task(VoiceId='Joanna',
                                                        OutputS3BucketName=outBucket,
                                                        OutputS3KeyPrefix='mypollyoutput',
                                                        OutputFormat='mp3',
                                                        Text=result.get('TranslatedText'))

    taskId = response['SynthesisTask']['TaskId']

    print(taskId)

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
