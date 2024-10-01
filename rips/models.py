from django.db import models
from django.utils.timezone import now

# Create your models here.


class RipsEnvios (models.Model):

    id = models.AutoField(primary_key=True)
    numeroEnvio = models.CharField(max_length=10, blank=True,null= True, editable=True)
    fechaEnvio  =  models.DateTimeField(default=now, blank=True, null=True, editable=True)
    fechaRespuesta =  models.DateTimeField(default=now, blank=True, null=True, editable=True)
    cantidadFacturas = models.CharField(max_length=5, blank=True,null= True, editable=True)
    cantidadPasaron = models.CharField(max_length=5, blank=True,null= True, editable=True)
    cantidadRechazadas = models.CharField(max_length=5, blank=True,null= True, editable=True)
    estadoPasoMinisterio=  models.CharField(max_length=1, default='S', editable=False)
    jsonError = models.CharField(max_length=5000, blank=True,null= True, editable=True)
    jsonAprobado = models.CharField(max_length=5000, blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.numeroEnvio

class RipsDetalle (models.Model):

    id = models.AutoField(primary_key=True)
    ripsEnvios =  models.ForeignKey('rips.RipsEnvios', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='Envios01')
    numeroFactura  =  models.CharField(max_length=20, blank=True,null= True, editable=True)
    cuv  =  models.CharField(max_length=500, blank=True,null= True, editable=True)
    estadoPasoMinisterio=  models.CharField(max_length=1, default='S', editable=False)
    jsonError = models.CharField(max_length=5000, blank=True,null= True, editable=True)
    jsonAprobado = models.CharField(max_length=5000, blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.numeroFactura

class RipsTransaccion (models.Model):

    id = models.AutoField(primary_key=True)
    numDocumentoIdObligado =   models.CharField(max_length=9, blank=True,null= True, editable=True)
    numFactura  =  models.CharField(max_length=20, blank=True,null= True, editable=True)
    tipoNota  =  models.ForeignKey('cartera.TiposNotas', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='TipoNota01')
    numNota =  models.CharField(max_length=20, default='S', editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)

    def __str__(self):
        return self.numDocumentoIdObligado

class RipsTipoUsuario (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsPaises (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=3, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre



class RipsUsuarios (models.Model):
    UNO =  'Rural'
    DOS = 'Urbano'
    TIPO_ZONAS = (
        (UNO, 'Rural'),
        (DOS, 'Urbano'),
    )	
    SI =  'Si'
    NO = 'NO'
    TIPO_INCAPACIDAD = (
        (SI, 'Si'),
        (NO, 'No'),
    )	
    H =  'Masculino'
    M = 'Femenino'
    I = 'Indeterminado'
    TIPO_SEXO = (
        (H, 'Masculino'),
        (M, 'Femenino'),
	(I, 'Indeterminado'),
     )	


    id = models.AutoField(primary_key=True)
    tipoDocumentoIdentificacion =   models.CharField(max_length=9, blank=True,null= True, editable=True)
    tipoUsuario  =  models.CharField(max_length=20, blank=True,null= True, editable=True)
    fechaNacimiento   =   models.DateTimeField(default=now, blank=True, null=True, editable=True)
    codSexo =  models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_SEXO)
    codPaisResidencia = models.ForeignKey('rips.RipsPaises', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='Paises01')
    codMunicipioResidencia = models.ForeignKey('sitios.Municipios', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='MunicipioRes01')
    codZonaTerritorialResidencia = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_ZONAS)
    incapacidad = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_INCAPACIDAD)
    consecutivo = models.CharField(max_length=10, blank=True,null= True, editable=True)
    codPaisOrigen = models.ForeignKey('rips.RipsPaises', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='Usu01')
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)

    def __str__(self):
        return self.nombre


class RipsGrupoServicios (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsModalidadAtencion (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsServicios (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=4, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsFinalidadConsulta (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsCausaExterna (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

class RipsConceptoRecaudo (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsTiposDocumento (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre



class RipsConsultas (models.Model):

    UNO = 'Impresion Diagnostica'
    DOS = 'Confirmado nuevo'
    TRES = 'Confirmado repetido'
    TIPO_DIAGNOSTICO = (
        (UNO, 'Impresion Diagnostica'),
        (DOS, 'Confirmado nuevo'),
        (TRES, 'Confirmado REPETIDO'),
    )
    id = models.AutoField(primary_key=True)
    codPrestador =  models.CharField(max_length=12, blank=True,null= True, editable=True)
    fechaInicioAtencion = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    numAutorizacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
    codConsulta = models.ForeignKey('clinico.Examenes', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Examen01')
    modalidadGrupoServicioTecSal = models.ForeignKey('rips.RipsGrupoServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Modal01')
    grupoServicios = models.ForeignKey('rips.RipsGrupoServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Grupo01')
    codServicio =   models.ForeignKey('rips.RipsServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Servicio01')
    finalidadTecnologiaSalud    = models.ForeignKey('rips.RipsFinalidadConsulta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Final01')
    causaMotivoAtencion = models.ForeignKey('rips.RipsCausaExterna', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Causa01')
    codDiagnosticoPrincipal = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost01')
    codDiagnosticoRelacionado1 =  models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost02')
    codDiagnosticoRelacionado2 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost03')
    codDiagnosticoRelacionado3 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost04')
    tipoDiagnosticoPrincipal = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_DIAGNOSTICO)
    tipoDocumentoIdentificacion = models.ForeignKey('rips.RipsTiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    numDocumentoIdentificacion = models.CharField(max_length=20, blank=True,null= True, editable=True)
    vrServicio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    conceptoRecaudo  = models.ForeignKey('rips.RipsConceptoRecaudo', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Recau01')
    valorPagoModerador = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    numFEVPagoModerador =  models.CharField(max_length=20, blank=True,null= True, editable=True)
    consecutivo = models.DecimalField(max_digits=7, decimal_places=0, default=0)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas01')
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)


    def __str__(self):
        return self.codPrestador

class RipsViasIngresoSalud (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsProcedimientos (models.Model):

   id = models.AutoField(primary_key=True)
   codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
   fechaInicioAtencion = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   idMIPRES = models.CharField(max_length=15, blank=True,null= True, editable=True)
   numAutorizacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
   codProcedimiento =  models.ForeignKey('clinico.Examenes', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Examen05')
   viaIngresoServicioSalud = models.ForeignKey('rips.RipsViasIngresoSalud', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='IngresoSal01')
   modalidadGrupoServicioTecSal = models.ForeignKey('rips.RipsGrupoServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='ModalServ01')
   grupoServicios =  models.ForeignKey('rips.RipsGrupoServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='GrupoServicios01')
   codServicio = models.ForeignKey('rips.RipsServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Serrvicio02')
   finalidadTecnologiaSalud = models.ForeignKey('rips.RipsFinalidadConsulta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Finalidad02')
   tipoDocumentoIdentificacion = models.ForeignKey('rips.RipsTiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='TipoDocu05')
   numDocumentoIdentificacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
   codDiagnosticoPrincipal = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost10')
   codDiagnosticoRelacionado = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost11')
   codComplicacion = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost12')
   vrServicio =  models.DecimalField(max_digits=15, decimal_places=0, default=0)
   conceptoRecaudo = models.ForeignKey('rips.RipsConceptoRecaudo', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Recaudo05')
   valorPagoModerador =  models.DecimalField(max_digits=10, decimal_places=0, default=0)
   numFEVPagoModerador = models.CharField(max_length=20, blank=True,null= True, editable=True)
   consecutivo  = models.DecimalField(max_digits=7, decimal_places=0, default=0)
   usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas02')
   fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)

   def __str__(self):
        return self.codPrestador

class RipsDestinoEgreso (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre

  

class RipsUrgenciasObservacion (models.Model):

   id = models.AutoField(primary_key=True)
   codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
   fechaInicioAtencion = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   causaMotivoAtencion = models.ForeignKey('rips.RipsCausaExterna', blank=True, null=True, editable=True, on_delete=models.PROTECT)
   codDiagnosticoPrincipal =  models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost21')
   codDiagnosticoPrincipalE = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost22')
   codDiagnosticoRelacionadoE1 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost23')
   codDiagnosticoRelacionadoE2 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost24')
   codDiagnosticoRelacionadoE3 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost25')
   condicionDestinoUsuarioEgreso = models.ForeignKey('rips.RipsDestinoEgreso', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='DestinoEgre01')
   codDiagnosticoCausaMuerte = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost26')
   fechaEgreso = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   consecutivo =  models.DecimalField(max_digits=7, decimal_places=0, default=0)
   usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas05')
   fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)


   def __str__(self):
        return self.codPrestador




class RipsHospitalizacion (models.Model):

   id = models.AutoField(primary_key=True)
   codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
   viaIngresoServicioSalud = models.ForeignKey('rips.RipsViasIngresoSalud', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='IngresoSal11')
   fechaInicioAtencion = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   numAutorizacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
   causaMotivoAtencion = models.ForeignKey('rips.RipsCausaExterna', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='CausaExt05')
   codDiagnosticoPrincipal = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost31')
   codDiagnosticoPrincipalE  = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost32')
   codDiagnosticoRelacionadoE1 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost33')
   codDiagnosticoRelacionadoE2 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost34')
   codDiagnosticoRelacionadoE3 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost35')
   codComplicacion = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost36')
   condicionDestinoUsuarioEgreso = models.ForeignKey('rips.RipsDestinoEgreso', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='DestinoUsu02') 
   codDiagnosticoCausaMuerte = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost37')
   fechaEgreso = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   consecutivo =  models.DecimalField(max_digits=7, decimal_places=0, default=0)
   usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas21')
   fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)



   def __str__(self):
        return self.codPrestador

class RipsRecienNacido(models.Model):
    H =  'Masculino'
    M = 'Femenino'
    I = 'Indeterminado'
    TIPO_SEXO = (
        (H, 'Masculino'),
        (M, 'Femenino'),
	(I, 'Indeterminado'),
     )
    id = models.AutoField(primary_key=True)
    codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
    tipoDocumentoIdentificacion = models.ForeignKey('rips.RipsTiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='TipoDocRips01')
    numDocumentoIdentificacion = models.CharField(max_length=20, blank=True,null= True, editable=True)
    fechaNacimiento = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    edadGestacional = models.CharField(max_length=2, blank=True,null= True, editable=True)
    numConsultasCPrenatal =  models.DecimalField(max_digits=1, decimal_places=0, default=0)
    codSexoBiologico = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_SEXO)
    peso =  models.DecimalField(max_digits=4, decimal_places=0, default=0)
    codDiagnosticoPrincipal = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost41')
    condicionDestinoUsuarioEgreso =  models.ForeignKey('rips.RipsDestinoEgreso', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost42')
    codDiagnosticoCausaMuerte = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost43')
    fechaEgreso = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    consecutivo =  models.DecimalField(max_digits=7, decimal_places=0, default=0)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas33')
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)


    def __str__(self):

        return self.codPrestador

class RipsTipoMedicamento (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsCums (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=20, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsUmm (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=4, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)
   descripcion = models.CharField(max_length=80, blank=True,null= True, editable=True)   

   def __str__(self):
        return self.nombre

class RipsFormaFarmaceutica (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=6, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)
   descripcion = models.CharField(max_length=500, blank=True,null= True, editable=True)   

   def __str__(self):
        return self.nombre


class RipsUnidadUpr (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsMedicamentos(models.Model):

   id = models.AutoField(primary_key=True)
   codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
   numAutorizacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
   idMIPRES = models.CharField(max_length=15, blank=True,null= True, editable=True)
   fechaDispensAdmon = models.DateTimeField(default=now, blank=True, null=True, editable=True)
   codDiagnosticoPrincipal = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost51')
   codDiagnosticoRelacionado = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Diagnost52')
   tipoMedicamento = models.ForeignKey('rips.RipsTipoMedicamento', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='TipoMed01')
   codTecnologiaSalud  = models.ForeignKey('rips.RipsCums', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Cums01')
   nomTecnologiaSalud = models.CharField(max_length=30, blank=True,null= True, editable=True)
   concentracionMedicamento = models.DecimalField(max_digits=3, decimal_places=0, default=0)
   unidadMedida =  models.ForeignKey('rips.RipsUmm', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Umedida11')
   formaFarmaceutica = models.ForeignKey('rips.RipsFormaFarmaceutica', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Farmaceu01')
   unidadMinDispensa = models.ForeignKey('rips.RipsUnidadUpr', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='UnidadUpr01')
   cantidadMedicamento = models.DecimalField(max_digits=10, decimal_places=0, default=0)
   diasTratamiento = models.DecimalField(max_digits=3, decimal_places=0, default=0)
   tipoDocumentoIdentificacion  = models.ForeignKey('rips.RipsTiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='RipsTiposDoc31')
   numDocumentoIdentificacion= models.CharField(max_length=20, blank=True,null= True, editable=True)
   vrUnitMedicamento = models.DecimalField(max_digits=15, decimal_places=0, default=0)
   vrServicio = models.DecimalField(max_digits=15, decimal_places=0, default=0)
   conceptoRecaudo = models.ForeignKey('rips.RipsConceptoRecaudo', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Recaudo41')
   valorPagoModerador = models.DecimalField(max_digits=10, decimal_places=0, default=0)
   numFEVPagoModerador = models.CharField(max_length=20, blank=True,null= True, editable=True)
   consecutivo =  models.DecimalField(max_digits=7, decimal_places=0, default=0)
   usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas61')
   fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
 


   def __str__(self):
        return self.codPrestador

class RipsTipoOtrosServicios (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsDci (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre


class RipsOtrosServicios(models.Model):

   id = models.AutoField(primary_key=True)
   codPrestador = models.CharField(max_length=12, blank=True,null= True, editable=True)
   numAutorizacion = models.CharField(max_length=30, blank=True,null= True, editable=True)
   idMIPRES = models.CharField(max_length=15, blank=True,null= True, editable=True)
   fechaSuministroTecnologia =  models.DateTimeField(default=now, blank=True, null=True, editable=True)
   tipoOS = models.ForeignKey('rips.RipsTipoOtrosServicios', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='OtrosServ01')
   codTecnologiaSalud =  models.ForeignKey('rips.RipsCums', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='RipsCums11')
   nomTecnologiaSalud = models.CharField(max_length=30, blank=True,null= True, editable=True)
   cantidadOS  =   models.DecimalField(max_digits=5, decimal_places=0, default=0)
   tipoDocumentoIdentificacion = models.ForeignKey('rips.RipsTiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='RipsTiposDoc21')
   numDocumentoIdentificacion = models.CharField(max_length=20, blank=True,null= True, editable=True)
   vrUnitOS = models.DecimalField(max_digits=15, decimal_places=0, default=0)
   vrServicio = models.DecimalField(max_digits=15, decimal_places=0, default=0)
   conceptoRecaudo = models.ForeignKey('rips.RipsConceptoRecaudo', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Recaudo50')
   valorPagoModerador = models.DecimalField(max_digits=10, decimal_places=0, default=0)
   numFEVPagoModerador = models.CharField(max_length=20, blank=True,null= True, editable=True)
   consecutivo =  models.DecimalField(max_digits=7, decimal_places=0, default=0)
   usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas12')
   fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
 


   def __str__(self):
        return self.codPrestador



