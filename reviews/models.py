from django.db import models
from users.models import User
from feeds.models import Feed
from common.models import CommonModel
# Create your models here.
class Review(CommonModel):
    caption= models.TextField(max_length=100, blank="", default="")
    
    # 1:N (User:Review or Feed:Review) 
    user= models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="reviews"
    )
    
    feed= models.ForeignKey(
        Feed, 
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    