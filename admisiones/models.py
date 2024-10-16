from django.db import models
from django.utils.timezone import now

# Create your models here.

class Ingresos(models.Model):

    id           = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica')
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento')
    hClinica = models.CharField(max_length=20,blank=True,null= True, editable=True,)
    consec    = models.IntegerField()
    fechaIngreso = models.DateTimeField( editable=True, null=True, blank=True)
    fechaSalida = models.DateTimeField(editable=True, null=True, blank=True)
    factura  = models.IntegerField(default=0)
    numcita  =  models.IntegerField(default=0)
    serviciosIng = models.ForeignKey('clinico.Servicios', blank=True,null= True, editable=True,  on_delete=models.PROTECT,   related_name='id9')
    dependenciasIngreso = models.ForeignKey('sitios.Dependencias', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id0')
    dxIngreso = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id3')
    medicoIngreso  =  models.ForeignKey('clinico.Medicos', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id6')

    especialidadesMedicosIngreso =  models.ForeignKey('clinico.Especialidades', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='EspIng')

    serviciosActual = models.ForeignKey('clinico.Servicios',blank=True,null= True, editable=True,  on_delete=models.PROTECT,  related_name='id10')
    dependenciasActual = models.ForeignKey('sitios.Dependencias', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='id1')
    dxActual = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id4')
    medicoActual =  models.ForeignKey('clinico.Medicos', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id7')
    especialidadesMedicosActual = models.ForeignKey('clinico.Especialidades', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='EspAct')
    estadoSalida  = models.ForeignKey('clinico.EstadosSalida', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    serviciosSalida  = models.ForeignKey('clinico.Servicios', blank=True,null= True, editable=True,  on_delete=models.PROTECT,  related_name='id11')
    dependenciasSalida = models.ForeignKey('sitios.Dependencias', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='id2')
    dxSalida = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='id5')
    medicoSalida =  models.ForeignKey('clinico.Medicos', blank=True,null= True, editable=True, on_delete=models.PROTECT,   related_name='id8')
    especialidadesMedicosSalida = models.ForeignKey('clinico.Especialidades', blank=True,null= True, editable=True,  on_delete=models.PROTECT, related_name='EspSal')
    salidaClinica = models.CharField(max_length=1,default='N')

    salidaDefinitiva =  models.CharField(max_length=1,default='N')
    salidaMotivo = models.ForeignKey('clinico.TiposSalidas', blank=True,null= True, editable=True,  on_delete=models.PROTECT, related_name='EspSal')

    empresa = models.ForeignKey('facturacion.Empresas', blank=True,null= True, editable=True,  on_delete=models.PROTECT)
    remitido =  models.CharField(max_length=1, blank=True,null= True, editable=True,)
    ipsRemite =  models.ForeignKey('clinico.Ips', blank=True,null= True, editable=True,  on_delete=models.PROTECT)
    contactoAcompañante = models.ForeignKey('usuarios.UsuariosContacto', blank=True,null= True, editable=True,  on_delete=models.PROTECT , related_name='Contac01')
    contactoResponsable = models.ForeignKey('usuarios.UsuariosContacto', blank=True,null= True, editable=True,  on_delete=models.PROTECT , related_name='Contac02')
    numManilla =  models.CharField(max_length=30, blank=True,null= True, editable=True,)


    ViasIngreso  = models.ForeignKey('clinico.ViasIngreso', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    causasExterna = models.ForeignKey('clinico.CausasExterna', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    regimen = models.ForeignKey('clinico.Regimenes', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    tiposCotizante =  models.ForeignKey('clinico.TiposCotizante', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    # supongo  tabla - ContratosPaciente(id, tipoDoc, documento, contrato, vigencia_desde, vigencia_hasta)
    # ContratosPacienteAdmisiones(id, tipoDoc, documento, contrato, consec)
    ViasEgreso = models.ForeignKey('clinico.ViasEgreso', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    muerte =  models.CharField(max_length=1,default='N')
    fechaMuerte = models.DateTimeField(editable=True, null=True, blank=True)
    ActaDefuncion =  models.CharField(max_length=30,default='')
    medicoDefuncion = models.ForeignKey('clinico.Medicos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsServiciosIng = models.ForeignKey('rips.RipsServicios', blank=True,null= True, editable=True,  on_delete=models.PROTECT,   related_name='ripssServicios01')
    ripsServiciosActual = models.ForeignKey('rips.RipsServicios', blank=True,null= True, editable=True,  on_delete=models.PROTECT,   related_name='ripssServicios02')
    ripsServiciosSalida = models.ForeignKey('rips.RipsServicios', blank=True,null= True, editable=True,  on_delete=models.PROTECT,   related_name='ripssServicios03')
    ripsRecienNacido = models.CharField(max_length=1, default='N', editable=False)
    ripsEdadGestacional = models.CharField(max_length=10,default='')
    ripsNumConsultasCPrenatal = models.CharField(max_length=10,default='')
    ripsPesoRecienNacido = models.CharField(max_length=10,default='')
    #ripsDestinoUsuarioEgresoRecienNacido = models.ForeignKey('rips.RipsDestinoEgreso', blank=True,null= True, editable=True, on_delete=models.PROTECT ,   related_name='ripssDestino10')
    ripsViaIngresoServicioSalud = models.ForeignKey('rips.RipsViasIngresoSalud', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsmodalidadGrupoServicioTecSal = models.ForeignKey('rips.RipsModalidadAtencion', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsGrupoServicios =  models.ForeignKey('rips.RipsGrupoServicios', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsCodServicio =  models.ForeignKey('rips.RipsServicios', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsCausaMotivoAtencion =  models.ForeignKey('rips.RipsCausaExterna', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsCondicionDestinoUsuarioEgreso  = models.ForeignKey('rips.RipsDestinoEgreso', blank=True,null= True, editable=True, on_delete=models.PROTECT ,   related_name='ripssServicios10')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    class Meta:
        unique_together = (('tipoDoc', 'documento','consec'),)


    def __integer__(self):
        return self.documento



class Furips(models.Model):
    A = 'A'
    I = 'I'
    TIPO_CHOICES = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO'),
    )
    S = 'S'
    N = 'N'
    TIPO_CHOICES1 = (
        ('S', 'Si'),
        ('N', 'No'),
    )
    Asegurado = 'A'
    No_Asegurado = 'N'
    Vehiculo_Fantasma = 'V'
    Poliza_Falsa = 'P'
    Vehiculo_en_fuga = 'F'
    TIPO_CONDICION = (
        (Asegurado, 'Asegurado'),
        (No_Asegurado, 'No Asegurado'),
        (Vehiculo_Fantasma, 'Vehiculo Fantasma'),
        (Poliza_Falsa, 'Poliza Falsa'),
        (Vehiculo_en_fuga, 'Vehiculo en fuga'),
    )
    P = 'Servicio Particular'
    U = 'Servicio Publico'
    O = 'Servicio Oficial'
    D = 'Servicio Diplomatico'
    T = 'De transporte Masivo'
    E =	'Escolar'
    TIPO_CHOICES3 = (
        (P, 'Servicio Particular'),
        (U, 'Servicio Publico'),
        (O, 'Servicio Oficial'),
        (D, 'Servicio Diplomatico'),
        (T, 'De transporte Masivo'),
	    (E, 'Escolar'),
    )
    R =  'Remision'
    O = 'Orden de Servicio'
    TIPO_CHOICES4 = (
        (R, 'Remision'),
        (O, 'Orden de Servicio'),
    )

    id = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica3')
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documentofur')
    consec    = models.IntegerField(default=0)
    fechaRadicado =  models.DateTimeField( editable=True, null=True, blank=True)
    numeroRadicacion = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    numeroRadicadoAnterior = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    numeroFactura = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    primerNombreVictima = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoNombreVictima = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    primerApellidoVictima = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoApellidoVictima = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    tipoDocVictima        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc14')
    documentoVictima      = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento14')
    consecVictima         = models.IntegerField( blank=True, null=True, editable=True,)
    condicionAccidentado = models.CharField(max_length=1, default='A',  blank=True, null=True,  editable=False ,choices = TIPO_CONDICION)
    evento = models.ForeignKey('basicas.Eventos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    direccionEvento = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    departamentoEvento = models.ForeignKey('sitios.Departamentos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dept10')
    municipioEvento = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni10')
    localidadEvento = models.ForeignKey('sitios.Localidades', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='local09')
    zonaEvento =  models.CharField(max_length=1, default='A',  blank=True, null=True,  editable=False )
    fechaEvento = models.DateTimeField( default=now,editable=True,  blank=True, null=True)
    eventoDescripcion = models.CharField(max_length=500,  blank=True, null=True, editable=True,)
    estado = models.CharField(max_length=20,  blank=True, null=True, editable=True, choices = TIPO_CHOICES1)
    marcaVehiculo = models.CharField(max_length=50,  blank=True, null=True, editable=True,)
    placaVehiculo = models.CharField(max_length=20, blank=True, null=True, editable=True,)
    tipoServicioVehiculo = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    tipoVehiculo = models.CharField(max_length=20,  blank=True, null=True, editable=True, choices = TIPO_CHOICES3)
    codigoaseguradora = models.CharField(max_length=20, blank=True, null=True, editable=True,)
    numeroPoliza= models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    fechaIniPoliza = models.DateTimeField(default=now,  editable=True, null=True, blank=True)
    fechaFinPoliza = models.DateTimeField(default=now, editable=True, null=True, blank=True)
    intervencionAutoridad = models.CharField(max_length=1,  blank=True, null=True, editable=True,)
    cobroExcedentePoliza = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    primerNombrePropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoNombrePropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    primerApellidoPropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoApellidoPropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True)
    tipoDocPropietario        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,   related_name='tipoDoc17')
    documentoPropietario      = models.CharField(max_length=20,  blank=True, null=True, editable=True)
    departamentoPropietario = models.ForeignKey('sitios.Departamentos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dept11')
    municipioPropietario = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni11')
    localidadPropietario = models.ForeignKey('sitios.Localidades', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='local10')
    direccionPropietario = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    primerNombreInvolucrado = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoNombreInvolucrado = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    primerApellidoInvolucrado = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    segundoApellidoInvolucrado = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    tipoDocInvolucrado        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,   related_name='tipoDoc15')
    documentoInvolucrado     = models.CharField(max_length=20,  blank=True, null=True, editable=True )
    departamentoInvolucrado = models.ForeignKey('sitios.Departamentos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dept12')
    municipioInvolucrado = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni12')
    localidadInvolucrado = models.ForeignKey('sitios.Localidades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    direccionInvolucrado = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    tipoReferencia =  models.CharField(max_length=20,  blank=True, null=True, editable=True, choices = TIPO_CHOICES4)
    fechaRemision = models.DateTimeField( default=now, editable=True, null=True, blank=True)
    prestadorRemite = models.ForeignKey('clinico.Ips', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='ips7' )
    codigoInscripcion = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    profesionalRemite = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True ,  related_name='planta112')
    fechaAceptacion = models.DateTimeField( editable=True, null=True, blank=True)
    prestadorRecibe = models.ForeignKey('clinico.Ips', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='ips86' )
    codigoInscripcionRecibe = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    profesionalRecibe = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    numeroPlacaTranporto = models.CharField(max_length=20, blank=True, null=True, editable=True,)
    trasportoVictimaDesde = models.CharField(max_length=80, blank=True, null=True, editable=True,)
    trasportoVictimaHasta = models.CharField(max_length=80, blank=True, null=True, editable=True,)
    tipoTransporteTransporto = models.CharField(max_length=80, blank=True, null=True, editable=True,)
    lugarRecogeVictima =models.CharField(max_length=80, blank=True, null=True, editable=True,)
    certificacionIngreso =  models.DateTimeField( editable=True, null=True, blank=True)
    certificacionEgreso =  models.DateTimeField( editable=True, null=True, blank=True)
    dxPrincIngreso     = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='dx1' )
    dxRel1Ingreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx2' )
    dxRel2Ingreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx3' )
    dxPrincEgreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx4' )
    dxRel1Egreso    = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx5' )
    dxRel2Egreso    = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx6' )
    tipoDocProfesionalAtendio   = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='tipoDoc16')
    documentoProfesionalAtendio =  models.ForeignKey('planta.planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    amparoReclamaFacturadoQx =  models.DecimalField(max_digits=7, decimal_places=2, default=0.0 , blank=True, null=True, editable=True,)
    amparoReclamaAFosygaQx =  models.DecimalField(max_digits=7, decimal_places=2, default=0.0, blank=True, null=True, editable=True,)
    amparoReclamaFacturadoGastos =  models.DecimalField(max_digits=7, decimal_places=2, default=0.0, blank=True, null=True, editable=True,)
    amparoReclamaAFosygaGastos =  models.DecimalField(max_digits=7, decimal_places=2, default=0.0, blank=True, null=True, editable=True,)
    fechaRegistro  = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='planta111')
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)

    def __str__(self):
        return self.numeroRadicacion
