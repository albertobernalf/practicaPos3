"""vulner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf  import settings
from django.conf.urls.static import  static

from django.urls import path, include
from camara import  views as viewsCamara

from Reportes import views as viewsReportes

from admisiones import views as viewsAdmisiones
from triage import views as viewsTriage

from usuarios import views as viewsUsuarios

from django.conf  import settings
from django.conf.urls.static import  static
from clinico import views as viewsClinico
from terapeutico import views as viewsApoyoTerapeutico
from facturacion import views as viewsFacturacion
from contratacion import views as viewsConvenios
#from mecanicosPacientes import views as viewsmecanicosPacientes



urlpatterns = [
    path('admin/', admin.site.urls),

    # Primero Reporteador

    path('chaining/', include('smart_selects.urls')),
    path('medicalReport/', viewsReportes.menuAcceso),

    #path('validaAcceso/', viewsReportes.validaAcceso),
    path('salir/', viewsReportes.salir),
    path('pantallaSubgrupos/<str:username>, <str:sedeSeleccionada>, <str:grupo>', viewsReportes.pantallaSubgrupos),
    path('emergenteGrupos/<str:username>, <str:sedeSeleccionada>, <str:grupo>', viewsReportes.emergenteGrupos),
    path('combo/<str:username>, <str:sedeSeleccionada>, <str:grupo>, <str:subGrupo>', viewsReportes.combo),
    #path('/combo/<str:username>, <str:sedeSeleccionada>, <str:grupo>, <str:subGrupo>', views.combo),

    # path('contrasena/<str:documento>', views.contrasena),
 
    ## Invoca Reporte

    path('Reporte1/<str:numreporte>,<str:username>,<str:sedeSeleccionada>,<str:grupo>,<str:subGrupo>',
         viewsReportes.Reporte1PdfView.as_view()),
    # path('Reporte2/<str:numreporte>,<str:username>,<str:sedeSeleccionada>,<str:grupo>,<str:subGrupo>', views.Reporte1PdfView.as_view()),

    # Fin Reporteador

    # Acceso al Programa General Clinico

    path('menu/', viewsCamara.menu),
    # path('menuAcceso/validaAcceso/', views.validaAcceso),
    path('contrasena/<str:documento>', viewsCamara.contrasena),
    # path('salir/validaAcceso/', views.validaAcceso),

    # HISTORIA CLINICA

    # path('accesoEspecialidadMedico/historiaView/<str:documento>', viewsClinico.nuevoView.as_view()),
    # path('historia1View/', viewsClinico.historia1View),
    # path('historiaExamenesView/', viewsClinico.historiaExamenesView),
    # path('consecutivo_folios/', viewsClinico.consecutivo_folios),
    # path('buscaExamenes/', viewsClinico.buscaExamenes),
    path('motivoSeñas/', viewsClinico.motivoSeñas),
    path('subjetivoSeñas/', viewsClinico.subjetivoSeñas),
    path('motivoInvidente/', viewsClinico.motivoInvidente),
    # path('resMotivoInvidente/', viewsClinico.s),
    path('reconocerAudio/', viewsCamara.reconocerAudio),
    path('reproduceAudio/', viewsCamara.reproduceAudio),
    path('accesoEspecialidadMedico/<str:documento>', viewsCamara.accesoEspecialidadMedico),
    path('crearHistoriaClinica/', viewsClinico.crearHistoriaClinica),
    # path('crearHistoriaClinica1/', viewsClinico.crearHistoriaClinica1.as_view()),
    #path('buscarAdmisionClinico/', viewsClinico.buscarAdmisionClinico),
    path('cargaPanelMedico/<str:data>',  viewsClinico.load_dataClinico, name='loaddataClinico'),
    #path('buscarAntecedentes/', viewsClinico.buscarAntecedentes),
    path('load_dataClinico/<str:data>', viewsClinico.load_dataClinico, name='loaddataClinico'),
    #path('creacionHC/postConsultaHc/<str:id>/edit/', viewsClinico.PostConsultaHc, name='Post_editHc'),
    #path('creacionHC/<str:id>', viewsClinico.PostConsultaHcli),
    path('creacionHc/postConsultaHcli/', viewsClinico.PostConsultaHcli , name='Post_editHc'),

    # Actividaes Mecanicas

    path('prueba/', viewsClinico.prueba),
    #   path('manejoLuz/', viewsmecanicosPacientes.manejoLuz.as_view()),
    #  path('ambienteMusical/', viewsmecanicosPacientes.ambienteMusical.as_view()),
    path('camara/', viewsCamara.camara),
    path('leeAudio/', viewsCamara.leeAudio),

    path('chaining/', include('smart_selects.urls')),

    # Acceso global

    path('medicalSocial/', viewsAdmisiones.menuAcceso),

    # Admisiones

    path('validaAcceso/', viewsAdmisiones.validaAcceso),
    #path('menuAccesoClinico/', viewsAdmisiones.menuAcceso),
    path('validaAccesoClinico/', viewsAdmisiones.validaAcceso),
    path('escoge/', viewsAdmisiones.escogeAcceso),
    path('escoge/<str:Sede>,<str:Username>,<str:Profesional>,<str:Documento>,<str:NombreSede>,<str:escogeModulo>', viewsAdmisiones.escogeAcceso),

    path('retornarAdmision/<str:Sede>, <str:Perfil> , <str:Username>, <str:Username_id>, <str:NombreSede>',
         viewsAdmisiones.retornarAdmision),

    path('retornarMen/<str:Sede>,<str:Username>,<str:Documento>,<str:NombreSede>,<str:Profesional>', viewsAdmisiones.retornarMen),
    path('grabar1/<str:username>,<str:contrasenaAnt>,<str:contrasenaNueva>,<str:contrasenaNueva2>',
         viewsAdmisiones.validaPassword),
    path('findOne/<str:username> , <str:password> , <str:tipoDoc>/', viewsAdmisiones.Modal),
    # path('buscarAdmision/<str:BusHabitacion>,<str:BusTipoDoc>,<str:BusDocumento>,<str:BusPaciente>,<str:BusDesde>,<str:BusHasta>', viewsAdmisiones.buscarAdmision),
    path('buscarAdmision/', viewsAdmisiones.buscarAdmision),

    path('buscarEspecialidadesMedicos/', viewsAdmisiones.buscarEspecialidadesMedicos),
    path('buscarCiudades/', viewsAdmisiones.buscarCiudades),
    path('buscarHabitaciones/', viewsAdmisiones.buscarHabitaciones),

    path('buscarSubServicios/', viewsAdmisiones.buscarSubServicios),
    # path('crearAdmision/<str:Sede>,<str:Perfil>, <str:Username>, <str:Username_id>', viewsAdmisiones.crearAdmision.as_view()),
    path('crearAdmisionDef/', viewsAdmisiones.crearAdmisionDef),

    path('findOneUsuario/', viewsAdmisiones.UsuariosModal),
    path('guardarUsuariosModal/', viewsAdmisiones.guardarUsuariosModal),
    path('crearResponsables/', viewsAdmisiones.crearResponsables),
    path('cambioServicio/', viewsAdmisiones.cambioServicio),
    path('guardaCambioServicio/', viewsAdmisiones.guardaCambioServicio),
    path('load_dataConvenioAdmisiones/<str:data>', viewsAdmisiones.load_dataConvenioAdmisiones, name='loaddataAdmisiones'),
    path('guardaConvenioAdmision/', viewsAdmisiones.GuardaConvenioAdmision, name='guardaConvenioAdmision'),
    path('postDeleteConveniosAdmision/', viewsAdmisiones.PostDeleteConveniosAdmision, name='postDeleteConveniosAdmision'),
    path('guardarResponsableAdmision/', viewsAdmisiones.GuardarResponsableAdmision, name='guardarResponsableAdmision'),
    path('guardarAcompananteAdmision/', viewsAdmisiones.GuardarAcompananteAdmision, name='guardarAcompananteAdmision'),
    path('load_dataAbonosAdmisiones/<str:data>', viewsAdmisiones.load_dataAbonosAdmisiones,   name='loaddataAbonosAdmisiones'),
    path('guardaAbonosAdmision/', viewsAdmisiones.GuardaAbonosAdmision, name='guardaAbonosAdmision'),
    path('postDeleteAbonosAdmision/', viewsAdmisiones.PostDeleteAbonosAdmision, name='postDeleteAbonosAdmision'),
    path('guardaFurips/', viewsAdmisiones.GuardaFurips, name='guardaFurips'),
    #path('encuentraAdmisionModal/<str:tipoDoc> , <str:documento> , <str:consec> , <str:sede>/', viewsAdmisiones.encuentraAdmisionModal, name='encuentraAdmisionModal'),
    path('encuentraAdmisionModal/', viewsAdmisiones.encuentraAdmisionModal),

    # Triage

    path('crearTriage/', viewsTriage.crearTriage),
    path('buscarTriage/', viewsTriage.buscarTriage),
    path('buscarSubServiciosTriage/', viewsTriage.buscarSubServiciosTriage),
    path('buscarHabitacionesTriage/', viewsTriage.buscarHabitacionesTriage),
    path('encuentraTriageModal/<str:tipoDoc> , <str:documento>, <str:sede>/', viewsTriage.encuentraTriageModal),
    path('encuentraTriageModal/', viewsTriage.encuentraTriageModal),
    path('findOneUsuarioTriage/', viewsTriage.UsuariosModalTriage),
    path('grabaUsuariosTriage/', viewsTriage.grabaUsuariosTriage),
    path('grabaTriageModal/', viewsTriage.grabaTriageModal),
    path('admisionTriageModal/', viewsTriage.admisionTriageModal),
    path('guardarAdmisionTriage/', viewsTriage.guardarAdmisionTriage),

    # Apoyo Terapeutico

    path('load_dataApoyoTerapeutico/<str:data>', viewsApoyoTerapeutico.load_dataApoyoTerapeutico, name='loaddataApoyoTerapeutico'),
    path('load_dataRasgos/<str:data>', viewsApoyoTerapeutico.load_dataRasgos, name='loadDataRasgos'),
    path('postConsultaApoyoTerapeutico/', viewsApoyoTerapeutico.PostConsultaApoyoTerapeutico , name='Post_editApoyoTerapeutico'),
    path('guardarResultadoRasgo/', viewsApoyoTerapeutico.GuardarResultadoRasgo, name='guardarResultado_Rasgo'),
    path('postDeleteExamenesRasgos/', viewsApoyoTerapeutico.PostDeleteExamenesRasgos, name='PostDeleteExamenesRasgos'),
    path('guardarResultado/', viewsApoyoTerapeutico.GuardarResultado, name='GuardarResultado'),
    path('load_dataTerapeuticoConsulta/<str:data>', viewsApoyoTerapeutico.load_dataTerapeuticoConsulta, name='loaddataTerapeuticoConsulta'),
    path('load_dataRasgosConsulta/<str:data>', viewsApoyoTerapeutico.load_dataRasgosConsulta, name='loadDataRasgos_Consulta'),
    path('postConsultaApoyoTerapeuticoConsulta/', viewsApoyoTerapeutico.PostConsultaApoyoTerapeuticoConsulta , name='Post_editApoyoTerapeutico_Consulta'),

    # Facturacion

    path('load_dataLiquidacion/<str:data>', viewsFacturacion.load_dataLiquidacion, name='loaddataLiquidacion'),
    path('load_dataLiquidacionDetalle/<str:data>', viewsFacturacion.load_dataLiquidacionDetalle, name='loaddataLiquidacionDetalle'),
    path('postConsultaLiquidacion/', viewsFacturacion.PostConsultaLiquidacion , name='Post_editLiquidacion'),
    path('postConsultaLiquidacionDetalle/', viewsFacturacion.PostConsultaLiquidacionDetalle , name='Post_editLiquidacionDetalle'),
    path('guardaAbonosFacturacion/', viewsFacturacion.GuardaAbonosFacturacion, name='guardaAbonosFacturacion'),
    path('postDeleteAbonosFacturacion/', viewsFacturacion.PostDeleteAbonosFacturacion, name='postDeleteAbonosFacturacion'),
    path('postDeleteLiquidacionDetalle/', viewsFacturacion.PostDeleteLiquidacionDetalle, name='postDeleteLiquidacionDetalle'),
    path('guardarLiquidacionDetalle/', viewsFacturacion.GuardarLiquidacionDetalle, name='guardarLiquidacionDetalle'),
    path('editarGuardarLiquidacionDetalle/', viewsFacturacion.EditarGuardarLiquidacionDetalle, name='editarGuardarLiquidacionDetalle'),
    path('load_dataAbonosFacturacion/<str:data>', viewsFacturacion.load_dataAbonosFacturacion, name='loaddataAbonosFacturacion'),

    # Contratacion
    path('load_dataConvenios/<str:data>', viewsConvenios.load_dataConvenios, name='loaddataConvenios'),
    path('load_dataConveniosProcedimientos/<str:data>', viewsConvenios.load_dataConveniosProcedimientos, name='loaddataConveniosProcedimientos'),
    path('postConsultaConvenios/', viewsConvenios.PostConsultaConvenios , name='Post_editConvenios'),
    path('guardarConveniosProcedimientos/', viewsConvenios.GuardarConveniosProcedimientos, name='guardarConveniosProcedimientos'),
    path('guardarConvenio/', viewsConvenios.GuardarConvenio , name='guadarConvenio'),
    path('guardarConvenio1/', viewsConvenios.GuardarConvenio1, name='guadarConvenio1'),
    path('grabarTarifa/', viewsConvenios.GrabarTarifa, name='grabarTarifa'),
    path('deleteConveniosProcedimientos/', viewsConvenios.DeleteConveniosProcedimientos, name='deleteConveniosProcedimientos'),

    path('load_dataConveniosSuministros/<str:data>', viewsConvenios.load_dataConveniosSuministros, name='loaddataConveniosSuministros'),
    path('grabarSuministro/', viewsConvenios.GrabarSuministro, name='grabarSuministro'),
    path('deleteConveniosSuministros/', viewsConvenios.DeleteConveniosSuministros, name='deleteConveniosSuministros'),
    path('guardarConveniosSuministros/', viewsConvenios.GuardarConveniosSuministros, name='guardarConveniosSuministros'),

    path('load_dataConveniosHonorarios/<str:data>', viewsConvenios.load_dataConveniosHonorarios, name='loaddataConveniosHonorarios'),
    path('grabarHonorarios/', viewsConvenios.GrabarHonorarios, name='grabarHonorarios'),
    path('deleteConveniosHonorarios/', viewsConvenios.DeleteConveniosHonorarios, name='deleteConveniosHonorarios'),
    path('guardarConveniosHonorarios/', viewsConvenios.GuardarConveniosHonorarios, name='guardarConveniosHonorarios'),

    # Citas Medicas

    # Usuarios

    path('crearUsuarios/', viewsUsuarios.crearUsuarios),
    # Fin Acceso al Programa General Clinico

]


if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# Añadir
admin.site.site_header = 'Administracion Medical Report'
admin.site.site_title = "Portal de Medical Report"
admin.site.index_title = "Bienvenidos al portal de administración Medical Report"
