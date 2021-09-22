from django.shortcuts import render
from django.views.generic.edit import CreateView
from twit.models import Twit
from .forms import MyForm
from .mixins import FormValid
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class Twit(CreateView):
	model = Twit
	form_class = MyForm
	template_name = "registration/create_twit.html"


	def form_valid(self, form):
		tw = form.save(commit=False)
		tw.author = self.request.user
		tw.save()

		return HttpResponseRedirect(reverse_lazy('twits:TimeLine'))

