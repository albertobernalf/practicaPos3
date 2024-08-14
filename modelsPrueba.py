TIPS THE WORK

-- PARTE I ADMISIONES - ADMINISTRATIVA  - FACTURACION

-- OJO EL DIA LUNES 8/07
En facturacion:
0.1 Tarifas (id, nombre,  convenioId, conceptoId, tipo, codigoCups, codigoSuministro, valor, grupoQx, paquete, Honorarios)
0.1.1 TiposTarifa(id, nombre ) EPS, ENTE TERRITORIAL Particular, Iss, soat, otros
0.2 TiposTarifa(id,nombre)  EPS,SOAT, ISS, ENTE TERRITORIAL, IPS, ARL, PARTICULAR)
0.11 FormasLiquidacion : (id, nombe,  Codigo,tipoCruento ,caracteristica, valorHonorario,tiposHonorarios,cuentaContable,centroCosto)

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

El lunes 22.

Terminar Clinico, buscar alog de farmacia, inventarios, compras

subir tablas, buscar ultimas tablas mipres 2024
-- segiir con mejoras presente chivo
-- Probar portar a una nueva instalacion

-- Ojo deja  grabar una cedula, documento en dos dependencias a la vez, controlar esop.
-- Los filtros del triage no funcionan VERIFICAR

-- Ojo un usuario no puede tener dis (2) Triages
-- OJOOO el ingreso de una Admision debe ser agil, veloz se debe arreglar el ingreso de acompanantes y de responsables de la cuenta . deben de quedar en las misma captura de la admision
   no en mas opciones.- (PRoPUESTAS) y si se crean nuevas ventanas modales para acompanantes, responsbles y empresas ???. Sera muy verraco crear tablas para solucionar esto en las modales asi :
   tabla de conveniosPacienteIngresos, tabla contactos (crea un contacto), tabla responsables. Yo creo que es mejor crear unas tablas dentro d ela modal que ingreses los datos y se van 
   a guardar en las tablas de usuarios_contactos (responsabe y contacto) y para el convenio es mas verraco, nop simplemente en otro lugar se crea la empresa para el paciente(usuario) y
   aqui en la tabla simplemente lo asocia parta pa la grabacion del convenioo de la empresa.-


-- ojo con los filtros d ebusqueda triage no estan funcionando
-- Ojo cuando edito una modal triage y cambio clasificacion no la graba
-- Ojo al editar la ventana modal triage se piederde profesional , nombreSede ??? ojo no se pueden perder estos valores basicos para el manejo d ela aplicacion
-- falta tener en cuenta clasificacion_triage, porque el combo al ser seleccionado no cambia ni graba el valor escogido por el usuario ???'
-- Ojo que paso al crear una admision no pone bien los subserviicios /habitaciones que paso si estaba funcionando.
-- Al crear un triage No refresca el listado de triages
-- Al crear un triage y colocar el numero del paciente en la ventana no cumple cabalmente el foco la ventana de modal usuario ver que pasa