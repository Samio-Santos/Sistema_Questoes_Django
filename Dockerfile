FROM python:3.8-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
