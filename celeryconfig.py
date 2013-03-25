import sys
import os
import json

sys.path.append('.')

vcap_srv = json.loads(os.environ['VCAP_SERVICES'])
cred = vcap_srv['rabbitmq'][0]['credentials']

BROKER_URL = cred['url']
# Deprecated
#BROKER_HOST = cred['host']
#BROKER_PORT = cred['port']
#BROKER_USER = cred['user']
#BROKER_PASSWORD = cred['pass']
#BROKER_VHOST = cred['vhost']

# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "celeryuser"
# BROKER_PASSWORD = "celery"
# BROKER_VHOST = "celeryvhost"

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("tasks",)
