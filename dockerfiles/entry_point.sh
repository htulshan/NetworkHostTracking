#!/bin/bash

service nginx start
cd /app
gunicorn trackhost:app

exec "$@"