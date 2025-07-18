from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .serializers import *

# Create your views here.
class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [permissions.AllowAny]

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = [permissions.AllowAny]

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.AllowAny]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.AllowAny]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('firstName')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = ExpenditureCode.objects.all()
    serializer_class = ExpenditureCodeSerializer
    permission_classes = [permissions.AllowAny]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.AllowAny]