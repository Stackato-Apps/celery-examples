# Celery Example using RabbitMQ

This is a small and extremely lightweight demo of using Celery for distributed computation.

You can read more about the Celery task queue [here][celery-homepage], and more about celery [here](http://en.wikipedia.org/wiki/Celery).

To learn more about the Rabbit Message Queueing service, read up their documentation on their homepage [here][rabbitmq-homepage].

## Stackato

This demo has been ported over to Stackato to demonstrate RabbitMQ as one of the provided
services within Stackato.

### Deploying

ensure that you have the Stackato CLI installed (which can be found [here][activestate-cli-download]):

    $ stackato push -n

### To run the demo

    $ stackato run python demo.py

[activestate-cli-download]: http://www.activestate.com/stackato/download_client
[rabbitmq-homepage]: http://www.rabbitmq.com/
[celery-homepage]: http://www.celeryproject.org/
