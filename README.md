# Simple RabbitMQ (AMQP) implementation


## Getting Started

### Installation:

Requirements: 
Docker must already be installed on the system
python 3.9 or above

*OSX/Linux*
```sh
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r --no-cache-dir requirements.txt
```
## What is RabbitMQ?
RabbitMQ is an Advanced Message Queuing Protocol in which the producer of a message does not require to take responsibility for the message reaching the consumer but can focus on another task. The message is sent to a broker which then pushes this message into a specific queue which can later be picked up by the consumer. This decouples the sender and the receiver and can work asynchronously.

### About the Project 
This project implements ......