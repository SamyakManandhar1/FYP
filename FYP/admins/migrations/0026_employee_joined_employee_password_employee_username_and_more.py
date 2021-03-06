# Generated by Django 4.0.3 on 2022-04-13 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0025_employee_accnum_employee_address_employee_bank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp677', max_length=70),
        ),
    ]
