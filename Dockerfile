# syntax=docker/dockerfile:1
FROM python:3.10.12
# RUN apt-get update
# RUN apt-get install -y net-tools
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
CMD export DOCKER_HOST_IP=$(route -n | awk '/UG[ \t]/{print $2}') && python manage.py migrate --noinput && gunicorn -w 2 -b 0.0.0.0:8080 -t 6000 --keep-alive 6000 naf.wsgi
