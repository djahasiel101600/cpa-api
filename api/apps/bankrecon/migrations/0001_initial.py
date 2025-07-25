# Generated by Django 5.2.3 on 2025-07-23 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountNumber',
            fields=[
                ('id', models.CharField(editable=False, max_length=12, primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AccountNumber_User', to=settings.AUTH_USER_MODEL)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountNumber_fund', to='core.fund')),
            ],
        ),
        migrations.CreateModel(
            name='BankRecon',
            fields=[
                ('id', models.CharField(editable=False, max_length=12, primary_key=True, serialize=False)),
                ('asOf', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('dateReceived', models.DateTimeField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('accountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankRecon_accountNumber', to='bankrecon.accountnumber')),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BankRecon_User', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankRecon_office', to='core.office')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankReconReceived_employee', to='core.employee')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankReconSender_employee', to='core.employee')),
            ],
        ),
    ]
