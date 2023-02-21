# Generated by Django 4.1.7 on 2023-02-21 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0003_feed_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feed",
            old_name="comment_count",
            new_name="likes_count",
        ),
        migrations.RenameField(
            model_name="feed",
            old_name="likes",
            new_name="reivews_count",
        ),
        migrations.AddField(
            model_name="feed",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="feed",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="feed",
            name="caption",
            field=models.CharField(blank="", default="", max_length=1000),
        ),
    ]
