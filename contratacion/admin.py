from django.contrib import admin

# Register your models here.


from clinico.models import TiposExamen
from contratacion.models import  Procedimientos, Convenios


@admin.register(Procedimientos)
class procedimientosAdmin(admin.ModelAdmin):

    list_display = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")
    search_fields = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")
    # Filtrar
    list_filter = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")


@admin.register(Convenios)
class conveniosAdmin(admin.ModelAdmin):

    list_display = ( "id","nombre", "empresa","vigenciaDesde","vigenciaHasta")
    search_fields = ( "id","nombre", "empresa","vigenciaDesde","vigenciaHasta")
    # Filtrar
    list_filter = ( "id","nombre", "empresa","vigenciaDesde","vigenciaHasta")
