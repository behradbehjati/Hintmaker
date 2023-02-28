from django.contrib import admin
from .models import MakeHint

class MakeHintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'site_name')
admin.site.register(MakeHint, MakeHintAdmin)
