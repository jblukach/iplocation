FROM public.ecr.aws/lambda/python:latest

WORKDIR /var/task

COPY DBASNLITEBIN.updated DBASNLITEBINIPV6.updated DB11LITEBIN.updated DB11LITEBINIPV6.updated PX12LITEBIN.updated .

COPY lookup.py requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]