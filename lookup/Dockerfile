# 1767453822

FROM public.ecr.aws/lambda/python:latest

WORKDIR /app

COPY IP2LOCATION-LITE-ASN.BIN IP2LOCATION-LITE-ASN.IPV6.BIN IP2LOCATION-LITE-DB11.BIN IP2LOCATION-LITE-DB11.IPV6.BIN IP2PROXY-LITE-PX12.BIN .

COPY DBASNLITEBIN.updated DBASNLITEBINIPV6.updated DB11LITEBIN.updated DB11LITEBINIPV6.updated PX12LITEBIN.updated .

COPY lookup.py requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]