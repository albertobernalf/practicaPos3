
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
   se debe seguir con Furips, Triage, Ingreso a Triage (Probar trabajar con clases)
2. No eta UPDATE /INSERT de ls campos manilla, acompanatete, responsable remitido ips 
	                 empresa_id=empresaId,
                         ipsRemite_id = ipsRemite,
                         numManilla =numManilla,
                         contactoAcompanante_id = contactoAcompanante,
                         contactoResponsable_id = contactoResponsable,
3. Ojo recuerda los permisos punuales DSACTIVAR / INACTIVAR Botones
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
-- Acabo de detectar algo recontra DURO, los quetys SQL, mundo aparte su complejidad es aparte de la armadura general del programa,.. No debe retrazar el desarrollo
   se deja hasta bun buen termino y se sigue con la armadura(desarrollo-software)

Terminar Clinico, buscar alog de farmacia, inventarios, compras

-- Ojo un usuario no puede tener dis (2) Triages
-- No me modifico el usuario creado desde la modal de triage-usuario. 
  -- Habitaciones (Mantenimiento)
  -- Hay que revisar Ingresos={}, poruqe hay dos diferentes querys y no puede actualziar
     en muchos de ellos la dependenciaActual_id. OJOOO 
   -- Colocar un control en guardar el cambio de servicio so no hay seleccionados datos en la ventana. para mantener robusta la Aplicacion..

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
   
RIPS:
numero de contrato
numero de poliza
modalidad de contratacion y pago
cobertura o plan de beneficios

-- Para consultas :

modalidadGrupoServicioTecSal": "09",
"grupoServicios": "01",
"codServicio": 1,
"finalidadTecnologiaSalud": "11",

- para procedimientos

"viaIngresoServicioSalud": "01",
"modalidadGrupoServicioTecSal": "01",
"grupoServicios": "04",
"codServicio": 123,
"finalidadTecnologiaSalud": "44",

-- UrgenciAS CON OBSERVAQCION
   No tiene
-- HOSPITALIZACION
"viaIngresoServicioSalud": "02",
-- RECIEN NACIDO 
   NO TIENE
-- MEDICAMNETOS
   MIPRES


-----------------------------------------------------------------------------------------------------------------------
--  TRIAGE, ADMISIONES - HISTORIA CLINICA
-----------------------------------------------------------------------------------------------------------------------

1  probar inser de clinicos
  cuando grabo se fuel por otra cosa y noreargo la pagina de ingresos clinicos ojop
  ojo No hay una dependencia llave foranea de la historia con el ingreso
  ojo al crear triage y crear modal usuario no carga la modal usuario
5 ojo no funciona mensajeria cuando actualiza un trige 
  ojo no cierra la modal cuando acatualiza un triege
  ojo No me edita por nada la Admision para actualziar Mo encuentraAdmisonModal URL ???
  ojo ops hay un eror en la vieww de admisiones linea 4388 se pierde un id
10ojo como manejamos las habitacione triage, desocupamos ???
  ojo en historia clinica coge bien la fecha-hora de la historia , popruq en admisiones y panel nop ??? Nop. Validar
  ojo en admisiones cuando hay cambio de servicio y graba hay que hacer refresh del tablero de admisiones para que miestre el cambio o sino pailas , toca hacerlo manual  .. Umm verificar creo esta bien
  ojo ops en admisiones error al crear conveniop (se debe siempre tener seleccionado un convenio papabero)
   ojo obligar siempre a ingresar diagnosticos en HC .. Nop  validar
15 ojo cuando se ingresa diagnostico se desplaza hacia abajo se pierde presentacion
   ojo SIGNOS VITALES POBNER CALENDARIO FECHA
   OJO ARREGLA PANTALA PROC Noqx 2 renglones
   ojo pestaña antecedentes. revsistemas imiden acceso footer pagina
   ojo calcular numero dias en incapacidad
20 ojo la fecha-hora de signos vitales pailas
   ojo verificar los medico consulta e interconsultado , creop esta m,al


  
-----------------------------------------------------------------------------------------------------------------------
--  APOYO TERAPEUTICO - FACTURACION
-----------------------------------------------------------------------------------------------------------------------
