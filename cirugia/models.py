from django.db import models

# Create your models here.

class Cirugias(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='DocumentoHistoria54')
    consecAdmision = models.IntegerField(default=0)
    folio = models.IntegerField(default=0)
    sedesClinica_id = models.ForeignKey('sitios.Sedesclinica', blank=True, null=True, editable=True,     on_delete=models.PROTECT)
    serviciosSedes_id = models.ForeignKey('sitios.Serviciossedes', blank=True, null=True, editable=True,      on_delete=models.PROTECT)
    subServiciosSedes_id = models.ForeignKey('sitios.Subserviciossedes', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    numero = models.CharField(max_length=50, blank=True, null=True, editable=True)
    especialidad = models.ForeignKey('clinico.Especialidades', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    urgente = models.CharField(max_length=1, blank=True, null=True, editable=True)
    tipoQx = models.CharField(max_length=20, blank=True, null=True, editable=True)
    anestesia = models.ForeignKey('cirugia.TiposAnestesia', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    autorizacion = models.CharField(max_length=30, blank=True, null=True, editable=True)
    usuarioSolicita = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Usuario40')
    fechaSolicia = models.DateTimeField()
    solicitaHospitalizacion = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaAyudante = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaTiempoQx = models.DecimalField(max_digits=5, decimal_places=0)
    solicitatipoQx = models.CharField(max_length=20, blank=True, null=True, editable=True)
    solicitaAnestesia = models.CharField(max_length=20, blank=True, null=True, editable=True)
    solicitaSangree = models.CharField(max_length=1, blank=True, null=True, editable=True)
    describeSangre = models.CharField(max_length=2000, blank=True, null=True, editable=True)
    cantidadSangre = models.DecimalField(max_digits=5, decimal_places=0)
    solicitaCamaUci = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaMicroscopio = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaRx = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaAutoSutura = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaOsteosintesis = models.CharField(max_length=2000, blank=True, null=True, editable=True)
    soliictaSoporte = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaBiopsia = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaMalla = models.CharField(max_length=1, blank=True, null=True, editable=True)
    solicitaOtros = models.CharField(max_length=1, blank=True, null=True, editable=True)
    describeOtros = models.CharField(max_length=2000, blank=True, null=True, editable=True)
    fechaProg = models.DateField()
    HoraProg = models.CharField(max_length=5, blank=True, null=True, editable=True)
    tiempoQxProg = models.DecimalField(max_digits=5, decimal_places=0)
    fechaQx = models.DateField()
    horaQx = models.CharField(max_length=5, blank=True, null=True, editable=True)
    tiempoQx = models.DecimalField(max_digits=5, decimal_places=0)
    fechaIniAnestesia = models.DateField()
    HoraIniAnestesia = models.CharField(max_length=5, blank=True, null=True, editable=True)
    fechaFinAnestesia = models.DateField()
    horaFinAnestesia = models.CharField(max_length=5, blank=True, null=True, editable=True)
    intervencion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    cups1 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups60')
    finalidad1 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups2 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups61')
    finalidad2 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups3 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups62')
    finalidad3 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups4 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups63')
    finalidad4 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups5 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups64')
    finalidad5 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups6 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups65')
    finalidad6 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups7 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups66')
    finalidad7 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups8 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups67')
    finalidad8 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups9 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups68')
    finalidad9 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups10 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups69')
    finalidad10 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups11 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups70')
    finalidad11 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups12 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups71')
    finalidad12 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups13 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups72')
    finalidad13 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups14 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups73')
    finalidad14 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cups15 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Cups74')
    finalidad15 = models.CharField(max_length=1, blank=True, null=True, editable=True)
    riesgos = models.CharField(max_length=3000, blank=True, null=True, editable=True)
    observaciones = models.CharField(max_length=5000, blank=True, null=True, editable=True)
    dxPreQx = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Dx51')
    dxPostQx = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT ,    related_name='Dx52')
    dxPrinc = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT ,    related_name='Dx53')
    dxRel1 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Dx54')
    dxRel2 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Dx55')
    dxRel3 = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Dx56')
    descripcionQx = models.CharField(max_length=10000, blank=True, null=True, editable=True)
    dxComplicacion = models.CharField(max_length=4, blank=True, null=True, editable=True)
    complicaciones = models.CharField(max_length=3000, blank=True, null=True, editable=True)
    patologia = models.CharField(max_length=500, blank=True, null=True, editable=True)
    formaRealiza = models.CharField(max_length=15, blank=True, null=True, editable=True)
    cirujano1 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta30')
    cirujano2 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta31')
    cirujano3 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta32')
    anestesiologo = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta33')
    ayudante1 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta34')
    ayudante2 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta35')
    circulante = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta36')
    instrumentador = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta37')
    estadoCirugia = models.ForeignKey('cirugia.EstadosCirugias', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    estadoSalida = models.CharField(max_length=1, default='A', editable=False)
    vboAdmon = models.CharField(max_length=1, blank=True, null=True, editable=True)
    hallazgos = models.CharField(max_length=5000, blank=True, null=True, editable=True)
    osteosintesis = models.CharField(max_length=300, blank=True, null=True, editable=True)
    auxiliar = models.CharField(max_length=200, blank=True, null=True, editable=True)
    materialEspecial = models.CharField(max_length=300, blank=True, null=True, editable=True)
    reprogramada = models.CharField(max_length=1, blank=True, null=True, editable=True)
    motivoReprogramada = models.CharField(max_length=500, blank=True, null=True, editable=True)
    tipoCancela = models.CharField(max_length=15, blank=True, null=True, editable=True)
    motivoCancela = models.CharField(max_length=500, blank=True, null=True, editable=True)
    timepoMaxQx = models.CharField(max_length=10, blank=True, null=True, editable=True)
    observacionesProgramacion = models.CharField(max_length=500, blank=True, null=True, editable=True)
    usuarioPrograma = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='Usuario41')
    fechaPrograma = models.DateTimeField()
    usuarioCancela = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT ,    related_name='Usuario42')
    fechaCancela = models.DateTimeField()
    usuarioReprograma = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,   on_delete=models.PROTECT,    related_name='Usuario43')
    fechaReprograma = models.DateTimeField()
    intensificador = models.CharField(max_length=1, blank=True, null=True, editable=True)
    tipofractura = models.CharField(max_length=30, blank=True, null=True, editable=True)
    recomendacionenfermeria = models.CharField(max_length=2000, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT,    related_name='planta39')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)



class EstadosCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class TiposAnestesia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class CirugiasMaterialQx(models.Model):
    id = models.AutoField(primary_key=True)
    cirugia = models.ForeignKey('cirugia.Cirugias', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    suministro = models.ForeignKey('facturacion.Suministros', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class RecordAnestesico(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True,
                                on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True,   on_delete=models.PROTECT, related_name='DocumentoHistoria122')
    consecAdmision = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class ProgramacionCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    sedesClinica_id = models.ForeignKey('sitios.Sedesclinica', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    serviciosSedes_id = models.ForeignKey('sitios.Serviciossedes', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    subServiciosSedes_id = models.ForeignKey('sitios.Subserviciossedes', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    numero = models.CharField(max_length=50, blank=True, null=True, editable=True)
    estadoSala = models.CharField(max_length=50, blank=False, null=False, default='L', editable=True)
    fecha_programacion = models.DateTimeField()
    hora_programacion = models.CharField(max_length=5, blank=True, null=True, editable=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='DocumentoHistoria123')
    consecAdmision = models.IntegerField(default=0)
    cups1 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,   on_delete=models.PROTECT, related_name='Cups80')
    cups2 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='Cups81')
    cups3 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,       on_delete=models.PROTECT, related_name='Cups82')
    cups4 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,   on_delete=models.PROTECT, related_name='Cups83')
    cups5 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,             on_delete=models.PROTECT, related_name='Cups84')
    cups6 = models.ForeignKey('clinico.TiposExamen', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='Cups85')
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __str__(self):
        return str(self.id)


class OrganosCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)


class IntervencionCirugias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class TiposHeridasOperatorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class FinalidadCirugia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class PlanificacionCirugia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class ZonasCirugia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)


class GravedadCirugia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)
