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

    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    class Meta:
        unique_together = (('tipoDoc', 'documento','consec'),)


    def __integer__(self):
        return self.nombre


class Triage(models.Model):

    ACTIVO = 'ACTIVO'
    INACTIVO = 'INACTIVO'

    TIPO_CHOICES = (
        (ACTIVO, 'ACTIVO'),
        (INACTIVO, 'INACTIVO')
    )
    id = models.AutoField(primary_key=True)
    sedesClinica   = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica1')
    fechaSolicita = models.DateTimeField( editable=True, null=True, blank=True)
    fechaAtendio = models.DateTimeField( editable=True, null=True, blank=True)
    tipoDoc        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento      = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento1')
    consec         = models.IntegerField()
    hClinica       = models.CharField(max_length=50,  blank=True, null=True, editable=True,)
    regimen        = models.ForeignKey('clinico.Regimenes', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    tiposCotizante  = models.ForeignKey('clinico.TiposCotizante', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    enfermedaActual= models.ForeignKey('clinico.Enfermedades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    motivo         = models.CharField(max_length=1000,  blank=True, null=True, editable=True,)
    examenFisico   = models.CharField(max_length=5000,  blank=True, null=True, editable=True,)
    frecCardiaca   = models.IntegerField()
    frecRespiratoria = models.IntegerField()
    taSist          = models.IntegerField()
    taDiast         = models.IntegerField()
    taMedia         = models.IntegerField()
    glasgow         = models.IntegerField()
    peso            = models.IntegerField()
    temperatura     = models.IntegerField()
    estatura        = models.IntegerField()
    clasificacionTriage = models.ForeignKey('clinico.TiposTriage', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    viaEgreso  = models.ForeignKey('clinico.ViasEgreso', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    glucometria = models.IntegerField()
    saturacion  = models.IntegerField()
    escalaDolor = models.IntegerField()
    causaExterna = models.ForeignKey('clinico.CausasExterna', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    vistobno    = models.CharField(max_length=1,  blank=True, null=True, editable=True,)
    tipoTrauma  = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    cinematicaTrauma = models.CharField(max_length=5,  blank=True, null=True, editable=True,)
    tipoIngreso = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    usuarioAutoriza = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    fechaModanexo = models.DateTimeField(editable=True, null=True, blank=True)
    observaciones = models.CharField(max_length=200, default='', editable=True)
    alergiasTriage = models.CharField(max_length=50, default='', editable=True)
    fechaRegistro  = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='Documento3')
    usuarioAtiende = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='Documento2')
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)


    def __str__(self):
            return self.nombre


class Furips(models.Model):
    ACTIVO = 'ACTIVO'
    INACTIVO = 'INACTIVO'
    TIPO_CHOICES = (
        (ACTIVO, 'ACTIVO'),
        (INACTIVO, 'INACTIVO'),
    )
    S = 'S'
    N = 'N'
    TIPO_CHOICES1 = (
        (S, 'S'),
        (N, 'N'),
    )
    id = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica3')
    tipoDoc        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento      = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento4')
    consec         = models.IntegerField()
    numeroFactura = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    fechaRadicado =  models.DateTimeField( editable=True, null=True, blank=True)
    direccionVictima = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    telVictima = models.CharField(max_length=10,  blank=True, null=True, editable=True,)
    evento = models.ForeignKey('basicas.Eventos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    eventoDescripcion = models.CharField(max_length=500,  blank=True, null=True, editable=True,)
    direccionEvento = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    fechaEvento = models.DateTimeField( editable=True,  blank=True, null=True)
    municipioEvento = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni2')
    localidadEvento = models.ForeignKey('sitios.Localidades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    estadoAsegurado = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    tipoVehiculo = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    placaAsegurado = models.CharField(max_length=10, blank=True, null=True, editable=True,)
    marcaAsegurado = models.CharField(max_length=15,  blank=True, null=True, editable=True,)
    codigoaseguradora = models.CharField(max_length=20, blank=True, null=True, editable=True,)
    poliza= models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    fechaIniPoliza = models.DateTimeField( editable=True, null=True, blank=True)
    fechaFinPoliza = models.DateTimeField( editable=True, null=True, blank=True)
    tipoDocPlaca2 = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc14')
    documentoPlaca2 =  models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    placa2  = models.CharField(max_length=10, blank=True, null=True, editable=True,)
    tipoDocPlaca3 = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc24')
    documentoPlaca3 =  models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    placa3 = models.CharField(max_length=10, default='', editable=True)
    tipoDocPropietario = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc4')
    documentoPropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    nombresPropietario = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    apellidosPropietario = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    direccionProietario = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    telefonoPropietario = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    municipioPropietario = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni1')
    tipoDocConductor = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='tipoDoc6')
    documentoConductor = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    nombresConductor = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    apellidosConductor = models.CharField(max_length=30,  blank=True, null=True, editable=True,)
    direccionConductor = models.CharField(max_length=80,  blank=True, null=True, editable=True,)
    telefonoConductor = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    municipioconductor = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    dxPrincIngreso     = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='dx1' )
    dxRel1Ingreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx2' )
    dxRel2Ingreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx3' )
    dxPrincEgreso   = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx4' )
    dxRel1Egreso    = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx5' )
    dxRel2Egreso    = models.ForeignKey('clinico.Diagnosticos', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx6' )
    tipoDocProfesional   = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='tipoDoc5')
    documentoProfesional =  models.ForeignKey('planta.planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    completo         =  models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES1)
    tipoAutomotor   = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    accidenteMultiple =   models.CharField(max_length=1,  blank=True, null=True, editable=True,choices = TIPO_CHOICES1)
    ingresoUci =  models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES1)
    velocidadAutomotor = models.CharField(max_length=50,  blank=True, null=True, editable=True,)
    dispositivoSeguridad = models.CharField(max_length=50,  blank=True, null=True, editable=True,)
    tipoColision = models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    radicadoSiras =  models.CharField(max_length=20,  blank=True, null=True, editable=True,)
    fechaRegistro  = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='planta1')
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)

    def __str__(self):
        return self.nombre