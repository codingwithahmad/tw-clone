from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from twit.models import Likes, Retweet, Twit
from rest_framework.generics import (
	RetrieveAPIView,
	ListAPIView,
	CreateAPIView,
	DestroyAPIView,
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
		username = self.request.POST.get('username')

		link = "{}:{}".format(app_name, url_name)

		if username is not None:
			return redirect(reverse_lazy(link, kwargs={ "username": username }))
		else:
			return redirect(link)



class MakeRetweet(CreateAPIView):
	queryset = Retweet.objects.all()
	serializer_class = RetweetSerializer

class DeleteLike(DestroyAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer


class Twits(ListAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer

class TwitDetails(RetrieveAPIView):
	queryset = Twit.objects.all()
	serializer_class = TwitSerializer
