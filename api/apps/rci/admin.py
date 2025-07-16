from django.contrib import admin
from .models import ReportOfCheckIssued, RCIPayee, AccountingEntry

# Register your models here.
admin.site.register(ReportOfCheckIssued)
admin.site.register(RCIPayee)
admin.site.register(AccountingEntry)
