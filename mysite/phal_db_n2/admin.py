from django.contrib import admin

# Register your models here.

from .models import V3Deg
class V3DegAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in V3Deg._meta.fields[1:])
    # def dataset(self):
    #     return self.dataset
    # dataset.short_description = 'MY_DATE'
    # using = 'phal_db_n2'
admin.site.register(V3Deg, V3DegAdmin)


