FROM ubuntu:20.04
USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install \
    python3.10 \
    python3-pip \
    python-is-python3
RUN apt-get clean

WORKDIR /app

RUN pip install mlflow

