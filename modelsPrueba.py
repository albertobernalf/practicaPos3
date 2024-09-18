TIPS THE WORK

-- PARTE I ADMISIONES - ADMINISTRATIVA  - FACTURACION

En facturacion:

0.11 FormasLiquidacion : (id, nombe,  Codigo,tipoCruento ,caracteristica, valorHonorario,tiposHonorarios,cuentaContable,centroCosto)


0.12 Tabla Facturacion : (id, tipoDoc,documento, consecAdmision,factura, fechaFactura,codigoDian, convenio, totalCopagos, totalCuotaModeradora,totalProcedimientos, totalSuministros, totalFactura, valorApagar, valorAPagarLetras, anulado, fechaCorte,cufeDefinitico,cufeValor,codigoQr, rutaQr, totalNotasDebito, totalnotasCredito, rutaXml,estadoEnvioDyan, tipoFacturaDyan, desbloqueada, rutaPdf, verLiquidacion, envioCorreo, anticipos, usuarioAnula, detalleAnulacion, fechaAnulacion,  observaciones, usuarioRegistra ,fechaRegistro)
0.13 tabla FacturacionDetalle : (id, tipoDoc,documento, consecAdmision, liquidacion, consecutivo, fecha, tarifa, codigoCups, cantidad, valorUnitario, valorTotal, registro, cirugia, tipoHonorario, grupoQx, grupoQxUvr, fechaCrea, usuarioCrea, fechaModifica, usuarioModifica,  observaciones, estadoRegistro,numeroglosa, cantidadGlosada, valorGlosado, cantidadAceptada , valorAceptado,, cantidadRechazada, valorRechazado)

0.14 tabla Liquidacion : (id, tipoDoc,documento, consecAdmision, fecha, convenio, totalCopagos, totalCuotaModeradora,totalProcedimientos, totalSuministros, totalFactura, valorApagar, anulado, fechaCorte,cr,codigoQr, rutaQr, totalNotasDebito, totalnotasCredito,  tipoFacturaDyan, desbloqueada,  verLiquidacion,  anticipos, usuarioAnula, detalleAnulacion, fechaAnulacion,  observaciones, usuarioRegistra ,fechaRegistro)
0.15 tabla LiquidacionDetalle : (id, tipoDoc,documento, consecAdmision, liquidacion, consecutivo, fecha, tarifa, codigoCups, cantidad, valorUnitario, valorTotal, registro, cirugia, tipoHonorario, grupoQx, grupoQxUvr, fechaCrea, usuarioCrea, fechaModifica, usuarioModifica,  observaciones, estadoRegistro  ,usuarioRegistra ,fechaRegistro)
0.16 tabla Refacturacion : (id, tipoDoc,documento, consecAdmision, fecha,facturaInicial, facturaFinal ,estadoRegistro  ,usuarioRegistra ,fechaRegistro)

0.17 tabla Remisiones(cartera)
0.18 tabla Radicaciones(cartera)


0.19 tabla Rips
0.20 tabla RipsDetalle



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
        
-- No graba num_manilla, remitido
-- ojo como carachas editas los existentes ???(ideas un link en html en la tabla y que llame una modal admisiones). Pero hay que ver que cambio es posible cambioar auqui ? Regimen?, num_manilla, remitido, ips_remite, empresa ???, responsable, acompañante, tipo de cotizante, muerte , defuncion, hclinica,fechaMuerte, causasMuerte,vias_deIngreso, viasdeegreso
        actadedefuncion, estadoSalida, especialidades, dx,  etc
    -- Pues datos como usuaruio no se hacen aqui, contactos, tampoco se hacen aquip,
--Ojo que pasa con os estadorREg de todos los modelos ojop definir de una vez despues es inmanejable

-- OJOP:
1. hilo de performance llenar tabla ingresos con 500000 registors o los mismo que tienen actualmente imhotep (para realizar consultas-filtros)
3. reorganizar los context para cada caso ahorrar memoria -cpu vien organizadito el codigo

FIN 15/julio

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



9. PENDIENTES (facturacion mae_topsesoat(Facturacion), (mae_tarifasqx(Contratacion),mae_tarifasSoat(Contratacion), 
	
Tablas = tblhcl_ingresos ( es la parte clinica del accidente)
Tablas= tbl_furips ( Es como la parte legal de datos)
Podria ser FuripsClinico, FuripsLegal
Mas la tabla normal de las evoluciones Clinicas
Ideas: ir backup de tablas sep

-- Acabo de detectar algo recontra DURO, los quetys SQL, mundo aparte su complejidad es aparte de la armadura general del programa,.. No debe retrazar el desarrollo
   se deja hasta bun buen termino y se sigue con la armadura(desarrollo-software)


El lunes 22.

Terminar Clinico, buscar alog de farmacia, inventarios, compras

subir tablas, buscar ultimas tablas mipres 2024
-- Probar portar a una nueva instalacion
-- Ojo un usuario no puede tener dis (2) Triages
-- cuandor creo una admision desde triage no me desaparece la ventana modal ??? /mymodal.hide() , ver si estop funcionap NO FUNCIONA DE PRONTO QUITAR WINDOW.RELOAD()/ 
  nota: definitivamente no la cierra ops por cua sera? investigar
-- ops otra vuelta se pierden los combos de de servicio y subservicio y habita en la edicion de la modal triage pero cuando he dado vueltas por la creacion
   de usuarios antes. Pero si entramos en una a triage y luego edicion no hay problema, es por paso de variables entre aplicaciones 
   Ops Verificar ....

-- No me modifico el usuario creado desde la modal de triage-usuario. 
-- Ojo se creo una modal de cambioServicioModal,  pero es mejor no hacerlo por modal sino en el article html pagina


--  IMPORTANTE VER COMO NO HAYA QUE CREAR UN CLICK QUE SEA AUTOMATICO por que si no ñucas cambioservico por ejemplo
 
-- La otra semana crear :
   -- Habitaciones (Mantenimiento)
  -- Hay que revisar Ingresos={}, poruqe hay dos diferentes querys y no puede actualziar
     en muchos de ellos la dependenciaActual_id. OJOOO 
   -- Colocar un control en guardar el cambio de servicio so no hay seleccionados datos en la ventana. para mantener robusta la Aplicacion..

-- ojo no edita la Admision Ver mañana JUEVES

-- Ojo mañana miercoles 05-sepr

   colocar mensaje bonito cuando no se escibe causa externa o diagnostico ojop
   porque l¿el datatable de rx diferente de laborat, no ingresa filas en blanco y no bonito // UNIFICAR PRESENTACION
   busacar capturav ronum de la tabla laboratorios , creop en paneladmisiones ,    implementa delete no funciona en ambos lab-rayx
   el tiposFolio aun no funciona solo trae 1 , no he podido pailas 
   el causaexterna or diagnosticos ='' No funciona
   crear prioridad en clinico examenes y clinico_prioridad
   tiposfolio (Pendiente que guarde y no se bloquee no se que pasa)

   Para el lunes 16-sept

   1. create facturacion_facturacion, facturacion_facturacionDetalle, involucrar glosas
   2.   bajar anexosa tecnicos de glosas. Crear carpetasde anexos tecnicos
   3. crear datatable medicamentos
   4. crear historia-clinicos con form . Es el historial como un resumen de historia en pantalla de consulta
   5.que crajop pasa con las fechas-hora
   6. algo pasda con el grid de revsion de sistemas/historia clinica
   

--  mañana jueves 19


  probar inser de clinicos
  cuando grabo se fuel por otra cosa y noreargo la pagina de ingresos clinicos ojop
  ojo No hay una dependencia llave foranea de la historia con el ingreso
  ojo al crear triage y crear modal usuario no carga la modal usuario
  ojo no funciona mensajeria cuando actualiza un trige 
  ojo no cierra la modal cuando acatualiza un triege
  ojo erro busqueda en moculo admisiones por nombre de medico
  ojo No me edita por nada la Admision para actualziar Mo encuentraAdmisonModal URL ???
  OJO EN BUSTEQUDA POR NOMBRE DE PACIENTE no funciona EN ADMISIONES
  ojo CUANSO CREE LA ADMISION ME DUPLICO LA CONSULTA verificar comando = al crear admisin
  ojo ops hay un eror en la vieww de admisiones linea 4388 se pierde un id
  ojo arreglar pantalla crear admision marco, margenes
  ojo al crear triage algo pasa con lops campos nulos creo los integerfield m, noa acpeta algo pasa
  ojo en historia clinica coge bien la fecha-hora de la historia , popruq en admisiones y panel nop ???
  ojo en historia clinica no devuelve  a la pantalla principal cuando graba la hclinica
  ojo obligar siempre a ingresar diagnosticos en HC
  ojo no esta grabando la dosisUnidad_id en formulacion
  ojo en admisiones cuando hay cambio de servicio y graba hay que hacer refresh del tablero de admisiones para que miestre el cambio o sino pailas , toca hacerlo manual
  ojo ops en admisiones error al crear conveniop (se debe siempre tener seleccionado un convenio papabero)


