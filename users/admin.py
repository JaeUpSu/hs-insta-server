from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUsersAdmin(UserAdmin):
    list_display=("pk","username","img","info","followerNumber",)