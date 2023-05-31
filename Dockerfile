# Dockerfile

# pull the official docker image
FROM python:3.8.5

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
USER root
# install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install SQLAlchemy 
RUN pip install pandas 



# copy project

COPY . . 
