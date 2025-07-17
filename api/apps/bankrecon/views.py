from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import BankReconSerializer
from .models import BankRecon

# Create your views here.
class BankReconViewSet(viewsets.ModelViewSet):
    queryset = BankRecon.objects.all()
    serializer_class = BankReconSerializer
    permission_classes = [permissions.AllowAny]