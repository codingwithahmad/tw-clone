from django.template.response import TemplateResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView
from twit.models import Twit
from .forms import MyForm, FollowForm, SignUpForm
from .models import User, UserFollowing
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.db.models import Q
from .mixins import EditProfileMixin
# Create your views here.

class Login(LoginView):
	def get_success_url(self):
		user = self.request.user

		if user.is_authenticated:
			return reverse_lazy('twits:TimeLine')

class Profile(ListView):
	template_name = "registration/profile.html"


	def get_queryset(self):
		global author
		username = self.kwargs.get("username")
		author = get_object_or_404(User, username=username)
		return author.user_twit.all().order_by('-created')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context

	def post(self, request, *args, **kwargs):
		
		self.twForm = MyForm(request.POST, request.FILES)
		twit = self.twForm.save(commit=False)
		twit.author = request.user
		twit.save()
		

		return HttpResponseRedirect(reverse_lazy('account:profile', kwargs={'username': author.username}))

class EditProfile(EditProfileMixin, UpdateView):
	model = User
	fields = ['username', 'first_name', 'last_name', 'bio', 'profile_photo']
	template_name = 'registration/edit_profile.html'

	def get_success_url(self):
		return reverse_lazy('account:profile', kwargs={'username': self.request.user.username})






from django.contrib.auth import login, authenticate
from .tokens import account_activation_token
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage




	
class Registration(CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'


	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = False
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = "???????? ???????? ???????? ????????????"
		message = render_to_string('registration/activate_account.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			'token': account_activation_token.make_token(user)
		})
		
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
			mail_subject, message, to=[to_email]
		)

		email.send()
		return TemplateResponse(self.request, 'registration/activate_link_send.html', {})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return TemplateResponse(request, 'registration/activate_confirm.html', {})
    else:
        return HttpResponse('???????? ???????? ???????? ?????????????? ??????. <a href="account/register" > ???????????? ???????????? ???????? </a>')


def handel404(request, exception):
	response = render(request, "404.html", {"exception": exception})
	response.status_code = 404
	return response   