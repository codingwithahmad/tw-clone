from django.shortcuts import render
from twit.models import Likes, Retweet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import LikeSerializer, RetweetSerializer
# Create your views here.

class LikeView(ListAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer

class LikeDetails(RetrieveAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer

class RetweetView(ListAPIView):
	queryset = Retweet.objects.all()
	serializer_class = RetweetSerializer

class RetweetDetails(RetrieveAPIView):
	queryset = Retweet.objects.all()
	serializer_class = RetweetSerializer