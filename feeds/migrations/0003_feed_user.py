# Generated by Django 4.1.7 on 2023-02-21 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feeds", "0002_feed_caption_feed_comment_count_feed_img_feed_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]