from django.db import models
from users.models import User
from feeds.models import Feed
from common.models import CommonModel
# Create your models here.
class Review(CommonModel):
    feed= models.ForeignKey(Feed, on_delete=models.CASCADE, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    caption= models.TextField(max_length=100, blank="", default="")
    