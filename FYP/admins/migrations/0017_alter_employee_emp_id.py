# Generated by Django 4.0.3 on 2022-04-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0016_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp476', max_length=70),
        ),
    ]