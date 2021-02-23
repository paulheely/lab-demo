# lab-demo

1. Deploy the tca_lab.yaml CloudFormation template to build out the lab environment and setup the Cloud9 environment.
2. Create Lambda function
3. Create zip file: zip my-deployment-package.zip lambda.py
4. aws lambda create-function --function-name tca-lab-function --zip-file fileb://my-deployment-package.zip --handler lambda.lambda_handler --runtime python3.8 --role arn:aws:iam::826799620820:role/TCA-Demo-Lab-LambdaLabRole-1LZNX2F9Z2H3B

# Invoke

aws lambda invoke --function-name tca-lab-function --payload '{"key": "value"}' out

# Cleanup

1. Delete lambda function
2. Delete CF stack
3.
