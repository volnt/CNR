# Generated by Django 3.2.15 on 2022-09-20 13:03

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("public_website", "0004_alter_subscription_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="participant",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
