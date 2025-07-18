from django.contrib import admin
from apps.bankrecon.models import BankRecon, AccountNumber

# Register your models here.
admin.site.register(BankRecon)
admin.site.register(AccountNumber)