FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install -U pytest

RUN pip3 install mysql-connector-python

RUN pip3 install pytest_mock