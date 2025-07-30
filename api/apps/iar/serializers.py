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
        fields = [
            'id',
            'iarNo',
            'supplier',
            'iarDate',
            'salesInvoiceNo',
            'dateInvoice',
            'dateReceivedOfficer',
            'dateAcceptance',
            'dateInspection',
            'dateReceivedCoa',
            'receivedBy',
            'submittedBy',
            'office',
            'remarks',
        ]
        read_only_fields = ['createdBy', 'createdAt', 'updatedAt']
        
class ParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particular
        fields = '__all__'