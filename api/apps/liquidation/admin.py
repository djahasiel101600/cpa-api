from django.contrib import admin
from .models import Payee, Liquidation, LiquidationAttachment 

# Register your models here.
admin.site.register(Payee)
admin.site.register(Liquidation)
admin.site.register(LiquidationAttachment)