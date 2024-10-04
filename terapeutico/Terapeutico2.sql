select * from clinico_historia;
select * from clinico_historiaexamenes;


select * from clinico_tiposexamen;
select * from clinico_examenes where nombre like ('%SOMA%');;

select exam.id examId,  exam."tiposExamen_id" tipoExamenId, tip.nombre tipoExamen, exam."codigoCups" CupsId , examenes.nombre nombreExamen,
exam.cantidad cantidad, exam.observaciones observaciones, exam."estadoExamenes_id" estado,historia.folio folio,
exam.interpretacion1 interpretacion1,exam.interpretacion2 interpretacion2, exam."medicoInterpretacion1_id" medicoInterpretacion1,
exam."medicoInterpretacion2_id" medicoInterpretacion2,exam."medicoReporte_id" medicoReporte, exam."rutaImagen" rutaImagen, exam."rutaVideo" rutaVideo


from clinico_historiaexamenes exam, clinico_historia historia, clinico_tiposexamen tip, clinico_examenes examenes
where historia.id= exam.historia_id and exam.historia_id = 236 and  tip.id=exam."tiposExamen_id" and exam."tiposExamen_id" = examenes."TiposExamen_id"
  And exam."codigoCups" = examenes."codigoCups";

select * from  clinico_historia where id= 236;
select * from clinico_examenesrasgos;
SELECT * FROM CLINICO_HISTORIArESULTADOS;
select * from clinico_historiaexamenes where id =127;
select * from clinico_estadoExamenes;
select * from clinico_tiposexamen;
select * from clinico_examenes where "codigoCups" = '871404'
update CLINICO_HISTORIArESULTADOS set  "examenesRasgos_id" = 6 where id = 1;
insert into CLINICO_HISTORIArESULTADOS (  "estadoReg" ,  "dependenciasRealizado_id" ,  "estadoExamenes_id" ,  "consecResultado" , 
 "examenesRasgos_id" ,  "fechaResultado" ,  "fechaServicio" ,    "historiaExamenes_id" ,  observaciones ,  valor )
values ('A',1,1,1,7,'2024-10-04 00:00:00','2024-10-04 00:00:00',127,'manual',45);

-- Query para rasgos 

select exam.id examId,  exam."tiposExamen_id" tipoExamenId, tip.nombre tipoExamen, exam."codigoCups" CupsId ,
 examenes.nombre nombreExamen,
exam.cantidad cantidad,rasgos.unidad unidad, exam.observaciones observaciones, exam."estadoExamenes_id" estado,
resul.valor valorResultado,rasgos.nombre nombreRasgo, rasgos.minimo minimo, rasgos.maximo maximo
from clinico_historiaexamenes exam, clinico_tiposexamen tip, clinico_examenes examenes, clinico_historiaresultados resul,
    clinico_examenesrasgos rasgos
where resul."historiaExamenes_id" = exam.id and exam.id = 127 and tip.id=exam."tiposExamen_id" and 
exam."tiposExamen_id" = examenes."TiposExamen_id"
 And exam."codigoCups" = examenes."codigoCups" AND resul."examenesRasgos_id" = rasgos.id  And exam."codigoCups" = rasgos."codigoCups";
 

-- Query para rasgos Acotado

detalle = 'select exam.id examId,  exam."tiposExamen_id" tipoExamenId, tip.nombre tipoExamen, exam."codigoCups" CupsId,examenes.nombre nombreExamen,exam.cantidad cantidad, exam.observaciones observaciones, exam."estadoExamenes_id" estado,resul.valor valorResultado,rasgos.nombre nombreRasgo, rasgos.minimo minimo, rasgos.maximo maximo from clinico_historiaexamenes exam, clinico_tiposexamen tip, clinico_examenes examenes, clinico_historiaresultados resul, clinico_examenesrasgos rasgos where resul."historiaExamenes_id" = exam.id and exam.id =' + "'" + str(valor) + "'" + ' and tip.id=exam."tiposExamen_id" and exam."tiposExamen_id" = examenes."TiposExamen_id" And exam."codigoCups" = examenes."codigoCups" AND resul."examenesRasgos_id" = rasgos.id  And exam."codigoCups" = rasgos."codigoCups"'


select * from usuarios_usuarios;
