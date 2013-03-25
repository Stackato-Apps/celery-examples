import sys
import os
import json

sys.path.append('.')

rabbitmq_url = json.loads(os.environ['RABBITMQ_URL'])

BROKER_URL = rabbitmq_url

# Deprecated
# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "celeryuser"
# BROKER_PASSWORD = "celery"
# BROKER_VHOST = "celeryvhost"

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("tasks",)
