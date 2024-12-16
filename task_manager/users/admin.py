from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users


class UsersAdmin(UserAdmin):
    model = Users
    list_display = ["username"]


admin.site.register(Users, UsersAdmin)
