from django.contrib import admin

# Register your models here.

from cirugia.models import OrganosCirugias, IntervencionCirugias, TiposHeridasOperatorias, PlanificacionCirugia,  FinalidadCirugia, GravedadCirugia, ZonasCirugia


@admin.register(OrganosCirugias)
class organosCirugiasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(IntervencionCirugias)
class intervencionCirugiasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)



@admin.register(TiposHeridasOperatorias)
class tiposHeridasOperatoriasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)



@admin.register(FinalidadCirugia)
class finalidadCirugiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)



@admin.register(PlanificacionCirugia)
class planificacionCirugiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)


@admin.register(ZonasCirugia)
class zonasCirugiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(GravedadCirugia)
class gravedadCirugiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)
