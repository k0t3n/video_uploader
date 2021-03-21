FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=settings

WORKDIR /code
COPY src /code
RUN apt-get update && apt-get install -y default-mysql-server default-libmysqlclient-dev gcc
RUN pip install -r requirements.txt && pip install uwsgi

EXPOSE 8080

CMD uwsgi --http 0.0.0.0:8080 --module wsgi --processes 4 --threads 2 --master
