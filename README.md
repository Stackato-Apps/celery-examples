# Celery Example using RabbitMQ

This is a small and extremely lightweight demo of using Celery for distributed computation.

## Stackato

This demo has been ported over to Stackato to demonstrate RabbitMQ as one of the provided
services within Stackato.

### Deploying

ensure that you have the Stackato CLI installed (can be found at http://www.activestate.com/stackato/download_client):

    $ stackato push -n

### To run the demo

    $ stackato run celery-example python demo.py
