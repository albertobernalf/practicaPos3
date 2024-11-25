from django.shortcuts import render
import json
from django import forms
import cv2
import numpy as np
from django.core.serializers import serialize
from django.db.models.functions import Cast, Coalesce
from django.utils.timezone import now
from django.db.models import Avg, Max, Min, Sum

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.http import JsonResponse
import MySQLdb
import pyodbc
import psycopg2
import json 
import datetime
from decimal import Decimal
from admisiones.models import Ingresos
from facturacion.models import ConveniosPacienteIngresos, Liquidacion, LiquidacionDetalle, Facturacion, FacturacionDetalle
from cartera.models import TiposPagos, FormasPagos, Pagos, PagosFacturas
from triage.models import Triage
from clinico.models import Servicios

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Type not serializable")

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 



# Create your views here.
def load_dataLiquidacion(request, data):
    print ("Entre load_data Liquidacion")

    context = {}
    d = json.loads(data)

    username = d['username']
    sede = d['sede']
    username_id = d['username_id']

    nombreSede = d['nombreSede']
    print ("sede:", sede)
    print ("username:", username)
    print ("username_id:", username_id)
    

    #print("data = ", request.GET('data'))

    # Combo Indicadores

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
    curt = miConexiont.cursor()


    comando = 'SELECT ser.nombre, count(*) total FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd  WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + str('O') + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' and tp.id = u."tipoDoc_id" and  i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"  group by ser.nombre UNION SELECT ser.nombre, count(*) total FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , sitios_serviciosSedes sd, clinico_servicios ser WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND  t."sedesClinica_id" =  ' + "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND  t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and  t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and  dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and  t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = '  + "'" + str('TRIAGE') + "'" + ' group by ser.nombre'

    curt.execute(comando)
    print(comando)

    indicadores = []

    for id, nombre in curt.fetchall():
            indicadores.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(indicadores)

    context['Indicadores'] = indicadores

    # Fin combo Indicadores


    liquidacion = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   

    #detalle = 'SELECT ' + "'" + str("INGRESO") + "'||" +  ' tipoIng, i.id'  + "||" +"'" + "-'||case when conv.id != 0 then conv.id else '00' end" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual , conv.nombre convenio, conv.id convenioId FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"  AND fac.documento_id = i.documento_id and fac."tipoDoc_id" = i."tipoDoc_id" and fac."consecAdmision" = i.consec and fac.convenio_id = conv.id UNION SELECT ' + "'"  + str("TRIAGE") + "'" + ' tipoIng, t.id'  + "||" +"'" + "-'||conv.id" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual , conv.nombre convenio, conv.id convenioId   FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'" + ' AND fac.documento_id = t.documento_id and fac."tipoDoc_id" = t."tipoDoc_id" and fac."consecAdmision" = t.consec and fac.convenio_id = conv.id'
    detalle = 'SELECT ' + "'" + str("INGRESO") + "'" + "||'-'||" + ' i.id'  + "||" +"'" + "-'||case when conv.id != 0 then conv.id else " + "'" + str('00') + "'" + ' end id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual,conv.nombre convenio, conv.id convenioId FROM admisiones_ingresos i INNER JOIN clinico_servicios ser ON (ser.id = i."serviciosActual_id" ) INNER JOIN sitios_serviciosSedes sd ON (i."sedesClinica_id" = sd."sedesClinica_id" AND sd.servicios_id  = ser.id) INNER JOIN  sitios_dependencias dep  ON (dep."sedesClinica_id" =  i."sedesClinica_id" and dep.id = i."dependenciasActual_id"  AND  (dep.disponibilidad= ' + "'" + str('O') + "'" + ' OR (dep.disponibilidad = ' + "'" + str('L') + "'" + ' AND ser.id=3)) AND dep."serviciosSedes_id" = sd.id ) INNER JOIN sitios_dependenciastipo deptip ON (deptip.id = dep."dependenciasTipo_id") INNER JOIN usuarios_usuarios u ON (u."tipoDoc_id" = i."tipoDoc_id" and u.id = i."documento_id" ) INNER JOIN usuarios_tiposDocumento tp ON (tp.id = u."tipoDoc_id") INNER JOIN clinico_Diagnosticos diag ON (diag.id = i."dxActual_id") LEFT JOIN facturacion_conveniospacienteingresos fac ON ( fac."tipoDoc_id" = i."tipoDoc_id" and fac.documento_id = i.documento_id and  fac."consecAdmision" = i.consec )  LEFT JOIN contratacion_convenios conv ON (conv.id  = fac.convenio_id) WHERE i."sedesClinica_id" =  ' "'" + str(sede) + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' and i."fechaSalida" is null UNION SELECT ' + "'"  + str("TRIAGE") + "'"+ "||'-'||"  + ' t.id'  + "||" +"'" + "-'||case when conv.id != 0 then conv.id else " + "'" + str('00') + "'" + ' end id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre, t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "' '" + ' dxActual , conv.nombre convenio, conv.id convenioId FROM triage_triage t INNER JOIN clinico_servicios ser ON ( ser.nombre = ' + "'" + str('TRIAGE') + "')" + ' INNER JOIN sitios_serviciosSedes sd ON (t."sedesClinica_id" = sd."sedesClinica_id" AND sd.servicios_id  = ser.id and sd.id = t."serviciosSedes_id" ) INNER JOIN  sitios_dependencias dep  ON (dep."sedesClinica_id" =  t."sedesClinica_id" and dep.id = t.dependencias_id  AND dep.disponibilidad = ' + "'" + str('O') + "'" + ' AND dep."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id") INNER JOIN sitios_dependenciastipo deptip ON (deptip.id = dep."dependenciasTipo_id") INNER JOIN usuarios_usuarios u ON (u."tipoDoc_id" = t."tipoDoc_id" and u.id = t."documento_id" ) INNER JOIN usuarios_tiposDocumento tp ON (tp.id = u."tipoDoc_id") LEFT JOIN facturacion_conveniospacienteingresos fac ON ( fac."tipoDoc_id" = t."tipoDoc_id" and fac.documento_id = t.documento_id and  fac."consecAdmision" = t.consec ) LEFT JOIN contratacion_convenios conv ON (conv.id  = fac.convenio_id) WHERE  t."sedesClinica_id" = ' + "'" + str(sede) + "'"

    print(detalle)

    curx.execute(detalle)

    for id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual , convenio, convenioId in curx.fetchall():
        liquidacion.append(
		{"model":"ingresos.ingresos","pk":id,"fields":
			{ 'id':id, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
                         'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida,
                         'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                         'dxActual': dxActual,'convenio':convenio, 'convenioId':convenioId}})

    miConexionx.close()
    print(liquidacion)
    context['Liquidacion'] = liquidacion


    serialized1 = json.dumps(liquidacion, default=serialize_datetime)


    return HttpResponse(serialized1, content_type='application/json')

def PostConsultaLiquidacion(request):
    print ("Entre PostConsultaLiquidacion ")

    Post_id = request.POST["post_id"]
    username_id = request.POST["username_id"]

    print("id = ", Post_id)
    llave = Post_id.split('-')
    print ("llave = " ,llave)
    print ("primero=" ,llave[0])
    print("segundo = " ,llave[1])
    print("tercero o convenio  = " ,llave[2])


    # Combo TiposPagos

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre nombre FROM cartera_tiposPagos c order by c.nombre'

    curt.execute(comando)
    print(comando)

    tiposPagos = []

    #tiposPagos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposPagos.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(tiposPagos)

    #context['TiposPagos'] = tiposPagos

    # Fin combo tiposPagos


    # Combo FormasPago

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre nombre FROM cartera_formasPagos c order by c.nombre'

    curt.execute(comando)
    print(comando)

    formasPagos = []

    #formasPagos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        formasPagos.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(formasPagos)


    # Fin combo formasPagos

    # Combo Cups

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre ||' + "'" + str(' ') + "'" +  '||c."codigoCups" nombre FROM clinico_examenes c order by c.nombre'

    curt.execute(comando)
    print(comando)

    cups = []

    cups.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        cups.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(cups)

    #context['Cups'] = cups

    # Fin combo Cups


    # Combo Suministros

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    #comando = 'SELECT c.id id, c.nombre||' + "' '" +  '||c.cums nombre FROM facturacion_suministros c order by c.nombre'
    comando = 'SELECT c.id id, c.nombre nombre FROM facturacion_suministros c order by c.nombre'

    curt.execute(comando)
    print(comando)

    suministros = []

    suministros.append({'id': '', 'nombre': ''})

    for id,  nombre in curt.fetchall():
        suministros.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(suministros)

    #context['Suministros'] = suministros

    # Fin combo suministros

    convenioId = llave[2]
    convenioId = convenioId.strip()

    print("Convenio despues de strip = ", convenioId)

    #if (convenioId == '0'):
    #    print("convenioId = ", convenioId)
    #    convenioId = ""

    print("convenioId FINAL= ", convenioId)


    if llave[0] == 'INGRESO':
        ingresoId = Ingresos.objects.get(id=llave[1])
        print ("ingresoId = ", ingresoId)
        print ("tipodDoc_id =" ,ingresoId.tipoDoc_id)
        print("documento_id =", ingresoId.documento_id)
        print("consec =", ingresoId.consec)
    else:
        triageId = Triage.objects.get(id=llave[1])
        print ("triageId = ", triageId.id)
        print ("tipodDoc_id =" ,triageId.tipoDoc_id)
        print("documento_id =", triageId.documento_id)
        print("consec =", triageId.consec)

    estadoReg= 'A'
    now = datetime.datetime.now()
    print("NOW  = ", now)
    fechaRegistro = now
    usuarioRegistro = ''
    #convenioIdU = ConveniosPacienteIngresos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consecAdmision=ingresoId.consec).aggregate(minimo=Coalesce(Min('consecAdmision'), 0))
    #convenioId = (convenioIdU['minimo']) + 0

    # Validacion si existe o No existe CABEZOTE

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")

    curt = miConexiont.cursor()

    if llave[0] == 'INGRESO':
        if (convenioId == '0'):
            comando = 'SELECT id FROM facturacion_liquidacion WHERE "tipoDoc_id" = ' + str(ingresoId.tipoDoc_id) + ' AND documento_id = ' + str(ingresoId.documento_id) + ' AND "consecAdmision" = ' + str(ingresoId.consec) + ' and convenio_id is null'
        else:
            comando = 'SELECT id FROM facturacion_liquidacion WHERE "tipoDoc_id" = ' + str(ingresoId.tipoDoc_id) + ' AND documento_id = ' + str(ingresoId.documento_id) + ' AND "consecAdmision" = ' + str(ingresoId.consec) + ' and convenio_id = ' + "'" + str(convenioId) + "'"
    else:
        if (convenioId == '0'):
            comando = 'SELECT id FROM facturacion_liquidacion WHERE "tipoDoc_id" = ' + str(triageId.tipoDoc_id) + ' AND documento_id = ' + str(triageId.documento_id) + ' AND "consecAdmision" = ' + str(triageId.consec) + ' and convenio_id is null'
        else:
            comando = 'SELECT id FROM facturacion_liquidacion WHERE "tipoDoc_id" = ' + str(triageId.tipoDoc_id) + ' AND documento_id = ' + str(triageId.documento_id) + ' AND "consecAdmision" = ' + str(triageId.consec) + ' and convenio_id = ' + "'" + str(convenioId) + "'"

    curt.execute(comando)

    cabezoteLiquidacion = []

    for id in curt.fetchall():
        cabezoteLiquidacion.append({'id': id})

    miConexiont.close()

    if (cabezoteLiquidacion == []):
        # Si no existe liquidacion CABEZOTE se debe crear con los totales, abonos, anticipos, procedimiento, suministros etc
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432",       user="postgres", password="pass123")
        curt = miConexiont.cursor()

        if llave[0] == 'INGRESO':
            if (convenioId == '0'):
                comando = 'INSERT INTO facturacion_liquidacion ("tipoDoc_id", documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalProcedimientos" , "totalSuministros" , "totalLiquidacion", "valorApagar", anticipos, "fechaRegistro", "estadoRegistro", convenio_id,  "usuarioRegistro_id", "totalAbonos" , "totalRecibido" ) VALUES (' + str(ingresoId.tipoDoc_id)  + ',' +  str(ingresoId.documento_id) + ',' + str(ingresoId.consec) + ',' +  "'" +  str(fechaRegistro) + "'," + '0,0,0,0,0,0,0,' + "'" + str(fechaRegistro) + "','" + str(estadoReg) + "', null"  + ',' + "'" + str(username_id) + "',0,0)"
            else:
                comando = 'INSERT INTO facturacion_liquidacion ("tipoDoc_id", documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalProcedimientos" , "totalSuministros" , "totalLiquidacion", "valorApagar", anticipos, "fechaRegistro", "estadoRegistro", convenio_id,  "usuarioRegistro_id", "totalAbonos" , "totalRecibido") VALUES (' + str(ingresoId.tipoDoc_id)  + ',' +  str(ingresoId.documento_id) + ',' + str(ingresoId.consec) + ',' +  "'" +  str(fechaRegistro) + "'," + '0,0,0,0,0,0,0,' + "'" + str(fechaRegistro) + "','" + str(estadoReg) + "'," + str(convenioId) + ',' + "'" + str(username_id) + "',0,0)"

        else:
            if (convenioId == '0'):
                comando = 'INSERT INTO facturacion_liquidacion ("tipoDoc_id", documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalProcedimientos" , "totalSuministros" , "totalLiquidacion", "valorApagar", anticipos, "fechaRegistro", "estadoRegistro", convenio_id,  "usuarioRegistro_id", "totalAbonos" , "totalRecibido") VALUES (' + str(triageId.tipoDoc_id)  + ',' +  str(triageId.documento_id) + ',' + str('0') + ',' +  "'" +  str(fechaRegistro) + "'," + '0,0,0,0,0,0,0,' + "'" + str(fechaRegistro) + "','" + str(estadoReg) + "', null" + ',' + "'" + str(username_id) + "',0,0)"
            else:
                comando = 'INSERT INTO facturacion_liquidacion ("tipoDoc_id", documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalProcedimientos" , "totalSuministros" , "totalLiquidacion", "valorApagar", anticipos, "fechaRegistro", "estadoRegistro", convenio_id,  "usuarioRegistro_id", "totalAbonos" , "totalRecibido") VALUES (' + str(triageId.tipoDoc_id)  + ',' +  str(triageId.documento_id) + ',' + str('0') + ',' +  "'" +  str(fechaRegistro) + "'," + '0,0,0,0,0,0,0,' + "'" + str(fechaRegistro) + "','" + str(estadoReg) + "'," + str(convenioId) + ',' + "'" + str(username_id) + "',0,0)"

        curt.execute(comando)
        miConexiont.commit()
        miConexiont.close()
        liquidacionU = Liquidacion.objects.all().aggregate(maximo=Coalesce(Max('id'), 0))
        liquidacionId = (liquidacionU['maximo']) + 0
    else:
        liquidacionId = cabezoteLiquidacion[0]['id']
        liquidacionId = str(liquidacionId)
        print("liquidacionId = ", liquidacionId)

    liquidacionId = str(liquidacionId)
    liquidacionId = liquidacionId.replace("(", ' ')
    liquidacionId = liquidacionId.replace(")", ' ')
    liquidacionId = liquidacionId.replace(",", ' ')

    print ("liquidacionId FINAL = ", liquidacionId  )

    # Fin validacion de Liquidacion cabezote

    if request.method == 'POST':

        # Abro Conexion

        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",password="pass123")
        cur = miConexionx.cursor()

        if llave[0] == 'INGRESO':	

            #comando = 'select ' + "'"  + str('INGRESO') + "'" + '  tipo, liq.id id,  "consecAdmision",  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", observaciones, liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos", conv.nombre nombreConvenio, usu.nombre paciente, adm.id ingresoId1, usu.documento documento, tip.nombre tipoDocumento FROM facturacion_liquidacion liq, contratacion_convenios conv, usuarios_usuarios usu, admisiones_ingresos adm, usuarios_tiposdocumento  tip where adm.id = ' + "'" + str(llave[1]) + "'" + '  AND  liq.convenio_id = conv.id and usu.id = liq.documento_id  and adm."tipoDoc_id" = liq."tipoDoc_id"   AND tip.id = adm."tipoDoc_id" AND adm.documento_id = liq.documento_id  AND adm.consec = liq."consecAdmision" AND conv.id = ' + str(convenioId)
            comando =  'select ' + "'"  + str('INGRESO') + "'" + '  tipo, liq.id id, dep.nombre dependenciaNombre, serv.nombre servicioNombre , "consecAdmision",  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", observaciones,  liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos",  conv.nombre nombreConvenio, usu.nombre paciente, adm.id ingresoId1, usu.documento documento, tip.nombre tipoDocumento FROM facturacion_liquidacion liq INNER JOIN usuarios_usuarios usu ON (usu."tipoDoc_id" = liq."tipoDoc_id" AND usu.id = liq.documento_id) INNER JOIN admisiones_ingresos adm ON (adm."tipoDoc_id" = liq."tipoDoc_id"  AND adm.documento_id = liq.documento_id  AND adm.consec = liq."consecAdmision"  ) INNER JOIN usuarios_tiposdocumento  tip ON (tip.id = adm."tipoDoc_id") LEFT JOIN clinico_servicios serv ON (serv.id = adm."serviciosActual_id") LEFT JOIN sitios_dependencias dep on (dep.id =adm."dependenciasActual_id") LEFT JOIN  contratacion_convenios conv ON (conv.id = liq.convenio_id) where adm.id = ' + "'" + str(llave[1]) + "'"
        else:

            #comando = 'select ' + "'"  + str('TRIAGE') + "'" + ' tipo, liq.id id,  tri."consecAdmision" consecAdmision,  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", tri.observaciones, liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos", conv.nombre nombreConvenio, usu.nombre paciente, tri.id triageId1, usu.documento documento, tip.nombre tipoDocumento FROM facturacion_liquidacion liq, contratacion_convenios conv, usuarios_usuarios usu, triage_triage tri, usuarios_tiposdocumento  tip where tri.id = ' + "'" + str(llave[1]) + "'" + '  AND  liq.convenio_id = conv.id and usu.id = liq.documento_id  and tri."tipoDoc_id" = liq."tipoDoc_id"   AND tip.id = tri."tipoDoc_id" AND tri.documento_id = liq.documento_id  AND tri.consec = liq."consecAdmision" AND conv.id = ' + str(convenioId)
            comando =  'select ' + "'"  + str('TRIAGE') + "'" + ' tipo, liq.id id, ' + "'" + str('Triage') + "'" + ' dependenciaNombre, ' + "'" + str('TRIAGE') + "'" + '  servicioNombre, tri."consecAdmision",  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", tri.observaciones, liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos", conv.nombre nombreConvenio, usu.nombre paciente, tri.id triageId1, usu.documento documento, tip.nombre tipoDocumento FROM facturacion_liquidacion liq inner join  triage_triage tri on (tri."tipoDoc_id" = liq."tipoDoc_id"  and tri.documento_id = liq.documento_id  AND tri.consec = liq."consecAdmision" ) left join  contratacion_convenios conv on (conv.id = liq.convenio_id) inner join  usuarios_usuarios usu on (usu."tipoDoc_id" = liq."tipoDoc_id" AND usu.id = liq.documento_id) inner join usuarios_tiposdocumento  tip on (tip.id = usu."tipoDoc_id") where tri.id = ' + "'" + str(llave[1]) + "'"
            print(comando)

        cur.execute(comando)

        liquidacion = []

        if llave[0] == 'INGRESO':

          for tipo, id, dependenciaNombre, servicioNombre, consecAdmision,fecha ,totalCopagos,totalCuotaModeradora,totalProcedimientos ,totalSuministros, totalLiquidacion, valorApagar, fechaCorte, anticipos, detalleAnulacion, fechaAnulacion, observaciones, fechaRegistro, estadoRegistro, convenio_id, tipoDoc_id , documento_id, usuarioRegistro_id, totalAbonos, nombreConvenio , paciente, ingresoId1 , documento, tipoDocumento in cur.fetchall():
            liquidacion.append( {"tipo":tipo, "id": id, "dependenciaNombre":dependenciaNombre,"servicioNombre":servicioNombre,
                     "consecAdmision": consecAdmision,
                     "fecha": fecha,
                     "totalCopagos": totalCopagos, "totalCuotaModeradora": totalCuotaModeradora,
                     "totalProcedimientos": totalProcedimientos,
                                 "totalSuministros": totalSuministros,
                                 "totalLiquidacion": totalLiquidacion, "valorApagar": valorApagar,
                                 "fechaCorte": fechaCorte,  "anticipos": anticipos,
                                 "detalleAnulacion": detalleAnulacion,  "fechaAnulacion": fechaAnulacion,  "observaciones": observaciones,
                                 "fechaRegistro": fechaRegistro, "estadoRegistro": estadoRegistro, "convenio_id": convenio_id,
            "tipoDoc_id": tipoDoc_id, "documento_id":documento_id,  "usuarioRegistro_id": usuarioRegistro_id,
            "totalAbonos": totalAbonos, "nombreConvenio": nombreConvenio,   "paciente": paciente,
            "ingresoId1": ingresoId1, "documento": documento, "tipoDocumento": tipoDocumento
                                 })
        else:
          for tipo, id, dependenciaNombre, servicioNombre, consecAdmision,fecha ,totalCopagos,totalCuotaModeradora,totalProcedimientos ,totalSuministros, totalLiquidacion, valorApagar, fechaCorte, anticipos, detalleAnulacion, fechaAnulacion, observaciones, fechaRegistro, estadoRegistro, convenio_id, tipoDoc_id , documento_id, usuarioRegistro_id, totalAbonos, nombreConvenio , paciente, triageId1 , documento, tipoDocumento in cur.fetchall():
            liquidacion.append( { "tipo":tipo, "id": id, "dependenciaNombre":dependenciaNombre,"servicioNombre":servicioNombre,
                     "consecAdmision": consecAdmision,
                     "fecha": fecha,
                     "totalCopagos": totalCopagos, "totalCuotaModeradora": totalCuotaModeradora,
                     "totalProcedimientos": totalProcedimientos,
                                 "totalSuministros": totalSuministros,
                                 "totalLiquidacion": totalLiquidacion, "valorApagar": valorApagar,
                                 "fechaCorte": fechaCorte,  "anticipos": anticipos,
                                 "detalleAnulacion": detalleAnulacion,  "fechaAnulacion": fechaAnulacion,  "observaciones": observaciones,
                                 "fechaRegistro": fechaRegistro, "estadoRegistro": estadoRegistro, "convenio_id": convenio_id,
            "tipoDoc_id": tipoDoc_id, "documento_id":documento_id,  "usuarioRegistro_id": usuarioRegistro_id,
            "totalAbonos": totalAbonos, "nombreConvenio": nombreConvenio,   "paciente": paciente,
            "triageId1": triageId1, "documento": documento, "tipoDocumento": tipoDocumento
                                 })


        miConexionx.close()
        print(liquidacion)

        # Cierro Conexion

        if llave[0] == 'INGRESO':	

           totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
           totalSuministros = (totalSuministros['totalS']) + 0
           print("totalSuministros", totalSuministros)
           totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
           totalProcedimientos = (totalProcedimientos['totalP']) + 0
           print("totalProcedimientos", totalProcedimientos)
           registroPago = Liquidacion.objects.get(id=liquidacionId)
           totalCopagos = registroPago.totalCopagos
           totalCuotaModeradora = registroPago.totalCuotaModeradora
           totalAnticipos = registroPago.anticipos
           totalAbonos = registroPago.totalAbonos
           totalRecibido = registroPago.totalRecibido
           totalAnticipos = registroPago.anticipos
           valorApagar = registroPago.valorApagar
           totalLiquidacion = registroPago.totalLiquidacion


        else:

           totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
           totalSuministros = (totalSuministros['totalS']) + 0
           print("totalSuministros", totalSuministros)
           totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
           totalProcedimientos = (totalProcedimientos['totalP']) + 0
           registroPago = Liquidacion.objects.get(id=liquidacionId)
           totalCopagos = registroPago.totalCopagos
           totalCuotaModeradora = registroPago.totalCuotaModeradora
           totalAnticipos = registroPago.anticipos
           totalAbonos = registroPago.totalAbonos
           totalRecibido = registroPago.totalRecibido
           totalAnticipos = registroPago.anticipos
           valorApagar = registroPago.valorApagar
           totalLiquidacion = registroPago.totalLiquidacion


        if llave[0] == 'INGRESO':

            return JsonResponse({'pk':liquidacion[0]['id'],'tipo':tipo, 'id':id,  "dependenciaNombre":liquidacion[0]['dependenciaNombre'] ,"servicioNombre":liquidacion[0]['servicioNombre'],'consecAdmision':liquidacion[0]['consecAdmision'],'fecha':liquidacion[0]['fecha'],
                             'totalCopagos':liquidacion[0]['totalCopagos'],  'totalCuotaModeradora': liquidacion[0]['totalCuotaModeradora'],
                             'totalProcedimientos': liquidacion[0]['totalProcedimientos'],
                             'totalSuministros': liquidacion[0]['totalSuministros'],
                             'totalLiquidacion': liquidacion[0]['totalLiquidacion'],
                             'fechaCorte': liquidacion[0]['fechaCorte'],
                             'valorApagar': liquidacion[0]['valorApagar'],
                             'anticipos': liquidacion[0]['anticipos'],
                             'detalleAnulacion': liquidacion[0]['detalleAnulacion'],
                             'fechaAnulacion': liquidacion[0]['fechaAnulacion'],
                             'observaciones': liquidacion[0]['observaciones'],
                             'fechaRegistro': liquidacion[0]['fechaRegistro'],
                             'estadoRegistro': liquidacion[0]['estadoRegistro'],
                             'convenio_id': liquidacion[0]['convenio_id'],
                             'tipoDoc_id': liquidacion[0]['tipoDoc_id'],
                             'documento_id': liquidacion[0]['documento_id'],
                             'usuarioRegistro_id': liquidacion[0]['usuarioRegistro_id'],
                             'totalAbonos': liquidacion[0]['totalAbonos'],
                             'nombreConvenio': liquidacion[0]['nombreConvenio'],
                             'paciente': liquidacion[0]['paciente'], 'Suministros':suministros, 'Cups':cups,
			     'totalSuministros':totalSuministros,'totalProcedimientos':totalProcedimientos,'totalCopagos':totalCopagos,
			     'totalCuotaModeradora':totalCuotaModeradora,'totalAnticipos':totalAnticipos, 'totalAbonos':totalAbonos,
			     'totalLiquidacion':totalLiquidacion, 'totalRecibido':totalRecibido , 'totalAPagar':valorApagar, 'TiposPagos':tiposPagos, 'FormasPagos':formasPagos,
			     'ingresoId1': ingresoId1, 'documento': documento, 'tipoDocumento': tipoDocumento

            })
        else:
            return JsonResponse(
                {'pk': liquidacion[0]['id'], 'tipo': tipo, 'id': id,"dependenciaNombre":liquidacion[0]['dependenciaNombre'] ,"servicioNombre":liquidacion[0]['servicioNombre'],  'consecAdmision': liquidacion[0]['consecAdmision'],
                 'fecha': liquidacion[0]['fecha'],
                 'totalCopagos': liquidacion[0]['totalCopagos'],
                 'totalCuotaModeradora': liquidacion[0]['totalCuotaModeradora'],
                 'totalProcedimientos': liquidacion[0]['totalProcedimientos'],
                 'totalSuministros': liquidacion[0]['totalSuministros'],
                 'totalLiquidacion': liquidacion[0]['totalLiquidacion'],
                 'fechaCorte': liquidacion[0]['fechaCorte'],
                 'valorApagar': liquidacion[0]['valorApagar'],
                 'anticipos': liquidacion[0]['anticipos'],
                 'detalleAnulacion': liquidacion[0]['detalleAnulacion'],
                 'fechaAnulacion': liquidacion[0]['fechaAnulacion'],
                 'observaciones': liquidacion[0]['observaciones'],
                 'fechaRegistro': liquidacion[0]['fechaRegistro'],
                 'estadoRegistro': liquidacion[0]['estadoRegistro'],
                 'convenio_id': liquidacion[0]['convenio_id'],
                 'tipoDoc_id': liquidacion[0]['tipoDoc_id'],
                 'documento_id': liquidacion[0]['documento_id'],
                 'usuarioRegistro_id': liquidacion[0]['usuarioRegistro_id'],
                 'totalAbonos': liquidacion[0]['totalAbonos'],
                 'nombreConvenio': liquidacion[0]['nombreConvenio'],
                 'paciente': liquidacion[0]['paciente'], 'Suministros': suministros, 'Cups': cups,
                 'totalSuministros': totalSuministros, 'totalProcedimientos': totalProcedimientos,
                 'totalCopagos': totalCopagos,
                 'totalCuotaModeradora': totalCuotaModeradora, 'totalAnticipos': totalAnticipos,
                 'totalAbonos': totalAbonos,
                 'totalLiquidacion': totalLiquidacion, 'totalRecibido':totalRecibido , 'totalAPagar': valorApagar, 'TiposPagos': tiposPagos,
                 'FormasPagos': formasPagos,
                 'triageId1': triageId1, 'documento': documento, 'tipoDocumento': tipoDocumento

                 })

    else:
        return JsonResponse({'errors':'Something went wrong!'})

def load_dataLiquidacionDetalle(request, data):
    print("Entre load_data LiquidacionDetalle")

    context = {}
    d = json.loads(data)

    username = d['username']
    sede = d['sede']
    username_id = d['username_id']
    valor = d['valor']
    liquidacionId = d['liquidacionId']

    nombreSede = d['nombreSede']
    print("sede:", sede)
    print("username:", username)
    print("username_id:", username_id)

    


    # Abro Conexion para la Liquidacion Detalle

    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur = miConexionx.cursor()

    comando = 'select liq.id id,consecutivo ,  cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , exa.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro" , liq."estadoRegistro" estadoReg FROM facturacion_liquidaciondetalle liq inner join clinico_examenes exa on (exa.id = liq."codigoCups_id")  where liquidacion_id= ' + "'" +  str(valor) + "'" +  ' UNION select liq.id id,consecutivo , cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , sum.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro" , liq."estadoRegistro" estadoReg FROM facturacion_liquidaciondetalle liq inner join facturacion_suministros sum on (sum.id = liq.cums_id)  where liquidacion_id= '  + "'" +  str(liquidacionId) + "'" + ' order by consecutivo'

    print(comando)

    cur.execute(comando)

    liquidacionDetalle = []

    for id, consecutivo, fecha, cantidad, valorUnitario, valorTotal, cirugia, fechaCrea, observaciones, estadoRegistro, codigoCups_id, cums_id, nombreExamen, liquidacion_id, tipoHonorario_id, tipoRegistro, estadoReg in cur.fetchall():
        liquidacionDetalle.append(
            {"model": "liquidacionDetalle.liquidacionDetalle", "pk": id, "fields":
                {"id": id, "consecutivo": consecutivo,
                 "fecha": fecha,
                 "cantidad": cantidad,
                 "valorUnitario": valorUnitario, "valorTotal": valorTotal,
                 "cirugia": cirugia,
                 #"fechaCrea": fechaCrea,
                 "observaciones": observaciones,
                 "estadoRegistro": estadoRegistro, "codigoCups_id": codigoCups_id,
                 "cums_id": cums_id, "nombreExamen": nombreExamen,
                 "liquidacion_id": liquidacion_id, "tipoHonorario_id": tipoHonorario_id,
                 "tipoRegistro": tipoRegistro, "estadoReg":estadoReg}})

    miConexionx.close()
    print(liquidacionDetalle)

    # Cierro Conexion

    serialized1 = json.dumps(liquidacionDetalle, default=decimal_serializer)
    #serialized1 = json.dumps(liquidacionDetalle, default=serialize_datetime)
    #serialized1 = json.dumps(liquidacionDetalle, safe=False)
    #serialized1 = json.dumps(liquidacionDetalle)

    return HttpResponse(serialized1, content_type='application/json')
    #return HttpResponse(serialized1, safe=False)



def PostConsultaLiquidacionDetalle(request):
    print ("Entre PostConsultaLiquidacionDetalle ")
    post_id =  request.POST["post_id"]

    # Combo Cups

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre ||' + "'" + str(' ') + "'" +  '||c."codigoCups" nombre FROM clinico_examenes c order by c.nombre'

    curt.execute(comando)
    print(comando)

    cups = []

    cups.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        cups.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(cups)


    # Fin combo Cups


    # Combo Suministros

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()


    comando = 'SELECT c.id id, c.nombre nombre FROM facturacion_suministros c order by c.nombre'

    curt.execute(comando)
    print(comando)

    suministros = []

    suministros.append({'id': '', 'nombre': ''})

    for id,  nombre in curt.fetchall():
        suministros.append({'id': id,  'nombre': nombre})

    miConexiont.close()
    print(suministros)

    # Fin combo suministros



    # Aqui RUTINA Leer el registro liquidacionDetalle


    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur = miConexionx.cursor()

    comando = 'select liq.id id,consecutivo ,  cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , exa.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro"  FROM facturacion_liquidaciondetalle liq left join clinico_examenes exa on (exa.id = liq."codigoCups_id")  where liq.liquidacion_id= ' + str(post_id)  +  ' UNION select liq.id id,consecutivo , cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , sum.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro"  FROM facturacion_liquidaciondetalle liq left join facturacion_suministros sum on (sum.id = liq.cums_id)  where liq.id= '  + str(post_id) 

    print(comando)

    cur.execute(comando)

    liquidacionDetalleU = []

    for id, consecutivo, fecha, cantidad, valorUnitario, valorTotal, cirugia, fechaCrea, observaciones, estadoRegistro, codigoCups_id, cums_id, nombreExamen, liquidacion_id, tipoHonorario_id, tipoRegistro in cur.fetchall():
        liquidacionDetalleU.append(
              {"id": id, "consecutivo": consecutivo,
                 #"fecha": fecha,
                 "cantidad": cantidad,
                 "valorUnitario": valorUnitario, "valorTotal": valorTotal,
                 "cirugia": cirugia,
                 #"fechaCrea": fechaCrea,
                 "observaciones": observaciones,
                 "estadoRegistro": estadoRegistro, "codigoCups_id": codigoCups_id,
                 "cums_id": cums_id, "nombreExamen": nombreExamen,
                 "liquidacion_id": liquidacion_id, "tipoHonorario_id": tipoHonorario_id,
                 "tipoRegistro": tipoRegistro, "cups": cups, "suministros":suministros})

    miConexionx.close()
    print(liquidacionDetalleU)

    # Cierro Conexion
    #
    #
    return JsonResponse({'pk':liquidacionDetalleU[0]['id'], 'id':liquidacionDetalleU[0]['id'], 'consecutivo':liquidacionDetalleU[0]['consecutivo'],'cantidad':liquidacionDetalleU[0]['cantidad'],
                             'valorUnitario':liquidacionDetalleU[0]['valorUnitario'],  'valorTotal': liquidacionDetalleU[0]['valorTotal'],
                             'cirugia': liquidacionDetalleU[0]['cirugia'],
                             'observaciones': liquidacionDetalleU[0]['observaciones'],
                             'estadoRegistro': liquidacionDetalleU[0]['estadoRegistro'],
                             'codigoCups_id': liquidacionDetalleU[0]['codigoCups_id'],
                             'cums_id': liquidacionDetalleU[0]['cums_id'],
                             'liquidacion_id': liquidacionDetalleU[0]['liquidacion_id'],
                             'tipoHonorario_id': liquidacionDetalleU[0]['tipoHonorario_id'],
                             'tipoRegistro': liquidacionDetalleU[0]['tipoRegistro'],
                             'Cups': cups, 'Suministros': suministros
                                                        })


    #serialized1 = json.dumps(liquidacionDetalleU, default=decimal_serializer)
    #serialized1 = json.dumps(liquidacionDetalleU, default=serialize_datetime)
    #serialized1 = json.dumps(liquidacionDetalleU, safe=False)
    #serialized1 = json.dumps(liquidacionDetalleU)

    #return HttpResponse(serialized1, content_type='application/json')
    #return HttpResponse(serialized1, safe=False)


def GuardaAbonosFacturacion(request):

    print ("Entre GuardaAbonosFacturacion" )

    liquidacionId = request.POST['liquidacionId1']
    #sede = request.POST['sede']
    tipoPago = request.POST['tipoPago']
    formaPago = request.POST['formaPago']
    valor = request.POST['valorAbono']
    #saldo = request.POST['saldo']
    #totalAplicado = request.POST['totalAplicado']
    descripcion = request.POST['descripcionAbono']
    print ("liquidacionId  = ", liquidacionId )
    # print("sede = ", sede)

    fechaRegistro = datetime.datetime.now()

    registroId = Liquidacion.objects.get(id=liquidacionId)
    print  ("registroId documento =" , registroId.documento_id)
    print  ("registroId tipoDoc =" , registroId.tipoDoc_id)
    print  ("registroId consec =" , registroId.consecAdmision)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'insert into cartera_Pagos ("fecha", "tipoDoc_id" , documento_id, consec,  "tipoPago_id" , "formaPago_id", valor, descripcion ,"fechaRegistro","estadoReg", saldo, "totalAplicado", "valorEnCurso") values ('  + "'" + str(fechaRegistro) + "'," +  "'" + str(registroId.tipoDoc_id) + "'" + ' , ' + "'" + str(registroId.documento_id) + "'" + ', ' + "'" + str(registroId.consecAdmision) + "'" + '  , ' + "'" + str(tipoPago) + "'" + '  , ' + "'" + str(formaPago) + "'" + ', ' + "'" + str(valor) + "',"   + "'" + str(descripcion) + "','"   + str(fechaRegistro) + "'," + "'" +  str("A") + "',0,0,0);"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Abono Actualizado satisfactoriamente!'})

def PostDeleteAbonosFacturacion(request):

    print ("Entre PostDeleteAbonosFacturacion" )

    id = request.POST["id"]
    print ("el id es = ", id)

    ## Se debe verificar antes que no haya valor aplicado en PagosFacturas

    #verAplicado = PagosFacturas.objects.get(id=id)

    #if verAplicado.id != '':
    #    return JsonResponse({'success': True, 'message': 'No se puede cancelar Abono. Esta relacionado con la Factura No' + verAplicado. facturaAplicada})

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE cartera_Pagos SET "estadoReg" = ' + "'" + str('N') + "' WHERE id =  " + id
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Abono Cancelado!'})
	

def GuardarLiquidacionDetalle(request):

    print ("Entre GuardarLiquidacionDetalle" )

    liquidacionId = request.POST["liquidacionId"]
    cups = request.POST["cups"]
    suministros = request.POST["suministros"]
    cantidad = request.POST["cantidad"]
    valorUnitario = request.POST['valorUnitario']
    valorTotal =  float(cantidad)  * float(valorUnitario)
    observaciones = request.POST['observaciones']
    username_id = request.POST['username_id']
    print ("liquidacionId  = ", liquidacionId )
    print ("observaciones" , observaciones)
    estadoReg= 'A'

    if cups == '':
           cups="null"

    if suministros == '':
           suministros="null"

 
    fechaRegistro = datetime.datetime.now()

    registroId = Liquidacion.objects.get(id=liquidacionId)
    print  ("registroId documento =" , registroId.documento_id)
    print  ("registroId tipoDoc =" , registroId.tipoDoc_id)
    print  ("registroId consec =" , registroId.consecAdmision)

    # Aqui RUTINA busca consecutivo de liquidacion


    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",        password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT COALESCE(max(p.consecutivo),0) + 1 cons FROM facturacion_liquidaciondetalle p WHERE liquidacion_id = ' + liquidacionId
    curt.execute(comando)

    print(comando)

    consecLiquidacion = []

    for cons in curt.fetchall():
         consecLiquidacion.append({'cons': cons})

    miConexiont.close()
    print("consecLiquidacion = ", consecLiquidacion[0])

    consecLiquidacion = consecLiquidacion[0]['cons']
    consecLiquidacion = str(consecLiquidacion)
    print ("consecLiquidacion = ", consecLiquidacion)

    consecLiquidacion = consecLiquidacion.replace("(",' ')
    consecLiquidacion = consecLiquidacion.replace(")", ' ')
    consecLiquidacion = consecLiquidacion.replace(",", ' ')

    # Fin RUTINA busca consecutivo de liquidacion


    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_liquidaciondetalle (consecutivo,fecha, cantidad, "valorUnitario", "valorTotal",cirugia,"fechaCrea", "fechaRegistro", "estadoRegistro", "codigoCups_id", cums_id,  "usuarioRegistro_id", liquidacion_id, "tipoRegistro", observaciones) VALUES (' + "'" +  str(consecLiquidacion)  + "','" + str(fechaRegistro) + "','" + str(cantidad) + "','"  + str(valorUnitario) + "','" + str(valorTotal)  + "','" + str('N') + "','" +  str(fechaRegistro) + "','" +  str(fechaRegistro) + "','" + str(estadoReg) + "'," + str(cups) + "," + str(suministros) +   ",'"  + str(username_id) + "'," + liquidacionId + ",'MANUAL'," + "'"  + str(observaciones) + "')"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    # Falta la RUTINA que actualica los cabezotes de la liquidacion

    totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
    totalSuministros = (totalSuministros['totalS']) + 0
    print("totalSuministros", totalSuministros)
    totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
    totalProcedimientos = (totalProcedimientos['totalP']) + 0
    print("totalProcedimientos", totalProcedimientos)
    registroPago = Liquidacion.objects.get(id=liquidacionId)
    totalCopagos = registroPago.totalCopagos
    totalCuotaModeradora = registroPago.totalCuotaModeradora
    totalAnticipos = registroPago.anticipos
    totalAbonos = registroPago.totalAbonos
    totalRecibido = registroPago.totalRecibido
    totalAnticipos = registroPago.anticipos
    totalLiquidacion = totalSuministros + totalProcedimientos
    valorApagar = totalLiquidacion -  totalRecibido
    

    # Rutina Guarda en cabezote los totales

    print ("Voy a grabar el cabezote")

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",                                       password="pass123")
    curt = miConexiont.cursor()
    comando = 'UPDATE facturacion_liquidacion SET "totalSuministros" = ' + str(totalSuministros) + ',"totalProcedimientos" = ' + str(totalProcedimientos) + ', "totalCopagos" = ' + str(totalCopagos) + ' , "totalCuotaModeradora" = ' + str(totalCuotaModeradora) + ', anticipos = ' +  str(totalAnticipos) + ' ,"totalAbonos" = ' + str(totalAbonos) + ', "totalLiquidacion" = ' + str(totalLiquidacion) + ', "valorApagar" = ' + str(valorApagar) +  ', "totalRecibido" = ' + str(totalRecibido) + ' WHERE id =' + str(liquidacionId)
    curt.execute(comando)
    miConexiont.commit()
    miConexiont.close()



    ## Fin rutina actualiza cabezotes

	

    return JsonResponse({'success': True, 'message': 'Registro Guardado satisfactoriamente!'})

def PostDeleteLiquidacionDetalle(request):

    print ("Entre PostDeleteLiquidacionDetalle" )

    id = request.POST["id"]
    print ("el id es = ", id)
    #post = LiquidacionDetalle.objects.get(id=id)
    #post.delete()

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE facturacion_liquidaciondetalle SET "estadoRegistro" = ' + "'" + str('N') + "' WHERE id =  " + id
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Registro de Liquidacion Anulado!'})


def EditarGuardarLiquidacionDetalle(request):

    print ("Entre EditarGuardarLiquidacionDetalle" )

    liquidacionDetalleId = request.POST['liquidacionDetalleId']
    cups = request.POST["ldcups"]
    suministros = request.POST["ldsuministros"]
    cantidad = request.POST['ldcantidad']
    valorUnitario = request.POST['ldvalorUnitario']
    valorTotal = request.POST['ldvalorTotal']
    observaciones = request.POST['ldobservaciones']
    username_id = request.POST['username_id2']
    print ("liquidacionDetalleId  = ", liquidacionDetalleId )
    tipoRegistro = request.POST['ldtipoRegistro']
    print ("tipoRegistro  = ", tipoRegistro )
    estadoReg='A'

    if cups == '':
           cups="null"

    if suministros == '':
           suministros="null"


    fechaRegistro = datetime.datetime.now()

    registroId = LiquidacionDetalle.objects.get(id=liquidacionDetalleId)
    print  ("liquiacion_id =" , registroId.liquidacion_id)



    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    #comando = 'insert into facturacion_liquidacionDetalle ("fecha", "tipoDoc_id" , documento_id, consec,  "tipoPago_id" , "formaPago_id", valor, descripcion ,"fechaRegistro","estadoReg") values ('  + "'" + str(fechaRegistro) + "'," +  "'" + str(registroId.tipoDoc_id) + "'" + ' , ' + "'" + str(registroId.documento_id) + "'" + ', ' + "'" + str(registroId.consec) + "'" + '  , ' + "'" + str(tipoPago) + "'" + '  , ' + "'" + str(formaPago) + "'" + ', ' + "'" + str(valor) + "',"   + "'" + str(descripcion) + "','"   + str(fechaRegistro) + "'," + "'" +  str("A") + "');"
    comando = 'UPDATE facturacion_liquidaciondetalle SET fecha = ' + "'" + str(fechaRegistro) + "', observaciones = " + "'" +  str(observaciones) + "', cantidad = "  + str(cantidad) +  ',"valorUnitario" = ' + str(valorUnitario) + ', "valorTotal" = '  +      str(valorTotal) + ',"fechaCrea" = '  + "'" + str(fechaRegistro) + "'" + ',"estadoRegistro" = ' + "'" + str(estadoReg) + "'" + ',"codigoCups_id" = ' + str(cups) +  ', cums_id = ' + str(suministros) +  ', "usuarioRegistro_id" = ' + "'" + str(username_id) + "', liquidacion_id = " + str(registroId.liquidacion_id) + ', "tipoRegistro" = ' + "'" + str(tipoRegistro) + "' WHERE id = " + str(liquidacionDetalleId)
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

  # Falta la RUTINA que actualica los cabezotes de la liquidacion

    totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=registroId.liquidacion_id).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
    totalSuministros = (totalSuministros['totalS']) + 0
    print("totalSuministros", totalSuministros)
    totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=registroId.liquidacion_id).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
    totalProcedimientos = (totalProcedimientos['totalP']) + 0
    print("totalProcedimientos", totalProcedimientos)
    registroPago = Liquidacion.objects.get(id=registroId.liquidacion_id)
    totalCopagos = registroPago.totalCopagos
    totalCuotaModeradora = registroPago.totalCuotaModeradora
    totalAnticipos = registroPago.anticipos
    totalAbonos = registroPago.totalAbonos
    totalRecibido = registroPago.totalRecibido
    totalAnticipos = registroPago.anticipos
    totalLiquidacion = totalSuministros + totalProcedimientos
    valorApagar = totalLiquidacion -  totalRecibido
    

    # Rutina Guarda en cabezote los totales

    print ("Voy a grabar el cabezote")

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",                                       password="pass123")
    curt = miConexiont.cursor()
    comando = 'UPDATE facturacion_liquidacion SET "totalSuministros" = ' + str(totalSuministros) + ',"totalProcedimientos" = ' + str(totalProcedimientos) + ', "totalCopagos" = ' + str(totalCopagos) + ' , "totalCuotaModeradora" = ' + str(totalCuotaModeradora) + ', anticipos = ' +  str(totalAnticipos) + ' ,"totalAbonos" = ' + str(totalAbonos) + ', "totalLiquidacion" = ' + str(totalLiquidacion) + ', "valorApagar" = ' + str(valorApagar) +  ', "totalRecibido" = ' + str(totalRecibido) + ' WHERE id =' + str(registroId.liquidacion_id)
    curt.execute(comando)
    miConexiont.commit()
    miConexiont.close()

    return JsonResponse({'success': True, 'message': 'Registro Actualizado satisfactoriamente!'})


def load_dataAbonosFacturacion(request, data):
    print("Entre  load_dataAbonosFacturacion")

    context = {}
    d = json.loads(data)
    
    tipoIngreso = d['tipoIngreso']


    if tipoIngreso == 'INGRESO':
       ingresoId = d['ingresoId']
       print("ingresoId:", ingresoId)
    else:
       triageId = d['triageId']
       print("triageId:", triageId)

    sede = d['sede']

    print("sede:", sede)


    # print("data = ", request.GET('data'))

    abonos  = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curx = miConexionx.cursor()

    if tipoIngreso == 'INGRESO':
      detalle = 'SELECT pag.id id , i."tipoDoc_id" tipoDoc , i.documento_id documentoId ,u.documento documento,u.nombre nombre,i.consec consec , tipdoc.nombre nombreDocumento , cast(date(pag.fecha) as text)  fecha, pag."tipoPago_id" tipoPago , pag."formaPago_id" formaPago, pag.valor valor, pag.descripcion descripcion ,tip.nombre tipoPagoNombre,forma.nombre formaPagoNombre, pag."totalAplicado" totalAplicado, pag.saldo saldo , pag."estadoReg" estadoReg FROM admisiones_ingresos i, cartera_pagos pag ,usuarios_usuarios u ,usuarios_tiposdocumento tipdoc, cartera_tiposPagos tip, cartera_formasPagos forma WHERE i.id = ' + "'" + str(ingresoId) + "'" + ' and i.documento_id = u.id and i."tipoDoc_id" = pag."tipoDoc_id" and i.documento_id  = pag.documento_id and  i.consec = pag.consec AND tipdoc.id = i."tipoDoc_id" and pag."tipoPago_id" = tip.id and pag."formaPago_id" = forma.id'
    else:
      detalle = 'SELECT pag.id id , t."tipoDoc_id" tipoDoc , t.documento_id documentoId ,u.documento documento,u.nombre nombre,t.consec consec , tipdoc.nombre nombreDocumento , cast(date(pag.fecha) as text)  fecha, pag."tipoPago_id" tipoPago , pag."formaPago_id" formaPago, pag.valor valor, pag.descripcion descripcion ,tip.nombre tipoPagoNombre,forma.nombre formaPagoNombre, pag."totalAplicado" totalAplicado, pag.saldo saldo , pag."estadoReg" estadoReg FROM triage_triage t, cartera_pagos pag ,usuarios_usuarios u ,usuarios_tiposdocumento tipdoc, cartera_tiposPagos tip, cartera_formasPagos forma WHERE t.id = ' + "'" + str(triageId) + "'" + ' and t.documento_id = u.id and t."tipoDoc_id" = pag."tipoDoc_id" and t.documento_id  = pag.documento_id and  t.consec = pag.consec AND tipdoc.id = t."tipoDoc_id" and pag."tipoPago_id" = tip.id and pag."formaPago_id" = forma.id'

    print(detalle)

    curx.execute(detalle)

    for id, tipoDoc, documentoId, documento, nombre, consec, nombreDocumento , fecha, tipoPago, formaPago, valor, descripcion, tipoPagoNombre,formaPagoNombre,totalAplicado, saldo, estadoReg  in curx.fetchall():
        abonos.append(
            {"model": "cartera_pagos.cartera_pagos", "pk": id, "fields":
                {'id': id, 'tipoDoc': tipoDoc, 'documentoId': documentoId, 'nombre':nombre,'consec':consec,  'nombreDocumento': nombreDocumento,
                 'fecha': fecha, 'tipoPago': tipoPago, 'formaPago': formaPago, 'valor':valor, 'descripcion':descripcion,'tipoPagoNombre': tipoPagoNombre, 'formaPagoNombre': formaPagoNombre, 'totalAplicado':totalAplicado, 'saldo':saldo , 'estadoReg': estadoReg}})

    miConexionx.close()
    print(abonos)
    context['Abonos '] = abonos

    serialized2 = json.dumps(abonos,  default=decimal_serializer)


    print("Envio = ", serialized2)

    return HttpResponse(serialized2, content_type='application/json')


def FacturarCuenta(request):

    print ("Entre FacturarCuenta" )

    liquidacionId = request.POST["liquidacionId"]
    print ("liquidacionId = ", liquidacionId)
    username_id = request.POST["username_id"]



    usuarioId = Liquidacion.objects.get(id=liquidacionId)
    print ("Usuario", usuarioId.documento_id)
    print ("TipoDoc", usuarioId.tipoDoc_id)
    print ("Consec", usuarioId.consecAdmision)

    now = datetime.datetime.now()
    print("NOW  = ", now)
    fechaRegistro = now
	
    liquidacionDatos = Liquidacion.objects.get(id=liquidacionId)
    print("convenio de la liquidacion = " , liquidacionDatos.convenio_id);

    if (liquidacionDatos.convenio_id ==''):
            print("ENTRE convenio de la liquidacion = " + liquidacionDatos.convenio_id)
            return JsonResponse({'success': True, 'message': 'Favor ingresar Convenio a Facturar !', 'Factura' : 0 })


    servicioAmb = Servicios.objects.get(nombre='AMBULATORIO')
    #ingresoId = Ingresos.objects.all().filter(tipoDoc_id=usuarioId.documento_id).filter(documento_id=usuarioId.tipoDoc_id).filter(consec=usuarioId.consecAdmision)
    ingresoId = Ingresos.objects.get(tipoDoc_id=usuarioId.tipoDoc_id , documento_id=usuarioId.documento_id ,consec=usuarioId.consecAdmision)
    print ("ingresoId = ", ingresoId.id)

    if (ingresoId.salidaClinica=='N' and ingresoId.serviciosIng_id != servicioAmb.id  ):
	    return JsonResponse({'success': True, 'message': 'Paciente NO tiene Salida Clinica. Consultar medico tratante !', 'Factura' : 0 })

    # RUTINA ACUMULAR ABONOS RECIBIDOS



    # FIN RUTINA



    ## RUTINA ACTUALIZA DX, SERV , MEDIODE AMBULATORIOS

    if (ingresoId.serviciosIng_id == servicioAmb.id) :
  
       miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
       cur3 = miConexion3.cursor()
       comando = 'UPDATE admisiones_ingresos SET  "dxSalida_id"= "dxActual_id", "medicoSalida_id" = "medicoActual_id",  "serviciosSalida_id" = "serviciosActual_id"  WHERE id =  ' + "'" +  str(ingresoId.id) + "'"
       print(comando)
       cur3.execute(comando)
       miConexion3.commit()
       miConexion3.close()
		
    ## AQUI RUTINA HISATORICO CAMA-DEPENDENCIA 

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    #comando = 'INSERT INTO sitios_historialdependencias  (consec, "fechaLiberacion" , "fechaRegistro" , "estadoReg" , dependencias_id, documento_id, "tipoDoc_id", "usuarioRegistro_id", disponibilidad ) VALUES (' + str(ingresoId.consec) + ','  + "'" + str(fechaRegistro) + "','" +    str(fechaRegistro) + "',"  +  "'" + str('A') + "'," + "'" +  str(ingresoId.dependenciasActual_id) + "'," + "'" + str(ingresoId.documento_id) + "'," + "'" + str(ingresoId.tipoDoc_id) + "'," + "'" +  str(username_id) + "',''" + ")"
    comando = 'INSERT INTO sitios_historialdependencias (consec,"fechaLiberacion","fechaRegistro","estadoReg", dependencias_id,documento_id,"tipoDoc_id","usuarioRegistro_id",disponibilidad)  SELECT consec,' + "'" + str(fechaRegistro) + "'," + "'" + str(fechaRegistro) + "'," + "'" + str('A') + "'" + ", id" + ",'" + str(ingresoId.documento_id) + "'," + "'" + str(ingresoId.tipoDoc_id) + "'," + "'" + str(username_id) + "'," + "'" + str('L') + "'" +  ' from sitios_dependencias where "tipoDoc_id" = ' + "'" + str(ingresoId.tipoDoc_id) + "' AND documento_id = "  + "'" + str(ingresoId.documento_id) + "' AND consec = " + "'" + str(ingresoId.consec) + "'"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()


    ## FIN HISTORICO CAMAA-DEPENDENCIA


    ## AQUI RUTINA DESOCUPAR CAMA-DEPENDENCIA 

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE sitios_dependencias SET disponibilidad = ' + "'" + str('L') + "'," + ' "tipoDoc_id" = null , documento_id = null,  consec= null, "fechaLiberacion" = ' + "'" + str(fechaRegistro) + "'"  + ' WHERE "tipoDoc_id" = ' + "'" + str(ingresoId.tipoDoc_id) + "'" + ' AND documento_id = ' + "'" + str(ingresoId.documento_id) + "'" + ' AND consec = ' + str(ingresoId.consec)
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()


    ## FIN DESOCUPAR CAMA-DEPENDENCIA



    # PRIMERO EL CABEZOTE	

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_facturacion (documento_id, "consecAdmision", "fechaFactura", "totalCopagos", "totalCuotaModeradora","totalProcedimientos",   "totalSuministros", "totalFactura", "valorApagar", anulado, anticipos, "fechaRegistro", "estadoReg", "fechaAnulacion", observaciones, "fechaCorte",convenio_id, "tipoDoc_id","usuarioAnula_id","usuarioRegistro_id") SELECT documento_id, "consecAdmision", ' + "'" + str(fechaRegistro) + "'" + ' , "totalCopagos", "totalCuotaModeradora", "totalProcedimientos",  "totalSuministros", "totalLiquidacion", "valorApagar", anulado, anticipos, ' + "'" + str(fechaRegistro) + "'" + ' ,  ' + "'" + str('A') + "'" + ' , "fechaAnulacion", observaciones, "fechaCorte",convenio_id, "tipoDoc_id","usuarioAnula_id", ' + "'" + str(username_id) + "'" + ' FROM facturacion_liquidacion WHERE id =  ' + liquidacionId
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    # AQUI CONSEGUIR EL ID DE LA FACTURA RECIEN CREADA
    # LO MEJOR ES conseguir el id en el mismo insert

    #facturacionId = Facturacion.objects.all().filter(tipoDoc_id=usuarioId.documento_id).filter(documento_id=usuarioId.tipoDoc_id).filter(consecAdmision=usuarioId.consecAdmision)
    facturacionId = Facturacion.objects.get(tipoDoc_id=usuarioId.tipoDoc_id , documento_id=usuarioId.documento_id, consecAdmision=usuarioId.consecAdmision, convenio_id=usuarioId.convenio_id)

    print ("facturacionId = ", facturacionId.id)

    ## COLOCAR EN LA TABLA INGRESOS , LA FECHA DE EGRESO Y EL NUMERO DE LA FACTURA GENERADO

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",                                       password="pass123")
    curt = miConexiont.cursor()
    comando = 'UPDATE admisiones_ingresos SET "fechaSalida" = ' + "'" +  str(fechaRegistro) + "'" + ', factura = ' + str(facturacionId.id)  +  ', "dependenciasSalida_id" = "dependenciasActual_id" ' +  ' WHERE id =' + str(ingresoId.id)
    curt.execute(comando)
    miConexiont.commit()
    miConexiont.close()

    # AHORA EL DETALLE

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_facturaciondetalle ("consecutivoFactura", fecha, cantidad, "valorUnitario", "valorTotal",  cirugia, "fechaCrea", "fechaModifica", observaciones, "fechaRegistro", "estadoRegistro", "codigoCups_id", cums_id, "usuarioModifica_id", "usuarioRegistro_id", facturacion_id, "tipoHonorario_id", "tipoRegistro") SELECT  consecutivo, fecha, cantidad, "valorUnitario", "valorTotal",  cirUgia, "fechaCrea", "fechaModifica", observaciones, "fechaRegistro", "estadoRegistro", "codigoCups_id", cums_id, "usuarioModifica_id", "usuarioRegistro_id", ' + str(facturacionId.id) + ', "tipoHonorario_id", "tipoRegistro" FROM facturacion_liquidaciondetalle WHERE liquidacion_id =  ' + liquidacionId
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    ## AQUI BORRAMOS EL DETALLE DE LA LIQUIDACION

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'DELETE FROM facturacion_liquidaciondetalle WHERE liquidacion_id =  ' + liquidacionId
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    ## AQUI BORRAMOS EL CABEZOTE DE LA LIQUIDACION

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'DElETE FROM facturacion_liquidacion WHERE id =  ' + liquidacionId

    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Factura Elaborada!', 'Factura' : facturacionId.id })



def LeerTotales(request):

    print ("Entre Leer Totales" )
    liquidacionId = request.POST["liquidacionId"]
    print ("liquidacionId = ", liquidacionId)

    liquidacionId1 = Liquidacion.objects.get(id=liquidacionId)

    totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
    totalSuministros = (totalSuministros['totalS']) + 0
    print("totalSuministros", totalSuministros)
    totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
    totalProcedimientos = (totalProcedimientos['totalP']) + 0
    print("totalProcedimientos", totalProcedimientos)
    registroPago = Liquidacion.objects.get(id=liquidacionId)
    totalCopagos = registroPago.totalCopagos
    totalCuotaModeradora = registroPago.totalCuotaModeradora
    totalAnticipos = registroPago.anticipos
    totalAbonos = registroPago.totalAbonos
    totalRecibido = registroPago.totalRecibido
    totalAnticipos = registroPago.anticipos
    valorApagar = registroPago.valorApagar
    totalLiquidacion = registroPago.totalLiquidacion


    return JsonResponse({'totalSuministros':totalSuministros,'totalProcedimientos':totalProcedimientos,'totalCopagos':totalCopagos,
			     'totalCuotaModeradora':totalCuotaModeradora,'totalAnticipos':totalAnticipos, 'totalAbonos':totalAbonos, 'totalRecibido':totalRecibido, 'totalLiquidacion':totalLiquidacion, 'totalAPagar':valorApagar})



# Create your views here.
def load_dataFacturacion(request, data):
    print ("Entre load_data Facturacion")

    context = {}
    d = json.loads(data)

    username = d['username']
    sede = d['sede']
    username_id = d['username_id']

    nombreSede = d['nombreSede']
    print ("sede:", sede)
    print ("username:", username)
    print ("username_id:", username_id)


    desdeFecha = d['desdeFecha']
    hastaFecha = d['hastaFecha']
    desdeFactura = d['desdeFactura']
    hastaFactura = d['hastaFactura']
    bandera = d['bandera']


    # Combo Indicadores

    # Fin combo Indicadores


    facturacion = []

    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()

    print ("bandera = " , bandera)
   
    if bandera == "Por Fecha":

       print ("Entre por Fecha")
       detalle = 'SELECT facturas.id id , facturas."fechaFactura" fechaFactura, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" fechaIngreso , i."fechaSalida" fechaSalida, ser.nombre servicioNombreSalida, dep.nombre camaNombreSalida , diag.nombre dxSalida , conv.nombre convenio, conv.id convenioId , i."salidaClinica" salidaClinica FROM admisiones_ingresos i INNER JOIN sitios_serviciosSedes sd ON (sd."sedesClinica_id" = i."sedesClinica_id") INNER JOIN sitios_dependencias dep ON (dep."sedesClinica_id" = i."sedesClinica_id" AND dep."serviciosSedes_id" = sd.id AND dep.id = i."dependenciasSalida_id")  INNER JOIN sitios_dependenciastipo deptip  ON (deptip.id = dep."dependenciasTipo_id") INNER JOIN usuarios_usuarios u ON (u."tipoDoc_id" =  i."tipoDoc_id" AND u.id = i."documento_id" ) INNER JOIN usuarios_tiposDocumento tp ON (tp.id = u."tipoDoc_id") INNER JOIN clinico_servicios ser  ON ( ser.id  = i."serviciosSalida_id")  INNER JOIN clinico_Diagnosticos diag ON (diag.id = i."dxSalida_id") INNER JOIN facturacion_facturacion facturas ON (facturas.documento_id = i.documento_id and facturas."tipoDoc_id" = i."tipoDoc_id" and facturas."consecAdmision" = i.consec ) LEFT JOIN contratacion_convenios conv  ON (conv.id = facturas.convenio_id ) WHERE i."fechaSalida" between ' + "'" + str(desdeFecha) + "'" + '  and ' + "'" + str(hastaFecha) + "'" + ' AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND i."fechaSalida" is not null '

    else:

        print ("Entre por Factura")
        detalle = 'SELECT facturas.id id , facturas."fechaFactura" fechaFactura, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" fechaIngreso , i."fechaSalida" fechaSalida, ser.nombre servicioNombreSalida, dep.nombre camaNombreSalida , diag.nombre dxSalida , conv.nombre convenio, conv.id convenioId , i."salidaClinica" salidaClinica FROM admisiones_ingresos i INNER JOIN sitios_serviciosSedes sd ON (sd."sedesClinica_id" = i."sedesClinica_id") INNER JOIN sitios_dependencias dep ON (dep."sedesClinica_id" = i."sedesClinica_id" AND dep."serviciosSedes_id" = sd.id AND dep.id = i."dependenciasSalida_id")  INNER JOIN sitios_dependenciastipo deptip  ON (deptip.id = dep."dependenciasTipo_id") INNER JOIN usuarios_usuarios u ON (u."tipoDoc_id" =  i."tipoDoc_id" AND u.id = i."documento_id" ) INNER JOIN usuarios_tiposDocumento tp ON (tp.id = u."tipoDoc_id") INNER JOIN clinico_servicios ser  ON ( ser.id  = i."serviciosSalida_id")  INNER JOIN clinico_Diagnosticos diag ON (diag.id = i."dxSalida_id") INNER JOIN facturacion_facturacion facturas ON (facturas.documento_id = i.documento_id and facturas."tipoDoc_id" = i."tipoDoc_id" and facturas."consecAdmision" = i.consec ) LEFT JOIN contratacion_convenios conv  ON (conv.id = facturas.convenio_id ) WHERE facturas.id between ' + "'" + str(desdeFactura) + "'" + '  and ' + "'" + str(hastaFactura) + "'" + ' AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' i."fechaSalida" is not null '

    print(detalle)

    curx.execute(detalle)

    for id ,fechaFactura, tipoDoc, documento, nombre, consec , fechaIngreso , fechaSalida, servicioNombreSalida, camaNombreSalida , dxSalida , convenio, convenioId , salidaClinica in curx.fetchall():
        facturacion.append(
		{"model":"facturacion.facturacion","pk":id,"fields":
			{'id':id, 'fechaFactura':fechaFactura, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
                         'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida,
                         'servicioNombreSalida': servicioNombreSalida, 'camaNombreSalida': camaNombreSalida,
                         'dxSalida': dxSalida,'convenio':convenio, 'convenioId':convenioId, 'salidaClinica':salidaClinica}})

    miConexionx.close()
    print(facturacion)


    serialized1 = json.dumps(facturacion, default=serialize_datetime)

    return HttpResponse(serialized1, content_type='application/json')



def PostConsultaFacturacion(request):
    print ("Entre PostConsultaFacturacion")

    Post_id = request.POST["post_id"]
    username_id = request.POST["username_id"]

    # Abro Conexion

    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",password="pass123")
    cur = miConexionx.cursor()

    comando = 'select fac.id id, fac.id factura, fac."fechaFactura" fechaFactura, tip.nombre tipoDoc, documento_id documento, usu.nombre paciente, fac."consecAdmision" consecAdmision, conv.nombre nombreConvenio FROM facturacion_facturacion fac, contratacion_convenios conv, usuarios_usuarios usu, usuarios_tiposdocumento tip where fac.id = ' + "'" + str(Post_id) + "'" + '  AND  fac.convenio_id = conv.id and usu.id = fac.documento_id  and fac."tipoDoc_id" = usu."tipoDoc_id"   AND tip.id = fac."tipoDoc_id" AND fac.documento_id = usu.id  AND conv.id = fac.convenio_id '

    print(comando)

    cur.execute(comando)

    facturacion = []

    for id,factura , fechaFactura , tipoDoc, documento, paciente, consecAdmision , nombreConvenio in cur.fetchall():
            facturacion.append( {"id": id,"factura":factura, "fechaFactura" : fechaFactura, "tipoDoc":tipoDoc, "documento":documento,
                     "paciente": paciente, "consecAdmision": consecAdmision, "nombreConvenio": nombreConvenio
                                 })


    miConexionx.close()
    print(facturacion)

    # Cierro Conexion


    return JsonResponse({'pk':facturacion[0]['id'],'id':facturacion[0]['id'], 'factura':facturacion[0]['factura'],'fechaFactura':facturacion[0]['fechaFactura'],
		          'tipoDoc':facturacion[0]['tipoDoc'],'documento':facturacion[0]['documento'],'paciente':facturacion[0]['paciente'],  'consecAdmision':facturacion[0]['consecAdmision'],
                             'nombreConvenio':facturacion[0]['nombreConvenio']        })




def AnularFactura(request):
    print ("Entre AnularFactura")
    username_id = request.POST["username_id"]

    id = request.POST["id"]
    print ("el id es = ", id)

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE facturacion_facturacion SET "estadoRegistro" = ' + "'" + str('N') + "' WHERE id =  " + id
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()


    return JsonResponse({'success': True, 'message': 'Factura Anulada!'})


def ReFacturar(request):
    print ("Entre ReFacturar")
    usuarioRegistro = request.POST["username_id"]

    id = request.POST["id"]
    print ("el id es = ", id)

    facturacionId = Facturacion.objects.all().filter(id=id)

    now = datetime.datetime.now()
    print("NOW  = ", now)
    fechaRegistro = now

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE facturacion_facturacion SET "estadoRegistro" = ' + "'" + str('R') + "' WHERE id =  " + id
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()


    # Aquip hacer los INSERT A LIQUIDACION a partir de facturacion




    # Aquip hacer los INSERT A LIQUIDACIONDETALLE a partir de facturacion detalle



   ##  Aquip hacer el INSERT a la tabla facturacion_refactura



    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_refacturacion ( documento_id,"consecAdmision" ,fecha ,  "facturaInicial" ,  "facturaFinal" ,  "fechaRegistro" ,  "estadoRegistro" ,  "tipoDoc_id" ,  "usuarioRegistro_id" ) values (' + "'" + str(facturacionId.documento_id) + "','" + str(facturacionId.consecAdmision) + "',"  + str(facturacionid.id) + ',,' + "'" + str(fechaRegistro) + "'," + "'" + str('A') + "'," +  "'" + str(facturacionId.tipoDoc_id) + "','" +               str(usuarioRegistro) + "'"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Factura Anulada!'})


def ApliqueParcialAbonos(request):
    print ("Entre ApliqueParcialAbonos" )

    liquidacionId = request.POST['liquidacionIdA']
    tipoPago = request.POST['AtipoPago']
    formaPago = request.POST['AformaPago']
    valor = request.POST['AvalorAbono']  
    valorEnCurso = request.POST['AvalorEnCurso']  
    print ("liquidacionId  = ", liquidacionId )
    abonoId = request.POST['post_id']


    fechaRegistro = datetime.datetime.now()

    registroId = Liquidacion.objects.get(id=liquidacionId)
    print  ("registroId documento =" , registroId.documento_id)
    print  ("registroId tipoDoc =" , registroId.tipoDoc_id)
    print  ("registroId consec =" , registroId.consecAdmision)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'UPDATE cartera_Pagos SET "valorEnCurso" = ' + str(valorEnCurso) + ' WHERE id = ' + str(abonoId)
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Valor abono en curso guardado satisfactoriamente!'})


