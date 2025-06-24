from .models import BankRecon
from rest_framework import serializers

class BankReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRecon
        fields = [
            'accountNumber',
            'asOf',
            'fund',
            'office',
            'dateReceived',
            'sender',
            'receiver',
            'remarks'
        ]
        