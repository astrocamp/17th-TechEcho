# Generated by Django 5.1.1 on 2024-09-15 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_chatgroup_members_online"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chatgroup",
            name="members_online",
        ),
        migrations.AddField(
            model_name="chatgroup",
            name="members_online",
            field=models.ManyToManyField(
                blank=True, related_name="online_group", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
