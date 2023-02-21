from django.db import models
from users.models import User
from common.models import CommonModel

# CommonModel 상속
class Feed(CommonModel):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    img= models.URLField(blank=True)
    caption= models.CharField(max_length=1000, blank="", default="")
    likes_count= models.PositiveIntegerField(default=0)
    reviews_count= models.PositiveIntegerField(default=0)
        
    def __str__(self) -> str:
        return str(self.pk)