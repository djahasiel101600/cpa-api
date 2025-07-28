from .models import *
from rest_framework import serializers

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ['id', 'agencyName', 'address']


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    officeAgency = AgencySerializer()
    class Meta:
        model = Office
        fields = ['id', 'officeName', 'officeAgency']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ExpenditureCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureCode
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'supplierName', 'supplierAddress']