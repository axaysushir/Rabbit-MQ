from typing import ChainMap
import pika
from pika.spec import Channel

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
Channel = connection.channel()

Channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = Channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

Channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press ctrl+c')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

Channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

Channel.start_consuming()