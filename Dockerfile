FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install -U pytest

COPY ppa-1.py /usr/src/src/ppa-1.py
COPY BMI.py /usr/src/src/BMI.py
COPY Retirement.py /usr/src/src/Retirement.py
COPY SplitTip.py /usr/src/src/SplitTip.py
COPY EmailVerifier.py /usr/src/src/EmailVerifier.py

CMD ["python3", "/usr/src/src/ppa-1.py"]
