from django.contrib import admin

from boss_test.apps.parser.models import TechCompany


@admin.register(TechCompany)
class TechCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
