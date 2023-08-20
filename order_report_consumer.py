import pika 
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue = channel.queue_declare('order_report')
queue_name = queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.report'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f" [x] Order Report: {payload}")
    print(" [x] Done")
    # Acknowledge RabbitMQ that message was recieved and delete it from queue
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback,
                      queue=queue_name)

print(" [*] Waitging for notify messages. To exit press CTRL^C.")

channel.start_consuming()