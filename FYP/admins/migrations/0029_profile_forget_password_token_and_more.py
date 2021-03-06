# Generated by Django 4.0.3 on 2022-04-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0028_profile_remove_employee_department_delete_attendance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.department'),
        ),
    ]
