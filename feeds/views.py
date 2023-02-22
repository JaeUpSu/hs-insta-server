from django.shortcuts import render
from .models import Feed
from users.models import User
from .serializers import FeedSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

class Feeds(APIView):
        ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get(self, request):
        model = Feed.objects.all()
        serializer = FeedSerializer(model, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

     
class FeedsByUsername(APIView):
    
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get_objects(self, _username):
        try:
            user = User.objects.get(username=_username)
            return Feed.objects.filter(user=user)
        except Feed.DoesNotExist or User.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        model = self.get_objects(username)
        serializer = FeedSerializer(model, many=True)
        return Response(serializer.data)
        
        

class Modify_Feed(APIView):
    
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(pk=feed_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, feed_id):
        model = self.get_object(feed_id)
        serializer = FeedSerializer(model)
        return Response(serializer.data)
    
    def put(self,request,feed_id):
        feed = Feed.objects.get(pk=feed_id)
        serializer = FeedSerializer(feed, data=request.data)
        
        if serializer.is_valid():
            feed = serializer.save()
            serializer = FeedSerializer(feed)
            return Response(serializer.data)
        else:
            return Response("invalid request")
            
   