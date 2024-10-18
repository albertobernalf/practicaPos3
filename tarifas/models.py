from django.db import models

# Create your models here.


class TiposTarifa (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)


class OxigenoIss (models.Model):
    id = models.AutoField(primary_key=True)
    codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Cups112')
    descripcion = models.CharField(max_length=30, blank=True, null=True, editable=True)
    metroHoraFraccion = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='plantas210')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )


    def __str__(self):
        return str(self.nombre)



class Tarifas (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TipoTarifa01')
    codigoHomologado = models.CharField(max_length=10, blank=True, null=True, editable=True)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Concepto01')
    codigoSuministro =  models.ForeignKey('facturacion.Suministros', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Suminis123')
    codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Cups101')
    cantidadUvr = models.DecimalField( max_digits=10, decimal_places=4,blank=True,null= True, editable=True,) 	
    uvrAño = models.ForeignKey('tarifas.Uvr', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Uvr101')
    valorIss = models.DecimalField( max_digits=20, decimal_places=4,blank=True,null= True, editable=True,)
    grupoQx = models.ForeignKey('tarifas.GruposQx', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Grupo01')
    valorSoat = models.DecimalField( max_digits=20, decimal_places=4,blank=True,null= True, editable=True,)
    valorPropio =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    paquete = models.CharField(max_length=1, blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='plantas200')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):

        return str(self.nombre)

class TarifasSuministros (models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TipoTarifa02')
    suministro =  models.ForeignKey('facturacion.Suministros', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Suministro101')
    codigoHomologado = models.CharField(max_length=20, blank=True, null=True, editable=True)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='Concepto02')
    valor = models.DecimalField( max_digits=20, decimal_places=2)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='platas201')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.suministro)




class GruposQx(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    #codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Cups101')
    #salariosMinimosLegales =  models.ForeignKey('facturacion.SalariosMinimosLegales', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='MinLeg02')
    #salMinLeg = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)

class TiposHonorarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)


class LiquidacionHonorarios(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa =  models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoTarifa03')
    codigoHomologado = models.CharField(max_length=10, blank=True,null= True , editable=True )
    tipoHonorario =  models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoHonorario01')
    descripcion =  models.CharField(max_length=100, blank=True,null= True , editable=True )
    codigoSuministro =  models.ForeignKey('facturacion.Suministros', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Suminis127')
    grupoQx =  models.ForeignKey('tarifas.GruposQx', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='GrupoQx01')
    salMinLeg = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    salariosMinimosLegales =  models.ForeignKey('facturacion.SalariosMinimosLegales', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='MinLeg01')
    #minUvr =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    #maxUvr =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    cantidadUvr = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    uvrAño = models.ForeignKey('tarifas.Uvr', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Uvr103')  
    valorIss =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorSoat =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valorPropio =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas217')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.codigoHomologado)




class HonorariosIss(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True, editable=True)
    tipoHonorario =  models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoHonorario122')
    minUvr =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    maxUvr =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valor =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas223')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.descripcion)


class Uvr(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa =  models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoTarifa05')
    año =  models.IntegerField(default=0)
    valor = models.DecimalField( max_digits=15, decimal_places=4 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas204')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )


    def __str__(self):
        return str(self.año)


class TiposSalas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)


class LiquidacionDerechos(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoTarifa08')
    codigoHomologado = models.CharField(max_length=10, blank=True,null= True , editable=True )
    tipoSala = models.ForeignKey('tarifas.TiposSalas', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoSala03')
    grupoQx =  models.ForeignKey('tarifas.GruposQx', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='GrupoQx12')
    salMinLeg = models.DecimalField( max_digits=15, decimal_places=2)
    salariosMinimosLegales =  models.ForeignKey('facturacion.SalariosMinimosLegales', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='SalMinLeg12')
    valor = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.codigoHomologado)


class LiquidacionDerechosIss(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TipoTarifa07')
    suministro = models.ForeignKey('facturacion.Suministros', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoSuminiistro112')
    codigoHomologado = models.CharField(max_length=10, blank=True,null= True , editable=True )
    tipoSala = models.ForeignKey('tarifas.TiposSalas', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='TipoSala01')
    desdeUvr = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    hastaUvr = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    valor = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.codigoHomologado)


class LiquidacionCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    tipo =  models.CharField(max_length=50, default='A', editable=False )
    tipoTarifa =  models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoTarifa06')
    cirujanoPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    anestesiologoPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    ayudantePorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    derechosSalaPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    materialesPorcentage      = models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas206')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.codigoHomologado)

class FormasLiquidacion(models.Model):
    id = models.AutoField(primary_key=True)
    #nombre =
    #Codigo =
    #tipoCruento =
    #caracteristica =
    #valorHonorario =
    #tiposHonorarios =
    #cuentaContable =
    #centroCosto=
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas205')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )


    def __str__(self):
        return str(self.id)


class ConceptosAfacturar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT , related_name='plantas207')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)

