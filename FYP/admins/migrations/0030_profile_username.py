# Generated by Django 4.0.3 on 2022-04-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0029_profile_forget_password_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
