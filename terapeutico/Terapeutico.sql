select * from admisiones_ingresos;
select * from facturacion_conveniospacienteingresos;
select * from usuarios_usuarios;

update usuarios_usuarios 
set nombre = 'nuevo4Modificado', direccion  = 'Cr 21 N° 169 15/25 Bodega 2', genero = 'M', "fechaNacio" = '2024-10-02T10:34', 
telefono= '7442565', contacto= 'totottito', "centrosC_id"= '1', "tiposUsuario_id" = '3' ,  
municipio_id = 2, localidad_id = 1, "estadoCivil_id"= ., ocupacion_id = 2, correo = 'astrid@yahoo.com.co' 
WHERE "tipoDoc_id" = 1 AND documento = '194656734'

select * from triage_triage;
select * from clinico_historiamedicamentos;
select * from clinico_historia order by id;


SELECT  i.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", 
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual 
FROM admisiones_ingresos i, usuarios_usuarios u,
 sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag 
, sitios_serviciosSedes sd 
WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND 
i."sedesClinica_id" = '1' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND 
dep.disponibilidad = 'O' AND i."salidaDefinitiva" = 'N' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and 
u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and 
dep.id = i."dependenciasActual_id" 
UNION 
SELECT t.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , 
cast('0001-01-01 00:00:00' as timestamp) fechaSalida,
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual 
FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, 
clinico_servicios ser 
WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND 
t."sedesClinica_id" = '1' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND 
t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and 
t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and 
t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and 
dep."documento_id" = t."documento_id" and ser.nombre = 'TRIAGE'

select documento_id, "tipoDoc_id",* from clinico_historia where id = 231;
select * from clinico_historiaexamenes where historia_id = 231; -- + folio y examen nombre y fECHAORDENADO Y ESTADO EXAMEN

SELECT * FROM clinico_tiposexamen;
select * from clinico_estadoexamenes;
select * from clinico_examenes;
select * from usuarios_usuarios

--  Aqui la parte TERAPEUTICA

-- 1er Query

SELECT  i.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", 
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual ,
    historia.fecha fechaExamen,
    tipoExa.nombre,exam.nombre ,estadosExam.nombre,histoexa.consecutivo,histoexa."codigoCups", histoexa.cantidad, 
    histoexa.observaciones, historia.folio
FROM admisiones_ingresos i, usuarios_usuarios u,
 sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag 
, sitios_serviciosSedes sd , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,
  clinico_historia historia, clinico_estadoexamenes estadosExam
WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND 
i."sedesClinica_id" = '1' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND 
dep.disponibilidad = 'O' AND i."salidaDefinitiva" = 'N' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and 
u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and 
dep.id = i."dependenciasActual_id"
AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id 
AND i.consec = historia."consecAdmision"
AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" 
AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO'



-- 2do Query

select * from triage_triage;

SELECT t.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , 
cast('0001-01-01 00:00:00' as timestamp) fechaSalida,
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual ,
    historia.fecha fechaExamen,
    tipoExa.nombre,exam.nombre ,estadosExam.nombre,histoexa.consecutivo,histoexa."codigoCups", histoexa.cantidad, 
    histoexa.observaciones, historia.folio
FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,
sitios_serviciosSedes sd, clinico_servicios ser , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,
  clinico_historia historia, clinico_estadoexamenes estadosExam
WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND 
t."sedesClinica_id" = '1' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND 
t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and 
t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and 
t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and 
dep."documento_id" = t."documento_id" and ser.nombre = 'TRIAGE'
AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id 
AND t."consecAdmision" = historia."consecAdmision"
AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" 
AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO'


-- Aqup query total
 

SELECT  i.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", 
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual ,
    historia.fecha fechaExamen,
    tipoExa.nombre tipoExamen ,exam.nombre examen ,estadosExam.nombre estadoExamen ,histoexa.consecutivo consecutivo,histoexa."codigoCups" cups, histoexa.cantidad cantidad, 
    histoexa.observaciones observa, historia.folio folio
FROM admisiones_ingresos i, usuarios_usuarios u,
 sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag 
, sitios_serviciosSedes sd , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,
  clinico_historia historia, clinico_estadoexamenes estadosExam
WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND 
i."sedesClinica_id" = '1' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND 
dep.disponibilidad = 'O' AND i."salidaDefinitiva" = 'N' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and 
u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and 
dep.id = i."dependenciasActual_id"
AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id 
AND i.consec = historia."consecAdmision"
AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" 
AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO'
UNION
SELECT t.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , 
cast('0001-01-01 00:00:00' as timestamp) fechaSalida,
ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual ,
    historia.fecha fechaExamen,
    tipoExa.nombre tipoExamen,exam.nombre examen,estadosExam.nombre estadoExamen,histoexa.consecutivo consecutivo,histoexa."codigoCups" cups, histoexa.cantidad cantidad, 
    histoexa.observaciones observa , historia.folio folio
FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,
sitios_serviciosSedes sd, clinico_servicios ser , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,
  clinico_historia historia, clinico_estadoexamenes estadosExam
WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND 
t."sedesClinica_id" = '1' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND 
t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and 
t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and 
t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and 
dep."documento_id" = t."documento_id" and ser.nombre = 'TRIAGE'
AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id 
AND t."consecAdmision" = historia."consecAdmision"
AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" 
AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO'
 

-- De aquip en adelante maquillado

    detalle = 'SELECT ' + "'" + str("INGRESO") + "'" +  ' tipoIng, i.id'  + "||" +"'" + '-INGRESO' + "'" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id" UNION SELECT ' + "'"  + str("TRIAGE") + "'" + ' tipoIng, t.id'  + "||" +"'" + '-TRIAGE' + "'" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'"


-- Este seria

    detalle = 'SELECT ' + "'" + str("INGRESO") + "'" +  ' tipoIng, i.id'  + "||" +"'" + '-INGRESO' + "'" + ' i.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida",ser.nombre servicioNombreIng, dep.nombre camaNombreIng ,diag.nombre dxActual ,historia.fecha fechaExamen,tipoExa.nombre,exam.nombre ,estadosExam.nombre,histoexa.consecutivo,histoexa."codigoCups", histoexa.cantidad,histoexa.observaciones, historia.folio FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa, clinico_historia historia, clinico_estadoexamenes estadosExam WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" +' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + str('O') + "'" + ' AND i."salidaDefinitiva" = 'N' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id" AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id AND i.consec = historia."consecAdmision" AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = ' + "'" + str('ORDENADO') + "'" + ' UNION SELECT ' + "'"  + str("TRIAGE") + "'" + ' tipoIng, t.id'  + "||" +"'" + '-TRIAGE' + "'" + ' SELECT t.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual , historia.fecha fechaExamen,tipoExa.nombre,exam.nombre ,estadosExam.nombre,histoexa.consecutivo,histoexa."codigoCups", histoexa.cantidad,     histoexa.observaciones, historia.folio FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,  clinico_historia historia, clinico_estadoexamenes estadosExam WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'" + ' AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id AND t."consecAdmision" = historia."consecAdmision" AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = ' + "'" + str('ORDENADO') +  "'"



-- Qury como quedop

SELECT 'INGRESO' tipoIng, i.id||'-INGRESO', i.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida",ser.nombre servicioNombreIng, dep.nombre camaNombreIng ,diag.nombre dxActual ,historia.fecha fechaExamen,tipoExa.nombre tipoExamen ,exam.nombre examen ,estadosExam.nombre estadoExamen ,histoexa.consecutivo consecutivo,histoexa."codigoCups" cups, histoexa.cantidad cantidad, histoexa.observaciones observa, historia.folio folio FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa, clinico_historia historia, clinico_estadoexamenes estadosExam WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = '1' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = 'O' AND i."salidaDefinitiva" = 'N'  and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id" AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id AND i.consec = historia."consecAdmision" AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO' UNION SELECT 'TRIAGE' tipoIng, t.id||'-TRIAGE', t.id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast('0001-01-01 00:00:00' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , '' dxActual , historia.fecha fechaExamen,    tipoExa.nombre tipoExamen,exam.nombre examen,estadosExam.nombre estadoExamen,histoexa.consecutivo consecutivo,histoexa."codigoCups" cups, histoexa.cantidad cantidad, histoexa.observaciones observa , historia.folio folio  FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser , clinico_tiposexamen tipoExa,  clinico_examenes exam, clinico_historiaexamenes histoexa,  clinico_historia historia, clinico_estadoexamenes estadosExam WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = '1' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = 'TRIAGE' AND u."tipoDoc_id" = historia."tipoDoc_id" AND u.id = historia.documento_id AND historia.id = histoexa.historia_id AND t."consecAdmision" = historia."consecAdmision" AND histoexa."tiposExamen_id" = tipoExa.id and  histoexa."tiposExamen_id" = exam."TiposExamen_id" and histoexa."codigoCups" = exam."codigoCups" AND histoexa."estadoExamenes_id" = estadosExam.id AND estadosExam.nombre = 'ORDENADO'
