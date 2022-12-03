from django.contrib import admin

# Register your models here.
from .models import Inmueble

class InmuebleAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(Inmueble, InmuebleAdmin)    