FROM python:3.8.3-alpine
LABEL maintainer="haudraufhaun"

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add -f \
        postgresql-client 

RUN apk add build-base 

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

COPY . /code/

RUN apk update && apk add -y netcat
 
ENTRYPOINT ["/code/entrypoint.sh"]
