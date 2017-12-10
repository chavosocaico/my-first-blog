from django.contrib import admin
from .models import Sala, Material, ReservarSala, ReservarMaterial
# Register your models here.

admin.site.register(Sala)
admin.site.register(Material)
admin.site.register(ReservarSala)
admin.site.register(ReservarMaterial)