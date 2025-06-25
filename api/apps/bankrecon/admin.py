from django.contrib import admin
from apps.bankrecon import models

# Register your models here.
admin.site.register(models.BankRecon)
admin.site.register(models.Employee)
admin.site.register(models.Fund)
admin.site.register(models.Office)
admin.site.register(models.Position)
admin.site.register(models.AccountNumber)
admin.site.register(models.Agency)