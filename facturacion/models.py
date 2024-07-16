from django.db import models
from django.utils.timezone import now

# Create your models here.


class Empresas (models.Model):

    id           = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.CharField(max_length=30, blank=True,null= True, editable=True,)
    nombre = models.CharField(max_length=50, blank=True,null= True, editable=True,)
    codigoEapb = models.CharField(max_length=10, blank=True,null= True, editable=True,)
    direccion = models.CharField(max_length=80, blank=True,null= True, editable=True,)
    telefono =  models.CharField(max_length=20, blank=True,null= True, editable=True,)
    representante =  models.CharField(max_length=80, blank=True,null= True, editable=True,)
    regimen =  models.ForeignKey('clinico.Regimenes', blank=True,null= True, editable=True,  on_delete=models.PROTECT)
    fosyga = models.CharField(max_length=1, default='N', editable=False)
    particular = models.CharField(max_length=1, default='N', editable=False)
    departamento = models.ForeignKey('sitios.Departamentos', blank=True,null= True, editable=True,  on_delete=models.PROTECT , related_name='Depto01')
    municipio  = models.ForeignKey('sitios.Municipios', blank=True,null= True, editable=True,  on_delete=models.PROTECT , related_name='Muni01')
    codigoPostal = models.CharField(max_length=30, blank=True,null= True, editable=True,)
    responsableFiscal = models.CharField(max_length=80, blank=True,null= True, editable=True,)
    identificadorDian = models.CharField(max_length=80, blank=True,null= True, editable=True,)
    fechaRegistro = models.DateTimeField(default=now, blank=True,null= True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre


class Cups(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    codigoCups = models.CharField(max_length=15, null=False)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    autoriza = models.CharField(max_length=1, null=False)
    codigoRips = models.CharField(max_length=15, null=False)
    cupsGrupo = models.CharField(max_length=15, null=False)
    cupsSubgrupo = models.CharField(max_length=15, null=False)
    cupsCategoria = models.CharField(max_length=15, null=False)
    resolucion1132 = models.CharField(max_length=15, null=False)
    nivelAtencion  =  models.CharField(max_length=15, null=False)
    centroCosto = models.CharField(max_length=15, null=False)
    finalidad = models.CharField(max_length=1, null=False)
    duracion =   models.CharField(max_length=15, null=False)
    manejaInterfaz = models.CharField(max_length=1, null=False)
    distribucionTerceros = models.CharField(max_length=1, null=False)
    consentimientoInformado = models.CharField(max_length=1, null=False)
    cita1Vez = models.CharField(max_length=1, null=False)
    cuentaContable = models.CharField(max_length=20, null=False)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre


class TiposCups(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __integer__(self):
      return self.nombre


class Conceptos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipoCups = models.ForeignKey('facturacion.TiposCups', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    codAd = models.CharField(max_length=2, default='A', editable=False)
    codAt = models.CharField(max_length=3, default='A', editable=False)
    ripsAc = models.CharField(max_length=1, default='A', editable=False)
    ripsAp = models.CharField(max_length=1, default='A', editable=False)
    ripsAt = models.CharField(max_length=1, default='A', editable=False)
    ripsAm = models.CharField(max_length=1, default='A', editable=False)
    ripsAh = models.CharField(max_length=1, default='A', editable=False)
    ripsAu = models.CharField(max_length=1, default='A', editable=False)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __integer__(self):
      return self.nombre

