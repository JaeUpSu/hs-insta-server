from django.shortcuts import render
from .models import User
from users.models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from rest_framework.permissions import IsAuthenticated

class Users(APIView):
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Modify_User(APIView):
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, user_id):
        model = self.get_object(user_id)
        serializer = UserSerializer(model)
        return Response(serializer.data)
    
    # def get(self, request):
    #     user = request.user # 한개만 가져옴
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
        
    def put(self,request,user_id):
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response("invalid request")
            

class Get_User(APIView):
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get_object(self, _username):
        try:
            return User.objects.get(username=_username)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        model = self.get_object(username)
        serializer = UserSerializer(model)
        return Response(serializer.data)
    