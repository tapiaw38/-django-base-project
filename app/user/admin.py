# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.user.models import User, Profile
# Register your models here.


class CustomUserAdmin(UserAdmin):
    """ User model admin. """
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile model admin ."""
    pass


admin.site.register(User, CustomUserAdmin)
