import pika 
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue = channel.queue_declare('order_notify')
queue_name = queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f" [x] Notifying: {payload['user_email']}")
    print(" [x] Done")
    # Acknowledge RabbitMQ that message was recieved and delete it from queue
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback,
                      queue=queue_name)

print(" [*] Waitging for notify messages. To exit press CTRL^C.")

channel.start_consuming()