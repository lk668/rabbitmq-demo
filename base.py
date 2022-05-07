import pika
import conf

class RabbitMQBase():
    def __init__(self):
        cred = None
        if conf.RABBIT_USER and conf.RABBIT_PASS:
            cred = pika.credentials.PlainCredentials(conf.RABBIT_USER, conf.RABBIT_PASS)
        parameter = pika.ConnectionParameters(host=conf.RABBIT_HOST, port=conf.RABBIT_PORT, credentials=cred)
        self.connection = pika.BlockingConnection(parameter)
        self.channel = self.connection.channel()