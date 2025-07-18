from django.test import TestCase
import uuid
from django.contrib.auth.models import User

# Create your tests here.
def generate_custom_id():
        # Example: return a fixed-length random alphanumeric string
        import random, string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

id = generate_custom_id()
# print(str(uuid.uuid4()).replace('-', '')[:12].upper())
print(uuid.uuid4())


# Testing Django Token
from rest_framework.authtoken.models import Token
def testToken():
        token = Token.objects.create(user=User.objects.get(pk=1))
        print(token.key)