# Use the official RabbitMQ image as the base image
FROM rabbitmq:3.12-management

# Expose the necessary ports
EXPOSE 5672 15672

# Start RabbitMQ server on container start
CMD ["rabbitmq-server"]