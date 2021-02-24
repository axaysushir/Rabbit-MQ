import pika, sys
from pika import channel

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# queue
# channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='', routing_key='hello', body='Hello World!..')

# channel.basic_publish(exchange='', routing_key='hello', body=message)

# print(" [x] Sent 'Hello World!...'")


# second part
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'

channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(
    delivery_mode= 2, # make message persiistant
    ))

print(" [x] Sent %r" % message)

connection.close()
