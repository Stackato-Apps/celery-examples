This is a small and extremely lightweight demo of using Celery for distributed computation.


## Required packages

    celery (http://celeryproject.org/)
        This example was tested with version 2.3.1

## Other requirements

    RabbitMQ
        This example was tested with version 2.6.1
    
    Several RabbitMQ server installation packages are also available here:
    http://www.rabbitmq.com/server.html

    You will need to run the following commands to configure RabbitMQ:
        $ sudo rabbitmqctl add_user celeryuser celery
        $ sudo rabbitmqctl add_vhost celeryvhost
        $ sudo rabbitmqctl set_permissions -p celeryvhost celeryuser ".*" ".*" ".*"
    (Note: the user/password configuration here must match celeryconfig.py.)

    Starting RabbitMQ:
        $ sudo rabbitmq-server

## To run the demo

    - start rabbitmq-server
    - cd into the directory containing celeryconfig.py
    - launch celery daemon: $ celeryd
    - in a separate terminal (in the same dir): $ python demo.py

===============================================================================================

# Stackato

This demo has been ported over to Stackato to demonstrate RabbitMQ as one of the provided
services within Stackato.

## Deploying

    - ensure that you have the Stackato CLI installed.
    - stackato push -n
    
    ** after being deployed and it's running:
    - stackato run <appname> python demo.py
