import pika
import time
import conf
import base

class MQConsumer(base.RabbitMQBase):
    def __init__(self, queue=""):
        super(MQConsumer, self).__init__()
        self.queue = queue if queue else conf.RABBIT_QUEUE
        self.channel.queue_declare(queue=self.queue, durable=True)
    
    def callback_with_ack(self, ch, method, properties, body):
        # 修改为自己的逻辑
        print(" [x] Received %r" % body)
        time.sleep(10)
        print('ok')

        # 确认ack
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    def callback_without_ack(self, ch, method, properties, body):
        # 修改为自己的逻辑
        print(" [x] Received %r" % body)
        time.sleep(10)
        print('ok')
    

    def start_consumer(self):
        # 需要ack
        self.channel.basic_consume(on_message_callback=self.callback_with_ack, queue=self.queue, auto_ack=False)
        # 不需要ack
        # self.channel.basic_consume(on_message_callback=self.callback_without_ack, queue=self.queue, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
    
if __name__ == "__main__":
    mq = MQConsumer()
    mq.start_consumer()