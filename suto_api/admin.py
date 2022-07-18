from django.contrib import admin

from suto_api.models import Apartment

@admin.action(description="Освободить")
def change_status_free(self, request, queryset):
    queryset.update(status='С')
    
@admin.action(description="Занять")
def change_status_busy(self, request, queryset):
    queryset.update(status='З')

class ApartmentAdmin(admin.ModelAdmin):
    model = Apartment
    list_display = ('name', 'type', 'address', 'address_details', 'status')

    actions = [change_status_free, change_status_busy]

admin.site.register(Apartment, ApartmentAdmin)