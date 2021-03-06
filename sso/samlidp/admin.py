from django.contrib import admin

from .models import SamlApplication


@admin.register(SamlApplication)
class SamlApplicationAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'entity_id', 'start_url', 'allow_access_by_email_suffix', 'enabled')
    prepopulated_fields = {'slug': ('name',)}
