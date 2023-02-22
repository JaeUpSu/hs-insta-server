from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Feed
from reviews.models import Review
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Feed
        
        # fields = "__all__" 은 모두 
        fields = ("img","caption","likes_count","reviews_count","user","reviews",)
        
   