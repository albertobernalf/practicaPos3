from django.contrib import admin

# Register your models here.


from clinico.models import TiposExamen
from contratacion.models import  Convenios,  ConveniosTarifasHonorarios, ConveniosSuministros, ConveniosProcedimientos , ConveniosLiquidacionTarifasHonorarios

@admin.register(Convenios)
class conveniosAdmin(admin.ModelAdmin):

    list_display = ( "id","nombre","descripcion", "empresa","vigenciaDesde","vigenciaHasta")
    search_fields = ( "id","nombre","descripcion", "empresa","vigenciaDesde","vigenciaHasta")
    # Filtrar
    list_filter = ( "id","nombre", "descripcion","empresa","vigenciaDesde","vigenciaHasta")



@admin.register( ConveniosTarifasHonorarios)
class  conveniosTarifasHonorariosAdmin(admin.ModelAdmin):

    list_display = ( "id","convenio",  "valor")
    search_fields = ( "id","convenio","valor")
    # Filtrar
    list_filter =  ( "id","convenio",  "valor")


@admin.register(ConveniosProcedimientos)
class conveniosProcedimientosAdmin(admin.ModelAdmin):

    list_display = ( "id","convenio","tipoTarifa", "codigoHomologado","cups","valor")
    search_fields = ( "id","convenio","tipoTarifa", "codigoHomologado","cups","valor")
    # Filtrar
    list_filter = ( "id","convenio","tipoTarifa", "codigoHomologado","cups","valor")


@admin.register(ConveniosSuministros)
class conveniosSuministrosAdmin(admin.ModelAdmin):

    list_display = ( "id","convenio","tipoTarifa", "codigoHomologado","suministro","valor")
    search_fields = ( "id","convenio","tipoTarifa", "codigoHomologado","suministro","valor")
    # Filtrar
    list_filter = ( "id","convenio","tipoTarifa", "codigoHomologado","suministro","valor")


@admin.register(ConveniosLiquidacionTarifasHonorarios)
class conveniosLiquidacionTarifasHonorariosAdmin(admin.ModelAdmin):

   list_display = ("id", "descripcion","tipoTarifa","codigoHomologado", "valor")
   search_fields = ("id", "descripcion","tipoTarifa","codigoHomologado", "valor")
   # Filtrar
   list_filter = ("id", "descripcion","tipoTarifa","codigoHomologado", "valor")

