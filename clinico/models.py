from django.db import models
from django.utils.timezone import now

# Create your models here.

class HistorialDiagnosticosCabezote(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios',  blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoHistoriaDiag')
    consecAdmision = models.IntegerField()
    folio = models.IntegerField()
    observaciones = models.CharField(max_length=200)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.observaciones


class TiposRadiologia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre



class Servicios(models.Model):
    id = models.AutoField(primary_key=True)
    #sedesClinica = models.ForeignKey('sitios.SedesClinica', default=1, on_delete=models.PROTECT, null=True)
    nombre = models.CharField(max_length=30, null = False)


    def __str__(self):
        return self.nombre

class EspecialidadesMedicos(models.Model):
    id = models.AutoField(primary_key=True)
    especialidades = models.ForeignKey('clinico.Especialidades', on_delete=models.PROTECT, null=False,related_name ='especialidadesMedicos1')
    planta = models.ForeignKey('planta.Planta', on_delete = models.PROTECT, null = False)
    nombre = models.CharField(max_length=30, default="" , null = False)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('planta.Planta',  blank=True, null=True, editable=True, on_delete=models.PROTECT,related_name ='usuarioRegistroPlanta')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __integer__(self):
        return self.nombre


class Especialidades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30 , null = False)
    interconsulta = models.CharField(max_length=1,  blank=True,null= True, editable=True,)
    cExterna    = models.CharField(max_length=1,  blank=True,null= True, editable=True,)
    quirurgica =  models.CharField(max_length=1,  blank=True,null= True, editable=True,)
    codigoCups = models.CharField(max_length=1,  blank=True,null= True, editable=True,)

    def __str__(self):
        return self.nombre


class Medicos(models.Model):
        id = models.AutoField(primary_key=True)
        planta = models.ForeignKey('planta.Planta',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
        tipoDoc = models.ForeignKey('usuarios.TiposDocumento',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
        documento = models.IntegerField(default=1)
        nombre = models.CharField(max_length=30)
        especialidades = models.ForeignKey('clinico.Especialidades',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
        registroMedico = models.CharField(max_length=50, default='')
        departamento = models.ForeignKey('sitios.Departamentos',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
        ciudad = models.ForeignKey('sitios.Ciudades',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
        direccion = models.CharField(max_length=50)
        telefono = models.CharField(max_length=20)
        contacto = models.CharField(max_length=50)
        centro = models.ForeignKey('sitios.Centros', blank=True, null=True, editable=True, on_delete=models.PROTECT)
        #firma = models.file()

        estado = models.CharField(max_length=1)

        def __str__(self):
            return self.nombre



class EstadoExamenes(models.Model):
      id = models.AutoField(primary_key=True)
      nombre = models.CharField(max_length=30, null=False)
      estadoReg = models.CharField(max_length=1, default='A', editable=False)

      def __str__(self):
          return self.nombre


class Enfermedades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre



class TiposExamen(models.Model):
            id = models.AutoField(primary_key=True)
            nombre = models.CharField(max_length=30, null=False)
            estadoReg = models.CharField(max_length=1, default='A', editable=False)

            def __str__(self):
                return self.nombre


class TiposFolio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class TiposAntecedente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre





class CausasExterna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre

class ViasIngreso(models.Model):
        id = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50, null=True)
        estadoReg = models.CharField(max_length=1, default='A', editable=False)

        def __str__(self):
            return self.nombre

class ViasEgreso(models.Model):
        id = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50, null=True)
        estadoReg = models.CharField(max_length=1, default='A', editable=False)

        def __str__(self):
            return self.nombre


class TiposIncapacidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre




class Examenes(models.Model):
    Si = 'S'
    No = 'N'
    TIPO_CHOICES = (
        (Si, 'Si'),
        (No, 'No'),
    )
    id = models.AutoField(primary_key=True)
    TiposExamen = models.ForeignKey('clinico.TiposExamen',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    codigoCups = models.CharField(max_length=20, null=False,  blank=True)
    nombre = models.CharField(max_length=300)
    edadIni = models.IntegerField(blank=True, null=True, editable=True)
    edadFin = models.IntegerField( blank=True, null=True, editable=True)
    solicitaEnfermeria = models.CharField(max_length=1, choices=TIPO_CHOICES,  null=False,  blank=True, )
    citaControl = models.CharField(max_length=1, blank=True, null=True, editable=True)
    concepto = models.ForeignKey('facturacion.Conceptos', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    codigoRips = models.CharField(max_length=6,  blank=True, null=True, editable=True)
    grupoQx =  models.ForeignKey('tarifas.GruposQx',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    cantidadUvr =  models.CharField(max_length=10,blank=True, null=True, editable=True)
    uvrAño = models.ForeignKey('tarifas.Uvr', blank=True,null= True, editable=True, on_delete=models.PROTECT , related_name='Uvr105')
    honorarios = models.CharField(max_length=1, blank=True, null=True, editable=True)
    autorizar = models.CharField(max_length=1,  blank=True, null=True, editable=True)
    tipoRadiologia = models.ForeignKey('clinico.TiposRadiologia',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    cupsGrupo = models.CharField(max_length=15,  blank=True, null=True, editable=True)
    cupsSubgrupo = models.CharField(max_length=15, blank=True, null=True, editable=True)
    cupsCategoria = models.CharField(max_length=15, blank=True, null=True, editable=True)
    cupsSubCategoria = models.CharField(max_length=15, blank=True, null=True, editable=True)
    resolucion1132 = models.CharField(max_length=15, blank=True, null=True, editable=True)
    nivelAtencion  =  models.CharField(max_length=15, blank=True, null=True, editable=True)
    centroCosto = models.CharField(max_length=15,  blank=True, null=True, editable=True)
    finalidad = models.CharField(max_length=1, blank=True, null=True, editable=True)
    duracion =   models.CharField(max_length=15, blank=True, null=True, editable=True)
    manejaInterfaz = models.CharField(max_length=1,  blank=True, null=True, editable=True)
    distribucionTerceros = models.CharField(max_length=1,  blank=True, null=True, editable=True)
    consentimientoInformado = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cita1Vez = models.CharField(max_length=1, blank=True, null=True, editable=True)
    cuentaContable = models.CharField(max_length=20, blank=True, null=True, editable=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    class Meta:
        unique_together = (('codigoCups'),)

    def __str__(self):
        return self.nombre

class EstadosInterconsulta(models.Model):
                id = models.AutoField(primary_key=True)
                nombre = models.CharField(max_length=30, null=False)
                estadoReg = models.CharField(max_length=1, default='A', editable=False)

                def __str__(self):
                    return self.nombre


class TiposInterconsulta(models.Model):
                id = models.AutoField(primary_key=True)
                nombre = models.CharField(max_length=30, null=False)
                estadoReg = models.CharField(max_length=1, default='A', editable=False)

                def __str__(self):
                    return self.nombre


class HistorialInterconsultas(models.Model):

                id  = models.AutoField(primary_key=True)
                historia =  models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag11')
                tipoInterconsulta = models.ForeignKey('clinico.TiposInterconsulta',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
                descripcionConsulta = models.CharField(max_length=200)
                especialidadConsulta = models.ForeignKey('clinico.Especialidades', default=1, on_delete=models.PROTECT, null=False)
                medicoConsulta  = models.ForeignKey('clinico.Medicos',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
                especialidadConsultada = models.ForeignKey('clinico.Especialidades', default=1, on_delete=models.PROTECT, null=False,    related_name='espe22')
                medicoConsultado  = models.ForeignKey('clinico.Medicos',  blank=True, null=True, editable=True, on_delete=models.PROTECT ,   related_name='med22')
                respuestaConsulta = models.CharField(max_length=800)
                diagnosticos = models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                estadosInterconsulta = models.ForeignKey('clinico.EstadosInterconsulta',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
                estadoReg = models.CharField(max_length=1, default='A', editable=False)

                def __str__(self):
                    return self.descripcionConsulta




class TiposEvolucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre




class Historia(models.Model):
    S = 'S'
    N = 'N'
    TIPO_CHOICES = (
        (S, 'S'),
        (N, 'N'),
    )
    id = models.AutoField(primary_key=True)
    tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True, null=True, editable=True,      on_delete=models.PROTECT)
    documento = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoria5672')
    consecAdmision = models.IntegerField(default=0)
    folio = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    tiposFolio = models.ForeignKey('clinico.TiposFolio', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    causasExterna = models.ForeignKey('clinico.causasExterna', blank=True, null=True, editable=True,             on_delete=models.PROTECT)
    dependenciasRealizado = models.ForeignKey('sitios.Dependencias', blank=True, null=True, editable=True,            on_delete=models.PROTECT)
    especialidades = models.ForeignKey('clinico.Especialidades', blank=True, null=True, editable=True,             on_delete=models.PROTECT)
    planta = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=250,  blank=True, null=True,)
    subjetivo = models.CharField(max_length=250,  blank=True, null=True,)
    objetivo = models.CharField(max_length=250,  blank=True, null=True,)
    analisis = models.CharField(max_length=250,  blank=True, null=True,)
    plann = models.CharField(max_length=250,  blank=True, null=True,)
    enfermedadActual = models.CharField(max_length=5000,  blank=True, null=True,)
    ingestaAlcohol = models.CharField(max_length=5000,  blank=True, null=True,)
    monitoreo = models.CharField(max_length=1,  blank=True, null=True,choices=TIPO_CHOICES,)
    examenFisico = models.CharField(max_length=5000,  blank=True, null=True,)
    justificacion = models.CharField(max_length=5000,  blank=True, null=True,)
    tipoEvolucion = models.ForeignKey('clinico.TiposEvolucion', blank=True, null=True, editable=True,               on_delete=models.PROTECT)
    apache2 = models.IntegerField(default=0 ,  blank=True, null=True,)
    indiceMortalidad = models.IntegerField(default=0 ,  blank=True, null=True )
    epicrisis = models.CharField(max_length=20000,  blank=True, null=True,)
    manejoQx = models.CharField(max_length=20000,  blank=True, null=True,)
    noQx = models.CharField(max_length=30,  blank=True, null=True,)
    antibioticos = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    tratamiento = models.CharField(max_length=5000,  blank=True, null=True,)
    llenadoCapilar = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    pulsos = models.CharField(max_length=1, blank=True, null=True, choices=TIPO_CHOICES,)
    vomito = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    nauseas = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    irritacion = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    neurologia = models.CharField(max_length=1, blank=True, null=True, choices=TIPO_CHOICES,)
    retiroPuntos = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    movilidadLimitada = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    interconsulta = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    observaciones = models.CharField(max_length=5000,  blank=True, null=True,)
    riesgos = models.CharField(max_length=5000,  blank=True, null=True,)
    notaAclaratoria = models.CharField(max_length=1,  blank=True, null=True, choices=TIPO_CHOICES,)
    fecNotaAclaratoria = models.DateTimeField(blank=True,  null=True,)
    textoNotaAclaratoria = models.CharField(max_length=5000,  blank=True, null=True,)
    usuarioNotaAclaratoria = models.ForeignKey('usuarios.Usuarios', blank=True, null=True, editable=True,          on_delete=models.PROTECT)
    inmovilizacion = models.CharField(max_length=1, blank=True, null=True,choices=TIPO_CHOICES,)
    inmovilizacionObservaciones = models.CharField(max_length=5000,  blank=True, null=True,)
    riesgoHemodinamico = models.CharField(max_length=15,  blank=True, null=True,)
    riesgoVentilatorio = models.CharField(max_length=15,  blank=True, null=True,)
    leucopenia = models.CharField(max_length=50,  blank=True, null=True,)
    trombocitopenia = models.CharField(max_length=50,  blank=True, null=True,)
    hipotension = models.CharField(max_length=50,  blank=True, null=True,)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT   ,          related_name='lanta345')
    estadoReg = models.CharField(max_length=1, default='A', editable=False,  blank=True, null=True,)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = (('tipoDoc', 'documento','consecAdmision','folio'),)
        ordering = ["tipoDoc", "documento", "folio", "fecha", "especialidades", "motivo", "subjetivo", "objetivo",
                    "analisis", "plann"]



class HistoriaExamenes(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    tiposExamen = models.ForeignKey('clinico.TiposExamen', default=1, on_delete=models.PROTECT, null=False)
    codigoCups = models.CharField(max_length=20, null=False, blank=True)
    dependenciasRealizado = models.ForeignKey('sitios.Dependencias', blank=True, null=True, editable=True,            on_delete=models.PROTECT)
    mipres = models.CharField(max_length=15, null=True, blank=True)
    consecutivo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField()
    observaciones = models.CharField(max_length=200, editable=True,blank=True, null=True)
    fechaToma = models.DateTimeField(blank=True, null=True)
    usuarioToma = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='usuarioToma1')
    #preliminar1 = models.CharField(max_length=300, editable=True,blank=True, null=True)
    interpretacion1 = models.CharField(max_length=500, editable=True ,blank=True, null=True)
    medicoInterpretacion1 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='medInterpreta1')
    fechaInterpretacion1 = models.DateTimeField(blank=True, null=True)
    #preliminar2 = models.CharField(max_length=300, editable=True,blank=True, null=True)
    interpretacion2 = models.CharField(max_length=500, editable=True,blank=True, null=True)
    medicoInterpretacion2 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='medInterpreta2')
    fechaInterpretacion2 = models.DateTimeField(blank=True, null=True)
    #preliminar3 = models.CharField(max_length=300, editable=True,blank=True, null=True)
    interpretacion3 = models.CharField(max_length=500, editable=True,blank=True, null=True)
    medicoInterpretacion3 = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='medInterpreta3')
    fechaInterpretacion3 = models.DateTimeField(blank=True, null=True)
    #resultado = models.CharField(max_length=5000, editable=True,blank=True, null=True)
    medicoReporte = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='medReporte')
    fechaReporte = models.DateTimeField(blank=True, null=True)
    opinion = models.CharField(max_length=1000, editable=True,blank=True, null=True)
    facturado = models.CharField(max_length=1, editable=True ,blank=True, null=True)
    anulado = models.CharField(max_length=1, editable=True, default = 'N')
    usuarioAnula = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,  on_delete=models.PROTECT, related_name='usuarioAnula1')
    rutaImagen = models.CharField(max_length=100, default='')
    rutaVideo = models.CharField(max_length=100, default='')
    estadoExamenes = models.ForeignKey('clinico.EstadoExamenes', default=1, on_delete=models.PROTECT)
    observaciones = models.CharField(max_length=200, editable=True,blank=True, null=True)
    usuaroRegistra = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT, related_name='usuarioRegistra1')
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.cantidad)


class HistoriaResultados(models.Model):

                    id = models.AutoField(primary_key=True)
                    #historia = models.ForeignKey('clinico.Historia', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                    historiaExamenes = models.ForeignKey('clinico.HistoriaExamenes', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                    #dependenciasRealizado = models.ForeignKey('sitios.Dependencias', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                    fechaServicio = models.DateTimeField(default=now, blank=True, null=True, editable=True)
                    fechaResultado = models.DateTimeField(default=now, blank=True, null=True, editable=True)
                    examenesRasgos = models.ForeignKey('clinico.ExamenesRasgos', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                    valor =  models.CharField(max_length=20,  blank=True, null=True, editable=True)
                    observaciones =  models.CharField(max_length=255,  blank=True, null=True, editable=True)
                    consecResultado = models.IntegerField(default=0, blank=True, null=True, editable=True)
                    #estadoExamenes =  models.ForeignKey('clinico.EstadoExamenes', blank=True, null=True, editable=True, on_delete=models.PROTECT)
                    estadoReg = models.CharField(max_length=1, default='A', editable=False)

                    def __str__(self):
                        return self.resultado



class TiposDiagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre



class Diagnosticos(models.Model):
    S = 'S'
    N = 'N'
    TIPO_CHOICES = (
        (S, 'S'),
        (N, 'N'),
    )
    id = models.AutoField(primary_key=True)
    cie10  = models.CharField(max_length=15, default='')
    nombre = models.CharField(max_length=300 , null=False)
    descripcion = models.CharField(max_length=300)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    edadIni = models.IntegerField(editable=True, null=True, blank=True)
    edadFin = models.IntegerField(editable=True, null=True, blank=True)
    flagSivigila = models.CharField(max_length=1, default='A', editable=False, choices=TIPO_CHOICES)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    #usuarioRegistro = models.ForeignKey('usuarios.Usuarios', default=1, on_delete=models.PROTECT, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class EstadosSalida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class HistorialIncapacidades(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia', on_delete=models.PROTECT, blank=True, null=True,  editable=True,  related_name='DocumentoHistoriaDiag10')

    tiposIncapacidad =  models.ForeignKey('clinico.TiposIncapacidad',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    desdeFecha = models.DateTimeField(default=now ,blank=True, null=True)
    hastaFecha = models.DateTimeField(default=now ,blank=True, null=True)
    numDias  = models.IntegerField(editable=True, null=True, blank=True)
    descripcion = models.CharField(max_length=4000 ,blank=True, null=True)
    diagnosticosIncapacidad = models.ForeignKey('clinico.Diagnosticos',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.documento


class HistorialDiagnosticos(models.Model):
    id = models.AutoField(primary_key=True)
    historia =  models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag8')
    tiposDiagnostico = models.ForeignKey('clinico.TiposDiagnostico',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='tiposDiagnostico')
    diagnosticos =  models.ForeignKey('clinico.Diagnosticos', blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='dxPpal')
    consecutivo = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=2000 ,blank=True, null=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.documento


class HistorialAntecedentes(models.Model):
    id = models.AutoField(primary_key=True)
    historia =  models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoHistoriaDiag9')
    tiposAntecedente = models.ForeignKey('clinico.TiposAntecedente', on_delete=models.PROTECT, null=False)
    #antecedentes  = models.ForeignKey('clinico.Antecedentes', on_delete=models.PROTECT, null=False)
    descripcion = models.CharField(max_length=200)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    usuarioRegistro = models.ForeignKey('usuarios.Usuarios',  blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.descripcion

## Desde aquip ingresar en Admin

class Regimenes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class TiposCotizante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class Eps(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class TiposSalidas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class TurnosEnfermeria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class TiposTriage(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre

class NivelesClinica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class RevisionSistemas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre


class Recomendaciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Hallazgos(models.Model):

    SI = 'S'
    NO = 'N'
    TIPO_CHOICES = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag13')
    nombre = models.CharField(max_length=50)
    miembrosSuperiores = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    miembrosInferiores = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    columna = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    ojos = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    nariz = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    oidos = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    cara = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    neurologicos = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    fxCraneo = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    torax = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    abdomen = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    exaMdGeneral = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    factorTvp = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    cuello = models.CharField(max_length=1, default='N', choices=TIPO_CHOICES, )
    fechaRegistro = models.DateTimeField(default=now, editable=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre



class NivelesRegimenes(models.Model):
    SI = 'S'
    NO = 'N'
    TIPO_CHOICES = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    regimen = models.ForeignKey('clinico.Regimenes', blank=True,null= True, editable=True, on_delete=models.PROTECT)
    porCuotaModeradora = models.DecimalField(max_digits=5, decimal_places=2)
    porCopago = models.DecimalField(max_digits=5, decimal_places=2)
    porTopeEve = models.DecimalField(max_digits=5, decimal_places=2)
    porTopeAnual = models.DecimalField(max_digits=5, decimal_places=2)
    estadoReg = models.CharField(max_length=1, default='A', editable=False ,choices = TIPO_CHOICES)

    def __str__(self):
        return str(self.regimen)


class Ips(models.Model):

    id       = models.AutoField(primary_key=True)
    nombre  =  models.CharField(max_length=30, blank=True,null= True, editable=True,)
    fechaRegistro = models.DateTimeField(default=now, blank=True,null= True, editable=True, )
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)

class Grupos(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=80, blank=True, null=True, editable=False)
    nombre = models.CharField(max_length=80, blank=True, null=True, editable=False)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombred)

class SubGrupos(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey('clinico.Grupos', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=80, blank=True, null=True, editable=False)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)

class ViasAdministracion(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)

class UnidadesDeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    nomenclatura = models.CharField(max_length=50, blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.descripcion)

class Presentacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)


class FormasFarmaceuticas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.nombre)

class UnidadesDeMedidaDosis(models.Model):
    id = models.AutoField(primary_key=True)
    unidadaDeMedidaPrincipioA = models.CharField(max_length=50, blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.descripcion)


class FrecuenciasAplicacion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.descripcion)

class IndicacionesEspeciales(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.descripcion)


class TiposMedicamento(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class MedicamentosDci(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    descripcionDciConcentracion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    tipoMedicamento = models.ForeignKey('clinico.TiposMedicamento', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)


class ExpedienteDCI(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    #formaFarmaceutica = models.ForeignKey('clinico.FormasFarmaceuticas', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class TiposDispositivoMedico(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.descripcion)

class TiposProductosNutricion(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True, editable=True)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class ProductosNutricion(models.Model):
    id = models.AutoField(primary_key=True)
    codigoMipres = models.DecimalField(max_digits=5, decimal_places=0 , blank=True, null=True, editable=True)
    nombreComercial = models.CharField(max_length=100, blank=True, null=True, editable=True)
    grupo =  models.CharField(max_length=100, blank=True, null=True, editable=True)
    formaFarmaceutica = models.ForeignKey('clinico.FormasFarmaceuticas', blank=True, null=True, editable=True,  on_delete=models.PROTECT)
    presentacion = models.ForeignKey('clinico.Presentacion', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    unidades = models.ForeignKey('clinico.UnidadesDeMedida', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    habilitadoMipres = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class SignosVitales(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag23')
    fecha = models.DateTimeField(default=now ,blank=True, null=True)
    frecCardiaca = models.CharField(max_length=5,null=True,  blank=True)
    frecRespiratoria = models.CharField(max_length=5,null=True,  blank=True)
    tensionADiastolica = models.CharField(max_length=5,null=True,  blank=True)
    tensionASistolica = models.CharField(max_length=5,null=True,  blank=True)
    tensionAMedia = models.CharField(max_length=5,null=True,  blank=True)
    temperatura = models.CharField(max_length=5,null=True,  blank=True)
    saturacion = models.CharField(max_length=5,null=True,  blank=True)
    glucometria = models.CharField(max_length=5,null=True,  blank=True)
    glasgow = models.CharField(max_length=5,null=True,  blank=True)
    apache = models.CharField(max_length=5,null=True,  blank=True)
    pvc = models.CharField(max_length=5,null=True,  blank=True)
    cuna = models.CharField(max_length=5,null=True,  blank=True)
    ic = models.CharField(max_length=5,null=True,  blank=True)
    glasgowOcular = models.CharField(max_length=5,null=True,  blank=True)
    glasgowVerbal = models.CharField(max_length=5,null=True,  blank=True)
    glasgowMotora = models.CharField(max_length=5,null=True,  blank=True)
    observacion = models.CharField(max_length=5000, null=True, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class HistoriaSignosVitales(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaSig2')
    fecha = models.DateTimeField(default=now ,blank=True, null=True)
    frecCardiaca = models.CharField(max_length=5,null=True,  blank=True)
    frecRespiratoria = models.CharField(max_length=5,null=True,  blank=True)
    tensionADiastolica = models.CharField(max_length=5,null=True,  blank=True)
    tensionASistolica = models.CharField(max_length=5,null=True,  blank=True)
    tensionAMedia = models.CharField(max_length=5,null=True,  blank=True)
    temperatura = models.CharField(max_length=5,null=True,  blank=True)
    saturacion = models.CharField(max_length=5,null=True,  blank=True)
    glucometria = models.CharField(max_length=5,null=True,  blank=True)
    glasgow = models.CharField(max_length=5,null=True,  blank=True)
    apache = models.CharField(max_length=5,null=True,  blank=True)
    pvc = models.CharField(max_length=5,null=True,  blank=True)
    cuna = models.CharField(max_length=5,null=True,  blank=True)
    ic = models.CharField(max_length=5,null=True,  blank=True)
    glasgowOcular = models.CharField(max_length=5,null=True,  blank=True)
    glasgowVerbal = models.CharField(max_length=5,null=True,  blank=True)
    glasgowMotora = models.CharField(max_length=5,null=True,  blank=True)
    observacion = models.CharField(max_length=5000, null=True, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class HistoriaRevisionSistemas(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaRev1')
    revisionSistemas = models.ForeignKey('clinico.RevisionSistemas', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    observacion = models.CharField(max_length=5000, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class Trasfusiones(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag25')
    fecha = models.DateTimeField()
    selloCalidad = models.CharField(max_length=5000, blank=True)
    grupoBolsa = models.CharField(max_length=50, blank=True)
    fechaCaducidad = models.DateTimeField()
    realizoTrasfusion = models.CharField(max_length=50, blank=True)
    trasfusionInicio = models.CharField(max_length=50, blank=True)
    trasfusionFinal = models.CharField(max_length=50, blank=True)
    complicaciones = models.CharField(max_length=5000, blank=True)
    tipoComponente = models.CharField(max_length=50, blank=True)
    epicrisis = models.CharField(max_length=5000, blank=True)
    compReactRtha = models.CharField(max_length=15, blank=True)
    compEnfInjerto = models.CharField(max_length=15, blank=True)
    compSobreCargaCirc = models.CharField(max_length=15, blank=True)
    compLesPulmonar = models.CharField(max_length=15, blank=True)
    compReacAlergica = models.CharField(max_length=15, blank=True)
    compSepsis = models.CharField(max_length=15, blank=True)
    compPurpPostTrans = models.CharField(max_length=15, blank=True)
    compReacFHemolitica = models.CharField(max_length=15, blank=True)
    compReacFNoHemolitica = models.CharField(max_length=15, blank=True)
    compEmboAereo = models.CharField(max_length=15, blank=True)
    compHipocalemia = models.CharField(max_length=15, blank=True)
    compHipotermia = models.CharField(max_length=15, blank=True)
    compTransMasiva = models.CharField(max_length=15, blank=True)
    compEscalofrios = models.CharField(max_length=15, blank=True)
    compOtro = models.CharField(max_length=15, blank=True)
    compOtroDesc = models.CharField(max_length=2000, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,     on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class Oxigeno(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag26')
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    tipoOxigenacion = models.CharField(max_length=15, blank=True)
    aire = models.CharField(max_length=1, blank=True)
    saturacionOxigeno = models.DecimalField(max_digits=3, decimal_places=2)
    flujoLtsOxigeno = models.DecimalField(max_digits=3, decimal_places=2)
    flujoLtsAire = models.DecimalField(max_digits=3, decimal_places=2)
    horasOxigeno = models.DecimalField(max_digits=3, decimal_places=2)
    horasAire = models.DecimalField(max_digits=3, decimal_places=2)
    totalLtsoxigeno = models.DecimalField(max_digits=3, decimal_places=2)
    totalLtsAire = models.DecimalField(max_digits=3, decimal_places=2)
    totalMetrocubicoOxigeno = models.DecimalField(max_digits=3, decimal_places=2)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True, on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class ImHaloTerapia(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag27')
    fecha = models.DateTimeField()
    salbutamol = models.CharField(max_length=50, blank=True)
    ipratropio = models.CharField(max_length=50, blank=True)
    beclometazona = models.CharField(max_length=50, blank=True)
    berudual = models.CharField(max_length=50, blank=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)


    def __str__(self):
        return str(self.id)

class Antibiotico(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia',  blank=True, null=True, editable=True, on_delete=models.PROTECT,   related_name='DocumentoHistoriaDiag28')
    fechaSolicitud = models.DateTimeField()
    fechaInicio = models.DateTimeField()
    suministro = models.ForeignKey('facturacion.Suministros', blank=True, null=True, editable=True, on_delete=models.PROTECT ,related_name='sumins03')
    profilaxis = models.CharField(max_length=10, blank=True, null=True, editable=True)
    ttoEmpirico = models.CharField(max_length=10, blank=True, null=True, editable=True)
    ttoetiologico = models.CharField(max_length=10, blank=True, null=True, editable=True)
    ampliacionTto = models.CharField(max_length=10, blank=True, null=True, editable=True)
    cambioEsquema = models.CharField(max_length=10, blank=True, null=True, editable=True)
    saludPublica = models.CharField(max_length=10, blank=True, null=True, editable=True)
    dxInfeccion = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    germenAislado = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    fechaVigencia = models.DateTimeField()
    fallaRenal = models.CharField(max_length=10, blank=True, null=True, editable=True)
    fallaHepatica = models.CharField(max_length=10, blank=True, null=True, editable=True)
    infeccionSevera = models.CharField(max_length=10, blank=True, null=True, editable=True)
    inmunoSupresion = models.CharField(max_length=10, blank=True, null=True, editable=True)
    aprobado = models.CharField(max_length=15, blank=True, null=True, editable=True)
    prescripcion = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    protocolo = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    noProtocolo = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    ajustadoCultivo = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    ajustadoDosiRenal = models.CharField(max_length=1000, blank=True, null=True, editable=True)
    autInfectologia = models.CharField(max_length=2, blank=True, null=True, editable=True)
    observacionEpidemilogia = models.CharField(max_length=10000, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class Medicamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True, editable=True)
    def __str__(self):
        return str(self.id)
	
class HistoriaMedicamentos(models.Model):
    id = models.AutoField(primary_key=True)
    historia = models.ForeignKey('clinico.Historia', default=1, on_delete=models.PROTECT, null=False, related_name='DocumentoHistoriaDiag12')
    orden = models.IntegerField(default=0)
    suministro = models.ForeignKey('facturacion.Suministros', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    dosisCantidad = models.DecimalField(max_digits=20, decimal_places=3)
    dosisUnidad = models.ForeignKey('clinico.UnidadesDeMedidaDosis', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    frecuencia = models.ForeignKey('clinico.FrecuenciasAplicacion', blank=True, null=True, editable=True,               on_delete=models.PROTECT)
    viaAdministracion = models.ForeignKey('clinico.ViasAdministracion', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    nota = models.CharField(max_length=5000, blank=True)
    cantidadOrdenada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    diasTratamiento =  models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    cantidadSolicitada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    cantidadEntregada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    cantidadDispensada = models.ForeignKey('rips.RipsUnidadUpr', blank=True, null=True, editable=True,   on_delete=models.PROTECT)
    cantidadAplicada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    cantidadDevuelta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    cantidadfacturada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True)
    nopos = models.CharField(max_length=1, blank=True, null=True, editable=True)
    estadoMedicamento = models.CharField(max_length=1, blank=True, null=True, editable=True)
    horarioDosis = models.CharField(max_length=200, blank=True, null=True, editable=True)
    dosisUnica = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, editable=True )
    dosisRescate = models.CharField(max_length=200, blank=True, null=True, editable=True)
    dosisProfilaxis = models.CharField(max_length=200, blank=True, null=True, editable=True)
    dosisAdelanto = models.CharField(max_length=200, blank=True, null=True, editable=True)
    urgente = models.CharField(max_length=1, blank=True, null=True, editable=True)
    dosificacion = models.CharField(max_length=2000, blank=True, null=True, editable=True)
    antibiotico = models.CharField(max_length=1, blank=True, null=True, editable=True)
    fechaSuspension = models.DateTimeField( blank=True, null=True, editable=True)
    usuarioRegistro = models.ForeignKey('planta.Planta', blank=True, null=True, editable=True,    on_delete=models.PROTECT)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return str(self.id)

class PrincipiosActivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre

class CodigosAtc(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, blank=True, null=True, editable=True)
    nombre = models.CharField(max_length=50, blank=True, null=True, editable=True)
    fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
    estadoReg = models.CharField(max_length=1, default='A', editable=False )

    def __str__(self):
        return str(self.id)


class ExamenesRasgos(models.Model):
    id = models.AutoField(primary_key=True)
    tiposExamen = models.ForeignKey('clinico.TiposExamen', default=1, on_delete=models.PROTECT, null=False)
    codigoCups = models.CharField(max_length=20, null=False, blank=True)
    nombre = models.CharField(max_length=80, null=False)
    unidad = models.CharField(max_length=20, null=False)
    minimo = models.CharField(max_length=20, null=False)
    maximo = models.CharField(max_length=20, null=False)
    estadoReg = models.CharField(max_length=1, default='A', editable=False)

    def __str__(self):
        return self.nombre
