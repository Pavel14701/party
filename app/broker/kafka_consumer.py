from aiokafka import AIOKafkaConsumer
import asyncio
import json
from kafka_producer import produce_message

async def consume_messages(topic, process_message):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        group_id="api_group",
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    await consumer.start()
    try:
        async for msg in consumer:
            await process_message(msg.key.decode('utf-8'), msg.value)
    finally:
        await consumer.stop()

async def process_message(key, message):
    # Логика обработки сообщения и выполнение необходимых операций
    response = {"status": "success", "original_message": message}
    await produce_message("response_topic", key, response)
