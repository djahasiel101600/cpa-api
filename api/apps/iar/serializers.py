from .models import *
from rest_framework import serializers
from apps.core.serializers import OfficeSerializer, SupplierSerializer, EmployeeSerializer

class InspectionAcceptanceReportSerializer(serializers.ModelSerializer):
    office = OfficeSerializer()
    supplier = SupplierSerializer()
    receivedBy = EmployeeSerializer()
    submittedBy = EmployeeSerializer()
    
    class Meta:
        model = InspectionAcceptanceReport
        fields = '__all__'
        read_only_fields = ['createdBy', 'createdAt', 'updatedAt']
        
class ParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particular
        fields = '__all__'