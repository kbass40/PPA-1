FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN apt-get install -y docker-compose

RUN pip3 install -U pytest

RUN pip3 install mysql-connector-python

RUN pip3 install pytest_mock

COPY ppa-1.py /usr/src/ppa-1.py
COPY BMI.py /usr/src/BMI.py
COPY Retirement.py /usr/src/Retirement.py
COPY SplitTip.py /usr/src/SplitTip.py
COPY EmailVerifier.py /usr/src/EmailVerifier.py
COPY EmailVerifier_test.py /usr/src/EmailVerifier_test.py
COPY BMI_test.py /usr/src/BMI_test.py
COPY Retirement_test.py /usr/src/Retirement_test.py
COPY SplitTip_test.py /usr/src/SplitTip_test.py
COPY docker-compose.yml /usr/local/bin/docker-compose.yml

# RUN python3 -m pytest