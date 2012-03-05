# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.models import AuthorProfile

class ProfileInline(admin.StackedInline):
  model = AuthorProfile
  fk_name = 'user'
  max_num = 1

class CustomUserAdmin(UserAdmin):
  inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)