from django.shortcuts import render
from .models import Liquidation
from .serializers import LiquidationSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class LiquidationViewSet(viewsets.ModelViewSet):
    queryset = Liquidation.objects.all()
    serializer_class = LiquidationSerializer
    permission_classes = [permissions.AllowAny]