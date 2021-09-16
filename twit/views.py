from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Twit
# Create your views here.

class TimeLine(ListView):
	model = Twit
	template_name = "twit/timeLine.html"
	context_name = "twits"
