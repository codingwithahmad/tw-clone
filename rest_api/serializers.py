from twit.models import Likes, Retweet, Twit
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):


	class Meta:
		model = Likes
		fields = '__all__'


class RetweetSerializer(serializers.ModelSerializer):


	class Meta:
		model = Retweet
		fields = '__all__'


class TwitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Twit
		fields = ['id', 'twit', 'author', 'created', 'like_count', 'retweet_count']