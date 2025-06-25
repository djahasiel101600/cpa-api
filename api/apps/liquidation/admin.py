from django.contrib import admin
from .models import Payee, Liquidation, LiquidationAttachment, ExpenditureCode

# Register your models here.
admin.site.register(Payee)
admin.site.register(Liquidation)
admin.site.register(LiquidationAttachment)
admin.site.register(ExpenditureCode)