from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "profile_picture")
    search_fields = ("username", "bio", "profile_picture")

    def username(self, obj):
        return obj.user.username
    username.admin_order_field = 'user__username'