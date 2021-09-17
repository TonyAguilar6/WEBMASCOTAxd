from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class resourcemascota(resources.ModelResource):
    class Meta:
        model = mascota

class adminmascota(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['type', 'color', 'age', 'state']
    resource_class = resourcemascota

admin.site.register(mascota, adminmascota)

"""-----------------------------"""
class resourceclient(resources.ModelResource):
    class Meta:
        model = client

class adminclient(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['tel', 'direction']
    resource_class = resourceclient

admin.site.register(client, adminclient)
"""-----------------------------"""
class resourcedate(resources.ModelResource):
    class Meta:
        model = date

class admindate(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['day']
    list_display = ['hour']
    resource_class = resourcedate

admin.site.register(date, admindate)