from django.contrib import admin
from .models import Twit, Likes
# Register your models here.
@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
	pass

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
	pass