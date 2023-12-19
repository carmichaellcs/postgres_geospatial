FROM python:3.10-alpine

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools

WORKDIR /src/app

COPY ./requirements.txt /src/app/requirements.txt

RUN pip3 install -r requirements.txt

RUN addgroup -g $GROUP_ID usergroup \
    && adduser -D -u $USER_ID -G usergroup user
RUN chown -R user:usergroup /src/app
RUN chmod -R 755 /src/app

USER user

EXPOSE 3333