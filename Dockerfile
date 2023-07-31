# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /fmu-to-resqml

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chown -R 1001:1001 /fmu-to-resqml
USER 1001
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "--chdir", "fmu-to-resqml", "wsgi:app" ]
EXPOSE 5000