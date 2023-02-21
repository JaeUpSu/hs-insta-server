# Generated by Django 4.1.7 on 2023-02-21 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
