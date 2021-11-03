from django.db import models
from account.models import User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse_lazy
from .twit import Twit



class Retweet(models.Model):
	user = models.ForeignKey(User, related_name="retweet", on_delete=models.CASCADE)

	twit = models.ForeignKey(Twit, related_name="retweet", on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)