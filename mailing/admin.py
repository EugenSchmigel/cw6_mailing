from django.contrib import admin

from mailing.models import Client, Mailing, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment', 'owner',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'period', 'status',)
    list_filter = ('status',)
    search_fields = ('status',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'mailing', 'error_msg')
    list_filter = ('status',)
    search_fields = ('status',)