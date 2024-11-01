from django.shortcuts import render
import json
from django import forms
import cv2
import numpy as np
from django.core.serializers import serialize
from django.db.models.functions import Cast, Coalesce
from django.utils.timezone import now
from django.db.models import Avg, Max, Min

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
from facturacion.models import ConveniosPacienteIngresos


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
   

    detalle = 'SELECT ' + "'" + str("INGRESO") + "'" +  ' tipoIng, i.id'  + "||" +"'" + '-INGRESO' + "'" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual , conv.nombre convenio FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"  AND fac.documento_id = i.documento_id and fac."tipoDoc_id" = i."tipoDoc_id" and fac."consecAdmision" = i.consec and fac.convenio_id = conv.id UNION SELECT ' + "'"  + str("TRIAGE") + "'" + ' tipoIng, t.id'  + "||" +"'" + '-TRIAGE' + "'" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual , conv.nombre convenio FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'" + ' AND fac.documento_id = t.documento_id and fac."tipoDoc_id" = t."tipoDoc_id" and fac."consecAdmision" = t.consec and fac.convenio_id = conv.id'

    print(detalle)

    curx.execute(detalle)

    for tipoIng, id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual , convenio in curx.fetchall():
        liquidacion.append(
		{"model":"ingresos.ingresos","pk":id,"fields":
			{'tipoIng':tipoIng, 'id':id, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
                         'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida,
                         'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                         'dxActual': dxActual,'convenio':convenio}})

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


    ingresoId = Ingresos.objects.get(id=llave[0])


    print ("tipodDoc_id =" ,ingresoId.tipoDoc_id)
    print("documento_id =", ingresoId.documento_id)
    print("consec =", ingresoId.consec)

    estadoReg= 'A'
    now = datetime.datetime.now()
    print("NOW  = ", now)
    fechaRegistro = now
    usuarioRegistro = ''
    convenioIdU = ConveniosPacienteIngresos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consecAdmision=ingresoId.consec).aggregate(minimo=Coalesce(Min('consecAdmision'), 0))
    convenioId = (convenioIdU['minimo']) + 0

    # Validacion si existe o No existe CABEZOTE

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")

    curt = miConexiont.cursor()
    comando = 'SELECT id FROM facturacion_liquidacion WHERE "tipoDoc_id" = ' + str(ingresoId.tipoDoc_id) + ' AND documento_id = ' + str(ingresoId.documento_id) + ' AND "consecAdmision" = ' + str(ingresoId.consec)
    curt.execute(comando)

    cabezoteLiquidacion = []

    for id in curt.fetchall():
        cabezoteLiquidacion.append({'id': id})

    miConexiont.close()

    if (cabezoteLiquidacion == []):
        # Si no existe liquidacion CABEZOTE se debe crear con los totales, abonos, anticipos, procedimiento, suministros etc
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432",       user="postgres", password="pass123")
        curt = miConexiont.cursor()
        comando = 'INSERT INTO facturacion_liquidacion ("tipoDoc_id", documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalProcedimientos" , "totalSuministros" , "totalLiquidacion", "valorApagar", anticipos, "fechaRegistro", "estadoRegistro", convenio_id,  "usuarioRegistro_id", "totalAbonos") VALUES (' + str(ingresoId.tipoDoc_id)  + ',' +  str(ingresoId.documento_id) + ',' + str(ingresoId.consec) + ',' +  "'" +  str(fechaRegistro) + "'," + '0,0,0,0,0,0,0,' + "'" + str(fechaRegistro) + "','" + str(estadoReg) + "'," + str(convenioId) + ',' + "'" + str(username_id) + "',0)"
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

    # Fin validacion de Liquidacion cabezote

    if request.method == 'POST':

        # Abro Conexion

        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",password="pass123")
        cur = miConexionx.cursor()

        comando = 'select liq.id id,  "consecAdmision",  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", observaciones, liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos", conv.nombre nombreConvenio, usu.nombre paciente FROM facturacion_liquidacion liq, contratacion_convenios conv, usuarios_usuarios usu, admisiones_ingresos adm where adm.id = ' + "'" + str(llave[0]) + "'" + '  AND  liq.convenio_id = conv.id and usu.id = liq.documento_id  and adm."tipoDoc_id" = liq."tipoDoc_id" AND adm.documento_id = liq.documento_id  AND adm.consec = liq."consecAdmision"'

        print(comando)

        cur.execute(comando)

        liquidacion = []

        for id,consecAdmision,fecha ,totalCopagos,totalCuotaModeradora,totalProcedimientos ,totalSuministros, totalLiquidacion, valorApagar, fechaCorte, anticipos, detalleAnulacion, fechaAnulacion, observaciones, fechaRegistro, estadoRegistro, convenio_id, tipoDoc_id , documento_id, usuarioRegistro_id, totalAbonos, nombreConvenio , paciente in cur.fetchall():
            liquidacion.append( {"id": id,
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
            "totalAbonos": totalAbonos, "nombreConvenio": nombreConvenio,   "paciente": paciente
                                 })


        miConexionx.close()
        print(liquidacion)

        # Cierro Conexion


        return JsonResponse({'pk':liquidacion[0]['id'],'id':id, 'consecAdmision':liquidacion[0]['consecAdmision'],'fecha':liquidacion[0]['fecha'],
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
                             'paciente': liquidacion[0]['paciente'], 'Suministros':suministros, 'Cups':cups
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

    nombreSede = d['nombreSede']
    print("sede:", sede)
    print("username:", username)
    print("username_id:", username_id)

    # Abro Conexion para la Liquidacion Detalle

    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur = miConexionx.cursor()

    comando = 'select liq.id id,consecutivo ,  cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , exa.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro"  FROM facturacion_liquidaciondetalle liq inner join clinico_examenes exa on (exa.id = liq."codigoCups_id")  where liquidacion_id= ' + valor +  ' UNION select liq.id id,consecutivo , cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , sum.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro"  FROM facturacion_liquidaciondetalle liq inner join facturacion_suministros sum on (sum.id = liq.cums_id)  where liquidacion_id= '  + valor + ' order by 1'

    print(comando)

    cur.execute(comando)

    liquidacionDetalle = []

    for id, consecutivo, fecha, cantidad, valorUnitario, valorTotal, cirugia, fechaCrea, observaciones, estadoRegistro, codigoCups_id, cums_id, nombreExamen, liquidacion_id, tipoHonorario_id, tipoRegistro in cur.fetchall():
        liquidacionDetalle.append(
            {"model": "liquidacionDetalle.liquidacionDetalle", "pk": id, "fields":
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
                 "tipoRegistro": tipoRegistro}})

    miConexionx.close()
    print(liquidacionDetalle)

    # Cierro Conexion

    serialized1 = json.dumps(liquidacionDetalle, default=decimal_serializer)
    #serialized1 = json.dumps(liquidacionDetalle, default=serialize_datetime)
    #serialized1 = json.dumps(liquidacionDetalle, safe=False)
    #serialized1 = json.dumps(liquidacionDetalle)

    return HttpResponse(serialized1, content_type='application/json')
    #return HttpResponse(serialized1, safe=False)

