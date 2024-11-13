from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone', 'address')