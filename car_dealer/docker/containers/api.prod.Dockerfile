FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /car_dealer

ENV PYTHONPATH "${PYTHONPATH}/car_dealer"
ENV PYTHONBUFFERED 1

RUN chmod +x /car_dealer/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /car_dealer/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /car_dealer/requirements/prod.txt