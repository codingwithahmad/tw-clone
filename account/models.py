from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.




class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name="ایمیل")

	profile_photo = models.ImageField(upload_to='images/profile_photo', verbose_name="عکس پروفایل", default="media/images/default.jpg")

	bio = models.TextField(max_length=280, blank=True, verbose_name="بیوگرافی")

	


	

class UserFollowing(models.Model):
	user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)

	following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)