FROM public.ecr.aws/lambda/python:latest

WORKDIR /var/task

COPY IP2LOCATION-LITE-ASN.BIN .
COPY IP2LOCATION-LITE-ASN.IPV6.BIN .
COPY IP2LOCATION-LITE-DB11.BIN .
COPY IP2LOCATION-LITE-DB11.IPV6.BIN .
COPY IP2PROXY-LITE-PX12.BIN .
RUN sleep 10
COPY DBASNLITEBIN.updated DBASNLITEBINIPV6.updated DB11LITEBIN.updated DB11LITEBINIPV6.updated lookup.py PX12LITEBIN.updated requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]