from .models import *
from rest_framework import serializers
from apps.core.serializers import OfficeSerializer, SupplierSerializer, EmployeeSerializer
from apps.core.models import Office, Supplier, Employee

class InspectionAcceptanceReportSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    supplier_details = SupplierSerializer(source='supplier', read_only=True)

    receivedBy = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    receivedBy_details = EmployeeSerializer(source='receivedBy', read_only=True)

    submittedBy = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    submittedBy_details = EmployeeSerializer(source='submittedBy', read_only=True)

    office = serializers.PrimaryKeyRelatedField(queryset=Office.objects.all())
    office_details = OfficeSerializer(source='office',read_only=True)

    
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
            'supplier_details',
            'submittedBy_details',
            'receivedBy_details',
            'office_details',
        ]
        # read_only_fields = ['createdBy', 'createdAt', 'updatedAt']
        
class ParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particular
        fields = '__all__'