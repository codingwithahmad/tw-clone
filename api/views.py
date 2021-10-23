from django.shortcuts import render
from account.models import User, UserFollowing
from twit.models import Twit, Likes, Retweet
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def follow(request, app_name, url_name, username):
	user = request.user
	author = get_object_or_404(User, username=username)

	if UserFollowing.objects.filter(Q(user_id=request.user) & Q(following_user_id=author)).exists():
		UserFollowing.objects.filter(Q(user_id=request.user) & Q(following_user_id=author)).delete()
	else:
		following_user = UserFollowing(user_id=request.user,following_user_id=author)
		following_user.save()
			

	link = "{}:{}".format(app_name, url_name)

	return redirect(reverse_lazy(link, kwargs={'username': username}))



def like(request, app_name, url_name, pk):
	user = request.user
	twit = get_object_or_404(Twit, pk=pk)
	if Likes.objects.filter(Q(users=user) & Q(twits=twit)).exists():
		Likes.objects.filter(Q(users=user) & Q(twits=twit)).delete()
	else:
		t_like = Likes(users=user, twits=twit)
		t_like.save()
	link = "{}:{}".format(app_name, url_name)

	return redirect(link)


def like_info(request, pk):
	twit = get_object_or_404(Twit, pk=pk)
	return JsonResponse({
			"likes": twit.like_count,
			"retweet": twit.retweet_count
	})

def follow_info(request, username):
	is_following = False
	user = get_object_or_404(User, username=username)
	followers = user.followers.all()

	if request.user in followers:
		is_following = True

	return JsonResponse({
		"is_following": is_following
	})





def retweet(request, app_name, url_name, pk):
	user = request.user
	twit = get_object_or_404(Twit, pk=pk)
	if Retweet.objects.filter(Q(user=user) & Q(twit=twit)).exists():
		Retweet.objects.filter(Q(user=user) & Q(twit=twit)).delete()
	else:
		t_retweet = Retweet(user=user, twit=twit)
		t_retweet.save()
	link = "{}:{}".format(app_name, url_name)

	return redirect(link)