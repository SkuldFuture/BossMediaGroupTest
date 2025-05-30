from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'last_login', 'is_superuser',
                    'username', 'first_name', 'last_name', 'email',
                    'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')