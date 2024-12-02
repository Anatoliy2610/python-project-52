from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin



# @admin.register(Users)
class UsersAdmin(UserAdmin):

    model = Users
    list_display = ["username"]


admin.site.register(Users, UsersAdmin)

