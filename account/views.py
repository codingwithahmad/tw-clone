from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from twit.models import Twit
from .forms import MyForm
from .models import User
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

		# return HttpResponseRedirect(reverse_lazy('account:tw'))

	def get_context_data(self, **kwargs):
		context = super(Twit, self).get_context_data(**kwargs)
		context['object_list'] = self.request.user.user_twit.all()
		return context

class Login(LoginView):
	def get_success_url(self):
		user = self.request.user

		if user.is_authenticated:
			return reverse_lazy('twits:TimeLine')

class Profile(ListView):
	template_name = "registration/profile.html"



	def get_queryset(self):
		global author
		username = self.kwargs.get("username")
		author = get_object_or_404(User, username=username)
		return author.user_twit.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		print(author)
		return context

