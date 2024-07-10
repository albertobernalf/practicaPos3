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
    hClinica       = models.CharField(max_length=50, default='', editable=True)
    regimen        = models.ForeignKey('clinico.Regimenes', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    tiposCotizante  = models.ForeignKey('clinico.TiposCotizante', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    enfermedaActual= models.ForeignKey('clinico.Enfermedades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    motivo         = models.CharField(max_length=1000, default='', editable=True)
    examenFisico   = models.CharField(max_length=5000, default='', editable=True)
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
    vistobno    = models.CharField(max_length=1, default='', editable=True)
    tipoTrauma  = models.CharField(max_length=20, default='', editable=True)
    cinematicaTrauma = models.CharField(max_length=5, default='', editable=True)
    tipoIngreso = models.CharField(max_length=20, default='', editable=True)
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
    numeroFactura = models.CharField(max_length=20, default='', editable=True)
    fechaRadicado =  models.DateTimeField( editable=True, null=True, blank=True)
    direccionVictima = models.CharField(max_length=80, default='', editable=True)
    telVictima = models.CharField(max_length=10, default='', editable=True)
    evento = models.ForeignKey('basicas.Eventos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    eventoDescripcion = models.CharField(max_length=500, default='', editable=True)
    direccionEvento = models.CharField(max_length=80, default='', editable=True)
    fechaEvento = models.DateTimeField( editable=True, null=True, blank=True)
    municipioEvento = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni2')
    localidadEvento = models.ForeignKey('sitios.Localidades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    estadoAsegurado = models.CharField(max_length=20, default='', editable=True)
    tipoVehiculo = models.CharField(max_length=20, default='', editable=True)
    placaAsegurado = models.CharField(max_length=10, default='', editable=True)
    marcaAsegurado = models.CharField(max_length=15, default='', editable=True)
    codigoaseguradora = models.CharField(max_length=20, default='', editable=True)
    poliza= models.CharField(max_length=20, default='', editable=True)
    fechaIniPoliza = models.DateTimeField( editable=True, null=True, blank=True)
    fechaFinPoliza = models.DateTimeField( editable=True, null=True, blank=True)
    tipoDocPlaca2 = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc14')
    documentoPlaca2 =  models.CharField(max_length=20, default='', editable=True)
    placa2  = models.CharField(max_length=10, default='', editable=True)
    tipoDocPlaca3 = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc24')
    documentoPlaca3 =  models.CharField(max_length=20, default='', editable=True)
    placa3 = models.CharField(max_length=10, default='', editable=True)
    tipoDocPropietario = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='tipoDoc4')
    documentoPropietario = models.CharField(max_length=20, default='', editable=True)
    nombresPropietario = models.CharField(max_length=30, default='', editable=True)
    apellidosPropietario = models.CharField(max_length=30, default='', editable=True)
    direccionProietario = models.CharField(max_length=80, default='', editable=True)
    telefonoPropietario = models.CharField(max_length=20, default='', editable=True)
    municipioPropietario = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='muni1')
    tipoDocConductor = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT  ,  related_name='tipoDoc6')
    documentoConductor = models.CharField(max_length=20, default='', editable=True)
    nombresConductor = models.CharField(max_length=30, default='', editable=True)
    apellidosConductor = models.CharField(max_length=30, default='', editable=True)
    direccionConductor = models.CharField(max_length=80, default='', editable=True)
    telefonoConductor = models.CharField(max_length=20, default='', editable=True)
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
    tipoAutomotor   = models.CharField(max_length=20, default='', editable=True)
    accidenteMultiple =   models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES1)
    ingresoUci =  models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES1)
    velocidadAutomotor = models.CharField(max_length=50, default='', editable=True)
    dispositivoSeguridad = models.CharField(max_length=50, default='', editable=True)
    tipoColision = models.CharField(max_length=20, default='', editable=True)
    radicadoSiras =  models.CharField(max_length=20, default='', editable=True)
    fechaRegistro  = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='planta1')
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)

    def __str__(self):
        return self.nombre