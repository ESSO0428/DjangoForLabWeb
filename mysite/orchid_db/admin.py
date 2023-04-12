from django.contrib import admin

# Register your models here.
from .models import Orchid

class OrchidAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Orchid._meta.fields[1:])
    # def dataset(self):
    #     return self.dataset
    # dataset.short_description = 'MY_DATE'
admin.site.register(Orchid, OrchidAdmin)

