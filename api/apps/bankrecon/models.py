from django.db import models
from apps.core.models import Fund, Office, Employee

# Create your models here.
class AccountNumber(models.Model):
    account = models.CharField(max_length=30)
    fund = models.ForeignKey(Fund, models.CASCADE, related_name="accountNumber_fund")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account


class BankRecon(models.Model):
    accountNumber = models.ForeignKey(AccountNumber, models.CASCADE, related_name="bankRecon_accountNumber")
    asOf = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    office = models.ForeignKey(Office, models.CASCADE, related_name="bankRecon_office")
    dateReceived = models.DateTimeField()
    sender = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconSender_employee")
    receiver = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconReceived_employee")
    remarks = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.accountNumber.account