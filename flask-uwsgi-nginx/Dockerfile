FROM python:3.7.6
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
        build-essential nginx curl less vim

RUN groupadd nginx \
    && useradd -g nginx nginx

RUN pip install \
        flask==1.1.1 \
        uwsgi==2.0.18
WORKDIR /home/api
