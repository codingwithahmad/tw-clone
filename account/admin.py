from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
										'is_staff',
										'profile_photo',
										'is_superuser',
										'groups',
										'user_permissions',
										'bio',
)



admin.site.register(User, UserAdmin)
