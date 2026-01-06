import base64
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
    now = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')

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

    with open(f'/tmp/{code}.updated', 'w') as f:
        f.write(now)
    f.close()

    if len(response.content) > 1024:
    
        response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
        response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')
        response = s3use1.upload_file(f'/tmp/{code}.updated',os.environ['S3_USE1'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_STAGED'],f'{code}.updated')
        response = s3usw2.upload_file(f'/tmp/{code}.updated',os.environ['S3_USW2'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.updated')

    code = 'DB11LITEBIN'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    with open(f'/tmp/{code}.updated', 'w') as f:
        f.write(now)
    f.close()

    if len(response.content) > 1024:

        response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
        response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')
        response = s3use1.upload_file(f'/tmp/{code}.updated',os.environ['S3_USE1'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_STAGED'],f'{code}.updated')
        response = s3usw2.upload_file(f'/tmp/{code}.updated',os.environ['S3_USW2'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.updated')

    code = 'DB11LITEBINIPV6'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    with open(f'/tmp/{code}.updated', 'w') as f:
        f.write(now)
    f.close()

    if len(response.content) > 1024:

        response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
        response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')
        response = s3use1.upload_file(f'/tmp/{code}.updated',os.environ['S3_USE1'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_STAGED'],f'{code}.updated')
        response = s3usw2.upload_file(f'/tmp/{code}.updated',os.environ['S3_USW2'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.updated')

    code = 'DBASNLITEBIN'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    with open(f'/tmp/{code}.updated', 'w') as f:
        f.write(now)
    f.close()

    if len(response.content) > 1024:

        response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
        response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')
        response = s3use1.upload_file(f'/tmp/{code}.updated',os.environ['S3_USE1'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_STAGED'],f'{code}.updated')
        response = s3usw2.upload_file(f'/tmp/{code}.updated',os.environ['S3_USW2'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.updated')

    code = 'DBASNLITEBINIPV6'
    url = f'https://www.ip2location.com/download/?token={token["token"]}&file={code}&format=bin'

    response = requests.get(url)

    with open(f'/tmp/{code}.BIN.ZIP', 'wb') as f:
        f.write(response.content)
    f.close()

    with open(f'/tmp/{code}.updated', 'w') as f:
        f.write(now)
    f.close()

    if len(response.content) > 1024:

        response = s3use1.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USE1'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_STAGED'],f'{code}.BIN.ZIP')
        response = s3usw2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_USW2'],f'{code}.BIN.ZIP')
        response = s3use2.upload_file(f'/tmp/{code}.BIN.ZIP',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.BIN.ZIP')
        response = s3use1.upload_file(f'/tmp/{code}.updated',os.environ['S3_USE1'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_STAGED'],f'{code}.updated')
        response = s3usw2.upload_file(f'/tmp/{code}.updated',os.environ['S3_USW2'],f'{code}.updated')
        response = s3use2.upload_file(f'/tmp/{code}.updated',os.environ['S3_RESEARCH'],year+'/'+month+'/'+day+'/'+hour+f'/{code}.updated')

    os.system('ls -lh /tmp')

    with open('/tmp/Dockerfile', 'w') as w:
        w.write('# '+str(now)+'\n')
        w.write('FROM public.ecr.aws/lambda/python:latest\n')
        w.write('WORKDIR /var/task\n')
        w.write('COPY IP2LOCATION-LITE-ASN.BIN IP2LOCATION-LITE-ASN.IPV6.BIN IP2LOCATION-LITE-DB11.BIN IP2LOCATION-LITE-DB11.IPV6.BIN IP2PROXY-LITE-PX12.BIN .\n')
        w.write('COPY DBASNLITEBIN.updated DBASNLITEBINIPV6.updated DB11LITEBIN.updated DB11LITEBINIPV6.updated PX12LITEBIN.updated .\n')
        w.write('COPY lookup.py requirements.txt .\n')
        w.write('RUN pip --no-cache-dir install -r requirements.txt --upgrade\n')
        w.write('CMD ["lookup.handler"]')
    w.close()

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer '+token['github'],
        'X-GitHub-Api-Version': '2022-11-28'
    }

    url = 'https://api.github.com/repos/jblukach/iplocation/contents/lookup/Dockerfile'

    with open('/tmp/Dockerfile', 'r') as f:
        content = f.read()
    f.close()

    content = base64.b64encode(content.encode()).decode()

    data = {
        'message': 'Updating Dockerfile '+str(now),
        'content': content
    }

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

    return {
        'statusCode': 200,
        'body': json.dumps('Completed!')
    }