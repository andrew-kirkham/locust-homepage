FROM python:3.7.3-slim-stretch

RUN pip install locust

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

WORKDIR /locust
COPY locust.py locustfile.py
