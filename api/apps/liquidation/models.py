from django.db import models
from django.contrib.auth.models import User
from apps.core.models import ExpenditureCode, Fund, Agency
from apps.core.uuid_generator import generate_custom_id

# Create your models here.
class Payee(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=1)
    lastName = models.CharField(max_length=200)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)

class Liquidation(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    transactionDate = models.DateField()
    payee = models.ForeignKey(Payee, models.CASCADE, related_name="liquidation_payee")
    checkNumber = models.IntegerField(null=True)
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
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.payee.firstName} {self.payee.lastName}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)

class LiquidationAttachment(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    liquidationRef = models.ForeignKey(Liquidation, models.CASCADE, related_name="attachment_liquidation")
    attachmentName = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.attachmentName
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)