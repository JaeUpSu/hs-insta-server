from django.db import models
from users.models import User

# Create your models here.
class Feed(models.Model):
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    img: models.TextField()
    caption: models.TextField()
    