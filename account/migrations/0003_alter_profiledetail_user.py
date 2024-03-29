# Generated by Django 5.0.1 on 2024-01-18 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profiledetail_email_profiledetail_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='real_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
