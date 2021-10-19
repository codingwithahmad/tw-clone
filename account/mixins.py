from django.http import HttpResponseNotFound

class EditProfileMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		if request.user.pk == pk:
			return super().dispatch(request, *args, **kwargs)
		else:
			return HttpResponseNotFound("شما اجازه دسترسی به این بخش را ندارید")  