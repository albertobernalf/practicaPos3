from django.contrib import admin

# Register your models here.


from clinico.models import TiposExamen
from contratacion.models import  Procedimientos, Convenios, ConveniosDetalle,  ConveniosLiquidacionHonorarios


@admin.register(Procedimientos)
class procedimientosAdmin(admin.ModelAdmin):

    list_display = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")
    search_fields = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")
    # Filtrar
    list_filter = ( "id","tiposExamen", "cups","nombre","solicitaEnfermeria")


@admin.register(Convenios)
class conveniosAdmin(admin.ModelAdmin):

    list_display = ( "id","nombre","descripcion", "empresa","vigenciaDesde","vigenciaHasta")
    search_fields = ( "id","nombre","descripcion", "empresa","vigenciaDesde","vigenciaHasta")
    # Filtrar
    list_filter = ( "id","nombre", "descripcion","empresa","vigenciaDesde","vigenciaHasta")

@admin.register(ConveniosDetalle)
class conveniosDetalleAdmin(admin.ModelAdmin):

    list_display = ( "id","convenio", "tarifa", "codigoCups", "tarifaSuministros","valorNeto")
    search_fields = ( "id","convenio", "tarifa", "codigoCups", "tarifaSuministros","valorNeto")
    # Filtrar
    list_filter =  ( "id","convenio","tarifa", "codigoCups", "tarifaSuministros","valorNeto")


@admin.register( ConveniosLiquidacionHonorarios)
class  conveniosLiquidacionHonorariosAdmin(admin.ModelAdmin):

    list_display = ( "id","convenio", "liquidacionHonorario", "valorNeto")
    search_fields = ( "id","convenio", "liquidacionHonorario", "valorNeto")
    # Filtrar
    list_filter =  ( "id","convenio","liquidacionHonorario", "valorNeto")
