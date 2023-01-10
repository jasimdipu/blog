from django.contrib import admin
from .models import User


# Register your models here.
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['created_at', 'is_staff', 'is_active']
    ordering = ['-created_at']
    list_editable = ['is_staff', 'is_active', 'is_superuser']
    readonly_fields = ['password']


admin.site.register(User, UsersModelAdmin)