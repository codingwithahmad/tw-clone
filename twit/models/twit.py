from django.db import models
from account.models import User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse_lazy





class Twit(models.Model):
	twit = models.TextField(max_length=280, verbose_name="توییت")
	img = models.ImageField(upload_to='images', blank=True, null=True)
	author = models.ForeignKey(User, related_name="user_twit", verbose_name="نویسنده", on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
	comments = GenericRelation(Comment)

	@property
	def like_count(self):
		return self.likes.all().count()

	@property
	def retweet_count(self):
		return self.retweet.all().count()
		
	def __str__(self):
		return "{} - {}".format(self.author, self.twit)

	class Meta:
		verbose_name = "توییت"
		verbose_name_plural = "توییت ها"