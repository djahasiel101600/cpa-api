from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.
class InspectionAcceptanceReportViewSet(viewsets.ModelViewSet):
    queryset = InspectionAcceptanceReport.objects.all()
    serializer_class = InspectionAcceptanceReportSerializer
    permission_classes = [permissions.AllowAny]
    
class ParticularViewSet(viewsets.ModelViewSet):
    queryset = Particular.objects.all()
    serializer_class = ParticularSerializer
    permission_classes = [permissions.AllowAny]