FROM public.ecr.aws/lambda/python:latest

WORKDIR /var/task

COPY IP2LOCATION-LITE-ASN.BIN DBASNLITEBIN.updated .
COPY IP2LOCATION-LITE-ASN.IPV6.BIN DBASNLITEBINIPV6.updated .
COPY IP2LOCATION-LITE-DB11.BIN DB11LITEBIN.updated .
COPY IP2LOCATION-LITE-DB11.IPV6.BIN DB11LITEBINIPV6.updated .
COPY IP2PROXY-LITE-PX12.BIN PX12LITEBIN.updated .
COPY lookup.py requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]