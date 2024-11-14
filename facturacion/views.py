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
from cartera.models import TiposPagos, FormasPagos, Pagos


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
   

    detalle = 'SELECT ' + "'" + str("INGRESO") + "'" +  ' tipoIng, i.id'  + "||" +"'" + "-'||conv.id" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual , conv.nombre convenio, conv.id convenioId FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"  AND fac.documento_id = i.documento_id and fac."tipoDoc_id" = i."tipoDoc_id" and fac."consecAdmision" = i.consec and fac.convenio_id = conv.id UNION SELECT ' + "'"  + str("TRIAGE") + "'" + ' tipoIng, t.id'  + "||" +"'" + "-'||conv.id" + ' id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual , conv.nombre convenio, conv.id convenioId   FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser , facturacion_conveniospacienteingresos fac,contratacion_convenios conv WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'" + ' AND fac.documento_id = t.documento_id and fac."tipoDoc_id" = t."tipoDoc_id" and fac."consecAdmision" = t.consec and fac.convenio_id = conv.id'

    print(detalle)

    curx.execute(detalle)

    for tipoIng, id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual , convenio, convenioId in curx.fetchall():
        liquidacion.append(
		{"model":"ingresos.ingresos","pk":id,"fields":
			{'tipoIng':tipoIng, 'id':id, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
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

    convenioId = llave[1]
    print ("Convenio = " , convenioId)

    # Combo TiposPagos

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre nombre FROM cartera_tiposPagos c order by c.nombre'

    curt.execute(comando)
    print(comando)

    tiposPagos = []

    tiposPagos.append({'id': '', 'nombre': ''})

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

    formasPagos.append({'id': '', 'nombre': ''})

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

        comando = 'select liq.id id,  "consecAdmision",  fecha ,  "totalCopagos" ,  "totalCuotaModeradora" ,  "totalProcedimientos" ,"totalSuministros", "totalLiquidacion", "valorApagar", "fechaCorte", anticipos, "detalleAnulacion", "fechaAnulacion", observaciones, liq."fechaRegistro", "estadoRegistro", convenio_id, liq."tipoDoc_id" , liq.documento_id, liq."usuarioRegistro_id", "totalAbonos", conv.nombre nombreConvenio, usu.nombre paciente, adm.id ingresoId1, usu.documento documento, tip.nombre tipoDocumento FROM facturacion_liquidacion liq, contratacion_convenios conv, usuarios_usuarios usu, admisiones_ingresos adm, usuarios_tiposdocumento  tip where adm.id = ' + "'" + str(llave[0]) + "'" + '  AND  liq.convenio_id = conv.id and usu.id = liq.documento_id  and adm."tipoDoc_id" = liq."tipoDoc_id"   AND tip.id = adm."tipoDoc_id" AND adm.documento_id = liq.documento_id  AND adm.consec = liq."consecAdmision" AND conv.id = ' + str(convenioId)

        print(comando)

        cur.execute(comando)

        liquidacion = []

        for id,consecAdmision,fecha ,totalCopagos,totalCuotaModeradora,totalProcedimientos ,totalSuministros, totalLiquidacion, valorApagar, fechaCorte, anticipos, detalleAnulacion, fechaAnulacion, observaciones, fechaRegistro, estadoRegistro, convenio_id, tipoDoc_id , documento_id, usuarioRegistro_id, totalAbonos, nombreConvenio , paciente, ingresoId1 , documento, tipoDocumento in cur.fetchall():
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
            "totalAbonos": totalAbonos, "nombreConvenio": nombreConvenio,   "paciente": paciente,
            "ingresoId1": ingresoId1, "documento": documento, "tipoDocumento": tipoDocumento
                                 })


        miConexionx.close()
        print(liquidacion)

        # Cierro Conexion

        totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
        totalSuministros = (totalSuministros['totalS']) + 0
        print("totalSuministros", totalSuministros)
        totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
        totalProcedimientos = (totalProcedimientos['totalP']) + 0
        print("totalProcedimientos", totalProcedimientos)
        totalCopagos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=4).aggregate(totalC=Coalesce(Sum('valor'), 0))
        totalCopagos = (totalCopagos['totalC']) + 0
        print("totalCopagos", totalCopagos)
        totalCuotaModeradora = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=3).aggregate(
            totalM=Coalesce(Sum('valor'), 0))
        totalCuotaModeradora = (totalCuotaModeradora['totalM']) + 0
        print("totalCuotaModeradora", totalCuotaModeradora)
        totalAnticipos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=1).aggregate(Anticipos=Coalesce(Sum('valor'), 0))
        totalAnticipos = (totalAnticipos['Anticipos']) + 0
        print("totalAnticipos", totalAnticipos)
        totalAbonos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter( consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=2).aggregate(totalAb=Coalesce(Sum('valor'), 0))
        totalAbonos = (totalAbonos['totalAb']) + 0
        # totalAbonos = totalCopagos + totalAnticipos + totalCuotaModeradora
        print("totalAbonos", totalAbonos)
        totalLiquidacion = totalSuministros + totalProcedimientos - totalAbonos
        print("totalLiquidacion", totalLiquidacion)
        totalAPagar = totalLiquidacion - totalAbonos
        print("totalAPagar", totalAPagar)

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
                             'paciente': liquidacion[0]['paciente'], 'Suministros':suministros, 'Cups':cups,
			     'totalSuministros':totalSuministros,'totalProcedimientos':totalProcedimientos,'totalCopagos':totalCopagos,
			     'totalCuotaModeradora':totalCuotaModeradora,'totalAnticipos':totalAnticipos, 'totalAbonos':totalAbonos,
			     'totalLiquidacion':totalLiquidacion, 'totalAPagar':totalAPagar, 'TiposPagos':tiposPagos, 'FormasPagos':formasPagos,
			     'ingresoId1': ingresoId1, 'documento': documento, 'tipoDocumento': tipoDocumento
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

    comando = 'select liq.id id,consecutivo ,  cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , exa.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro" , liq."estadoRegistro" estadoReg FROM facturacion_liquidaciondetalle liq inner join clinico_examenes exa on (exa.id = liq."codigoCups_id")  where liquidacion_id= ' + "'" +  str(valor) + "'" +  ' UNION select liq.id id,consecutivo , cast(date(fecha)||\' \'||to_char(fecha, \'HH:MI:SS\') as text) fecha  ,  liq.cantidad ,  "valorUnitario" ,  "valorTotal" ,  cirugia ,  cast(date("fechaCrea")||\' \'||to_char("fechaCrea", \'HH:MI:SS\') as text)  fechaCrea , liq.observaciones ,  "estadoRegistro" ,  "codigoCups_id" ,  cums_id , sum.nombre  nombreExamen  ,  liquidacion_id ,  liq."tipoHonorario_id" ,  "tipoRegistro" , liq."estadoRegistro" estadoReg FROM facturacion_liquidaciondetalle liq inner join facturacion_suministros sum on (sum.id = liq.cums_id)  where liquidacion_id= '  + "'" +  str(valor) + "'" + ' order by consecutivo'

    print(comando)

    cur.execute(comando)

    liquidacionDetalle = []

    for id, consecutivo, fecha, cantidad, valorUnitario, valorTotal, cirugia, fechaCrea, observaciones, estadoRegistro, codigoCups_id, cums_id, nombreExamen, liquidacion_id, tipoHonorario_id, tipoRegistro, estadoReg in cur.fetchall():
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
    comando = 'insert into cartera_Pagos ("fecha", "tipoDoc_id" , documento_id, consec,  "tipoPago_id" , "formaPago_id", valor, descripcion ,"fechaRegistro","estadoReg") values ('  + "'" + str(fechaRegistro) + "'," +  "'" + str(registroId.tipoDoc_id) + "'" + ' , ' + "'" + str(registroId.documento_id) + "'" + ', ' + "'" + str(registroId.consecAdmision) + "'" + '  , ' + "'" + str(tipoPago) + "'" + '  , ' + "'" + str(formaPago) + "'" + ', ' + "'" + str(valor) + "',"   + "'" + str(descripcion) + "','"   + str(fechaRegistro) + "'," + "'" +  str("A") + "');"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Abono Actualizado satisfactoriamente!'})

def PostDeleteAbonosFacturacion(request):

    print ("Entre PostDeleteAbonosFacturacion" )

    id = request.POST["id"]
    print ("el id es = ", id)

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'UPDATE carteraPagosSET "estadoReg" = ' + "'" + str('N') + "' WHERE id =  " + id
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
    #valorTotal = request.POST['valorTotal']
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

    #return HttpResponse("Convenio Adicionado", content_type='application/json')

    return JsonResponse({'success': True, 'message': 'Abono Actualizado satisfactoriamente!'})

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

    #return HttpResponse("Convenio Adicionado", content_type='application/json')

    return JsonResponse({'success': True, 'message': 'Registro Actualizado satisfactoriamente!'})


def load_dataAbonosFacturacion(request, data):
    print("Entre  load_dataAbonosFacturacion")

    context = {}
    d = json.loads(data)

    ingresoId = d['ingresoId']
    sede = d['sede']

    print("sede:", sede)
    print("ingresoId:", ingresoId)

    # print("data = ", request.GET('data'))

    abonos  = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curx = miConexionx.cursor()

    detalle = 'SELECT pag.id id , i."tipoDoc_id" tipoDoc , i.documento_id documentoId ,u.documento documento,u.nombre nombre,i.consec consec , tipdoc.nombre nombreDocumento , cast(date(pag.fecha) as text)  fecha, pag."tipoPago_id" tipoPago , pag."formaPago_id" formaPago, pag.valor valor, pag.descripcion descripcion ,tip.nombre tipoPagoNombre,forma.nombre formaPagoNombre FROM admisiones_ingresos i, cartera_pagos pag ,usuarios_usuarios u ,usuarios_tiposdocumento tipdoc, cartera_tiposPagos tip, cartera_formasPagos forma WHERE i.id = ' + "'" + str(ingresoId) + "'" + ' and i.documento_id = u.id and i."tipoDoc_id" = pag."tipoDoc_id" and i.documento_id  = pag.documento_id and  i.consec = pag.consec AND tipdoc.id = i."tipoDoc_id" and pag."tipoPago_id" = tip.id and pag."formaPago_id" = forma.id'
    print(detalle)

    curx.execute(detalle)

    for id, tipoDoc, documentoId, documento, nombre, consec, nombreDocumento , fecha, tipoPago, formaPago, valor, descripcion, tipoPagoNombre,formaPagoNombre,  in curx.fetchall():
        abonos.append(
            {"model": "cartera_pagos.cartera_pagos", "pk": id, "fields":
                {'id': id, 'tipoDoc': tipoDoc, 'documentoId': documentoId, 'nombre':nombre,'consec':consec,  'nombreDocumento': nombreDocumento,
                 'fecha': fecha, 'tipoPago': tipoPago, 'formaPago': formaPago, 'valor':valor, 'descripcion':descripcion,'tipoPagoNombre': tipoPagoNombre, 'formaPagoNombre': formaPagoNombre}})

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

    usuarioId = Liquidacion.objects.all().filter(id=liquidacionId)
    print ("Usuario", usuarioId.documento_id)
    print ("TipoDoc", usuarioId.tipoDoc_id)
    print ("Consec", usuarioId.consec)

    # PRIMERO EL CABEZOTE	

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_facturacion (documento_id, "consecAdmision", "fechaFactura", "totalCopagos", "totalCuotaModeradora", "totalSuministros", "totalFactura", "valorApagar", anulado, anticipos, "fechaRegistro", "estadoReg", "fechaAnulacion", observaciones, "fechaCorte",convenio_id, "tipoDoc_id","usuarioAnula_id","usuarioRegistro_id") SELECT documento_id, "consecAdmision", fecha, "totalCopagos", "totalCuotaModeradora", "totalSuministros", "totalLiquidacion", "valorApagar", anulado, anticipos, "fechaRegistro", "estadoRegistro", "fechaAnulacion", observaciones, "fechaCorte",convenio_id, "tipoDoc_id","usuarioAnula_id","usuarioRegistro_id" FROM facturacion_liquidacion WHERE id =  ' + liquidacionId
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    # AQUI CONSEGUIR EL ID DE LA FACTURA RECIEN CREADA
    # LO MEJOR ES conseguir el id en el mismo insert

    facturacionId = Facturacion.objects.all().filter(tipoDoc_id=usuarioId.documento_id).filter(documento_id=usuarioId.tipoDoc_id).filter(consec=usuarioId.consec)

    #facturacionIdU = Facturacion.objects.all().aggregate(maximo=Coalesce(Max('id'), 0))
    #facturacionId = (facturacionIdU['maximo']) + 0
    #facturacionId = str(facturacionId)
    #facturacionId = facturacionId.replace("(", ' ')
    #facturacionId = facturacionId.replace(")", ' ')
    #facturacionId = facturacionId.replace(",", ' ')

    ## COLOCAR EN LA TABLA INGRESOS , LA FECHA DE EGRESO Y EL NUMERO DE LA FACTURA GENERADO

    now = datetime.datetime.now()
    print("NOW  = ", now)
    fechaRegistro = now

    ingresoId = Ingresos.objects.all().filter(tipoDoc_id=usuarioId.documento_id).filter(documento_id=usuarioId.tipoDoc_id).filter(consec=usuarioId.consec)

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",                                       password="pass123")
    curt = miConexiont.cursor()
    comando = 'UPDATE admisiones_ingresos SET "fechaSalida" = ' + str(fechaRegistro) + ', factura = ' + str(facturacionId)  + ' WHERE id =' + str(ingresoId)
    curt.execute(comando)
    miConexiont.commit()
    miConexiont.close()

    # AHORA EL DETALLE

    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()

    comando = 'INSERT INTO facturacion_facturaciondetalle ("consecutivoFactura", fecha, cantidad, "valorUnitario", "valorTotal",  cirugia, "fechaCrea", "fechaModifica", observaciones, "fechaRegistro", "estadoRegistro", "codigoCups_id", cums_id, "usuarioModifica_id", "usuarioRegistro_id", facturacion_id, "tipoHonorario_id", "tipoRegistro") SELECT  consecutivo, fecha, cantidad, "valorUnitario", "valorTotal",  cirUgia, "fechaCrea", "fechaModifica", observaciones, "fechaRegistro", "estadoRegistro", "codigoCups_id", cums_id, "usuarioModifica_id", "usuarioRegistro_id", ' + str(facturacionId) + ', "tipoHonorario_id", "tipoRegistro" FROM facturacion_liquidaciondetalle WHERE liquidacion_id =  ' + liquidacionId
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

    return JsonResponse({'success': True, 'message': 'Factura Elaborada!', 'Factura' : facturacionId })



def LeerTotales(request):

    print ("Entre Leer Totales" )
    liquidacionId = request.POST["liquidacionId"]
    print ("liquidacionId = ", liquidacionId)

    totalSuministros = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(codigoCups_id = None).exclude(estadoRegistro='N').aggregate(totalS=Coalesce(Sum('valorTotal'), 0))
    totalSuministros = (totalSuministros['totalS']) + 0
    print("totalSuministros", totalSuministros)
    totalProcedimientos = LiquidacionDetalle.objects.all().filter(liquidacion_id=liquidacionId).filter(cums_id = None).exclude(estadoRegistro='N').aggregate(totalP=Coalesce(Sum('valorTotal'), 0))
    totalProcedimientos = (totalProcedimientos['totalP']) + 0
    print("totalProcedimientos", totalProcedimientos)
    totalCopagos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=4).aggregate(totalC=Coalesce(Sum('valor'), 0))
    totalCopagos = (totalCopagos['totalC']) + 0
    print("totalCopagos", totalCopagos)
    totalCuotaModeradora = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=3).aggregate(
            totalM=Coalesce(Sum('valor'), 0))
    totalCuotaModeradora = (totalCuotaModeradora['totalM']) + 0
    print("totalCuotaModeradora", totalCuotaModeradora)
    totalAnticipos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter(consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=1).aggregate(Anticipos=Coalesce(Sum('valor'), 0))
    totalAnticipos = (totalAnticipos['Anticipos']) + 0
    print("totalAnticipos", totalAnticipos)
    totalAbonos = Pagos.objects.all().filter(tipoDoc_id=ingresoId.tipoDoc_id).filter(documento_id=ingresoId.documento_id).filter( consec=ingresoId.consec).exclude(estadoReg='N').filter(formaPago_id=2).aggregate(totalAb=Coalesce(Sum('valor'), 0))
    totalAbonos = (totalAbonos['totalAb']) + 0
    # totalAbonos = totalCopagos + totalAnticipos + totalCuotaModeradora
    print("totalAbonos", totalAbonos)
    totalLiquidacion = totalSuministros + totalProcedimientos - totalAbonos
    print("totalLiquidacion", totalLiquidacion)
    totalAPagar = totalLiquidacion - totalAbonos
    print("totalAPagar", totalAPagar)

    return JsonResponse({'totalSuministros':totalSuministros,'totalProcedimientos':totalProcedimientos,'totalCopagos':totalCopagos,
			     'totalCuotaModeradora':totalCuotaModeradora,'totalAnticipos':totalAnticipos, 'totalAbonos':totalAbonos,'totalLiquidacion':totalLiquidacion, 'totalAPagar':totalAPagar})



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
   
    if bandera == "Por Fecha":

       detalle = 'SELECT i.id id , facturas."fechaFactura" fechaFactura, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" fechaIngreso , i."fechaSalida" fechaSalida, ser.nombre servicioNombreSalida, dep.nombre camaNombreSalida , diag.nombre dxSalida , conv.nombre convenio, conv.id convenioId , i."salidaClinica" salidaClinica, estadosalida.nombre estadoSalida FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , contratacion_convenios conv , facturacion_facturacion facturas, clinico_estadossalida estadoSalida WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND  i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosSalida_id" = ser.id AND i."salidaClinica" = ' + "'" + str('S') + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and  u.id = i."documento_id" and diag.id = i."dxSalida_id" and i."fechaSalida" is not null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasSalida_id" AND facturas.documento_id = i.documento_id and facturas."tipoDoc_id" = i."tipoDoc_id" and facturas."consecAdmision" = i.consec and facturas.convenio_id = conv.id and estadosalida.id = i."salidaMotivo_id" and i."fechaSalida" between ' + "'" + str(desdeFecha) + "'" + '  and ' + "'" + str(hastaFecha) + "'"

    else:
       detalle = 'SELECT i.id id , facturas."fechaFactura" fechaFactura, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" fechaIngreso , i."fechaSalida" fechaSalida, ser.nombre servicioNombreSalida, dep.nombre camaNombreSalida , diag.nombre dxSalida , conv.nombre convenio, conv.id convenioId , i."salidaClinica" salidaClinica, estadosalida.nombre estadoSalida FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , contratacion_convenios conv , facturacion_facturacion facturas, clinico_estadossalida estadoSalida WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND  i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosSalida_id" = ser.id AND i."salidaClinica" = ' + "'" + str('S') + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and  u.id = i."documento_id" and diag.id = i."dxSalida_id" and i."fechaSalida" is not null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasSalida_id" AND facturas.documento_id = i.documento_id and facturas."tipoDoc_id" = i."tipoDoc_id" and facturas."consecAdmision" = i.consec and facturas.convenio_id = conv.id and estadosalida.id = i."salidaMotivo_id" and i."fechaSalida" between ' + "'" + str(desdeFactura) + "'" + ' and ' + str(hastaFactura) + "'"

    print(detalle)

    curx.execute(detalle)

    for id ,fechaFactura, tipoDoc, documento, nombre, consec , fechaIngreso , fechaSalida, servicioNombreSalida, camaNombreSalida , dxSalida , convenio, convenioId , salidaClinica, estadoSalida in curx.fetchall():
        facturacion.append(
		{"model":"ingresos.ingresos","pk":id,"fields":
			{'id':id, 'fechaFactura':fechafactura, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
                         'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida,
                         'servicioNombreSalida': servicioNombreSalida, 'camaNombreSalida': camaNombreSalida,
                         'dxSalida': dxSalida,'convenio':convenio, 'convenioId':convenioId, 'salidaClinica':salidaClinica, 'estadoSalida':estadoSalida}})

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