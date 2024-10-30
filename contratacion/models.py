from django.db import models
from django.utils.timezone import now
from smart_selects.db_fields import GroupedForeignKey

from tarifas.models import Tarifas


# Create your models here.



class ConveniosProcedimientos(models.Model):
    Si = 'S'
    No = 'N'
    TIPO_CHOICES = (
        (Si, 'Si'),
        (No, 'No'),
    )
    id = models.AutoField(primary_key=True)
    convenio = models.ForeignKey('contratacion.Convenios', blank=True,null= True, editable=True, on_delete=models.PROTECT)        
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)    
    codigoHomologado = models.CharField(max_length=10, blank=True, null=True, editable=True)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Concepto21')
    cups = models.ForeignKey('clinico.Examenes',   blank=True,null= True, editable=True,  on_delete=models.PROTECT,  related_name='Cups206')
    valor = models.DecimalField( max_digits=15, decimal_places=2, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    class Meta:
        unique_together = (('tipoTarifa', 'cups'),)


    def __str__(self):
            return self.nombre


class Convenios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True,null= True, editable=True)
    descripcion = models.CharField(max_length=80, blank=True,null= True, editable=True)
    empresa =  models.ForeignKey('facturacion.Empresas', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    vigenciaDesde = models.DateTimeField()
    vigenciaHasta = models.DateTimeField()
    #tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)    
    porcTarifario = models.DecimalField( max_digits=5, decimal_places=2, blank=True,null= True, editable=True)
    porcSuministros = models.DecimalField( max_digits=5, decimal_places=2, blank=True,null= True, editable=True)
    valorOxigeno = models.DecimalField( max_digits=8, decimal_places=2, blank=True,null= True, editable=True)
    porcEsterilizacion = models.DecimalField( max_digits=5, decimal_places=2,blank=True,null= True, editable=True)
    porcMaterial  = models.DecimalField( max_digits=5, decimal_places=2,blank=True,null= True, editable=True)
    hospitalario = models.CharField(max_length=1, blank=True,null= True, editable=True)
    urgencias = models.CharField(max_length=1, blank=True,null= True, editable=True)
    ambulatorio = models.CharField(max_length=1, blank=True,null= True, editable=True)
    consultaExterna = models.CharField(max_length=1, blank=True,null= True, editable=True)
    copago = models.CharField(max_length=1, blank=True,null= True, editable=True)
    moderadora = models.CharField(max_length=1, blank=True,null= True, editable=True)
    tipofactura  = models.CharField(max_length=1, blank=True,null= True, editable=True)
    agrupada = models.CharField(max_length=1, blank=True,null= True, editable=True)
    facturacionSuministros = models.CharField(max_length=1, blank=True,null= True, editable=True)
    facturacionCups  = models.CharField(max_length=1, blank=True,null= True, editable=True)
    cuentaContable= models.CharField(max_length=20, blank=True,null= True, editable=True)
    requisitos = models.CharField(max_length=2000, blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.nombre)


class ConveniosTarifasHonorarios (models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.ForeignKey('contratacion.Convenios', blank=True,null= True, editable=True, on_delete=models.PROTECT)        
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)    
    tipoHonorario =  models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoHonorario05')
    codigoHomologado = models.CharField(max_length=10, blank=True, null=True, editable=True)
    cups = models.ForeignKey('clinico.Examenes',  blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Cups215')
    valor = models.DecimalField( max_digits=15, decimal_places=2, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    class Meta:
        unique_together = (('convenio','tipoTarifa', 'tipoHonorario'),)


    def __str__(self):
            return self.convenio


class ConveniosSuministros(models.Model):
    Si = 'S'
    No = 'N'
    TIPO_CHOICES = (
        (Si, 'Si'),
        (No, 'No'),
    )
    id = models.AutoField(primary_key=True)
    convenio = models.ForeignKey('contratacion.Convenios', blank=True,null= True, editable=True, on_delete=models.PROTECT)        
    tipoTarifa = models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)    
    codigoHomologado = models.CharField(max_length=10, blank=True, null=True, editable=True)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Concepto221')
    suministro = models.ForeignKey('facturacion.Suministros',on_delete=models.PROTECT, null= False)
    valor = models.DecimalField( max_digits=15, decimal_places=2, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    class Meta:
        unique_together = (('convenio','tipoTarifa', 'suministro'),)


    def __str__(self):
            return self.convenio



class ConveniosLiquidacionTarifasHonorarios(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTarifa =  models.ForeignKey('tarifas.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoTarifa037')
    codigoHomologado = models.CharField(max_length=10, blank=True,null= True , editable=True )
    tipoHonorario =  models.ForeignKey('tarifas.TiposHonorarios', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name='TipoHonorario017')
    descripcion =  models.CharField(max_length=300, blank=True,null= True , editable=True )
    codigoSuministro =  models.ForeignKey('facturacion.Suministros', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Suminis1277')
    codigoCups = models.ForeignKey('clinico.Examenes', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Cups1177')
    valor =  models.DecimalField( max_digits=15, decimal_places=2 , blank=True,null= True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='plantas2177')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )


    def __str__(self):
            return self.descripcion

