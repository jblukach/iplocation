FROM public.ecr.aws/lambda/python:latest

RUN dnf install -y unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws \
    && dnf clean all

WORKDIR /var/task

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION

RUN aws s3 cp s3://iplocation-staged-use2-lukach-io/DB11LITEBIN.BIN.ZIP .
RUN unzip DB11LITEBIN.BIN.ZIP -d .

COPY lookup.py requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt --upgrade

CMD ["lookup.handler"]