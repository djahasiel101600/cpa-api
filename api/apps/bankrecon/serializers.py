from .models import BankRecon, AccountNumber
from apps.core.models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers


class BankReconSerializer(serializers.ModelSerializer):
    accountNumber = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()
    # createdBy = serializers.SerializerMethodField()
    
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
            'remarks',
            'createdBy'
        ]
        
    def get_accountNumber(self, obj):
        return obj.accountNumber.account
    
    def get_office(self, obj):
        return f"{obj.office.officeName} - {obj.office.officeAgency}"
    
    def get_sender(self, obj):
        return f"{obj.sender.firstName} {obj.sender.lastname} - {obj.sender.position}"
    
    def get_receiver(self, obj):
        return f"{obj.receiver.firstName} {obj.receiver.lastname} - {obj.receiver.position}"