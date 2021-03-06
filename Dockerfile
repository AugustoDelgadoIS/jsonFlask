FROM python:alpine

WORKDIR /app

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY . /app

RUN chmod +x gunicorn.sh

ENTRYPOINT [ "./gunicorn.sh" ]



