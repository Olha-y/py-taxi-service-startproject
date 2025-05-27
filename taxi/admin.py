from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)

@admin.register(Manufacturer)
class ManufacturerAdmin(ModelAdmin):
    list_display = ModelAdmin.list_display + ("country",)


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ModelAdmin.list_display + ("model",)
    search_fields = ModelAdmin.search_fields + ("model",)
    list_filter = ModelAdmin.list_filter + ("manufacturer",)
