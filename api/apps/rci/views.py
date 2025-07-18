from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ReportOfCheckIssued, AccountingEntry, RCIPayee, Attachment
from .serializers import ReportOfCheckIssuedSerializer
from .serializers import AccountingEntrySerializer
from .serializers import RCIPayeeSerializer
from .serializers import AttachmentSerializer

# Create your views here.
class ReportOfCheckIssuedViewSet(viewsets.ModelViewSet):
    queryset = ReportOfCheckIssued.objects.all()
    serializer_class = ReportOfCheckIssuedSerializer

class AccountingEntryViewSet(viewsets.ModelViewSet):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer
    
class RCIPayeeViewSet(viewsets.ModelViewSet):
    queryset = RCIPayee.objects.all()
    serializer_class = RCIPayeeSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer