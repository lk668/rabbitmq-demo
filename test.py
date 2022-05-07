import producer
import time

mq = producer.MQProducer()
for i in range(10):
    mq.send_message(f"hello world {i}")
    time.sleep(1)
mq.close_connection()