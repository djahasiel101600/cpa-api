from .models import *
from rest_framework import serializers

class InspectionAcceptanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionAcceptanceReport
        fields = '__all__'
        
class ParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particular
        fields = '__all__'