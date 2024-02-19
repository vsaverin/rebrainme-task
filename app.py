import argparse
import logging
import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def produce_message(message, topic, kafka_broker):
    producer = AIOKafkaProducer(
        bootstrap_servers=kafka_broker, value_serializer=lambda v: v.encode("utf-8")
    )
    await producer.start()
    await producer.send_and_wait(topic, message)
    await producer.stop()
    logger.info(f"Message produced to topic '{topic}': {message}")


async def consume_messages(topic, kafka_broker):
    logger.info(f"Creating consumer on host: {kafka_broker}")
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=kafka_broker,
        value_deserializer=lambda v: v.decode("utf-8"),
    )
    await consumer.start()
    try:
        async for message in consumer:
            logger.info(f"Received message: {message.value}")
    finally:
        await consumer.stop()
    logger.info("Exiting")


async def main():
    parser = argparse.ArgumentParser(description="Kafka Producer/Consumer")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    produce_parser = subparsers.add_parser("produce", help="Produce a message")
    produce_parser.add_argument("--message", required=True, help="Message to produce")
    produce_parser.add_argument("--topic", required=True, help="Kafka topic")
    produce_parser.add_argument(
        "--kafka", required=True, help="Kafka broker address (ip:port)"
    )

    consume_parser = subparsers.add_parser("consume", help="Consume messages")
    consume_parser.add_argument("--topic", required=True, help="Kafka topic")
    consume_parser.add_argument(
        "--kafka", required=True, help="Kafka broker address (ip:port)"
    )

    args = parser.parse_args()

    if args.command == "produce":
        await produce_message(args.message, args.topic, args.kafka)
    elif args.command == "consume":
        await consume_messages(args.topic, args.kafka)
    else:
        logger.error("Invalid command. Use 'produce' or 'consume'")


if __name__ == "__main__":
    asyncio.run(main())
