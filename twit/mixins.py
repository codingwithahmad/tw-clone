from django.http import Http404
from .models import Likes, Twit
from .forms import LikesForm
from django.shortcuts import get_object_or_404

class LikesRequestMixin():
	def post(self, request, *args, **kwargs):
		if kwargs.get('twit_pk'):
			pk = kwargs.get('twit_pk')
			twit = get_object_or_404(Twit, pk=pk)
			self.likeform = LikesForm(request.POST)
			like = self.likeform.save(commit=False)
			like.user = request.user
			like.twits = twit
			like.save()

		return super().post(request, *args, **kwargs)

