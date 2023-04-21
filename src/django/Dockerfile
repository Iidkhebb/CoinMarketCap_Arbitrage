FROM python:3.8.2-slim-buster


EXPOSE 8000
ENV PYTHONUNBUFFERED=1

COPY src /app
COPY conf/requirements.txt /app
COPY tools/setup.sh /app/CMC

WORKDIR /app

RUN pip install -r requirements.txt
WORKDIR /app/CMC

CMD ["sh", "setup.sh"]