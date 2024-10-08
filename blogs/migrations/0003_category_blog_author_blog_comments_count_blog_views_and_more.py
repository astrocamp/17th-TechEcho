# Generated by Django 5.1.1 on 2024-09-14 05:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_rename_article_blog"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogs",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="comments_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blog",
            name="views",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blogs.category",
            ),
        ),
    ]
