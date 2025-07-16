from django.db import models
from django.contrib.auth.models import User
from apps.core.uuid_generator import generate_custom_id
from apps.core.models import ExpenditureCode, Fund, Agency

# Create your models here.
class RCIPayee(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="RCIPayee_User")
    
    def __str__(self):
        return f"{self.name}, {self.address}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)


class ReportOfCheckIssued(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    dvNo = models.CharField(max_length=16)
    checkDate = models.DateField()
    asaNo = models.CharField(max_length=24, null=True, blank=True)
    payee = models.ForeignKey(RCIPayee, models.CASCADE, related_name="ReportOfCheckIssued_Payee")
    natureOfTransaction = models.TextField()
    amountNetOfTax = models.DecimalField(decimal_places=2, max_digits=18)
    grossAmount = models.DecimalField(decimal_places=2, max_digits=18)
    remarks = models.TextField(blank=True, null=True)
    isCancelled = models.BooleanField(default=False)
    fund = models.ForeignKey(Fund, on_delete=models.SET_NULL, null=True, related_name="ReportOfCheckIssued_Fund")
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True, related_name="ReportOfCheckIssued_Agency")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="ReportOfCheckIssued_User")

class AccountingEntry(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    rciId = models.ForeignKey(ReportOfCheckIssued, models.CASCADE, related_name="AccountingEntry_ReportOfCheckIssued")
    title = models.ForeignKey(ExpenditureCode, models.CASCADE, related_name="AccountingEntry_ExpenditureCode")
    debit = models.DecimalField(decimal_places=2, max_digits=18, default=0)
    credit = models.DecimalField(decimal_places=2, max_digits=18, default=0)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="AccountingEntry_User")

    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)

# class Attachment(models.Model):
#     id = models.CharField(primary_key=True, max_length=12, editable=False)
#     rciId = models.ForeignKey(ReportOfCheckIssued, models.CASCADE, related_name="Attachment_ReportOfCheckIssued")
#     name = models.CharField(max_length=100)
#     filePath = models.FileField()

#     def save(self,*args, **kwargs):
#         if not self.id:
#             self.id = generate_custom_id()
#         super().save(*args, **kwargs)