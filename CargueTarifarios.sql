select * from tarifas_tarifassuministros where "tipoTarifa_id"=5;
update tarifas_tarifassuministros set concepto_id =6 where "tipoTarifa_id"=5;
select * from contratacion_conveniossuministros;
select * from contratacion_convenioSPROCEDIMIENTOS

select * from facturacion_suministros where id =  616;
select * from facturacion_conceptos

select * from contratacion_conveniossumnistros;

SELECT * FROM TARIFAS_TIPOSTARIFA;
select * from contratacion_convenios

-- honor

select id,"tipoHonorario_id", "tipoSalas_id",descripcion,"minUvr", "maxUvr", valor, *
from tarifas_honorariosiss 
order by "tipoHonorario_id";




select "codigoCups", nombre, "cantidadUvr", "uvrAño_id","grupoQx_id",  * from clinico_examenes  where id <=  1600 order by "codigoCups" ;

update clinico_examenes set "grupoQx_id" = 5 , "uvrAño_id" = 1 where nombre <= 'C';

update clinico_examenes set "grupoQx_id" = 12 , "uvrAño_id" = 1   where nombre > 'C' and nombre <= 'H';

update clinico_examenes set "grupoQx_id" = 17 , "uvrAño_id" = 1   where nombre > 'I' and nombre <= 'M';

update clinico_examenes set "grupoQx_id" = 23 , "uvrAño_id" = 1  where nombre > 'M' and nombre <= 'Z'

select * from tarifas_GruposQx;

select * from tarifas_liquidaciontarifashonorarios;

update tarifas_honorariosiss set "tipoSalas_id" = 10  WHERE id in (15);

select * from tarifas_tipossalas;
select * from tarifas_tiposHonorarios;

select * from tarifas_liquidaciontarifashonorarios;

select id,"grupoQx_id", "tipoHonorario_id", "tipoSalas_id",descripcion, valor, *
from tarifas_HonorariosSoat 
order by "tipoHonorario_id", "grupoQx_id";

select "codigoCups", nombre, "cantidadUvr", "uvrAño_id","grupoQx_id",  * from clinico_examenes order by "grupoQx_id" --  where id <=  1600 order by "codigoCups" ;
-- 3876 / 9787


select * from contratacion_liquidaciontarifashonorarios ;
-- Carque SOAT

INSERT INTO tarifas_liquidaciontarifashonorarios ("codigoHomologado",descripcion,valor,"fechaRegistro","estadoReg", "codigoCups_id", "codigoSuministro_id",
               "tipoHonorario_id", "tipoTarifa_id","usuarioRegistro_id")
select 'yyyy',exa.nombre,soat.valor,'2024-10-30 00:00:00','A',exa.id,null,soat."tipoHonorario_id",1,1
from clinico_examenes exa,tarifas_HonorariosSoat soat
where exa."grupoQx_id" = soat."grupoQx_id" and soat."tipoHonorario_id"=1 -- 3482
order by exa.nombre
-- group by exa.nombre,soat.valor,exa.id,soat."tipoHonorario_id"

-- Carque ISS
select id,"tipoHonorario_id", "tipoSalas_id",descripcion,"minUvr", "maxUvr", valor, *
from tarifas_honorariosiss 
order by "tipoHonorario_id";

select "codigoCups", nombre, "cantidadUvr", "uvrAño_id","grupoQx_id",  * from clinico_examenes order by "cantidadUvr"

update clinico_examenes set "cantidadUvr" = 31 , "uvrAño_id" = 1 where nombre <= 'C';
update clinico_examenes set "cantidadUvr" = 42 , "uvrAño_id" = 1   where nombre > 'C' and nombre <= 'H';
update clinico_examenes set "cantidadUvr" = 18 , "uvrAño_id" = 1   where nombre > 'I' and nombre <= 'M';
update clinico_examenes set "cantidadUvr" = 25 , "uvrAño_id" = 1  where nombre > 'M' and nombre <= 'Z'



INSERT INTO tarifas_liquidaciontarifashonorarios ("codigoHomologado",descripcion,valor,"fechaRegistro","estadoReg", "codigoCups_id", "codigoSuministro_id",
               "tipoHonorario_id", "tipoTarifa_id","usuarioRegistro_id")
select 'hhhh',exa.nombre,iss.valor,'2024-10-30 00:00:00','A',exa.id,null,iss."tipoHonorario_id",5,1
from clinico_examenes exa,tarifas_honorariosiss iss
where iss."tipoTarifa_id"=5  and "tipoHonorario_id" <= 3 and exa.id in (2073,2074,2075,2115,1601,1602,1603,1604,1605,1606,1607)-- 3482
order by exa.nombre -- 6030 registros


select * from tarifas_honorariosiss; 
select * from tarifas_liquidaciontarifashonorarios order by "tipoHonorario_id"

select * from contratacion_conveniosliquidaciontarifashonorarios


