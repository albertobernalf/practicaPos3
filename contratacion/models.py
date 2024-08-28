from django.db import models
from django.utils.timezone import now

# Create your models here.


class Procedimientos(models.Model):
    Si = 'S'
    No = 'N'
    TIPO_CHOICES = (
        (Si, 'Si'),
        (No, 'No'),
    )
    id = models.AutoField(primary_key=True)
    tiposExamen = models.ForeignKey('clinico.TiposExamen',on_delete=models.PROTECT, null= False)
    cups = models.CharField(max_length=20, null=False, default=0)
    nombre = models.CharField(max_length=80)
    solicitaEnfermeria = models.CharField(max_length=1 ,choices=TIPO_CHOICES,)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
            return self.nombre


class Convenios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True,null= True, editable=True)
    empresa =  models.ForeignKey('facturacion.Empresas', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    tipoTarifa  =  models.ForeignKey('facturacion.TiposTarifa', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    vigenciaDesde = models.DateTimeField()
    vigenciaHasta = models.DateTimeField()
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
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.id)
