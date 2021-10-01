from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	profile_photo = models.ImageField(upload_to='images/profile_photo', verbose_name="عکس پروفایل", default="default.jpg")

	bio = models.TextField(max_length=280, null=True, verbose_name="بیوگرافی")

