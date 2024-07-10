from django.contrib import admin

# Register your models here.


from admisiones.models import Ingresos, Triage



class ingresosAdmin(admin.ModelAdmin):

    list_display=("id","sedesClinica","tipoDoc","documento","consec","fechaIngreso","fechaSalida","dependenciasActual","salidaClinica","especialidadesMedicosActual")
    search_fields =("id","sedesClinica","tipoDoc","documento","consec","fechaIngreso","fechaSalida","dependenciasActual","salidaClinica","especialidadesMedicosActual")


@admin.register(Triage)
class triageAdmin(admin.ModelAdmin):
    list_display = ("id", "sedesClinica","fechaSolicita", "fechaAtendio", "tipoDoc","documento","hClinica","regimen","tiposCotizante","motivo")
    search_fields = ("id", "sedesClinica","fechaSolicita", "fechaAtendio", "tipoDoc","documento","hClinica","regimen","tiposCotizante","motivo")
    # Filtrar
    list_filter =("id", "sedesClinica","fechaSolicita", "fechaAtendio", "tipoDoc","documento","hClinica","regimen","tiposCotizante","motivo")


admin.site.register(Ingresos, ingresosAdmin)