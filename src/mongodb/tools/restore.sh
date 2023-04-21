#!/bin/bash

if [ -e /data/db/mongod.lock ]; then
    echo "The lock file exists."
    docker-entrypoint.sh mongod

else
    echo "The lock file does not exist."

    mongod --fork --logpath /var/log/mongodb.log; mongorestore -d clocker /docker-entrypoint-initdb.d/test; mongod --shutdown; docker-entrypoint.sh mongod

fi
