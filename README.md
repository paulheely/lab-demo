# lab-demo

1. Deploy the tca_lab.yaml CloudFormation template to build out the lab environment and setup the Cloud9 environment.
2. Create Lambda function
3. Create zip file: zip my-deployment-package.zip lambda.py
4. aws lambda create-function --function-name tca-lab-function --zip-file fileb://my-deployment-package.zip --handler lambda.lambda_handler --runtime python3.8 --role arn:aws:iam::826799620820:role/TCA-Lab-Dev-LambdaLabRole-1MF8NLS87T9IO

# Invoke

aws lambda invoke --function-name tca-lab-function --payload '{"SrcLang": "en", "TgtLang": "el", "OutVoice": "Miguel", "msg": "This is a test message from the TCA lab demo."}' out

# Cleanup

1. Delete lambda function
2. Delete CF stack
3.
