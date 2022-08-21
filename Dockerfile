
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
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

COPY ./scripts /scripts

RUN chmod +x /scripts/*

# folder to serve media files by nginx
RUN mkdir -p /vol/web/media
# folder to serve static files by nginx
RUN mkdir -p /vol/web/static

# always good to run our source code with a different user other than root user
RUN useradd user
RUN chown -R user:user /vol
# chmod 755 means full access to owner and read-access to everyone else
RUN chmod -R 755 /vol/web
RUN chown -R user:user /app
RUN chmod -R 755 /app
# switch to our user
USER user

CMD ["entrypoint.sh"]