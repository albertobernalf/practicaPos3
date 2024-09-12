from django.contrib import admin

# Register your models here.

from facturacion.models import Empresas, Cups, TiposCups, Conceptos, ConveniosPaciente, ConveniosPacienteIngresos, SalariosLegales, RegimenesTipoPago, TiposSuministro


@admin.register(Empresas)
class empresasAdmin(admin.ModelAdmin):

   list_display = ("id", "tipoDoc", "documento","nombre","codigoEapb","direccion","telefono")
   search_fields = ("id", "tipoDoc", "documento","nombre","codigoEapb","direccion","telefono")
   # Filtrar
   list_filter = ("id", "tipoDoc", "documento","nombre","codigoEapb","direccion","telefono")


@admin.register(Cups)
class cupsAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre", "codigoCups","concepto")
   search_fields = ("id", "nombre", "codigoCups","concepto")
   # Filtrar
   list_filter = ("id", "nombre", "codigoCups","concepto")




@admin.register(TiposCups)
class tiposCupsAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(Conceptos)
class conceptosAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre", "tipoCups")
   search_fields = ("id", "nombre", "tipoCups")
   # Filtrar
   list_filter = ("id", "nombre", "tipoCups")

@admin.register(ConveniosPaciente)
class conveniosPacienteAdmin(admin.ModelAdmin):
   list_display = ("id", "tipoDoc", "documento", "convenio")
   search_fields = ("id", "tipoDoc", "documento", "convenio")
   # Filtrar
   list_filter = ("id", "tipoDoc", "documento", "convenio")

@admin.register(ConveniosPacienteIngresos)
class conveniosPacienteIngresosAdmin(admin.ModelAdmin):
   list_display = ("id", "tipoDoc", "documento", "consecAdmision", "convenio")
   search_fields = ("id", "tipoDoc", "documento", "consecAdmision", "convenio")
   # Filtrar
   list_filter = ("id", "tipoDoc", "documento", "consecAdmision", "convenio")


@admin.register(SalariosLegales)
class salariosLegalesAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")


@admin.register(RegimenesTipoPago)
class regimenesTipoPagoAdmin(admin.ModelAdmin):

   list_display = ("id", "regimen","salarioLegal", "año","valorModeradora","valorCopago")
   search_fields = ("id", "regimen","salarioLegal", "año","valorModeradora","valorCopago")
   # Filtrar
   list_filter = ("id", "regimen","salarioLegal", "año","valorModeradora","valorCopago")


@admin.register(TiposSuministro)
class tiposSuministroAdmin(admin.ModelAdmin):

   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

