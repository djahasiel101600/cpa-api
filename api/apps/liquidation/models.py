from django.db import models
from apps.core.models import ExpenditureCode, Fund, Agency

# Create your models here.
class Payee(models.Model):
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=1)
    lastName = models.CharField(max_length=200)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Liquidation(models.Model):
    transactionDate = models.DateField()
    payee = models.ForeignKey(Payee, models.CASCADE, related_name="liquidation_payee")
    checkNumber = models.IntegerField()
    referenceJEV_DV = models.CharField(max_length=100)
    expenseCode = models.ForeignKey(ExpenditureCode, models.CASCADE, related_name="liquidation_expeditureCode")
    amountCashAdvance = models.DecimalField(max_digits=18, decimal_places=2)
    amountSpent = models.DecimalField(max_digits=18, decimal_places=2)
    amountRefund = models.DecimalField(max_digits=18, decimal_places=2)
    amountReimbursed = models.DecimalField(max_digits=18, decimal_places=2)
    fund = models.ForeignKey(Fund, models.CASCADE, related_name="liquidation_fund")
    periodStart = models.DateField()
    periodEnd = models.DateField()
    remarks = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency, models.CASCADE, related_name="liquidation_agency")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class LiquidationAttachment(models.Model):
    liquidationRef = models.ForeignKey(Liquidation, models.CASCADE, related_name="attachment_liquidation")
    attachmentName = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)