FROM public.ecr.aws/lambda/python:latest

WORKDIR /var/task

COPY lookup.py requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]