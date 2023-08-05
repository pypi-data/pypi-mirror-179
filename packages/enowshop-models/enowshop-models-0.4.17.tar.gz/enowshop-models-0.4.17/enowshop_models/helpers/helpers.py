import uuid
from datetime import datetime


def get_uuid():
    return str(uuid.uuid4())


def generate_uuid(mapper, connection, instance):
    if instance.uuid is None:
        instance.uuid = get_uuid()


def generate_data(mapper, connection, instance):
    instance.created_at = datetime.now()