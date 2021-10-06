from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Twit
from account.forms import MyForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

class TimeLine(LoginRequiredMixin, ListView):
	template_name = "twit/timeLine.html"
	context_name = "twits"

	def get_queryset(self):
		following_list = self.request.user.following.all()
		for f in following_list:
				return Twit.objects.filter(Q(author=self.request.user) | Q(author=f.following_user_id)).order_by('-created')

	def post(self, request, *args, **kwargs):
		self.form = MyForm(request.POST, request.FILES)
		twit = self.form.save(commit=False)
		twit.author = request.user
		twit.save()

		return HttpResponseRedirect(reverse_lazy('twits:TimeLine'))

