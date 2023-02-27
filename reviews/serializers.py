from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import UserSerializer
class ReviewSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Review
        
        # fields = "__all__" 은 모두 
        fields = ("pk","feed","caption","user",)
        
class ReviewPostSerializer(ModelSerializer):
    class Meta:
        model = Review
        
        # fields = "__all__" 은 모두 
        fields = ("pk","feed","caption","user",)
        
