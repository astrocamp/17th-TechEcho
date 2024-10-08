# Generated by Django 5.1.1 on 2024-09-25 01:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0006_remove_blog_tags_remove_blog_comments_count_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_blogs", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
