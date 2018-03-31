#!/usr/bin/env bash
git pull
kill $(ps aux | grep 'is4302' | awk '{print $2}')
nohup gunicorn -k gevent -b 0.0.0.0:3000 --worker-connections 10 wsgi:app &