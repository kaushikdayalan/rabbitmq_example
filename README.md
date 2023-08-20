# Simple RabbitMQ (AMQP) implementation
## Introduction
This project implements direct topic excahnge using RabbitMQ.

## Getting Started

### Installation:
#### Setup environment 

Requirements: 
1. Docker must already be installed on the system
2. python 3.9 or above
3. git

*OSX/Linux*
```sh
$ git clone https://github.com/kaushikdayalan/rabbitmq_example.git
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r --no-cache-dir requirements.txt
```
#### Start RabbitMQ Server
I would suggest running RabbitMQ on Docker as it saves you the time to
setup and install it on your local machine.
This project was implemented when RabbitMQ 3.12 was the latest version. 
refer to this link for more information: https://www.rabbitmq.com/download.html
```
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
```

## What is RabbitMQ?
RabbitMQ is an Advanced Message Queuing Protocol in which the producer of a message does not require to take responsibility for the message reaching the consumer but can focus on another task. The message is sent to a broker which then pushes this message into a specific queue which can later be picked up by the consumer. This decouples the sender and the receiver and can work asynchronously.

