from django.db import models
from users.models import User
from common.models import CommonModel

# CommonModel 상속
class Feed(CommonModel):
    img= models.URLField(blank=True)
    caption= models.CharField(max_length=1000, blank="", default="")
    likes_count= models.PositiveIntegerField(default=0)
    reviews_count= models.PositiveIntegerField(default=0)
   
    # 1:N (User:Feed)     
    user= models.ForeignKey(
        User,
        ## user 삭제시 feed 도 삭제 
        on_delete=models.CASCADE, 
        ## reverse accesor 에서 불러올 이름 수정
        ## (users.feed_set.all() -> users.feeds.all())
        related_name="feeds"
    )
   
    def __str__(self) -> str:
        return str(self.pk)