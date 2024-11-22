from django.db import models
from django.utils.timezone import now

# Create your models here.


class FormasPagos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)     

    def __integer__(self):
        return self.nombre



class TiposPagos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)     

    def __integer__(self):
        return self.nombre

class Pagos(models.Model):

    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento77')
    consec    = models.IntegerField()
    tipoPago = models.ForeignKey('cartera.TiposPagos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    formaPago = models.ForeignKey('cartera.FormasPagos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    valor = models.DecimalField( max_digits=20, decimal_places=2)
    descripcion = models.CharField(max_length=200, null=False)
    totalAplicado = models.DecimalField( max_digits=20, decimal_places=2 , blank=True, null=True, editable=True , default=0.0)
    valorEnCurso = models.DecimalField( max_digits=20, decimal_places=2 , blank=True, null=True, editable=True , default=0.0)
    saldo = models.DecimalField( max_digits=20, decimal_places=2, default=0.0)
    #facturaAplicada  =  models.ForeignKey('facturacion.facturacion',blank=True,null= True, editable=True, on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre

class PagosFacturas(models.Model):

    id = models.AutoField(primary_key=True)
    pago = models.ForeignKey('cartera.Pagos', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    facturaAplicada  =  models.ForeignKey('facturacion.facturacion',blank=True,null= True, editable=True, on_delete=models.PROTECT)
    valorAplicado = models.DecimalField( max_digits=20, decimal_places=2)
    fechaRegistro = models.DateTimeField(default=now, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre


class TiposGlosas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)     

    def __integer__(self):
        return self.nombre

class MotivosGlosas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, null=False)  
    nombre = models.CharField(max_length=50, null=False)     
    descripcion = models.CharField(max_length=600, null=True)     

    def __integer__(self):
        return self.nombre

class Radicaciones(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    remision= models.CharField(max_length=20, null=False)
    radicacion= models.CharField(max_length=20, null=False)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre


class Remisiones(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(editable=True, null=True, blank=True)
    remision= models.CharField(max_length=20, null=False)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre

class TiposNotas (models.Model):

   id = models.AutoField(primary_key=True)
   codigo = models.CharField(max_length=2, blank=True,null= True, editable=True)
   nombre =   models.CharField(max_length=80, blank=True,null= True, editable=True)

   def __str__(self):
        return self.nombre



class Glosas(models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.ForeignKey('contratacion.Convenios',blank=True,null= True, editable=True, on_delete=models.PROTECT)
    fechaGlosa = models.DateTimeField(editable=True, null=True, blank=True)
    numeroGlosa = models.CharField(max_length=20, blank=True,null= True, editable=True)
    detalladaParcial = models.CharField(max_length=1, blank=True,null= True, editable=True)
    detalladaTotal = models.CharField(max_length=1, blank=True,null= True, editable=True)
    totalGlosa =  models.DecimalField( max_digits=15, decimal_places=2)
    totalSoportado =  models.DecimalField( max_digits=15, decimal_places=2)
    totalAceptado =  models.DecimalField( max_digits=15, decimal_places=2)
    observacones = models.CharField(max_length=120, blank=True,null= True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __integer__(self):
        return self.nombre