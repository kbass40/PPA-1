FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install -U pytest
