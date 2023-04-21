FROM python:3.8-slim-buster

EXPOSE 5555
ENV PYTHONUNBUFFERED=1

COPY conf/requirements.txt /


RUN pip install -r ./requirements.txt


WORKDIR /app/CMC

CMD [ "celery", "-A", "CMC.celery", "worker", "-l", "INFO", "-B"]
