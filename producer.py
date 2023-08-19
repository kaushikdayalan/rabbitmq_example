import pika
from pika import exceptions
import json
import uuid


try: 
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
except exceptions.AMQPConnectionError as e:
    print("Unable to establish connection to RabbitMQ Server.")
    exit()

    
    
    
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
        body=json.dump({
            'user_email': order['user_email']
        })
    )
except Exception as e:
    print(e)


print(" [x] notify message sent!")

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dump(order)
)

print(' [x] Sent report message!')

connection.close()
