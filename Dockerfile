# pull official base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
WORKDIR /code
COPY . /code/

# install psycopg2
RUN apt update && apt install -y libpq-dev gcc

RUN pip install psycopg2

# run gunicorn
CMD gunicorn deli.wsgi:application --bind 0.0.0.0:$PORT
