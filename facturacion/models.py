from django.db import models
from django.utils.timezone import now

# Create your models here.


class Eapb (models.Model):

    id = models.AutoField(primary_key=True)
    codigoEapb=models.CharField(max_length=8, blank=True,null= True, editable=True)
    nombre = models.CharField(max_length=30, null=False)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento =models.CharField(max_length=30, blank=True,null= True, editable=True)
    direccion= models.CharField(max_length=150, blank=True,null= True, editable=True)
    telefono =models.CharField(max_length=30, blank=True,null= True, editable=True)
    codigoRips= models.CharField(max_length=8, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre

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

class TiposSuministro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)


class Suministros (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True,null= True, editable=True)
    tipoSuministro =   models.ForeignKey('facturacion.TiposSuministro', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    nombreGenerico  =  models.CharField(max_length=250, default='A', editable=False )
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    concentracion = models.ForeignKey('clinico.MedicamentosDci', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    grupo =  models.ForeignKey('clinico.Grupos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    subGrupo = models.ForeignKey('clinico.Grupos', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Subgrupo01i01')
    unidadMedida =  models.ForeignKey('clinico.UnidadesDeMedidaDosis', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    fraccion =  models.DecimalField( max_digits=20, decimal_places=2)
    unidadFraccion =    models.CharField(max_length=20, blank=True,null= True, editable=True)
    viaAdministracion = models.ForeignKey('clinico.ViasAdministracion', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    vence =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    control =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    antibiotico =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    pos	 =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    facturable   = models.CharField(max_length=1, blank=True,null= True, editable=True)
    stockMinimo = models.DecimalField( max_digits=20, decimal_places=2)
    stockMaximo = models.DecimalField( max_digits=20, decimal_places=2)
    maxOrdenar = models.DecimalField( max_digits=20, decimal_places=2)
    estabilidad	 = models.DecimalField( max_digits=20, decimal_places=0)
    invFarmacia = models.CharField(max_length=1, blank=True,null= True, editable=True)
    invAlmacen = models.CharField(max_length=1, blank=True,null= True, editable=True)
    enfermeria = models.CharField(max_length=1, blank=True,null= True, editable=True)
    terapia = models.CharField(max_length=1, blank=True,null= True, editable=True)
    nutricion = models.CharField(max_length=1, blank=True,null= True, editable=True)
    cantidad	 = models.DecimalField( max_digits=20, decimal_places=2)
    cums = models.CharField(max_length=30, blank=True,null= True, editable=True)
    formaFarmaceutica = models.CharField(max_length=250, blank=True,null= True, editable=True)
    regSanitario = models.CharField(max_length=30, blank=True,null= True, editable=True)
    altoCosto = models.CharField(max_length=1, blank=True,null= True, editable=True)
    vrCompra = models.DecimalField( max_digits=20, decimal_places=2)
    vrUltimaCompra = models.DecimalField( max_digits=20, decimal_places=2)
    codigoAtc	= models.CharField(max_length=10, blank=True,null= True, editable=True)
    infusion  = models.CharField(max_length=1, blank=True,null= True, editable=True)
    tipoAdministracion = models.CharField(max_length=20, blank=True,null= True, editable=True)
    regulado = models.CharField(max_length=1, blank=True,null= True, editable=True)
    vaorRegulado = models.DecimalField( max_digits=20, decimal_places=2)
    observaciones = models.CharField(max_length=250, blank=True,null= True, editable=True)
    sispro = models.CharField(max_length=1, blank=True,null= True, editable=True)
    oncologico = models.CharField(max_length=1, blank=True,null= True, editable=True)
    ortesis = models.CharField(max_length=1, blank=True,null= True, editable=True)
    mipres = models.CharField(max_length=15, blank=True,null= True, editable=True)
    epiHigiene = models.CharField(max_length=1, blank=True,null= True, editable=True)
    controlStock = models.CharField(max_length=1, blank=True,null= True, editable=True)
    AnatoPos = models.CharField(max_length=1, blank=True,null= True, editable=True)
    magistralControl  = models.CharField(max_length=1, blank=True,null= True, editable=True)
    genericoPos = models.CharField(max_length=1, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.id)

class TiposTarifa (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.id)

class ConveniosPaciente(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='DocumentoHistoria')
    convenio = models.ForeignKey('contratacion.Convenios', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class ConveniosPacienteIngresos(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoHistoria2')
    consecAdmision = models.IntegerField(default=0)
    convenio = models.ForeignKey('contratacion.Convenios', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    class Meta:
        unique_together = (('tipoDoc', 'documento','consecAdmision','convenio'),)

    def __str__(self):
        return str(self.id)





