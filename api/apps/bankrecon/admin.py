from django.contrib import admin
from apps.bankrecon.models import BankRecon, AccountNumber
from apps.core.models import Agency, Fund, Office, Position, Employee

# Register your models here.
admin.site.register(BankRecon)
admin.site.register(Employee)
admin.site.register(Fund)
admin.site.register(Office)
admin.site.register(AccountNumber)
admin.site.register(Agency)
admin.site.register(Position)