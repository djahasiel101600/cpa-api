import uuid

# Create your models here.
def generate_custom_id():
    return str(uuid.uuid4()).replace('-', '')[:12].upper()