#!/bin/bash

git pull origin main

pip3 install --upgrade pip
pip3 install -r requirements.txt

TARGET_PORT=5000

TARGET_PID=$(lsof -Fp -i TCP:${TARGET_PORT} | grep -Po 'p[0-9]+' | grep -Po '[0-9]+')

if [ ! -z ${TARGET_PID} ]; then
  echo "> Kill WAS running at ${TARGET_PORT}."
  sudo kill ${TARGET_PID}
fi

nohup python app.py > /home/ubuntu/nohup_flask.out 2>&1 &
echo "> Now new WAS runs at ${TARGET_PORT}."
exit 0
