from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Twit
from account.forms import MyForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TimeLine(LoginRequiredMixin, ListView):
	model = Twit
	template_name = "twit/timeLine.html"
	context_name = "twits"

	def post(self, request, *args, **kwargs):
		self.form = MyForm(request.POST, request.FILES)
		twit = self.form.save(commit=False)
		twit.author = request.user
		twit.save()

		return HttpResponseRedirect(reverse_lazy('twits:TimeLine'))

