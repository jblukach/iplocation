FROM public.ecr.aws/lambda/python:latest

WORKDIR /var/task

COPY IP2LOCATION-LITE-ASN.BIN .
COPY IP2LOCATION-LITE-ASN.IPV6.BIN .
COPY IP2LOCATION-LITE-DB11.BIN .
COPY IP2LOCATION-LITE-DB11.IPV6.BIN .
COPY IP2PROXY-LITE-PX12.BIN .

COPY DBASNLITEBIN.updated .
COPY DBASNLITEBINIPV6.updated .
COPY DB11LITEBIN.updated .
COPY DB11LITEBINIPV6.updated .
COPY PX12LITEBIN.updated .

COPY lookup.py .
COPY requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]