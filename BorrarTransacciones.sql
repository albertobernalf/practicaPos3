select * from facturacion_liquidacion;

select pag.id id, pag.fecha, pag.consec, pag.valor, pag.descripcion, pag."estadoReg", pag."tipoPago_id" , pag."formaPago_id", 
 pag.saldo, pag."totalAplicado", pag."valorEnCurso" 
FROM cartera_pagos pag where pag.id = '54'

SELECT pag.id id , i."tipoDoc_id" tipoDoc , i.documento_id documentoId ,u.documento documento,u.nombre nombre,i.consec consec ,
 tipdoc.nombre nombreDocumento , cast(date(pag.fecha) as text)  fecha, pag."tipoPago_id" tipoPago , pag."formaPago_id" formaPago,
 pag.valor valor, pag.descripcion descripcion ,tip.nombre tipoPagoNombre,forma.nombre formaPagoNombre,
 pag."totalAplicado" totalAplicado, pag.saldo saldo , pag."estadoReg" estadoReg, pag."valorEnCurso"  valorEnCurso
 FROM admisiones_ingresos i, cartera_pagos pag ,usuarios_usuarios u ,usuarios_tiposdocumento tipdoc, cartera_tiposPagos tip,
 cartera_formasPagos forma
 WHERE i.id = 50095 and i.documento_id = u.id and i."tipoDoc_id" = pag."tipoDoc_id" and i.documento_id  = pag.documento_id and 
 i.consec = pag.consec AND tipdoc.id = i."tipoDoc_id" and pag."tipoPago_id" = tip.id and pag."formaPago_id" = forma.id 
ORDER BY pag.fecha desc

select * FROM cartera_pagos pag where pag.id = '54'

select * from clinico_historia order by id;
select * from clinico_historiaexamenes where historia_id = 543 order by id;
 select * from clinico_historiaexamenes order by id

select * from clinico_examenes where "codigoCups" in ('908501','875603')

-- delete from clinico_historiaresultados; -- ok
-- delete from clinico_historiaexamenes;  -- ok

-- delete from facturacion_refacturacion; -- ok
-- delete from facturacion_facturaciondetalle; -- ok
-- delete from facturacion_liquidaciondetalle; -- ok
 -- delete from facturacion_liquidacion; -- ok
-- delete from facturacion_facturacion; -- ok
-- delete from facturacion_facturaciondetalle; -- ok
-- delete from clinico_historialantecedentes; -- ok
-- delete from clinico_historialdiagnosticos; -- ok
-- delete from clinico_historialincapacidades; -- ok
-- delete from clinico_historialinterconsultas; -- ok
-- delete from clinico_historiamedicamentos; -- ok
-- delete from clinico_historiaoxigeno; -- ok
-- delete from clinico_historiarevisionsistemas; --ok
-- delete from clinico_historiasignosvitales; --ok
-- delete from clinico_historiarevisionsistemas; --ok
-- delete from clinico_historia; --ok
-- delete from sitios_historialdependencias; --ok
-- update sitios_dependencias set "tipoDoc_id" = null, documento_id=null,consec = null,"fechaLiberacion"=null,"fechaOcupacion"=null,disponibilidad='L' --ok
-- delete from cartera_pagos; --ok
-- delete from admisiones_furips; --ok
-- delete from admisiones_ingresos; -- ok
-- delete from triage_triage - ok
-- delete from facturacion_conveniospacienteingresos;
-- delete from facturacion_conveniospaciente;





