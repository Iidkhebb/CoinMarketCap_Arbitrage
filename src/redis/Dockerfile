FROM debian:buster

RUN apt-get update
RUN apt-get install -y redis-server
RUN sed -i 's/# bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis/redis.conf

EXPOSE 6379

ENTRYPOINT [ "redis-server", "--protected-mode no" ]