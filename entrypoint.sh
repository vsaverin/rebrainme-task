#!/bin/bash

echo "[entrypoint] - Starting python app.py"
python3 app.py consume --topic 'hello_topic' --kafka 'kafka:29092'
echo "[entrypoint] - Exiting"

