# Generated by Django 4.0.3 on 2022-04-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0013_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp457', max_length=70),
        ),
    ]
