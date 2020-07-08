FROM python:3.8.3-alpine
LABEL maintainer="haudraufhaun"

ENV PYTHONBUFFERED 1

RUN apk update \
    && apk add -f \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
