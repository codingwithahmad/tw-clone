from django.shortcuts import render
from django.views.generic.edit import CreateView
from twit.models import Twit
from .forms import MyForm
from .mixins import FormValid
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
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

