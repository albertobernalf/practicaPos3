from django.contrib import admin

# Register your models here.

from clinico.models import Medicos, Especialidades , TiposExamen, Examenes, Historia, HistoriaExamenes, HistoriaResultados, EspecialidadesMedicos, Servicios, Diagnosticos, EstadosSalida,   EstadoExamenes,  Enfermedades, TiposFolio, TiposAntecedente, Antecedentes ,  CausasExterna, ViasIngreso , TiposIncapacidad,  HistorialAntecedentes, TiposDiagnostico, HistorialDiagnosticos, Interconsultas, EstadosInterconsulta
from clinico.models import ViasEgreso, RevisionSistemas, NivelesClinica, TiposTriage, TurnosEnfermeria, TiposSalidas, Eps, TiposCotizante,  Regimenes, Recomendaciones, Hallazgos, NivelesRegimenes, Ips

@admin.register(Servicios)
class serviciosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)


@admin.register(Especialidades)
class especialidadesAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")
        # Filtrar
        list_filter = ('nombre',)

@admin.register(EspecialidadesMedicos)
class especialidadesMedicosAdmin(admin.ModelAdmin):
    list_display = ("id", "especialidades", "planta", "nombre")
    search_fields = ("id", "especialidades", "planta", "nombre")
    # Filtrar
    list_filter = ( "especialidades", "planta", "nombre")


@admin.register(EstadoExamenes)
class estadoExamenesAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")
        # Filtrar
        list_filter = ('nombre',)


@admin.register(Enfermedades)
class enfermedadesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)




@admin.register(TiposExamen)
class tiposExamenAdmin(admin.ModelAdmin):
        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")
        # Filtrar
        list_filter = ('nombre',)


@admin.register(TiposFolio)
class tiposFolioAdmin(admin.ModelAdmin):
        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")
        # Filtrar
        list_filter = ('nombre',)

@admin.register(TiposAntecedente)
class tiposAntecedenteAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre")
            search_fields = ("id", "nombre")
            # Filtrar
            list_filter = ('nombre',)


@admin.register(Antecedentes)
class antecedenteAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre","tiposAntecedente")
            search_fields = ("id", "nombre","tiposAntecedente")
            # Filtrar
            list_filter = ('nombre','tiposAntecedente')

@admin.register(CausasExterna)
class causasExternaAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre")
            search_fields = ("id", "nombre")
            # Filtrar
            list_filter = ('nombre',)

@admin.register(ViasIngreso)
class viasIngresoAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre")
            search_fields = ("id", "nombre")
            # Filtrar
            list_filter = ('nombre',)

@admin.register(TiposIncapacidad)
class tiposIncapacidadAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre")
            search_fields = ("id", "nombre")
            # Filtrar
            list_filter = ('nombre',)

@admin.register(Examenes)
class examenesAdmin(admin.ModelAdmin):

    list_display = ("id","nombre","TiposExamen","codigo")
    search_fields = ("id","nombre","TiposExamen" ,"codigo")
    # Filtrar
    list_filter = ('nombre','TiposExamen','codigo')



@admin.register(HistoriaExamenes)
class historiaExamenesAdmin(admin.ModelAdmin):

    list_display = ( "id", "cantidad","estadoExamenes")
    search_fields = ( "id","cantidad","estadoExamenes")
    # Filtrar
    list_filter = ( "id", "cantidad","estadoExamenes")




@admin.register(HistorialDiagnosticos)
class historialDiagnosticosAdmin(admin.ModelAdmin):
        list_display = ("id", "diagnosticos","tiposDiagnostico")
        search_fields = ("id", "diagnosticos","tiposDiagnostico")
        # Filtrar
        list_filter = ("id", "diagnosticos","tiposDiagnostico")



@admin.register(Historia)
class historiaAdmin(admin.ModelAdmin):

        list_display = ("id", "tipoDoc", "documento","folio","fecha","causasExterna","dependenciasRealizado")
        search_fields = ("id", "tipoDoc", "documento","folio","fecha","causasExterna","dependenciasRealizado")
        # Filtrar
        list_filter = ('id', 'tipoDoc', 'documento', 'folio', 'fecha', 'causasExterna','dependenciasRealizado')



@admin.register(TiposDiagnostico)
class tiposDiagnosticoAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre")
            search_fields = ("id", "nombre")
            # Filtrar
            list_filter = ('nombre',)



@admin.register(Diagnosticos)
class diagnosticosAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre","edadIni","edadFin")
     search_fields = ("id", "nombre","edadIni","edadFin")
      # Filtrar
     list_filter = ('id', 'nombre',"edadIni","edadFin")

@admin.register(EstadosSalida)
class estadosSalidaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")

    # Filtrar
    list_filter = ('id', 'nombre',)


@admin.register(HistorialAntecedentes)
class historialAntecedentesAdmin(admin.ModelAdmin):

        list_display = ("id", "historia","tiposAntecedente","antecedentes","descripcion")
        search_fields = ("id", "historia","tiposAntecedente","antecedentes","descripcion")
        # Filtrar
        list_filter = ("id", "historia","tiposAntecedente","antecedentes","descripcion")



@admin.register(EstadosInterconsulta)
class estadosInterconsultaAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre")
     search_fields = ("id", "nombre")
      # Filtrar
     list_filter = ('id', 'nombre',)


@admin.register(Interconsultas)
class interconsultasAdmin(admin.ModelAdmin):

        list_display = ("id", "historia","descripcionConsulta","especialidadConsultada","respuestaConsulta")
        search_fields = ("id", "historia","descripcionConsulta","especialidadConsultada","respuestaConsulta")
        # Filtrar
        list_filter =("id", "historia","descripcionConsulta","especialidadConsultada","respuestaConsulta")


@admin.register(Medicos)
class medicosAdmin(admin.ModelAdmin):

        list_display = ("id", "planta","tipoDoc","documento","nombre","especialidades","departamento")
        search_fields = ("id", "planta","tipoDoc","documento","nombre","especialidades","departamento")
        # Filtrar
        list_filter =("id", "planta", "tipoDoc","documento","nombre","especialidades","departamento")



@admin.register(Regimenes)
class regimenesAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre")
     search_fields = ("id", "nombre")
      # Filtrar
     list_filter = ('id', 'nombre',)


@admin.register(TiposCotizante)
class tiposCotizanteAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre")
     search_fields = ("id", "nombre")
      # Filtrar
     list_filter = ('id', 'nombre',)


@admin.register(Eps)
class epsAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre")
     search_fields = ("id", "nombre")
      # Filtrar
     list_filter = ('id', 'nombre',)

@admin.register(TiposSalidas)
class tiposSalidasAdmin(admin.ModelAdmin):
     list_display = ("id", "nombre")
     search_fields = ("id", "nombre")
      # Filtrar
     list_filter = ('id', 'nombre',)


@admin.register(TurnosEnfermeria)
class turnosEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('id', 'nombre',)


@admin.register(TiposTriage)
class tiposTriageAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('id', 'nombre',)


@admin.register(NivelesClinica)
class nivelesClinicaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('id', 'nombre',)


@admin.register(RevisionSistemas)
class revisionSistemasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('id', 'nombre',)


@admin.register(Recomendaciones)
class recomendacionesesAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")
        # Filtrar
        list_filter = ('nombre',)

@admin.register(Hallazgos)
class hallazgosAdmin(admin.ModelAdmin):
            list_display = ("id", "nombre","miembrosSuperiores","miembrosInferiores","columna","ojos","nariz","oidos","cara","neurologicos","fxCraneo","torax","abdomen","exaMdGeneral","factorTvp","cuello")
            search_fields = ("id", "nombre","miembrosSuperiores","miembrosInferiores","columna","ojos","nariz","oidos","cara","neurologicos","fxCraneo","torax","abdomen","exaMdGeneral","factorTvp","cuello")
            # Filtrar
            list_filter = ("id", "nombre","miembrosSuperiores","miembrosInferiores","columna","ojos","nariz","oidos","cara","neurologicos","fxCraneo","torax","abdomen","exaMdGeneral","factorTvp","cuello")

@admin.register(NivelesRegimenes)
class nivelesRegimenesAdmin(admin.ModelAdmin):
            list_display = ("id","nombre", "regimen","porCuotaModeradora","porCopago","porTopeEve","porTopeAnual")
            search_fields = ("id","nombre", "regimen","porCuotaModeradora","porCopago","porTopeEve","porTopeAnual")
            # Filtrar
            list_filter = ("id", "nombre","regimen","porCuotaModeradora","porCopago","porTopeEve","porTopeAnual")


@admin.register(Ips)
class ipssAdmin(admin.ModelAdmin):

    list_display = ("id", "nombre")
    search_fields =("id", "nombre")
    # Filtrar
    list_filter =("id", "nombre")