from django.contrib import admin

# Register your models here.

from rips.models import RipsEnvios, RipsDetalle, RipsTransaccion, RipsTipoUsuario, RipsPaises, RipsUsuarios, RipsGrupoServicios, RipsModalidadAtencion, RipsServicios, RipsCausaExterna, RipsConceptoRecaudo, RipsTiposDocumento, RipsConsultas, RipsViasIngresoSalud, RipsProcedimientos, RipsDestinoEgreso, RipsUrgenciasObservacion
from rips.models import RipsTipoOtrosServicios,  RipsHospitalizacion, RipsRecienNacido, RipsTipoMedicamento, RipsCums, RipsUmm, RipsFormaFarmaceutica, RipsUnidadUpr, RipsMedicamentos, RipsOtrosServicios, RipsFinalidadConsulta, RipsDci

@admin.register(RipsEnvios)
class ripsEnviosAdmin(admin.ModelAdmin):
   list_display = ("id", "numeroEnvio", "fechaEnvio")
   search_fields =  ("id", "numeroEnvio", "fechaEnvio")
   # Filtrar
   list_filter = ("id", "numeroEnvio", "fechaEnvio")


@admin.register(RipsDetalle)
class ripsDetalleAdmin(admin.ModelAdmin):
   list_display = ("id", "ripsEnvios", "numeroFactura")
   search_fields =   ("id", "ripsEnvios", "numeroFactura")
   # Filtrar
   list_filter =  ("id", "ripsEnvios", "numeroFactura")


@admin.register(RipsTransaccion)
class ripsTransaccionAdmin(admin.ModelAdmin):
   list_display = ("id", "numDocumentoIdObligado", "numFactura")
   search_fields =   ("id", "numDocumentoIdObligado", "numFactura")
   # Filtrar
   list_filter =  ("id", "numDocumentoIdObligado", "numFactura")

@admin.register(RipsTipoUsuario)
class ripsTipoUsuarioAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsPaises)
class ripsPaisesAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsUsuarios)
class ripsUsuariosAdmin(admin.ModelAdmin):
   list_display = ("id", "tipoDocumentoIdentificacion", "tipoUsuario")
   search_fields =   ("id", "tipoDocumentoIdentificacion", "tipoUsuario")
   # Filtrar
   list_filter = ("id", "tipoDocumentoIdentificacion", "tipoUsuario")


@admin.register(RipsGrupoServicios)
class ripsGrupoServiciosAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsModalidadAtencion)
class ripsModalidadAtencionAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsServicios)
class ripsServiciosAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsFinalidadConsulta)
class ripsFinalidadConsultaAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsCausaExterna)
class ripsCausaExternaAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsConceptoRecaudo)
class ripsConceptoRecaudoAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsTiposDocumento)
class ripsTiposDocumentoAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsConsultas)
class ripsConsultasAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "numAutorizacion")
   search_fields =   ("id", "codPrestador", "numAutorizacion")
   # Filtrar
   list_filter = ("id", "codPrestador", "numAutorizacion")

@admin.register(RipsViasIngresoSalud)
class ripsViasIngresoSaludAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsProcedimientos)
class ripsProcedimientosAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "idMIPRES")
   search_fields =  ("id", "codPrestador", "idMIPRES")
   # Filtrar
   list_filter = ("id", "codPrestador", "idMIPRES")

@admin.register(RipsDestinoEgreso)
class ripsDestinoEgresoAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsUrgenciasObservacion)
class ripsUrgenciasObservacionAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "fechaInicioAtencion")
   search_fields =  ("id", "codPrestador", "fechaInicioAtencion")
   # Filtrar
   list_filter = ("id", "codPrestador", "fechaInicioAtencion")

@admin.register(RipsHospitalizacion)
class ripsHospitalizacionAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "viaIngresoServicioSalud")
   search_fields =  ("id", "codPrestador", "viaIngresoServicioSalud")
   # Filtrar
   list_filter = ("id", "codPrestador", "viaIngresoServicioSalud")

@admin.register(RipsRecienNacido)
class ripsRecienNacidoAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "numDocumentoIdentificacion")
   search_fields =  ("id", "codPrestador", "numDocumentoIdentificacion")
   # Filtrar
   list_filter = ("id", "codPrestador", "numDocumentoIdentificacion")


@admin.register(RipsTipoMedicamento)
class ripsTipoMedicamentoAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsCums)
class ripsCumsAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")


@admin.register(RipsUmm)
class ripsUmmAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsFormaFarmaceutica)
class ripsFormaFarmaceuticaAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsUnidadUpr)
class ripsUnidadUprAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")

@admin.register(RipsMedicamentos)
class ripsMedicamentosAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "numAutorizacion")
   search_fields =   ("id", "codPrestador", "numAutorizacion")
   # Filtrar
   list_filter = ("id", "codPrestador", "numAutorizacion")



@admin.register(RipsTipoOtrosServicios)
class ripsTipoOtrosServiciosAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =    ("id", "codigo", "nombre")
   # Filtrar
   list_filter =  ("id", "codigo", "nombre")


@admin.register(RipsOtrosServicios)
class ripsOtrosServiciosAdmin(admin.ModelAdmin):
   list_display = ("id", "codPrestador", "numAutorizacion")
   search_fields =  ("id", "codPrestador", "numAutorizacion")
   # Filtrar
   list_filter = ("id", "codPrestador", "numAutorizacion")

@admin.register(RipsDci)
class ripsDciAdmin(admin.ModelAdmin):
   list_display = ("id", "codigo", "nombre")
   search_fields =   ("id", "codigo", "nombre")
   # Filtrar
   list_filter = ("id", "codigo", "nombre")