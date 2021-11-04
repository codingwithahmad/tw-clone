from django.shortcuts import render
from twit.models import Likes, Retweet, Twit
from rest_framework.generics import (
	RetrieveAPIView,
	ListAPIView,
	CreateAPIView,
)
from .serializers import LikeSerializer, RetweetSerializer, TwitSerializer
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


class MakeLike(CreateAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer


class MakeRetweet(CreateAPIView):
	queryset = Retweet.objects.all()
	serializer_class = RetweetSerializer



class Twits(ListAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer

class TwitDetails(RetrieveAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer
