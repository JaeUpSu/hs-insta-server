from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        
        # fields = "__all__" 은 모두 
        fields = ("pk","username","img","info","followerNumber",)
        