import pika
import base
import conf

class MQProducer(base.RabbitMQBase):
    def __init__(self, queue=""):
        super(MQProducer, self).__init__()
        self.queue = queue if queue else conf.RABBIT_QUEUE
        self.channel.queue_declare(queue=self.queue, durable=True)
    
    # 发送消息
    def send_message(self, msg):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=2, # 消息持久化
            )
        )
        print(f"[x] Sent {msg} into queue {self.queue}")
    
    # 发送完需要关闭连接
    def close_connection(self):
        self.connection.close()
