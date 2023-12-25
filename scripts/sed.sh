#!/bin/bash

sed  -i "s/{\$$1}/$2/g" ./docker-entrypoint-initdb.d/docker-entrypoint-initdb.sql