from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

class Twit(models.Model):
	twit = models.TextField(max_length=280, verbose_name="توییت")
	img = models.ImageField(upload_to='images', blank=True, null=True)
	author = models.ForeignKey(User, related_name="user_twit", verbose_name="نویسنده", on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now(), verbose_name="زمان انتشار")

	def __str__(self):
		return "{} - {}".format(self.author, self.twit)

	class Meta:
		verbose_name = "توییت"
		verbose_name_plural = "توییت ها"