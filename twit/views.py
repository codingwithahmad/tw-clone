from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Twit
from account.forms import MyForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Twit
from django.shortcuts import get_object_or_404
# Create your views here.

class TimeLine(LoginRequiredMixin, ListView):
	template_name = "twit/timeLine.html"
	context_name = "twits"
	# queryset = Twit.objects.all()
	
	def get_queryset(self):
		following_list = self.request.user.following.all()
		print(following_list)
		if following_list:
			for f in following_list:
					return Twit.objects.filter(Q(author=self.request.user) | Q(author=f.following_user_id)).order_by('-created')
		else:
			return Twit.objects.filter(author=self.request.user)			

	def post(self, request, *args, **kwargs):
		self.form = MyForm(request.POST, request.FILES)
		twit = self.form.save(commit=False)
		twit.author = request.user
		twit.save()

		return HttpResponseRedirect(reverse_lazy('twits:TimeLine'))

class TwitDetail(DetailView):
	template_name = 'twit/twit.html'
	context_object_name = "twit"



	def get_object(self):
		pk = self.kwargs.get('pk')
		twit = get_object_or_404(Twit, pk=pk)

		return twit