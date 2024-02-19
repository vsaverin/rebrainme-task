# Kafka Producer/Consumer
#### *Test task for Rebrainme*

This Python script provides functionality for both producing and consuming messages to/from Kafka topics. It utilizes the `aiokafka` library for asynchronous Kafka interactions.

## Prerequisites
- Python 3.7 or higher
- Install dependencies using `pip3 install -r requirements.txt`

## Usage

### Producing a Message
To produce a message to a Kafka topic, use the following command:

```bash
python app.py produce --message "your_message" --topic "your_topic" --kafka "kafka_broker_address"
```

- `--message`: The message you want to produce.
- `--topic`: The Kafka topic to which the message will be sent.
- `--kafka`: The address (ip:port) of the Kafka broker.

### Consuming Messages
To consume messages from a Kafka topic, use the following command:

```bash
python app.py consume --topic "your_topic" --kafka "kafka_broker_address"
```

- `--topic`: The Kafka topic from which to consume messages.
- `--kafka`: The address (ip:port) of the Kafka broker.

## Example

### Producing a Message
```bash
python app.py produce --message "Hello, Kafka!" --topic "example_topic" --kafka "localhost:9092"
```

### Consuming Messages
```bash
python app.py consume --topic "example_topic" --kafka "localhost:9092"
```

## Notes
- Ensure that the Kafka broker is running and accessible at the specified address.


## Running Script using Docker:

### Replace ur topic data and kafka host in entrypoint:
```bash
#!/bin/bash

echo "[entrypoint] - Starting python app.py"
python3 app.py consume --topic 'YOUR_TOPIC' --kafka 'HOST:PORT'
echo "[entrypoint] - Exiting"
```

### Build image
```commandLine
docker build -t your-custom-image-name .
```

### Run image
```commandLine
docker run --network=mynetwork your-custom-image-name
```

*mynetwork* - your docker network with running Kafka


## Running kafka using Docker:
### Build in compose
```commandLine
docker-compose -f docker-compose-kafka.yml up --build
```

Kafka-ui will be available on - http://localhost:8080/

## Notes
- add -d to run in background
- Don't forget to replace mynetwork in docker-compose file with your bridge network name


