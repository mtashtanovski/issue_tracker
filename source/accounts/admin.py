from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from accounts.models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    fields = ("birth_date", "avatar", "git_profile", "about_me")
    model = Profile


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
