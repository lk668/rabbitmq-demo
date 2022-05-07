# 简单的异步RabbitMQ消息队列

本文基于python实现一个简单的消息队列，底层需要部署rabbitmq-server，producer发送消息到rabbitmq-server的某个queue，consumer从对应queue中读取消息体，并进行相应的处理。


## 1. 环境搭建

1. 部署rabbitmq-server

```bash
方式一、选用docker部署，rabbitmq的用户名和密码均为root
docker run -d --hostname my-rabbit --name dev-rabbit -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=root -p 5672:5672 -p 15672:15672 daocloud.io/rabbitmq:3-management
```

2. 安装python依赖

```bash
pip3 install -r requirements.txt
```

3. 测试
```
1. 启动consumer，本文通过脚本启动三个线程来监控example的queue
bash start_worker.sh

2. 给消息队列发送消息
python3 test.py
```

## 2. 使用说明

1. 访问localhost:15672 是rabbitmq的ui界面，可以在`Queue`界面，查看当前每个队列的消息情况
2. 本次demo开启了ACK确认机制，消息发送到queue以后，在queue中是`Ready`的状态，消费者从`Queue`接收到消息以后，消息是`Unacked`状态，只有在消费者处理完消息，回复ack以后，消息才会从`Queue`中删除。所以如果消费者还没有处理完消息，服务挂掉了，消息依然会在消息队列存在，状态会从`Unacked`重置为`Ready`。等消费者服务恢复以后，消费者会重新从消息队列读取消息。
3. 每个消费者是同步处理消息的，即处理完一个消息以后，才会处理下一个消息。所以你可以修改`start_worker.sh`开启多个consumer线程。
4. 消息在消息队列是持久化存储的，即rabbitmq重启了以后，重启之前在消息队列存储的消息，依然存在。