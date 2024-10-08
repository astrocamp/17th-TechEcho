# Generated by Django 5.1.1 on 2024-09-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0004_alter_votes_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="title",
            field=models.CharField(
                error_messages={"max_length": "問題標題不能超過五十個字"}, max_length=50
            ),
        ),
    ]
