from crispy_forms.helper import FormHelper
from django import forms
from twit.models import Twit
from django.urls import reverse_lazy, reverse

class MyForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False		 

	# def form_valid(self, form):
	# 	self.obj = form.save(commit=False)
	# 	self.obj.author = self.request.user
	# 	return super(MyForm, self).form_valid(form)

	# def save(self):
	# 	twit = super(MyForm, self).save(commit=False)
	# 	twit.author = self.request.user
	# 	twit.save()
	# 	return twit

	
	class Meta:
		model = Twit
		fields = ["twit", "img"]