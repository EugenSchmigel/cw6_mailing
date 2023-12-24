from django.contrib import admin

from main.models import Customer, Newsletter


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fio', 'email', 'comment',)
    search_fields = ('fio',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'interval', 'status',)
    list_filter = ('status',)
    search_fields = ('status', 'customer',)
