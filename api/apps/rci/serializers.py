from rest_framework import serializers
from .models import ReportOfCheckIssued, AccountingEntry, RCIPayee, Attachment

class ReportOfCheckIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfCheckIssued
        fields = '__all__'

class AccountingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingEntry
        fields = '__all__'


class RCIPayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RCIPayee
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'