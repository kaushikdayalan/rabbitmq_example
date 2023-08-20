import pika
from pika import exceptions
import json
import uuid

try: 
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
except exceptions.AMQPConnectionError as e:
    print("Unable to establish connection to RabbitMQ Server.")
    
    
channel = connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

order = {
    'id': str(uuid.uuid4()),
    'user_email' : 'john.doe@example.com',
    'product' : 'Leather Jacket',
    'quantity' : 1
}

try: 
    channel.basic_publish(
        exchange='order',
        routing_key='order.notify',
        body=json.dumps({
            'user_email': order['user_email']
        })
    )
except Exception as e:
    print(" [x] Unable to send notify message!")
else:
    print(" [x] Message sent to notify!")


try:
    channel.basic_publish(
        exchange='order',
        routing_key='order.report',
        body=json.dumps(order)
    )
except Exception as e:
    print(" [x] Unable to send report message!")
else:
    print(' [x] Sent report message!')


print("Closing Connection")
connection.close()
