from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
class InspectionAcceptanceReportViewSet(viewsets.ModelViewSet):
    queryset = InspectionAcceptanceReport.objects.all()
    serializer_class = InspectionAcceptanceReportSerializer
    
    def perform_create(self, serializer):
        token = self.request.auth
        serializer.save(createdBy=User.objects.get(username=token.user))
    
class ParticularViewSet(viewsets.ModelViewSet):
    queryset = Particular.objects.all()
    serializer_class = ParticularSerializer