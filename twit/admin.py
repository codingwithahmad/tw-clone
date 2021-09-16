from django.contrib import admin
from .models import Twit
# Register your models here.
@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
	pass