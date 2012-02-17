from django.contrib import admin
from tastypie.models import ApiKey
from app.models import Beloved

def tags(instance):
    return ', '.join(instance.tags)

class BelovedAdmin(admin.ModelAdmin):
    list_display = ['name', tags]

admin.site.register(Beloved, BelovedAdmin)
