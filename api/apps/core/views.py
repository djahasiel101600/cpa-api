from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Agency, Fund, Office, Position, Employee, ExpenditureCode
from .serializers import AgencySerializer, FundSerializer, OfficeSerializer
from .serializers import PositionSerializer, EmployeeSerializer, ExpenditureCodeSerializer

# Create your views here.
class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [permissions.IsAdminUser]

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = [permissions.IsAdminUser]

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAdminUser]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = ExpenditureCode.objects.all()
    serializer_class = ExpenditureCodeSerializer
    permission_classes = [permissions.IsAdminUser]

