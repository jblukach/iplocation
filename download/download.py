import boto3
import datetime
import json
import os
import requests

def handler(event, context):

    secret = boto3.client('secretsmanager')

    getsecret = secret.get_secret_value(
        SecretId = os.environ['SECRET_MGR_ARN']
    )

    token = json.loads(getsecret['SecretString'])







    return {
        'statusCode': 200,
        'body': json.dumps('Completed!')
    }