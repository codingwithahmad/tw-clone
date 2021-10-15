from django import forms
from .models import Likes

class LikesForm(forms.ModelForm):
	class Meta:
		model = Likes
		fields = []