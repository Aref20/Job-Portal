
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
WORKDIR /app
COPY requirements5.txt ./
RUN python -m pip install --upgrade pip
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc \
  && apt-get install --yes --no-install-recommends \
        apt-transport-https \
        curl \
        gnupg \  
        tdsodbc\
 && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y msodbcsql17\
 && apt-get install -y  unixodbc-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/*
RUN pip3 install -r requirements5.txt
COPY . .