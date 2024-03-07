from django.contrib import admin

from .models import Characteristic, Vehicle


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', )
    ordering = ('-pk', )


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'year', 'type', 'active' )
    search_fields = ('model_name', 'year' )
    ordering = ('-pk', )


admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Vehicle, VehicleAdmin)
