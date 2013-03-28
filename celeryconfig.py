import sys
import os

sys.path.append('.')

rabbitmq_url = os.environ['RABBITMQ_URL']

BROKER_URL = rabbitmq_url

# Deprecated
# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "celeryuser"
# BROKER_PASSWORD = "celery"
# BROKER_VHOST = "celeryvhost"

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("tasks",)
