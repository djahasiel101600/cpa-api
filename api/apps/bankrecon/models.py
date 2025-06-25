from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agency(models.Model):
    agencyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    # createAt = models.DateTimeField(auto_now_add=True)
    # updatedAt = models.DateTimeField(auto_now=True)
    # createdBy = models.ForeignKey(User, models.CASCADE, related_name="agencyCreatedBy_user")
    
    def __str__(self):
        return self.agencyName
    

class Fund(models.Model):
    fundName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.fundName


class AccountNumber(models.Model):
    account = models.CharField(max_length=30)
    fund = models.ForeignKey(Fund, models.CASCADE, related_name="accountNumber_fund")

    def __str__(self):
        return self.account


class Office(models.Model):
    officeName = models.CharField(max_length=100)
    officeAgency = models.ForeignKey(Agency, models.CASCADE, related_name="office_agency")
    
    def __str__(self):
        return self.officeName


class Position(models.Model):
    positionName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.positionName


class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.ForeignKey(Position, models.CASCADE, related_name="employee_position")
    
    def __str__(self):
        return self.firstName


class BankRecon(models.Model):
    accountNumber = models.ForeignKey(AccountNumber, models.CASCADE, related_name="bankRecon_accountNumber")
    asOf = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    office = models.ForeignKey(Office, models.CASCADE, related_name="bankRecon_office")
    dateReceived = models.DateTimeField()
    sender = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconSender_employee")
    receiver = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconReceived_employee")
    remarks = models.CharField(max_length=255)
    
    def __str__(self):
        return self.accountNumber.account