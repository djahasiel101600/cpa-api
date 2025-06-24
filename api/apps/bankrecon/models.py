from django.db import models

# Create your models here.
class Fund(models.Model):
    fundName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.fundName


class Office(models.Model):
    officeName = models.CharField(max_length=100)
    officeLocation = models.CharField(max_length=255)
    officeAgency = models.CharField(max_length=255, null=True)
    
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
    accountNumber = models.CharField(max_length=24)
    asOf = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    fund = models.ForeignKey(Fund, models.CASCADE, related_name="bankRecon_fund")
    office = models.ForeignKey(Office, models.CASCADE, related_name="bankRecon_office")
    dateReceived = models.DateTimeField()
    sender = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconSender_employee")
    receiver = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconReceived_employee")
    remarks = models.CharField(max_length=255)
    
    def __str__(self):
        return self.accountNumber