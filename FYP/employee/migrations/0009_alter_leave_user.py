# Generated by Django 4.0.3 on 2022-04-17 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0037_alter_profile_department'),
        ('employee', '0008_alter_leave_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.customuser'),
        ),
    ]
