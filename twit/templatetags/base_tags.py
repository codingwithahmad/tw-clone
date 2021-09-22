from django import template
from account.forms import MyForm
from django.http import HttpResponse
from django.urls import reverse_lazy

register = template.Library()


@register.inclusion_tag('twit/partial/create_twit.html', takes_context=True)
def twit_bar(context):
	request = context['request']
	user = request.user
	return {'form': MyForm, 'user': user }