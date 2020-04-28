from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Exhibit

admin.site.site_header = 'Богд хааны ордон музей - Удирдлага'

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('title', 'nfc_id', 'created')
    list_filter = ('created',)

admin.site.register(Exhibit, ExhibitAdmin)
admin.site.unregister(Group)

