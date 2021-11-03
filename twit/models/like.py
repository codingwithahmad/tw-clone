from django.db import models
from account.models import User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse_lazy
from .twit import Twit



class Likes(models.Model):
	users = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

	twits = models.ForeignKey(Twit, related_name="likes", on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)