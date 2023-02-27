from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer, ReviewPostSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from rest_framework.permissions import IsAuthenticated

class Reviews(APIView):
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get(self, request):
        model = Review.objects.all()
        serializer = ReviewSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
class Modify_Review(APIView):
    ## 로그인한 유저만 허용한다라는 의미.
    permission_classes = [IsAuthenticated]
    def get_object(self, review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise NotFound

    def get(self, request, review_id):
        model = self.get_object(review_id)
        serializer = ReviewSerializer(model)
        return Response(serializer.data)
    
    # def get(self, request):
    #     Review = request.Review # 한개만 가져옴
    #     serializer = ReviewSerializer(Review)
    #     return Response(serializer.data)
        
    def put(self,request,review_id):
        review = Review.objects.get(pk=review_id)
        serializer = ReviewSerializer(review, data=request.data)
        
        if serializer.is_valid():
            review = serializer.save()
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            return Response("invalid request")
            
    def delete(self,request,review_id):
        review = Review.objects.get(pk=review_id)
        review.delete()
        return Response("success delete")
   