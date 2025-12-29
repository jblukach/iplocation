import boto3
import datetime
import json
import os
import requests

def handler(event, context):

    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')
    hour = datetime.datetime.now().strftime('%H')

    s3use1 = boto3.client('s3', region_name = 'us-east-1')
    s3use2 = boto3.client('s3', region_name = 'us-east-2')
    s3usw2 = boto3.client('s3', region_name = 'us-west-2')

    secret = boto3.client('secretsmanager')

    getsecret = secret.get_secret_value(
        SecretId = os.environ['SECRET_MGR_ARN']
    )

    token = json.loads(getsecret['SecretString'])

    code = 'PX12LITEBIN'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
    response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')

    code = 'DB11LITEBIN'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
    response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')

    code = 'DB11LITEBINIPV6'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
    response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')

    code = 'DBASNLITEBIN'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
    response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')

    code = 'DBASNLITEBINIPV6'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
    response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
    response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')

    os.system('ls -lh /tmp')

    return {
        'statusCode': 200,
        'body': json.dumps('Completed!')
    }