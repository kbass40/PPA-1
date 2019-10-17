FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install -U pytest

RUN pip3 install mysql-connector-python

RUN apt-get install -y docker-compose

COPY ppa-1.py /usr/src/ppa-1.py
COPY BMI.py /usr/src/BMI.py
COPY Retirement.py /usr/src/Retirement.py
COPY SplitTip.py /usr/src/SplitTip.py
COPY EmailVerifier.py /usr/src/EmailVerifier.py
COPY database.py /usr/src/database.py
COPY docker-compose.yml /usr/src/docker-compose.yml

CMD ["python3", "/usr/src/ppa-1.py"]