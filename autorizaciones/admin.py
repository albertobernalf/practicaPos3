from django.contrib import admin

# Register your models here.


from autorizaciones.models import  Autorizaciones, AutorizacionesCups, AutorizacionesCirugias


@admin.register(Autorizaciones)
class autorizacionesAdmin(admin.ModelAdmin):
    list_display = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "fechaSolicitud","empresa","fechaAutorizacion")
    search_fields = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "fechaSolicitud","empresa","fechaAutorizacion")
    # Filtrar
    list_filter = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "fechaSolicitud","empresa","fechaAutorizacion")


@admin.register(AutorizacionesCups)
class autorizacionesCupsAdmin(admin.ModelAdmin):
    list_display = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec","autorizacionesId", "codigoCups","autorizado","cantidadSolicitada","cantidadAutorizada")
    search_fields = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "autorizacionesId", "codigoCups","autorizado","cantidadSolicitada","cantidadAutorizada")
    # Filtrar
    # list_filter =("id", "sedesClinica", "tipoDoc","documento","hClinica","consec","autorizacionesId", "codigoCups","autorizado","cantidadSolicitada","cantidadAutorizada")



@admin.register(AutorizacionesCirugias)
class autorizacionesCirugiasAdmin(admin.ModelAdmin):

   list_display = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "autorizacionesId","fechaRegistro","usuarioRegistro")
   search_fields = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "autorizacionesId","fechaRegistro","usuarioRegistro")
   # Filtrar
   # list_filter = ("id", "sedesClinica", "tipoDoc","documento","hClinica","consec", "autorizacionesId","fechaRegistro","usuarioRegistro")

