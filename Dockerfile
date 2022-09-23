FROM python:3.10-alpine

WORKDIR /magazinesite/

RUN pip install --upgrade pip
COPY reqiurements.txt /magazinesite/
RUN pip install -r reqiurements.txt

COPY . /magazinesite/