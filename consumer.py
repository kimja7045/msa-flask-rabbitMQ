import pika
from os import getenv
from dotenv import load_dotenv

load_dotenv(verbose=True)

params = pika.URLParameters(getenv('AMQP_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')


def callback(ch, method, properties, body):
    print('Received in boss')
    print(body)


channel.basic_consume(queue='boss', on_message_callback=callback, auto_ack=True)

print('Started consuming at boss')

channel.start_consuming()

channel.close()
