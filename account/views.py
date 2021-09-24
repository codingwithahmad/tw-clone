from django.shortcuts import render
from django.views.generic.edit import CreateView
from twit.models import Twit
from .forms import MyForm
from .mixins import FormValid
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
# Create your views here.

class Twit(CreateView):
	model = Twit
	form_class = MyForm
	# success_url = reverse_lazy('twits:TimeLine')
	template_name = "registration/create_twit.html"


	def form_valid(self, form):
		tw = form.save(commit=False)
		tw.author = self.request.user
		tw.save()

		return HttpResponseRedirect(reverse_lazy('twits:TimeLine'))

class Login(LoginView):
	def get_success_url(self):
		user = self.request.user

		if user.is_authenticated:
			return reverse_lazy('twits:TimeLine')