from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    img = models.URLField(blank=True)
    info = models.TextField(max_length=150,blank="")
    followerNumber = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.pk)