from rest_framework import serializers
from .models import ReportOfCheckIssued, AccountingEntry, RCIPayee

class ReportOfCheckIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfCheckIssued
        fields = "id,dvNo,checkDate,payee,natureOfTransaction,amountNetOfTax,grossAmount,remarks".split(",")

class AccountingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingEntry
        fields = '__all__'


class RCIPayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RCIPayee
        fields = '__all__'