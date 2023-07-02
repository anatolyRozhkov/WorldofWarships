FROM python:3.9-slim

MAINTAINER Anatoly Rozhkov <anatoly.rozhkov1998@gmail.com>

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

COPY . /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    /py/bin/pip install -r /tmp/requirements.txt

WORKDIR /app

ENV PATH="/py/bin:$PATH"