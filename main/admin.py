from django.contrib import admin

from main.models import Customer, Newsletter, Message


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fio', 'email', 'comment',)
    search_fields = ('fio',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'message_body',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'interval', 'status',)
    list_filter = ('status',)
    search_fields = ('status', 'customer',)
