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

    def __str__(self):
        return self.nombre

class TiposEmpresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class Empresas (models.Model):

    id           = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    tipoEmpresa = models.ForeignKey('facturacion.TiposEmpresa', blank=True,null= True, editable=True, on_delete=models.PROTECT)
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

    def __str__(self):
        return self.nombre


class Conceptos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    #tipoCups = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT)
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


    def __str__(self):
        return self.nombre

class TiposSuministro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)


class Suministros (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True,null= True, editable=True)
    tipoSuministro =   models.ForeignKey('facturacion.TiposSuministro', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    nombreGenerico  =  models.CharField(max_length=300, blank=True,null= True,  editable=True )
    descripcionComercial  =  models.CharField(max_length=250,blank=True,null= True,  editable=True )
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    grupo =  models.ForeignKey('clinico.Grupos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    subGrupo = models.ForeignKey('clinico.Grupos', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Subgrupo01i01')
    unidadMedida =  models.ForeignKey('rips.RipsUmm', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    principioActivo =  models.ForeignKey('clinico.PrincipiosActivos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    concentracion = models.ForeignKey('clinico.MedicamentosDci', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    formasFarmaceutica = models.ForeignKey('rips.RipsFormaFarmaceutica', blank=True,null= True, editable=True, on_delete=models.PROTECT )
    viaAdministracion = models.ForeignKey('clinico.ViasAdministracion', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    codigoAtc  =  models.ForeignKey('clinico.Atc', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    cantidadUvr =  models.CharField(max_length=10,blank=True, null=True, editable=True)
    cums =  models.CharField(max_length=50,blank=True,null= True,  editable=True )
    tipoHonorario = models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    ripsTipoMedicamento = models.ForeignKey('rips.RipsTipoMedicamento', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='RipsTipo01')
    ripsCums = models.ForeignKey('rips.RipsCums', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='RipsCums01')
    ripsDci = models.ForeignKey('rips.RipsDci', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='RipsDci01')
    ripsUnidadMedica = models.ForeignKey('rips.RipsUmm', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='RipsUnidad01')
    ripsFormaFarmaceutica = models.ForeignKey('rips.RipsFormaFarmaceutica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='RipsFfm01')
    ripsUnidadDispensa = models.ForeignKey('rips.RipsUnidadUpr', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='RipsDispensa01')
    registroSanitario = models.CharField(max_length=50, blank=True,null= True, editable=True)
    fechaExpedicion = models.DateTimeField(editable=True, null=True, blank=True)
    fechaVencimiento =  models.DateTimeField(editable=True, null=True, blank=True)
    fraccion =  models.DecimalField( max_digits=20, decimal_places=2, blank=True,null= True)
    unidadFraccion =    models.CharField(max_length=20, blank=True,null= True, editable=True)
    vence =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    control =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    antibiotico =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    pos	 =   models.CharField(max_length=1, blank=True,null= True, editable=True)
    facturable   = models.CharField(max_length=1, blank=True,null= True, editable=True)
    stockMinimo = models.DecimalField( max_digits=20, decimal_places=2, blank=True,null= True)
    stockMaximo = models.DecimalField( max_digits=20, decimal_places=2, blank=True,null= True)
    maxOrdenar = models.DecimalField( max_digits=20, decimal_places=2, blank=True,null= True)
    estabilidad	 = models.DecimalField( max_digits=20, decimal_places=0, blank=True,null= True)
    invFarmacia = models.CharField(max_length=1, blank=True,null= True, editable=True)
    invAlmacen = models.CharField(max_length=1, blank=True,null= True, editable=True)
    enfermeria = models.CharField(max_length=1, blank=True,null= True, editable=True)
    terapia = models.CharField(max_length=1, blank=True,null= True, editable=True)
    nutricion = models.CharField(max_length=1, blank=True,null= True, editable=True)
    cantidad	 = models.DecimalField( max_digits=20, decimal_places=2, blank=True,null= True)
    regSanitario = models.CharField(max_length=30, blank=True,null= True, editable=True)
    altoCosto = models.CharField(max_length=1, blank=True,null= True, editable=True)
    vrCompra = models.DecimalField( max_digits=20, decimal_places=2 , blank=True,null= True)
    vrUltimaCompra = models.DecimalField( max_digits=20, decimal_places=2 , blank=True,null= True)
    codigoAtc	= models.CharField(max_length=10, blank=True,null= True, editable=True)
    infusion  = models.CharField(max_length=1, blank=True,null= True, editable=True)
    tipoAdministracion = models.CharField(max_length=20, blank=True,null= True, editable=True)
    regulado = models.CharField(max_length=1, blank=True,null= True, editable=True)
    vaorRegulado = models.DecimalField( max_digits=20, decimal_places=2 , blank=True,null= True)
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
        return '%s %s' % (self.nombre , self.cums)
        #return str(self.nombre)


class ConveniosPaciente(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='DocumentoHistoria')
    convenio = models.ForeignKey('contratacion.Convenios', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.documento)

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


class SalariosLegales(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)

class SalariosMinimosLegales(models.Model):
    id = models.AutoField(primary_key=True)
    año =  models.CharField(max_length=5, blank=True, null=True, editable=True )
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    valor  =  models.DecimalField( max_digits=15, decimal_places=2, editable=True, null=True, blank=True)
    valorSubsidio =  models.DecimalField( max_digits=15, decimal_places=2 , editable=True, null=True, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)



class RegimenesTipoPago(models.Model):
    id = models.AutoField(primary_key=True)
    regimen =  models.ForeignKey('clinico.Regimenes', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    salarioLegal =  models.ForeignKey('facturacion.SalariosLegales', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    año =  models.IntegerField(editable=True, null=True, blank=True)
    valorModeradora = models.DecimalField( max_digits=20, decimal_places=2)
    valorCopago = models.DecimalField( max_digits=20, decimal_places=2)
    valorTopeMaximoCopagoEvento= models.DecimalField( max_digits=20, decimal_places=2)
    valorTopeMaximoCopagoCalendario=models.DecimalField( max_digits=20, decimal_places=2)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.regimen)



class ConceptosAfacturar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)




class LiquidacionCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    tipo =  models.CharField(max_length=50, default='A', editable=False )
    tipoTarifa =  models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    cirujanoPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    anestesiologoPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    ayudantePorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    derechosSalaPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    materialesPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.codigoHomologado)


class Facturacion(models.Model):
    id  = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TiposDoc101')
    #documento = models.CharField(max_length=30, blank=True,null= True, editable=True,)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoFac2')
    consecAdmision = models.IntegerField(editable=True, null=True, blank=True)
    factura = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    fechaFactura =  models.DateTimeField(editable=True, null=True, blank=True)
    codigoDian =  models.CharField(max_length=30, blank=True,null= True, editable=True,)
    convenio =   models.ForeignKey('contratacion.Convenios', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Conv08')
    totalCopagos =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalCuotaModeradora = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalAbonos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalProcedimientos =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalSuministros = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalFactura = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorApagar =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorAPagarLetras =  models.CharField(max_length=120, blank=True,null= True, editable=True,)
    anulado =  models.CharField(max_length=1, blank=True,null= True, editable=True,)
    fechaCorte =   models.DateTimeField(editable=True, null=True, blank=True)
    cufeDefinitivo =  models.CharField(max_length=100, blank=True,null= True, editable=True,)
    cufeValor =   models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    codigoQr = models.CharField(max_length=100, blank=True,null= True, editable=True,)
    rutaQr =  models.CharField(max_length=100, blank=True,null= True, editable=True,)
    rutaXml = models.CharField(max_length=100, blank=True,null= True, editable=True,)
    rutaAd =  models.CharField(max_length=1000, blank=True,null= True, editable=True,)
    rutaXmlFirmado =  models.CharField(max_length=1000, blank=True,null= True, editable=True,)
    mensajeDian =  models.CharField(max_length=1000, blank=True,null= True, editable=True,)
    rutaXmlRta =  models.CharField(max_length=1000, blank=True,null= True, editable=True,)
    nombreArchivo =  models.CharField(max_length=1000, blank=True,null= True, editable=True,)
    estado =   models.CharField(max_length=100, blank=True,null= True, editable=True,)
    fechaEnvioDian =  models.DateTimeField(editable=True, null=True, blank=True)
    reprocesarDian =models.CharField(max_length=1, blank=True,null= True, editable=True,)
    estadoEnvioDyan =models.CharField(max_length=1, blank=True,null= True, editable=True,)
    tipoFacturaDyan = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    rutaPdf = models.CharField(max_length=100, blank=True,null= True, editable=True,)
    envioCorreo = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    desbloqueada =  models.CharField(max_length=1, blank=True,null= True, editable=True,)
    verLiquidacion = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    anticipos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    numeroglosa = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    motivoGlosa = models.ForeignKey('cartera.MotivosGlosas', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Glosa01')
    totalCantidadGlosada = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalValorGlosado = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalCantidadAceptada =models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalValorAceptado =models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalCantidadSoportado =models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalValorSoportado =models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalNotasCredito =models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalNotasDebito = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioAnula = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='Plantas100')
    detalleAnulacion = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    fechaAnulacion =  models.DateTimeField(editable=True, null=True, blank=True)
    observaciones = models.CharField(max_length=100, blank=True,null= True, editable=True,)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Plantas101')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )


    def __str__(self):
        return str(self.documento)

class FacturacionDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    facturacion = models.ForeignKey('facturacion.facturacion', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Fact01')
    consecutivoFactura =  models.IntegerField(editable=True, null=True, blank=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    #tarifa =
    codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TablaCups121')
    cums = models.ForeignKey('rips.RipsCums', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Cums101')
    cantidad =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorUnitario =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorTotal =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    cirugia = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    #tipoHonorario =
    #grupoQx = 
    #grupoQxUvr =
    fechaCrea = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta105') 
    fechaModifica = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioModifica = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta106') 
    observaciones = models.CharField(max_length=200, blank=True,null= True, editable=True,)
    numeroglosa = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    motivoGlosa = models.ForeignKey('cartera.MotivosGlosas', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Motiv03')
    cantidadGlosada = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorGlosado =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    cantidadAceptada = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorAceptado = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    cantidadSoportado = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorSoportado = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    fechaNotaCredito = models.DateTimeField(editable=True, null=True, blank=True)
    numeroNotaCredito = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    valorNotaCredito = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    observacionNotaCredito = models.CharField(max_length=200, blank=True,null= True, editable=True,)
    fechaOtraNotaCredito = models.DateTimeField(editable=True, null=True, blank=True)
    numeroOtraNotaCredito = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    valorOtraNotaCredito = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    observacionOtraNotaCredito = models.CharField(max_length=200, blank=True,null= True, editable=True,)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='Planta107') 
    estadoRegistro = models.CharField(max_length=1, blank=True,null= True, editable=True,)


    def __str__(self):
        return str(self.codigoHomologado)

class Liquidacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TiposDoc120')
    #documento = models.CharField(max_length=30, blank=True,null= True, editable=True,)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoFac3')
    consecAdmision = models.IntegerField(editable=True, null=True, blank=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    convenio = models.ForeignKey('contratacion.Convenios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Convenio102')
    totalCopagos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalCuotaModeradora = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalAbonos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalProcedimientos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalSuministros = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    totalLiquidacion = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorApagar = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    anulado = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    fechaCorte = models.DateTimeField(editable=True, null=True, blank=True)
    anticipos = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioAnula =  models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta108') 
    detalleAnulacion =  models.CharField(max_length=120, blank=True,null= True, editable=True,)
    fechaAnulacion = models.DateTimeField(editable=True, null=True, blank=True)
    observaciones  = models.CharField(max_length=120, blank=True,null= True, editable=True,)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta109') 
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoRegistro = models.CharField(max_length=1, blank=True,null= True, editable=True,)


    def __str__(self):
        return str(self.id)


class LiquidacionDetalle(models.Model):

    M = 'MANUAL'
    S = 'SISTEMA'
    TIPO_REGISTRO = (
        ('M', 'MANUAL'),
        ('S', 'SISTEMA'),
    )
    id = models.AutoField(primary_key=True)
    liquidacion = models.ForeignKey('facturacion.Liquidacion', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Liquid01')
    consecutivo = models.IntegerField(editable=True, null=True, blank=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TablaCups101')
    cums = models.ForeignKey('rips.RipsCums', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TablaCums101')
    cantidad =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorUnitario =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorTotal = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    cirugia = models.CharField(max_length=1, blank=True,null= True, editable=True,)
    fechaCrea = models.DateTimeField(editable=True, null=True, blank=True)
    tipoRegistro = models.CharField(max_length=20,  blank=True, null=True, editable=True, choices = TIPO_REGISTRO)
    tipoHonorario =  models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoHonorario091')
    #usuarioCrea = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta120') 
    fechaModifica = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioModifica = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planat121') 
    observaciones =  models.CharField(max_length=120, blank=True,null= True, editable=True,)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta122') 
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoRegistro = models.CharField(max_length=1, blank=True,null= True, editable=True,)

    def __str__(self):
        return str(self.id)


class Refacturacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TiposDoc145')
    #documento = models.CharField(max_length=30, blank=True,null= True, editable=True,)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoFac4')
    consecAdmision = models.IntegerField(editable=True, null=True, blank=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    facturaInicial = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    facturaFinal  = models.CharField(max_length=20, blank=True,null= True, editable=True,)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Planta123') 
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoRegistro = models.CharField(max_length=1, blank=True,null= True, editable=True,)


    def __str__(self):
        return str(self.id)


