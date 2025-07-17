from .models import Payee, Liquidation, LiquidationAttachment
from rest_framework import serializers

class LiquidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquidation
        fields = [
            'id',
            'transactionDate',
            'payee',
            'checkNumber',
            'referenceJEV_DV',
            'expenseCode',
            'amountCashAdvance',
            'amountSpent',
            'amountRefund',
            'amountReimbursed',
            'fund',
            'periodStart',
            'periodEnd',
            'remarks',
            'agency'
        ]