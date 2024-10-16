from django.contrib import admin

# Register your models here.

from tarifas.models import TiposHonorarios, LiquidacionHonorarios, Uvr, TiposSalas, LiquidacionDerechos, Tarifas, TiposTarifa, GruposQx, Tarifassuministros


@admin.register(TiposHonorarios)
class tiposHonorariosAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")


@admin.register(LiquidacionHonorarios)
class liquidacionHonorariosAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoTarifa","codigoHomologado","tipoHonorario","grupoQx","salMinLeg")
   search_fields = ("id", "tipoTarifa","codigoHomologado","tipoHonorario","grupoQx","salMinLeg")
   # Filtrar
   list_filter = ("id", "tipoTarifa","codigoHomologado","tipoHonorario","grupoQx","salMinLeg")


@admin.register(Uvr)
class uvrsAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoTarifa", "año", "valor")
   search_fields = ("id", "tipoTarifa", "año", "valor")
   # Filtrar
   list_filter = ("id", "tipoTarifa", "año", "valor")




@admin.register(TiposSalas)
class tiposSalasAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")



@admin.register(LiquidacionDerechos)
class liquidacionDerechosAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoTarifa","codigoHomologado","tipoSala","grupoQx","salMinLeg")
   search_fields = ("id", "tipoTarifa","codigoHomologado","tipoSala","grupoQx","salMinLeg")
   # Filtrar
   list_filter = ("id", "tipoTarifa","codigoHomologado","tipoSala","grupoQx","salMinLeg")

@admin.register(Tarifas)
class tarifasAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoTarifa", "nombre", "codigoHomologado")
   search_fields = ("id", "tipoTarifa", "nombre", "codigoHomologado")
   # Filtrar
   list_filter =("id", "tipoTarifa", "nombre", "codigoHomologado")

@admin.register(TiposTarifa)
class tiposTarifaAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(GruposQx)
class gruposQxAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")


@admin.register(Tarifassuministros)
class tarifassuministrosAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoTarifa", "suministro_id", "codigoHomologado")
   search_fields = ("id", "tipoTarifa", "suministro_id", "codigoHomologado")
   # Filtrar
   list_filter =("id", "tipoTarifa", "suministro_id", "codigoHomologado")