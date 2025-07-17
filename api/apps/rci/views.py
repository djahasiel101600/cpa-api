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
    permission_classes = [permissions.AllowAny]

class AccountingEntryViewSet(viewsets.ModelViewSet):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer
    permission_classes = [permissions.IsAdminUser]


class RCIPayeeViewSet(viewsets.ModelViewSet):
    queryset = RCIPayee.objects.all()
    serializer_class = RCIPayeeSerializer
    permission_classes = [permissions.IsAdminUser]

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAdminUser]