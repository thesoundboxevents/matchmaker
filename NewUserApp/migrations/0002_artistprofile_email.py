# Generated by Django 4.2.7 on 2023-12-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NewUserApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="artistprofile",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
    ]
