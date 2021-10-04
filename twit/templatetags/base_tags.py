from django import template
from account.forms import MyForm, FollowForm
from django.http import HttpResponse
from django.urls import reverse_lazy
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

@register.inclusion_tag('registration/partial/following.html', takes_context=True)
def following(context):
	button_name = None
	author = context['author']
	user = context['request'].user
	if UserFollowing.objects.filter(Q(user_id=user) & Q(following_user_id=author)).exists():
		button_name = "دنبال نکردن"
	else:
		button_name = "دنبال کردن"


	if author != user:
		return {'follow_form': FollowForm, 'btn_name': button_name }