from django.contrib import admin

from users.models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('pk', 'email', 'is_active', 'email_verified', 'country')