from django.shortcuts import render
from django.views.generic.edit import CreateView
from twit.models import Twit
from .forms import MyForm
# Create your views here.

class Twit(CreateView):
	model = Twit
	form_class = MyForm
	template_name = "registration/create_twit.html"
