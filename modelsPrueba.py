TIPS THE WORK

-- PARTE I ADMISIONES - ADMINISTRATIVA  - FACTURACION

-- OJO EL DIA LUNES 8/07
En facturacion:
0.1 Tarifas (id, nombre,  convenioId, conceptoId, tipo, codigoCups, codigoSuministro, valor, grupoQx, paquete, Honorarios)
0.1.1 TiposTarifa(id, nombre ) EPS, ENTE TERRITORIAL Particular, Iss, soat, otros
0.2 TiposTarifa(id,nombre)  EPS,SOAT, ISS, ENTE TERRITORIAL, IPS, ARL, PARTICULAR)
0.3  Eapb (id,nombre,codigoEapb, codigoRips, tipoDoc, documento)-- Entidades de aseguramiento del plan de beneficios
0.4 Empresas (id,  tipoDoc, documento,nombre, codigoEapb , direccion, telefono, representante,  regimen, fosyga, particular, departamento, municipio, codigoPostal, responsableFiscal, identificadorDian )


0.5  -- sunpongo la tabla ConveniosPaciente (id,tipoDoc,documento,convenio)
0.6 -- ConveniosPacienteIngresos (id,tipoDoc,documento,consec, convenio)

0.7 Conceptos (id, nombre,tipoCups, codAd, codAt, ripsAc, ripsAp, ripsAt, ripsAm, ripsAh, ripsAu)
0.8 TipoCups (id, nombre)  Son : Cups, Articulos
0.9 Cups (id, nombre,codigoCups, concepto,autorizar, codigoRips,cupsGrupo, cupsSubgrupo;cupsCategoria, resolucion1132,
	 Tipo,nivelAtencion,Plan,centroCosto ,finalidad, duracion, manejaInterfaz,DistribucionTerceros,consentimientoInformado,cita1Vez, cContable)
   
-- En facturacion a ver que oasa
0.0.1 TiposSuministro (id, nombre)  -- Material,Articulo, Medicamento, osteosisntesis ,etc
0.10 Suministros (id, nombre, tipoSuministro, nombreGenerico, concepto, concentracion,grupo,unidadaMedida, fraccion, unidadFraccion, viaAdministracion, vence,control,antibiotico,pos, facturable,stockMinimo,stockMaximo,maxOrdenar,estabilidad, invFarmacia,invAlmacen, enfermeria, terapia, nutricion, cantidad, cums, formaFarmaceutica,regSanitario, altoCosto, vrCompra, vrUltimaCompra, codigoAtc, infusion, tipoAdministracion, regulado, calorRegulado,observaciones, sispro, oncologico, ortesis, mipres, epiHigiene, controlStock
		        AnatoPos, magistral control , genericoPos)


0.11 FormasLiquidacion : (id, nombe,  Codigo,tipoCruento ,caracteristica, valorHonorario,tiposHonorarios,cuentaContable,centroCosto)

En contratacion:
0.9 -- supongo tabla - Convenios (id,nombre, empresa, tipoTarifa etc, vigencia_desde, vigencia_hasta, porcTarifario, porcSuministros, valorOxigeno,porcEsterilizacion, porcMaterial, hospitalario, urgencias, ambulatorio, consultaExterna
								    copago, moderadora, tipofactura , agrupada, facturacionSuministros, facturacionCups , cuentaContable, requisitos)

para el lunes 15/julio

1. Poder grabar una Admision (una vez guarde el nuevo usuario se pueda seguir la modal desaparezca y pueda crear correctamente una admision al igual con actualizar probar)
2. Probar todos los filtros de consultas en admisiones (por servicios, sedes, subservicios, habitaciones, nombres etc)
   se debe seguir con Furips, Triage, Ingreso a Triage (Probar trabajar con clases)
3. No eta UPDATE /INSERT de ls campos manilla, acompanatete, responsable remitido ips 

	                 empresa_id=empresaId,
                         ipsRemite_id = ipsRemite,
                         numManilla =numManilla,
                         contactoAcompanante_id = contactoAcompanante,
                         contactoResponsable_id = contactoResponsable,
4. Ojo recuerda los permisos punuales DSACTIVAR / INACTIVAR Botones
5. Ojo como genera el consecutivo de ingreso, tiene que NOO observar la sede o sea va a tener un consecutivo permanente, no pueden haber mas d eun consecutivo, o repetido
   son independientes de la sede , son ascendentes
6. Crear modulos de farmacia, inventarios y creo pare de contar no va mas ...
        
-- No graba num_manilla, remitido
-- ojo como carachas editas los existentes ???(ideas un link en html en la tabla y que llame una modal admisiones). Pero hay que ver que cambio es posible cambioar auqui ? Regimen?, num_manilla, remitido, ips_remite, empresa ???, responsable, acompañante, tipo de cotizante, muerte , defuncion, hclinica,fechaMuerte, causasMuerte,vias_deIngreso, viasdeegreso
        actadedefuncion, estadoSalida, especialidades, dx,  etc
    -- Pues datos como usuaruio no se hacen aqui, contactos, tampoco se hacen aquip,
-- ojo cuando fitra o cuando cre admision No cocerva el modulo, profesioal,sede
-- Ojo cuando se hace le ingreso no parece no graba bien el Id del medico
-- ojo el combo de especialidad en ingresos trae medicos de las americas error
-- ojo hay que unificar mayuscula y minuscula un estandrad o sino paila por ejemplo Profesional / profesional
--Ojo que pasa con os estadorREg de todos los modelos ojop definir de una vez despues es inmanejable
-- OJO NO ESTA PASANDO EL MODELO A LA VISTA ACOMPAN, RESPO, IPS, MANULLA, ETC
-- cuando voya craer in creadmision por segunda vez pierde los cmbos de empresas, acompanamtes, repospoonsables, ips por  cua ?
-- OJO SE DEBEBN CREAR CONTEXTOS DE ACUERDO A LOS MODULOS EJEMPLO INGRESOS uno HISPTRIA CLINICA OTRO DIRIA YO SOLO LAS TABLAS CLINICAS
-- la funcion retornarAdmision que hace ?
-- ojo cuando retorna en algunas pantallas se pieerde la sede, profesioonal,colaborador

--Hay que organizar todo eso papaberol antes d eseguir adelante si no PAILANDER, la tiene dura el dia LUNES PAPABEROL
-- TIENE QUE ESTANDARIZAR EL SOFTWARE O SI NOP PAILAS ANTES DE SEGUIR ORDEN SI NO PASA ESTA PRUEBA ADIOS SERVER

-- OJOP:
1. hilo de performance llenar tabla ingresos con 500000 registors o los mismo que tienen actualmente imhotep (para realizar consultas-filtros)
2. crear los boceto de todos las paginas-programa con el boton retorn volviendo al menu anterioro, admiisone-autorizaciones etc
3. reorganizar los context para cada caso ahorrar memoria -cpu vien organizadito el codigo
4. cvarialene¿s am pasar a los html ,os mismo para todas las paginas

FIN 15/julio


5. Crear Proceso Traslados de Habitaciones/Servicio/etc
6. Crear un proceso masivo de actualizacion a una nueva instalacion python, con export de bdatos y creacion global d eun nuevo sitio
   es como ir creando algo asi como un instalador del programa y un backup/restore de la informacion postgres como le parece . AUTOMATIZAR
7. ojo tengo quemado un centroc_id en 1 creo para que guarde la modal usuario (NO SE PORQUE)/ tambien en main, ausuario1 fecIngreso esta quemado 2024-01-01
8.  Creo crear programa autorizaciones con panelAutorizaciones y demas depronot un menuAutorizaciones para comenzar a diferenciar y yap todo
   con el estandard de programacion


   PROCESO TENTATIVO INICIAL
   0. Justo antes de realizar cualquier cambio en los modelos del aplicativo1. Crear un ambiente python exacto al que hay (Mediante archivo .bat de Windows)
	Algo asi :
        cmd
        cd\
        cd EntornosPythn  alberto@
        virtualenv nuevoProyecto
        cd nuevoProyecto
        cd scripts
        activate
        cd ..
        requeriments.bat
        django-admin startproject vulner
        cd vulner
        django-admin start app Administracion
        .
        .
        django-admin startapp usuarios
        xcopy c:\entornosPython\proyectoAnterior\vulner\Administracion\*.py  c:\entornosPython\proyectoANuevo\vulner\Administracion\*.py 
        .
        .
        .
	xcopy c:\entornosPython\proyectoAnterior\vulner\usuarios\*.py  c:\entornosPython\proyectoANuevo\vulner\usuarios\*.py 
	xcopy c:\entornosPython\proyectoAnterior\vulner\vulner\urls.py  c:\entornosPython\proyectoANuevo\vulner\vulner\urls.py
	xcopy c:\entornosPython\proyectoAnterior\vulner\static  c:\entornosPython\proyectoANuevo\vulner\static
	xcopy c:\entornosPython\proyectoAnterior\vulner\media  c:\entornosPython\proyectoANuevo\vulner\media
	xcopy c:\entornosPython\proyectoAnterior\vulner\templates  c:\entornosPython\proyectoANuevo\vulner\templates

        # crear el nuevo settings.py en el proyecto nuevo
        python manage.py makemigrations
	python manage.py migrate
        python manage.py createsuperuser
          -- respuestas
        python manage.py runserver 8082
         	
   2. Backup Base de Datos Postgres solo data (puede ser solo instrucciones SQL)

	Se saco backup tipo Tar, pero exceptuando todas las tablas auth* y django*. Pero ojo no me subio las tablas con campos timestamp
        Lo logre sin activar insert column ni activar oids ni activar insert commands
        planito planito y yap probar mañana TODO


   3. Restore Bases de Datos a nuevo ambiente (solo data el mismo archivo). correr script SQL
   4. Actualizar Aplicativo (Crear nuevos Modelos, vistas, templates, etc)-  Aplicar makemigrations - migrate
   5. Correr script que pueblan tablas recien creadas o actualizan campos si los hay
   6. Listop


7. Seguir con clinico.*, nuevas tablas, campos , logica etc de imh(Ojop)
7.1 vERIFICAR LOS CHOICES EN EL PROGRAMA


9. PENDIENTES (facturacion mae_topsesoat(Facturacion), (mae_tarifasqx(Contratacion),mae_tarifasSoat(Contratacion), 
	
Tablas = tblhcl_ingresos ( es la parte clinica del accidente)
Tablas= tbl_furips ( Es como la parte legal de datos)
Podria ser FuripsClinico, FuripsLegal
Mas la tabla normal de las evoluciones Clinicas
Ideas: ir backup de tablas sep



-- PARTE II CLINICA

-- Ojo ver tabla de incapacidades 

clinico_historia:


-- modulo  clinico

class Historia(models.Model):
                id = models.AutoField(primary_key=True)
                tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                documento = models.ForeignKey('usuarios.Usuarios', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoHistoria')
                consecAdmision = models.IntegerField(default=0)
                folio =  models.IntegerField(default=0)
                fecha = models.DateTimeField()
                tiposFolio = models.ForeignKey('clinico.TiposFolio', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                causasExterna = models.ForeignKey('clinico.causasExterna', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                dependenciasRealizado = models.ForeignKey('sitios.Dependencias', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                especialidades = models.ForeignKey('clinico.Especialidades', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                planta   = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                motivo     = models.CharField(max_length=250,blank=True)
                subjetivo  = models.CharField(max_length=250, blank=True)
                objetivo   = models.CharField(max_length=250,blank=True)
                analisis   = models.CharField(max_length=250, blank=True)
                plann       = models.CharField(max_length=250, blank=True)
                enfermedadActual =  models.CharField(max_length=5000, blank=True)
 		ingestaAlcohol =  models.CharField(max_length=5000, blank=True)
	        monitoreo =  models.CharField(max_length=1,blank=True)
                examenFisico = models.CharField(max_length=5000,blank=True)
 		justificacion = models.CharField(max_length=5000,blank=True)
                tipoEvolucion = models.ForeignKey('clinico.TiposEvolucion', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                apache2 = models.IntegerField(default=0)
                indiceMortalidad = models.IntegerField(default=0)
		epicrisis = models.CharField(max_length=20000,blank=True)
                manejoQx =   models.CharField(max_length=20000,blank=True)
                noQx = models.CharField(max_length=30,blank=True)
		antibioticos = models.CharField(max_length=1,blank=True)
                tratamiento = models.CharField(max_length=5000,blank=True)
                llenadoCapilar = models.CharField(max_length=1,blank=True)
		pulsos = models.CharField(max_length=1,blank=True)
		vomito = models.CharField(max_length=1,blank=True)
		nauseas = models.CharField(max_length=1,blank=True)
		irritacion = models.CharField(max_length=1,blank=True)
		neurologia = models.CharField(max_length=1,blank=True)
		retiroPuntos = models.CharField(max_length=1,blank=True)
		movilidadLimitada = models.CharField(max_length=1,blank=True)
		interconsulta =  models.CharField(max_length=1,blank=True)
		observaciones = models.CharField(max_length=5000,blank=True)
		riesgos = models.CharField(max_length=5000,blank=True)
		notaAclaratoria =  models.CharField(max_length=1,blank=True)
		fecNotaAclaratoria = models.DateTimeField()
		textoNotaAclaratoria = models.CharField(max_length=5000,blank=True)
		usuarioNotaAclaratoria = models.ForeignKey('usuarios.Usuarios', blank=True,null= True, editable=True,  on_delete=models.PROTECT)
		inmovilizacion = models.CharField(max_length=1,blank=True)
                inmovilizacionObservaciones = models.CharField(max_length=5000,blank=True)
		riesgoHemodinamico = models.CharField(max_length=15,blank=True)
		riesgoVentilatorio =  models.CharField(max_length=15,blank=True)
		leucopenia = models.CharField(max_length=50,blank=True)
		trombocitopenia = models.CharField(max_length=50,blank=True)
		hipotension = models.CharField(max_length=50,blank=True)
	        fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
		usuarioRegistro = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
		estadoReg = models.CharField(max_length=1, default='A', editable=False)

             
                def __str__(self):
                    return str(self.id)

                class Meta:
                    ordering = ["tipoDoc","documento","folio","fecha","especialidades","motivo","subjetivo","objetivo","analisis","plann"]

-- modulo  enfermeria



class SignosEnfermeria(models.Model):
                id = models.AutoField(primary_key=True) 
                tipoDoc = models.ForeignKey('usuarios.TiposDocumento', blank=True,null= True, editable=True, on_delete=models.PROTECT)
                documento = models.ForeignKey('usuarios.Usuarios', blank=True,null= True, editable=True, on_delete=models.PROTECT,  related_name='DocumentoHistoria')
                consecAdmision = models.IntegerField(default=0)
	        folio =  models.IntegerField(default=0)
		turno= models.ForeignKey('enfermeri.TurnosEnfermeria', blank=True,null= True, editable=True, on_delete=models.PROTECT)
		fecha=models.DateTimeField()
		taSistolica=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		taDiastolica=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		taMedia=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		frecuenciaCardiaca=models.CharField(max_length=100, blank=False,null= False, editable=True)
		frecuenciaRespiratoria=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		temperatura=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		pvc=models.CharField(max_length=100, blank=False,null= False, editable=True)
		glucometria=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		saturacionO=models.CharField(max_length=100, blank=False,null= False, editable=True)
		pia=models.CharField(max_length=100, blank=False,null= False, editable=True)
		pulsoPeriferico=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		unidadesinsulina=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		glasgowVerbal=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		glasgowOcular=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		glasgowTotal=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		pupilasOdt=models.CharField(max_length=100, blank=False,null= False, editable=True)
		pupilasOdr=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		pupilasOir=models.CharField(max_length=100, blank=False,null= False, editable=True)
		pic=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		pam=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		fuerzaMsd=models.CharField(max_length=100, blank=False,null= False, editable=True)
		fuerzaMsi=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		fuerzaMid=models.CharField(max_length=100, blank=False,null= False, editable=True)
		fuerzaMii=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		ppc=models.CharField(max_length=100, blank=False,null= False, editable=True)
		uniddesDeInsulina=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		tipo=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		reflejos=models.CharField(max_length=100, blank=False,null= False, editable=True)
		sensibilidad=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		cefalea=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		marcha=models.CharField(max_length=100, blank=False,null= False,editable=True)
		vomito=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		memoria=models.CharField(max_length=100, blank=False,null= False, editable=True)
		coordinacion=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		rigidezEsfiter=models.CharField(max_length=100, blank=False,null= False, editable=True)
		tos=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		disnea=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		cianosis=models.CharField(max_length=100, blank=False,null= False, editable=True)
		sdra=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		dolorToraxico=models.CharField(max_length=100, blank=False,null= False,editable=True)
		hemoptisis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		dolorAbdominal=	models.CharField(max_length=100, blank=False,null= False,  editable=True)
		presenciaHematemesis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		signosIrritacion=models.CharField(max_length=100, blank=False,null= False, editable=True)
		melenas=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		presenciaDeposicion=models.CharField(max_length=100, blank=False,null= False, editable=True)
		vomitoGastro=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		doopler=models.CharField(max_length=100, blank=False,null= False, editable=True)
		lividez=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		pulsos=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		llenadoCapilar=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		controlPerimetro=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		ansiedad=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		continuaObservacion=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		turno=models.CharField(max_length=100, blank=False,null= False, editable=True)
		horaVitales=	models.CharField(max_length=5, blank=False,null= False, editable=True)
		horaNeurologica=models.CharField(max_length=5, blank=False,null= False, editable=True)
		horaRespiratoria=models.CharField(max_length=5, blank=False,null= False,  editable=True)
		horaGastroIntestinal=models.CharField(max_length=5, blank=False,null= False,  editable=True)
		horaVasculares=	models.CharField(max_length=5, blank=False,null= False,  editable=True)
		usuSignosNeurologicos=models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='usu12')
		usuCompresp=models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='usu13')
		usuGastro=models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='usu14')
		usuCompVascular=	models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT ,  related_name='usu15')
		ta=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		deposicion=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		glasgow=models.CharField(max_length=100, blank=False,null= False, editable=True)
		hematemesis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		hemotitis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		diuresis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		observaDiuresis=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		dolor=models.CharField(max_length=100, blank=False,null= False,  editable=True)
		observaDolor=models.CharField(max_length=50, blank=False,null= False, editable=True)
		drenes=models.CharField(max_length=50, blank=False,null= False, editable=True)
		observaDrenes=models.CharField(max_length=50, blank=False,null= False, editable=True)
		funcional=models.CharField(max_length=50, blank=False,null= False, editable=True)
		observaFuncional=models.CharField(max_length=50, blank=False,null= False,  editable=True)
		suturas=models.CharField(max_length=50, blank=False,null= False,  editable=True)
		observaSuturas=models.CharField(max_length=50, blank=False,null= False, editable=True)
		inmovilizacion=models.CharField(max_length=50, blank=False,null= False,  editable=True)
		observaInmovilizacion=models.CharField(max_length=50, blank=False,null= False,  editable=True)
		fechaRegistro = models.DateTimeField(editable=True, null=True, blank=True)
		usuarioRegistro = models.ForeignKey('planta.Planta', blank=True,null= True, editable=True, on_delete=models.PROTECT)
		estadoReg = models.CharField(max_length=1, default='A', editable=False)


                def __str__(self):
                    return str(self.id)


