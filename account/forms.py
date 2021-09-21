from crispy_forms.helper import FormHelper
from django import forms
from twit.models import Twit


class MyForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False		 

	# def form_valid(self, form):
	# 	twit = form.save(commit=False)
	# 	user = self.request.user
	# 	twit.user = user
	# 	twit.save()
	# 	return super(MyForm, self).form_valid(form)

	class Meta:
		model = Twit
		fields = ["twit", "img", "author"]