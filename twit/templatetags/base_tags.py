from django import template
from account.forms import MyForm, FollowForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from account.models import User

register = template.Library()


@register.inclusion_tag('twit/partial/create_twit.html', takes_context=True)
def twit_bar(context):
	request = context['request']
	user = request.user
	return {'form': MyForm, 'user': user }

@register.inclusion_tag("registration/partial/follow.html", takes_context=True)
def following(context):
	author = context['author']
	twits = len(author.user_twit.all())
	return { 'user': author, 'form': FollowForm, 'twits': twits }