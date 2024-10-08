# Generated by Django 5.1.1 on 2024-09-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_blog_is_draft"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="blog",
            name="category",
        ),
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name="blog",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="blogs", to="blogs.tag"
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
