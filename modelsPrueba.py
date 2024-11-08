-----------------------------------------------------------------------------------------------------------------------
--  TRIAGE
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
--  ADMISIONES
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
--  HISTORIA CLINICA
-----------------------------------------------------------------------------------------------------------------------


ojo --> Todo esto son horas y horas de camello. Work, Trabajop

1. Poder grabar una Admision (una vez guarde el nuevo usuario se pueda seguir la modal desaparezca y pueda crear correctamente una admision al igual con actualizar probar)
   se debe seguir con Furips, Triage, Ingreso a Triage (Probar trabajar con clases)
2. No eta UPDATE /INSERT de ls campos manilla, acompanatete, responsable remitido ips 
	                 empresa_id=empresaId,
                         ipsRemite_id = ipsRemite,
                         numManilla = numManilla,
                         contactoAcompanante_id = contactoAcompanante,
                         contactoResponsable_id = contactoResponsable,
3. Ojo recuerda los permisos punuales DESACTIVAR / INACTIVAR Botones
4. Ojo como genera el consecutivo de ingreso, tiene que NOO observar la sede o sea va a tener un consecutivo permanente, no pueden haber mas d eun consecutivo, o repetido
   son independientes de la sede , son ascendentes
-- ojo como carachas editas los existentes ???(ideas un link en html en la tabla y que llame una modal admisiones). Pero hay que ver que cambio es posible cambioar auqui ? Regimen?, num_manilla, remitido, ips_remite, empresa ???, responsable, acompañante, tipo de cotizante, muerte , defuncion, hclinica,fechaMuerte, causasMuerte,vias_deIngreso, viasdeegreso
        actadedefuncion, estadoSalida, especialidades, dx,  etc
-- Pues datos como usuaruio no se hacen aqui, contactos, tampoco se hacen aquip,
--Ojo que pasa con os estadorREg de todos los modelos ojop definir de una vez despues es inmanejable
7. ojo tengo quemado un centroc_id en 1 creo para que guarde la modal usuario (NO SE PORQUE)/ tambien en main, ausuario1 fecIngreso esta quemado 2024-01-01
8.  Creo crear programa autorizaciones con panelAutorizaciones y demas depronot un menuAutorizaciones para comenzar a diferenciar y yap todo
   con el estandard de programacion

Tablas = tblhcl_ingresos ( es la parte clinica del accidente)
Tablas= tbl_furips ( Es como la parte legal de datos)
Podria ser FuripsClinico, FuripsLegal
-- Acabo de detectar algo recontra DURO, los querys SQL, mundo aparte su complejidad es aparte de la armadura general del programa,.. No debe retrazar el desarrollo
   se deja hasta bun buen termino y se sigue con la armadura(desarrollo-software)

Terminar Clinico, buscar alog de farmacia, inventarios, compras

-- Ojo un usuario no puede tener dis (2) Triages
-- No me modifico el usuario creado desde la modal de triage-usuario. 
  -- Habitaciones (Mantenimiento)
  -- Hay que revisar Ingresos={}, poruqe hay dos diferentes querys y no puede actualziar
     en muchos de ellos la dependenciaActual_id. OJOOO 
   -- Colocar un control en guardar el cambio de servicio so no hay seleccionados datos en la ventana. para mantener robusta la Aplicacion..

   colocar mensaje bonito cuando no se escibe causa externa o diagnostico ojop
   busacar capturav ronum de la tabla laboratorios , creop en paneladmisiones ,    implementa delete no funciona en ambos lab-rayx
   el tiposFolio aun no funciona solo trae 1 , no he podido pailas 
   crear prioridad en clinico examenes y clinico_prioridad
   tiposfolio (Pendiente que guarde y no se bloquee no se que pasa)

   Para el lunes 16-sept

   1. create facturacion_facturacion, facturacion_facturacionDetalle, involucrar glosas
   2.   bajar anexosa tecnicos de glosas. Crear carpetasde anexos tecnicos
   4. crear historia-clinicos con form . Es el historial como un resumen de historia en pantalla de consulta
   5.que crajop pasa con las fechas-hora
   6. algo pasda con el grid de revsion de sistemas/historia clinica
   

-----------------------------------------------------------------------------------------------------------------------
--  TRIAGE, ADMISIONES - HISTORIA CLINICA
-----------------------------------------------------------------------------------------------------------------------

1  probar inser de clinicos
  cuando grabo se fuel por otra cosa y noreargo la pagina de ingresos clinicos ojop
  ojo No hay una dependencia llave foranea de la historia con el ingreso
5 ojo no funciona mensajeria cuando actualiza un trige 
  ojo no cierra la modal cuando acatualiza un triege
  ojo No me edita por nada la Admision para actualziar Mo encuentraAdmisonModal URL ???
10ojo como manejamos las habitacione triage, desocupamos ???
  ojo en historia clinica coge bien la fecha-hora de la historia , popruq en admisiones y panel nop ??? Nop. Validar
  ojo en admisiones cuando hay cambio de servicio y graba hay que hacer refresh del tablero de admisiones para que miestre el cambio o sino pailas , toca hacerlo manual  .. Umm verificar creo esta bien
  ojo ops en admisiones error al crear conveniop (se debe siempre tener seleccionado un convenio papabero)
   ojo obligar siempre a ingresar diagnosticos en HC .. Nop  validar
15 ojo cuando se ingresa diagnostico se desplaza hacia abajo se pierde presentacion
   OJO ARREGLA PANTALA PROC Noqx 2 renglones
   ojo pestaña antecedentes. revsistemas impiden acceso footer pagina
   ojo calcular numero dias en incapacidad y solo readonly el campo numDIas
   ojo la fecha-hora de signos vitales pailas  .. Nop fecha en signos vitales no deb ir es la fecha del folio
20 ojo verificar los medico consulta e interconsultado , creop esta mal
21 ojo Problemas error al guardar null en acompanantes y responsables
22 El mensaje no sale de responsable actualizao por cua ?.
23. Ojo hay un erro al cargar la paginma admisione. es en cambioServico.change se activa pero no hay sede , por cua? no hay sede?
24. Toca arregalr el tema de los ingresoIDxx, sedexx de acompanantes, responsable y abonos. ORGANIZAR bien

    PARA EL DIA LUNES 30 DE Septiembre . PILAS SEGUIR CON FURIPS Y TODO LO QUE FALTA DE INGRESOS/TRIAGE/HC

    No me marca o me selecciona el primer registro de la tabla en admiisones NOSE POR CUA
    Apenas arregle todo esto si crearFURIPs. Se debe crear enarticle copiao de crearadmisiones a bloc de notas , se maquilla con datos FURIPS, se envian combos alarticle y opcion guardar
   ojo. No actualizo el consecutivo al  maria paula en dependencias. ops supongo ops esta raro que cambio de servicoi o que paso ??, ops la tabla admisiones no
            tiene un sdo ingreso ops que paso ase activo el consecutovo cuando nop ops.
   ojo recuerde el boton crear responsables acompañante no ta creado hay que desarrollarlo
   para servicios en admisiones y de pronto clinico evaluar antes de seguir

   TAREAS HOY O MEJOR DIAS LUNES

   3. se debe subir la tabla cumm de rips a facturacion_suministros
   4. Es necesario atar los itmes de examens de la HClinica a la facturacion los del sistema. Los demas son ajustes o manuales No se ligan
   5. OJO PPILAS QUE UD. ESTA TRABAJANDO FURIPS (ya paso el parrentesis de rips , facturacion y glosas) . Hay que terminar primero admisiones-triage-histora clinica , luego si seguir
   6. Reorganizar la captura de la admision con los nuevos campos de rips ripsServiciosActual etc
   7. Comenzar a crear tablas cums, cups solidas las dfinitivas
   8. No me desaparecio la ventana  Modal .crear admison desde triage, el query de regreso Nop funciono mostraba en triage aun la persona
   9. Esta pendiente aun no abre la modal encuentraModal, para editar admision 
      Pendiente colocar el default de la fecha de nacimiento en usuarios.-
   11. el alto de la tabla pilas debe ser fijo para que funcione el scroll   
       trabajar sobbre DELETE,mensajes de error, presesntacion apoyo terapeutico
       Hay un problema con el delete de apoyo terapeutico RASGOS, por cua ?
       Falta colocar el nombre del paciente en respuestas apoyo terapeutico

       hoy
	1. indicadores (como enviarlo por load_ en ajax estos valores)
        2. delete terapeutico
        3. consulta resultados (solo falta al momento de ingresar selccinar un registro)
        4. furips
    

-----------------------------------------------------------------------------------------------------------------------
--  APOYO TERAPEUTICO 
-----------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------
--  MODELO TARIFARIO 
-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------
--  FACTURACION 
-----------------------------------------------------------------------------------------------------------------------
	-- Ojo en buscar examenes EN ADMIN error en buscar campo
        -- Ojo crear programa ( Query) que tomo un porcentaje de una tarifa ejempo SOAT - 10% y cree nuevo tarifario
        -- Ojo crear programa (Query) que tome toda la tarifa y lo copie a un convenio
        -- Ojo ops no hay forma de traer un convenio a una persona con TRIAGE ops, ERROR como arreglar???
        -- ojo en Apoyo terapeutico falta colocar el nombre del paciente, servicio, cama
        -- ojo en apoyp terapeutico cuando responden hacer la parte de factutracionm crear cabeza detalle con los datos
           que ingresan


       Mañana : -- formular a paula, medica, proc qx, etc
         
                -- Responder por apoyo teraputico lo uqe se pueda
                -- crear ventana liquidacion con datatables a liquidacion, liquidaciondetalle

  -- Procesos de Calculo para Tarifas (Se debe crear aplicativo, que actualize en tabla Tarifas , LiquidacionHonorarios)

        La tabla TarifasSuministros creo desaparece


	a) Se consulta el convenio del paciente y el tipo de tarifa que maneja el convenio del paciente
        b) Se va al detalle del convenio, se consulta el CUPS A calcular
           b) Si es SOAT

              Es cirugia : El liquidacionHonorarios se buscan los tiposhonorarios: medico,anestesiologo,audante
			   Se liquidan los Derechos de Sala
			   Se liquidan los materilaes de SUTURA
			   

	      No es cirugia: se busca en examenes el gruppoqx, se ubica en la tabla tarifas y en examenes se busca el grupoQx se actualzian salmingel minlegaño y valorSoat

	      Se liquidan los medicamentos
	      Se liquida el oxigeno
	
				 
 	   c) Si es ISS2001

	     Es cirugia : De acuerdo tabla HonorariosIss creo

                        Se liquidan el Honorario Profesional,, de acuerdo a la tabla HonorariosIss
			Se liquida el honorario Anestesilogo ,, de acuerdo a la tabla HonorariosIss
 			Se liquida el honorario Ayudante ,, de acuerdo a la tabla HonorariosIss
			Se liquidan Derechos de Sala, creo tabla liquidacionHonorarios
			Se liquida los materiales de sutura y curacion creo tabla de acuerdo a la tabla HonorariosIss y se graban en la tabla LiquidacionHonorarios
			Se liquida oxigeno  ??? Crear esto como un honorario

	    No es Cirugia, es Procedimiento

			Crea en la tabla Tarifas se consulta, se crea alli creo.-

 			  (Se busca en la tabla examenes, el codigoCups_id 
			   y se compara la cantidad de uvr del proced con minUvr, maxUvr de la tabla TarifasIss
                           y de acuerdo a cada tipo de honorario, se extracta el valor en uvr * el valoruvrAño y
                          de acuerdo a cada tipo de honorario y yap y se guarda en liquidacionHonorarios)



           Se liquidan los medicamentos , creo en la tabla Tarifas, pues sacamosTarifasSuministros
	   Se liquida el oxigeno, estop de donde ????



	   d) Particular


	      Si es cirugia

			 Es Honorario Profesional
			 Es honorario anestesiologo
			 Es honoraro ayudante
			 Es material de sautura y/o curacion
			 Es sala de Cirugia
			
			(Se busca en la tabla LiquidacionHonorarios el codigoCups_id de acuerdo a la tabla examenes
                        y ser guarda en liquidacionHonorarios y de acuerdo al tipo de honorario)
	     Si no es cirugia
			  (Se busca en la tabla tarifas.Tarifas el valorPropio)
                       
	   e) Propias

  			 Es Honorario Profesional
			 Es material de sautura y/o curacion
			 Es sala de Cirugia

			(Se busca en la tabla LiquidacionHonorarios el codigoCups_id de acuerdo a la tabla examenes
                         y de acuerdo al Valor se liquida y de acuerdo al tipo de honorario)

		  Si No existe Grupo Qx, o hay un valorPropio en la tabla Tarifas para el Cups en cuestion:	

			  (Se busca en la tabla tarifas.Tarifas el valorPropio)                  

  -- Procesos de Calculo para traer convenio - tarifa (Aqui ya esta todo calculado, solo es leer ele valor)

  -- Orden Procesos de Tarifacion , convenios , Soat, Iss

     Lo cups, el Grupo Qx Soat, Las uvr Iss estan en la tabla examenes, para Cups, 
     Los cums  para uvr Iss estan en la tabla FacturacionSuministros (medicamentos, materiales, sutura, etc)

	En tarifas_Tarifas van todas las tarifas, cups . Menos Honorarios
           tarifas_TarifasSuministros, Esmejor mtodos los suministros aquip, para no complicar
	   tarifas_GruposQx, grupos Qx Soat
           tarifas_TiposHonorarios, tipos honorarios
           tarifas_LiquidacionTarifasHonorarios Todos los honorarios ISS + SOAT y demas tipostarifa
	   tarifas_LiquidacionHonorarios (creo se debe borrar)
	   tarifas_HonorariosIss ( iss manual tarifario honoraros)
	   tarifas_HonorariosSoat (solo soat Honorarios manual tarifario)
           tarifas_Uvr valor de las uvr x Año
	   tarifas_TiposSalas
           tarifas_conceptosAfacturar (No creo que sirva a lo mejor borrar)

	ojo falta cuando se consulta un convenio coloque la vigenciaDesde , vigenciaHasta
	el window.reload() nop funciona cuando se graba y/o actualiza un coonvenio

        Mejorar la presicion de la presentacion de los convenios los datatables, titulos , etc
       

	-- Ojo arreglar conveniosHonorarios a base de if, else:
	-- Ojo PARON 
	-- ojo probar convenios liquidacionhonorariortarifas
      	-- Ojo en contratacion panel creo en suministro,honorario no se si proced hay UN </DIV> volado falta

	-- ojo el dia martes 12-nov 
           -- Crear TAB de facturacion
           -- Crear Anulacion de Facturas
           -- Crear Refacturacion
	-- hacer proba medicamentos (Aunque es mejor cuando se dispensa o despacha deberan caer a la facturacion), noqx facturacion automatica
       -- ojop ver facturacion automatico de No qx
       -- El proceso de facturacion cuando crea la factura crtear boton de impresion de factura y que devuelva el numero de la factura a IMPRIMIR
        -- OJO hay que refrescar los totales. Crear funcion totales javascript
          -- datarablke de abonos esta muy grande arreglar
         -- arreglar el delete de abosno/pagos marcarlos con 'N' de ANULADO como se hizpo con liquidacion
         -- 
		

-----------------------------------------------------------------------------------------------------------------------
--  GLOSAS
-----------------------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------------------
--  RIPS 
-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------
--  REMISIONES 
-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------
--  RADICACIONES
-----------------------------------------------------------------------------------------------------------------------






