# Generated by Django 4.0.3 on 2022-04-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_remove_department_history_department_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp129', max_length=70),
        ),
    ]
