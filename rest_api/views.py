from django.shortcuts import render, redirect
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

	def post(self, *args, **kwargs):
		super().post(*args, **kwargs)
		url_name = self.request.POST.get('url_name')
		app_name = self.request.POST.get('app_name')

		link = "{}:{}".format(app_name, url_name)


		return redirect(link)



class MakeRetweet(CreateAPIView):
	queryset = Retweet.objects.all()
	serializer_class = RetweetSerializer



class Twits(ListAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer

class TwitDetails(RetrieveAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer
