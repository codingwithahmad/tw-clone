from crispy_forms.helper import FormHelper
from django import forms
from twit.models import Twit
from .models import UserFollowing, User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm

class MyForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False		 

	# def form_valid(self, form):
	# 	self.obj = form.save(commit=False)
	# 	self.obj.author = self.request.user
	# 	return super(MyForm, self).form_valid(form)

	# def form_valid(self, form):
	# 	tw = form.save(commit=False)
	# 	tw.author = self.request.user
	# 	tw.save()

	# 	return HttpResponseRedirect(reverse_lazy('account:tw'))

	# def save(self):
	# 	twit = super(MyForm, self).save(commit=False)
	# 	twit.author = self.request.user
	# 	twit.save()
	# 	return twit

	
	class Meta:
		model = Twit
		fields = ["twit", "img"]

class FollowForm(forms.ModelForm):
	class Meta:
		model = UserFollowing
		fields = []

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=200)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']