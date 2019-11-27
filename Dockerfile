FROM python:3.7-slim
# setup system
RUN apt-get update && \ 
    apt-get install -y \ 
    build-essential \
    git
# install python dependencies
WORKDIR /code
COPY requirements.txt .
COPY setup.py .
RUN pip install -r requirements.txt
