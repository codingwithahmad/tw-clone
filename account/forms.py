from crispy_forms.helper import FormHelper
from django import forms
from twit.models import Twit


class MyForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False		 

	class Meta:
		model = Twit
		fields = ["twit", "img", "author"]