
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements2.txt requirements2.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements2.txt




COPY . .
CMD ["python","manage.py","runserver"]
EXPOSE 3000