FROM python:3.8-slim-buster

COPY . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
