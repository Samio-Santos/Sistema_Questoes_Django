FROM python:3.8-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

COPY requeriments.txt requeriments.txt
RUN pip install -r requeriments.txt

WORKDIR /app
