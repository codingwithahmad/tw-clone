from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Twit
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TimeLine(LoginRequiredMixin, ListView):
	model = Twit
	template_name = "twit/timeLine.html"
	context_name = "twits"
