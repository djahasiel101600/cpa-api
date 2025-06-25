from .models import BankRecon
from rest_framework import serializers

class BankReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRecon
        fields = [
            'id',
            'accountNumber',
            'asOf',
            'office',
            'dateReceived',
            'sender',
            'receiver',
            'remarks'
        ]
        