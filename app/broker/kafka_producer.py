from aiokafka import AIOKafkaProducer
import asyncio
import json

async def produce_message(topic, key, value):
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    await producer.start()
    try:
        await producer.send_and_wait(topic, key=key.encode('utf-8'), value=value)
    finally:
        await producer.stop()
