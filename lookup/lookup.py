import json
import os

def handler(event, context):

    os.system('ls -lh /app')

    return {
        'statusCode': 200,
        'body': json.dumps('Completed!')
    }