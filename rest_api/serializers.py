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
	is_liked = serializers.SerializerMethodField('check_like')
	like_pk = serializers.SerializerMethodField('like_info')

	def check_like(self, obj):
		return obj.likes.filter(users=self.context['request'].user).exists()

	def like_info(self, obj):
		likes = obj.likes.all()
		for like in likes:
			if like.users == self.context['request'].user:
				return { "pk": like.pk }


	class Meta:
		model = Twit
		fields = ['id', 'twit', 'author', 'created', 'like_count', 'retweet_count', 'is_liked', 'like_pk']