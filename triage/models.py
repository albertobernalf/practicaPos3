from django.db import models

# Create your models here.


class Triage(models.Model):

    A = 'A'
    I = 'I'

    TIPO_CHOICES = (
        (A, 'ACTIVO'),
        (I, 'INACTIVO')
    )
    id = models.AutoField(primary_key=True)
    sedesClinica   = models.ForeignKey('sitios.SedesClinica', blank=True,null= True, editable=True, on_delete=models.PROTECT, related_name = 'SedesClinica1')
    serviciosSedes = models.ForeignKey('sitios.ServiciosSedes', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='Serv21')
    subServiciosSedes = models.ForeignKey('sitios.SubServiciosSedes', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='SubServ21')
    dependencias = models.ForeignKey('sitios.Dependencias', blank=True, null=True, editable=True,   on_delete=models.PROTECT, related_name='depCli01')
    fechaSolicita = models.DateTimeField( editable=True, null=True, blank=True)
    fechaAtendio = models.DateTimeField( editable=True, null=True, blank=True)
    tipoDoc        = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    documento      = models.ForeignKey('usuarios.Usuarios',blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='Documento1')
    consec         = models.IntegerField()
    consecAdmision = models.IntegerField(default=0)
    hClinica       = models.CharField(max_length=50,  blank=True, null=True, editable=True,)
    regimen        = models.ForeignKey('clinico.Regimenes', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    tiposCotizante  = models.ForeignKey('clinico.TiposCotizante', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    enfermedaActual= models.ForeignKey('clinico.Enfermedades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    motivo         = models.CharField(max_length=1000,  blank=True, null=True, editable=True,)
    examenFisico   = models.CharField(max_length=5000,  blank=True, null=True, editable=True,)
    frecCardiaca   = models.CharField(max_length=10,  blank=True, null=True,)
    frecRespiratoria = models.CharField(max_length=10,  blank=True, null=True,)
    taSist          = models.CharField(max_length=10,  blank=True, null=True,)
    taDiast         = models.CharField(max_length=10,  blank=True, null=True,)
    taMedia         = models.CharField(max_length=10,  blank=True, null=True,)
    glasgow         = models.CharField(max_length=10,  blank=True, null=True,)
    peso            = models.CharField(max_length=10,  blank=True, null=True,)
    temperatura     = models.CharField(max_length=10,  blank=True, null=True,)
    estatura        = models.CharField(max_length=10,  blank=True, null=True,)
    clasificacionTriage = models.ForeignKey('clinico.TiposTriage', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    viaEgreso  = models.ForeignKey('clinico.ViasEgreso', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    glucometria = models.CharField(max_length=50,  blank=True, null=True,)
    saturacion  = models.CharField(max_length=50,  blank=True, null=True,)
    escalaDolor = models.CharField(max_length=50,  blank=True, null=True,)
    causaExterna = models.ForeignKey('clinico.CausasExterna', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    vistobno    = models.CharField(max_length=50,  blank=True, null=True,)
    tipoTrauma  = models.CharField(max_length=50,  blank=True, null=True,)
    cinematicaTrauma = models.CharField(max_length=50,  blank=True, null=True,)
    tipoIngreso = models.CharField(max_length=50,  blank=True, null=True,)
    usuarioAutoriza = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    fechaModanexo = models.DateTimeField(editable=True, null=True, blank=True)
    observaciones = models.CharField(max_length=200, default='', editable=True)
    alergiasTriage = models.CharField(max_length=50, default='', editable=True)
    fechaRegistro  = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioCrea = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='Documento3')
    usuarioAtiende = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='Documento2')
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)


    class Meta:
        unique_together = (('tipoDoc', 'documento'),)

    def __str__(self):
            return self.nombre

