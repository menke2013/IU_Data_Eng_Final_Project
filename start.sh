#!/bin/bash

docker build -t me-cassandra-image .

docker run --rm -p 9042:9042 --name me-cassandra-container -d me-cassandra-image

docker exec -it me-cassandra-container bash






