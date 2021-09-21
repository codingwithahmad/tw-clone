from django import template
from account.forms import MyForm


register = template.Library()


@register.inclusion_tag('twit/partial/create_twit.html', takes_context=True)
def twit_bar(context):
	user = context['request'].user
	return {'form': MyForm, 'user': user }