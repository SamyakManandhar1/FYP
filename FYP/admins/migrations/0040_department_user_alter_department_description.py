# Generated by Django 4.0.3 on 2022-04-24 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0039_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
