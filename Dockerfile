FROM python:alpine

COPY . /app

WORKDIR /app

RUN apt install python3-pip

RUN pip install -r requirements.txt