from django import template
from account.forms import MyForm, FollowForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from ..models import Twit
from django.shortcuts import get_object_or_404
from account.models import User, UserFollowing
from django.db.models import Q


register = template.Library()


@register.inclusion_tag('twit/partial/create_twit.html', takes_context=True)
def twit_bar(context):
	request = context['request']
	user = request.user
	if "author" in context:
		if context['author'] == user:
			return {'form': MyForm }
	else:
		return {'form': MyForm }

	


@register.inclusion_tag("registration/partial/followـinfo.html", takes_context=True)
def follow_info(context):
	author = context['author']
	twits = len(author.user_twit.all())
	following = len(author.following.all())
	followers = len(author.followers.all())
	return { 'user': author, 'twits': twits, 'following': following, 'followers': followers }

@register.inclusion_tag('registration/partial/following.html')
def following(request, url_name, app_name, username):
	is_following = False
	author = get_object_or_404(User, username=username)
	user = request.user
	if UserFollowing.objects.filter(Q(user_id=user) & Q(following_user_id=author)).exists():
		is_following = True
	else:
		is_following = False


	# if author != user:
	# 	return {'follow_form': FollowForm, 'btn_name': button_name }

	return {
		"request": request,
		"username": username,
		"app_name": app_name,
		"url_name": url_name,
		"is_following": is_following
	}



@register.inclusion_tag('twit/partial/like.html')
def like(request, count, pk, url_name, app_name):
	is_liked = None
	twit = Twit.objects.get(pk=pk)
	if twit.likes.filter(users=request.user).exists():
		is_liked = True
	else:
		is_liked = False


	return {
		"request": request,
		"pk": pk,
		"app_name": app_name,
		"url_name": url_name,
		"count": count,
		"is_liked": is_liked
	}

@register.inclusion_tag('twit/partial/retweet.html')
def retweet(request, count, pk, url_name, app_name):
	return {
		"request": request,
		"pk": pk,
		"app_name": app_name,
		"url_name": url_name,
		"count": count,
	}

@register.inclusion_tag('twit/partial/userbox.html')
def box(request, url_name, app_name):
	following = request.user.following.all()
	f_list = [f.following_user_id.pk for f in following]
	f_list.append(request.user.pk)
	users = User.objects.exclude(pk__in=f_list)

	return {
		"users": users,
		"url_name": url_name,
		"app_name": app_name
	}