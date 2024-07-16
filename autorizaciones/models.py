from django.db import models

from django.utils.timezone import now

# Create your models here.

class Autorizaciones(models.Model):

    id           = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica13')
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento7')
    hClinica = models.CharField(max_length=20,blank=True,null= True, editable=True,)
    consec    = models.IntegerField()
    fechaSolicitud = models.DateTimeField( editable=True, null=True, blank=True)
    empresa = models.ForeignKey('facturacion.Empresas',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento77')
    prioritario = models.CharField(max_length=1,blank=True,null= True, editable=True,)
    justificacion =  models.CharField(max_length=5000,blank=True,null= True, editable=True,)
    plantaSolicita = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT)
    numeroAutorizacion=  models.CharField(max_length=5000,blank=True,null= True, editable=True,)
    fechaAutorizacion = models.DateTimeField( editable=True, null=True, blank=True)
    plantaAutoriza = models.ForeignKey('planta.Planta',blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name ='Planta1')
    observaciones =  models.CharField(max_length=1000,blank=True,null= True, editable=True,)
    estadoAutorizacion =  models.CharField(max_length=1,blank=True,null= True, editable=True,)
    fechaModifica = models.DateTimeField( editable=True, null=True, blank=True)
    numeroSoclicitud = models.DecimalField(max_digits=6, decimal_places=2)
    fechaVigencia = models.DateTimeField( editable=True, null=True, blank=True)
    medicoAutoriza = models.ForeignKey('clinico.Medicos',blank=True,null= True, editable=True, on_delete=models.PROTECT)
    dxPrinc = models.ForeignKey('clinico.Diagnosticos',blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx21' )
    dxRel1      = models.ForeignKey('clinico.Diagnosticos',blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx22' )
    dxRel2      = models.ForeignKey('clinico.Diagnosticos',blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='dx23' )
    fechaRegistro = models.DateTimeField(default=now, blank=True,null= True, editable=True, )
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True,null=True, editable=True, on_delete=models.PROTECT, related_name ='Planta2')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre

class AutorizacionesCups(models.Model):

    id           = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica14')
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento8')
    hClinica = models.CharField(max_length=20,blank=True,null= True, editable=True,)
    consec    = models.IntegerField()
    autorizacionesId = models.ForeignKey('autorizaciones.Autorizaciones',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento88')
    codigoCups =  models.ForeignKey('facturacion.Cups',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento888')
    autorizado = models.CharField(max_length=1,blank=True,null= True, editable=True,)
    cantidadSolicitada = models.DecimalField(max_digits=6, decimal_places=2)
    cantidadAutorizada =  models.DecimalField(max_digits=6, decimal_places=2)
    fechaRegistro = models.DateTimeField(default=now, blank=True,null= True, editable=True, )
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=False,null= False, editable=True, on_delete=models.PROTECT, related_name ='Planta3')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __integer__(self):
        return self.nombre


class AutorizacionesCirugias(models.Model):

    id           = models.AutoField(primary_key=True)
    sedesClinica = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica5')
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento9')
    hClinica = models.CharField(max_length=20,blank=True,null= True, editable=True,)
    consec    = models.IntegerField()
    autorizacionesId = models.ForeignKey('autorizaciones.Autorizaciones',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento99')
    fechaRegistro = models.DateTimeField(default=now, blank=True,null= True, editable=True, )
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name ='usuarioRegistroPlanta2')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre