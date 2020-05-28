#!/bin/bash

service nginx start
cd /app
gunicorn TrackHost:app

exec "$@"