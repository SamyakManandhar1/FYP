# Generated by Django 4.0.3 on 2022-04-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0023_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
    ]