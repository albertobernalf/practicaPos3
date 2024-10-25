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


# Create your views here.

def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 


# Create your views here.
def load_dataConvenios(request, data):
    print ("Entre load_data Convenios")

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

    # Combo Empresas

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM facturacion_empresas c"

    curt.execute(comando)
    print(comando)

    empresas = []

    for id, nombre in curt.fetchall():
        empresas.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(empresas)

    context['Empresas'] = empresas

    # Fin combo empresas

    # Combo Tipos Tarifa

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM tarifas_TiposTarifa c"

    curt.execute(comando)
    print(comando)

    tiposTarifa = []

    for id, nombre in curt.fetchall():
        tiposTarifa.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposTarifa)

    context['TiposTarifa'] = tiposTarifa

    # Fin combo Tipos Tarifa


    # Combo Cups

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c."codigoCups" codigoCups, c.nombre nombre FROM clinico_examenes c order by c.nombre'

    curt.execute(comando)
    print(comando)

    cups = []

    for id, codigoCups, nombre in curt.fetchall():
        cups.append({'id': id, 'codigoCups':codigoCups,  'nombre': nombre})

    miConexiont.close()
    print(cups)

    context['Cups'] = cups

    # Fin combo Cups

    # Combo Concpetos

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id, c.nombre nombre FROM facturacion_conceptos c order by c.nombre'

    curt.execute(comando)
    print(comando)

    conceptos = []

    for id, codigoCups, nombre in curt.fetchall():
        conceptos.append({'id': id, 'codigoCups':codigoCups,  'nombre': nombre})

    miConexiont.close()
    print(conceptos)

    context['Conceptos'] = conceptos

    # Fin combo conceptos

    convenios = []


    
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   
    detalle = 'select conv.id id,conv.nombre nombre, "vigenciaDesde" vigenciaDesde, "vigenciaHasta" vigenciaHasta, emp.nombre  empresa from contratacion_convenios conv, facturacion_empresas emp WHERE emp.id = conv.empresa_id '

    print(detalle)

    curx.execute(detalle)

    for id, nombre, vigenciaDesde, vigenciaHasta, empresa  in curx.fetchall():
        convenios.append(
		{"model":"convenios.convenios","pk":id,"fields":
			{'id':id, 'nombre': nombre, 'vigenciaDesde': vigenciaDesde, 'vigenciaHasta': vigenciaHasta, 'empresa': empresa,
                         }})

    miConexionx.close()
    print(convenios)
    context['Convenios'] = convenios
    convenios.append({"model":"convenios.convenios","pk":id,"fields":{'empresas':empresas}})
    convenios.append({"model":"convenios.convenios","pk":id,"fields":{'tiposTarifa':tiposTarifa}})
    convenios.append({"model":"convenios.convenios","pk":id,"fields":{'cups':cups}})
    convenios.append({"model":"convenios.convenios","pk":id,"fields":{'conceptos':conceptos}})


    serialized1 = json.dumps(convenios, default=serialize_datetime)


    return HttpResponse(serialized1, content_type='application/json')



def PostConsultaConvenios(request):
    print ("Entre PostConsultaConvenios ")


    Post_id = request.POST["post_id"]

    print("id = ", Post_id)
    llave = Post_id.split('-')
    print ("llave = " ,llave)
    print ("primero=" ,llave[0])



    if request.method == 'POST':

        # Abro Conexion

        conveniosD = []

    
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
        curx = miConexionx.cursor()
   
        detalle = 'select conv.id id,conv.nombre nombre, "vigenciaDesde" vigenciaDesde, "vigenciaHasta" vigenciaHasta, emp.nombre  empresa,   "porcTarifario",  "porcSuministros",  "valorOxigeno" ,  "porcEsterilizacion",  "porcMaterial" ,  hospitalario ,  urgencias ,  ambulatorio ,  "consultaExterna" ,  copago ,  moderadora ,   tipofactura ,  agrupada ,  "facturacionSuministros" ,  "facturacionCups" ,  "cuentaContable" ,  requisitos  from contratacion_convenios conv, facturacion_empresas emp WHERE emp.id = conv.empresa_id and  conv.id = ' + "'" + str(Post_id) + "'"

        print(detalle)

        curx.execute(detalle)

        for id, nombre, vigenciaDesde, vigenciaHasta, empresa,  porcTarifario,  porcSuministros,  valorOxigeno ,  porcEsterilizacion,  porcMaterial ,  hospitalario ,  urgencias ,  ambulatorio ,  consultaExterna ,  copago ,  moderadora ,   tipofactura ,  agrupada ,  facturacionSuministros ,  facturacionCups ,  cuentaContable ,  requisitos   in curx.fetchall():
           conveniosD.append(
		{"model":"convenios.convenios","pk":id,"fields":
			{'id':id, 'nombre': nombre, 'vigenciaDesde': vigenciaDesde, 'vigenciaHasta': vigenciaHasta, 'empresa': empresa,
          
             'porcTarifario': porcTarifario, 'porcSuministros': porcSuministros,
             'valorOxigeno': valorOxigeno,
             'porcEsterilizacion': porcEsterilizacion,
             'porcMaterial': porcMaterial,
             'hospitalario': hospitalario,
             'urgencias': urgencias,
             'ambulatorio': ambulatorio,
             'consultaExterna': consultaExterna,
             'copago': copago,
             'moderadora': moderadora,
             'tipofactura': tipofactura,
             'agrupada': agrupada,
             'facturacionSuministros': facturacionSuministros,
             'facturacionCups': facturacionCups,
             'cuentaContable': cuentaContable,
             'requisitos': requisitos }})

        miConexionx.close()
        print(conveniosD)

        # Cierro Conexion

        print ("Prueba convenioNombre" , conveniosD[0]['fields']['nombre'])


        return JsonResponse({'pk':conveniosD[0]['pk'], 'id':conveniosD[0]['pk'], 'nombre':conveniosD[0]['fields']['nombre'],'vigenciaDesde':conveniosD[0]['fields']['vigenciaDesde'],
                             'vigenciaHasta':conveniosD[0]['fields']['vigenciaHasta'],  'empresa': conveniosD[0]['fields']['empresa'],
                             'porcTarifario':conveniosD[0]['fields']['porcTarifario'] ,    'porcSuministros':conveniosD[0]['fields']['porcSuministros'],
                             'valorOxigeno': conveniosD[0]['fields']['valorOxigeno'],
                             'porcEsterilizacion': conveniosD[0]['fields']['porcEsterilizacion'],
                             'porcMaterial': conveniosD[0]['fields']['porcMaterial'],
                             'hospitalario': conveniosD[0]['fields']['hospitalario'],
                             'urgencias': conveniosD[0]['fields']['urgencias'],
                             'ambulatorio': conveniosD[0]['fields']['ambulatorio'],
                             'consultaExterna': conveniosD[0]['fields']['consultaExterna'],
                             'copago': conveniosD[0]['fields']['copago'],
                             'moderadora': conveniosD[0]['fields']['moderadora'],
                             'tipofactura': conveniosD[0]['fields']['tipofactura'],
                             'agrupada': conveniosD[0]['fields']['agrupada'],
                             'facturacionSuministros': conveniosD[0]['fields']['facturacionSuministros'],
                             'facturacionCups': conveniosD[0]['fields']['facturacionCups'],
                             'cuentaContable': conveniosD[0]['fields']['cuentaContable'],
                             'requisitos': conveniosD[0]['fields']['requisitos']
                             })

    else:
        return JsonResponse({'errors':'Something went wrong!'})


# Create your views here.
def load_dataConveniosProcedimientos(request, data):
    print ("Entre load_data Conveniosrocedimientos")

    context = {}
    d = json.loads(data)

    username = d['username']
    sede = d['sede']
    username_id = d['username_id']

    nombreSede = d['nombreSede']
    print ("sede:", sede)
    print ("username:", username)
    print ("username_id:", username_id)

    convenioId = d['valor']
    

    #print("data = ", request.GET('data'))

    convenios = []

    
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   
    detalle = 'select conv.id id, convProc."codigoHomologado" codigoHomologado, convProc.valor valor,  convProc.cups_id cupsId ,exa.nombre cupsNombre, tipostar.nombre tarifa FROM contratacion_convenios conv , contratacion_conveniosprocedimientos convProc, tarifas_tipostarifa tipostar, clinico_examenes exa WHERE conv.id = convProc.convenio_id and convProc."tipoTarifa_id" = tipostar.id and convProc.cups_id = exa.id and conv.id = ' + "'" + str(convenioId) + "'"

    print(detalle)

    curx.execute(detalle)

    conveniosP = []

    for id, codigoHomologado, valor,  cupsId ,cupsNombre,tarifa in curx.fetchall():
            conveniosP.append( {"id": id,
                     "codigoHomologado": codigoHomologado,
                     "valor": valor,
                     "cupsId": cupsId, "cupsNombre": cupsNombre,
                     "tarifa": tarifa })

    miConexionx.close()
    print(conveniosP)

    context['ConveniosP'] = conveniosP


    serialized1 = json.dumps(conveniosP, default=serialize_datetime)


    return HttpResponse(serialized1, content_type='application/json')




def GuardarConveniosProcedimientos( request):

    if request.method == 'POST':

        codigoHomologado = request.POST["codigoHomologado"]
        tiposTarifa = request.POST["tiposTarifa"]
        nombreTiposTarifa = request.POST["nombreTiposTarifa"]
        cups = request.POST["cups"]
        nombreCups = request.POST["nombreCups"]
        valor = request.POST["valor"]
        convenioId = request.POST["convenioId"]
     
        if tiposTarifa == '':
           tiposTarifa="null"

        if cups == '':
            cups ="null"


        estadoReg= 'A'
        username_id = request.POST["username_id"]
        fechaRegistro = datetime.datetime.now()

     

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
        curt = miConexiont.cursor()
        comando = 'INSERT INTO contratacion_conveniosprocedimientos ("codigoHomologado", valor, "fechaRegistro", "estadoReg", convenio_id, cups_id, "tiposTarifa_id", "usuarioRegistro_id") values (' + "'" + star(codigoHomologado) + "'," + "'" + str(valor) + "'," + "'" + str(fechaRegistro) +"'," + "'" + str(estadoReg) + "'," + "'" + str(convenioId) + "'," + "'" + str(cups) + "'," + "'" + str(tiposTarifa) + "'," + "'" + str(username_id) + "'"

        print(comando)
        curt.execute(comando)
        miConexiont.commit()
        miConexiont.close()



        return JsonResponse({'success': True, 'message': 'Convenio Creado satisfactoriamente!'})



def GuardarConvenio( request):

    print ("Entre Guardar Convenio")	

    if request.method == 'POST':

        convenioId=request.POST["convenioId"]
        nombre = request.POST["nombre"]
        empresa=request.POST["empresa"]
        vigenciaDesde=request.POST["vigenciaDesde"]
        vigenciaHasta=request.POST["vigenciaHasta"]

        porcTarifario=request.POST["porcTarifario"]
        porcSuministros=request.POST["porcSuministros"]
        valorOxigeno=request.POST["valorOxigeno"]
        porcEsterilizacion=request.POST["porcEsterilizacion"]
        porcMaterial=request.POST["porcMaterial"]
        hospitalario=request.POST["hospitalario"]
        urgencias=request.POST["urgencias"]
        consultaExterna=request.POST["consultaExterna"]
        copago=request.POST["copago"]
        moderadora=request.POST["moderadora"]
        tipoFactura=request.POST["tipoFactura"]
        agrupada=request.POST["agrupada"]
        facturacionSuministros=request.POST["facturacionSuministros"]
        facturacionCups=request.POST["facturacionCups"]
        cuentaContable=request.POST["cuentaContable"]
        requisitos=request.POST["requisitos"]

        if vigenciaDesde == '':
            vigenciaDesde="0001-01-01 00:00:00"

        if vigenciaHasta == '':
            vigenciaHasta="0001-01-01 00:00:00"

        if porcTarifario == '':
            porcTarifario=0

        if porcSuministros == '':
            porcSuministros=0

        if valorOxigeno == '':
            valorOxigeno=0

        if porcEsterilizacion == '':
            porcEsterilizacion=0

        if porcMaterial == '':
            porcMaterial=0


        estadoReg= 'A'
        username_id = request.POST["username_id"]
        fechaRegistro = datetime.datetime.now()

        #ultId = Convenios.objects.all().aggregate(maximo=Coalesce(Max('id'), 0 ))
        #ultId1 = (ultId['maximo']) + 1

     

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
        curt = miConexiont.cursor()

        comando = 'INSERT INTO contratacion_convenios (nombre,empresa_id,"vigenciaDesde","vigenciaHasta","porcTarifario", "porcSuministros", "valorOxigeno", "porcEsterilizacion", "porcMaterial",hospitalario, urgencias,"consultaExterna",copago, moderadora, "tipofactura",agrupada,"facturacionSuministros","facturacionCups", "cuentaContable", requisitos,"fechaRegistro","estadoReg","usuarioRegistro_id") VALUES (' + "'" + str(nombre) + "'," + "'" + str(empresa) + "'," + "'" + str(vigenciaDesde) + "'," + "'" + str(vigenciaHasta) + "',"  +  str(porcTarifario) + "," + str(porcSuministros) + "," + str(valorOxigeno) + "," + str(porcEsterilizacion) + ","  + str(porcMaterial) + "," + "'" + str(hospitalario) + "'," + "'" + str(urgencias) + "'," + "'" + str(consultaExterna) + "'," + "'" + str(copago) + "'," + "'" + str(moderadora) + "'," + "'" + str(tipoFactura) + "'," + "'" + str(agrupada) + "'," + "'" + str(facturacionSuministros) + "'," + "'" + str(facturacionCups) + "'," + "'" + str(cuentaContable) + "'," + "'" + str(requisitos) + "'," + "'" + str(fechaRegistro) + "'," + "'" + str(estadoReg) + "'," + "'" + str(username_id) + "')"



        print(comando)
        curt.execute(comando)
        miConexiont.commit()
        miConexiont.close()



        return JsonResponse({'success': True, 'message': 'Convenio Creado satisfactoriamente!'})




def GuardarConvenio1( request):

    print ("Entre Guardar Convenio1")	

    if request.method == 'POST':

        convenioId=request.POST["convenioId"]
        print("convenioId = " , convenioId)
        nombre=request.POST["nombre"]
        empresa=request.POST["empresa"]
        vigenciaDesde=request.POST["vigenciaDesde"]
        vigenciaHasta=request.POST["vigenciaHasta"]
        porcTarifario=request.POST["porcTarifario"]
        porcSuministros=request.POST["porcSuministros"]
        valorOxigeno=request.POST["valorOxigeno"]
        porcEsterilizacion=request.POST["porcEsterilizacion"]
        porcMaterial=request.POST["porcMaterial"]
        hospitalario=request.POST["hospitalario"]
        urgencias=request.POST["urgencias"]
        consultaExterna=request.POST["consultaExterna"]
        copago=request.POST["copago"]
        moderadora=request.POST["moderadora"]
        tipoFactura=request.POST["tipoFactura"]
        agrupada=request.POST["agrupada"]
        facturacionSuministros=request.POST["facturacionSuministros"]
        facturacionCups=request.POST["facturacionCups"]
        cuentaContable=request.POST["cuentaContable"]
        requisitos=request.POST["requisitos"]

        if vigenciaDesde == '':
            vigenciaDesde="0001-01-01 00:00:00"

        if vigenciaHasta == '':
            vigenciaHasta="0001-01-01 00:00:00"



        estadoReg= 'A'
        username_id = request.POST["username_id"]
        fechaRegistro = datetime.datetime.now()



     

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
        curt = miConexiont.cursor()

        #comando = 'UPDATE contratacion_convenios (nombre,empresa_id,"vigenciaDesde","vigenciaHasta",tarifa, "porcTarifario", "porcSuministros", "valorOxigeno", "porcEsterilizacion", "porcMaterial",hospitalario, urgencias,"consultaExterna",copago, moderadora, "tipoFactura",agrupada,"facturacionSuministros","facturacionCups", "cuentaContable", requisitos,"fechaRegistro",estadoReg,"usuarioRegistro_id") VALUES (' + "'" + str(nombre) + "'," + "'" + str(empresa) + "'," + "'" + str(vigenciaDesde) + "'," + "'" + str(vigenciaHasta) + "'," + "'" + str(tarifa) + "'," + "'" + str(porcTarifario) + "'," + "'" + str(porcSuministros) + "'," + "'" + str(valorOxigeno) + "'," + "'" + str(porcEsterilizacion) + "'," + "'" + str(porcMaterial) + "'," + "'" + str(hospitalario) + "'," + "'" + str(urgencias) + "'," + "'" + str(consultaExterna) + "'," + "'" + str(copago) + "'," + "'" + str(moderadora) + "'," + "'" + str(tipoFactura) + "'," + "'" + str(agrupada) + "'," + "'" + str(acturacionSuministros) + "'," + "'" + str(facturacionCups) + "'," + "'" + str(cuentaContable) + "'," + "'" + str(requisitos) + "'," + "'" + str(fechaRegistro) + "'," + "'" + str(estadoReg) + "'," + "'" + str(username_id) + "'"
        comando = 'UPDATE contratacion_convenios set nombre = ' + "'" + str(nombre) + "'," + '"vigenciaDesde" = ' + "'" + str(vigenciaDesde) + "'," + '"vigenciaHasta" = ' + "'" + str(vigenciaHasta) + "'," + '"porcTarifario" = ' + "'" + str(porcTarifario) + "'," + '"porcSuministros" = ' + "'" + str(porcSuministros) + "'," + '"valorOxigeno" = ' + "'" + str(valorOxigeno) + "'," + '"porcEsterilizacion" = ' + "'" + str(porcEsterilizacion) + "'," + 'hospitalario = ' + "'" + str(hospitalario) + "'," + 'urgencias = ' + "'" + str(urgencias) + "'," + '"consultaExterna" = ' + "'" + str(consultaExterna) + "'," + 'copago = ' + "'" + str(copago) + "'," + 'moderadora = ' + "'" + str(moderadora) + "'," + 'agrupada = ' + "'" + str(agrupada) + "'," + '"facturacionSuministros" = ' + "'" + str(facturacionSuministros) + "'," + '"facturacionCups" = ' + "'" + str(facturacionCups) + "'," + '"cuentaContable" = ' + "'" + str(cuentaContable) + "'," + 'requisitos = ' + "'" + str(requisitos) + "'," + '"fechaRegistro" = ' + "'" + str(fechaRegistro) + "'," + 'estadoReg = ' + "'" + str(estadoReg) + "'," + '"usuarioRegistro_id" = ' + "'" + str(username_id) + "'" + ' WHERE id = ' + "'" + str(convenioId) + "'"


        print(comando)
        curt.execute(comando)
        miConexiont.commit()
        miConexiont.close()



        return JsonResponse({'success': True, 'message': 'Convenio Creado satisfactoriamente!'})



def GrabarTarifa( request):

    print ("Entre Grabar Tarifa")	

    if request.method == 'POST':

        estadoReg= 'A'
        username_id = request.POST["username_id"]
        fechaRegistro = datetime.datetime.now()

  

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
        curt = miConexiont.cursor()

        comando = 'INSERT INTO contratacion_convenios (nombre,empresa_id,"vigenciaDesde","vigenciaHasta","porcTarifario", "porcSuministros", "valorOxigeno", "porcEsterilizacion", "porcMaterial",hospitalario, urgencias,"consultaExterna",copago, moderadora, "tipofactura",agrupada,"facturacionSuministros","facturacionCups", "cuentaContable", requisitos,"fechaRegistro","estadoReg","usuarioRegistro_id") VALUES (' + "'" + str(nombre) + "'," + "'" + str(empresa) + "'," + "'" + str(vigenciaDesde) + "'," + "'" + str(vigenciaHasta) + "',"  +  str(porcTarifario) + "," + str(porcSuministros) + "," + str(valorOxigeno) + "," + str(porcEsterilizacion) + ","  + str(porcMaterial) + "," + "'" + str(hospitalario) + "'," + "'" + str(urgencias) + "'," + "'" + str(consultaExterna) + "'," + "'" + str(copago) + "'," + "'" + str(moderadora) + "'," + "'" + str(tipoFactura) + "'," + "'" + str(agrupada) + "'," + "'" + str(facturacionSuministros) + "'," + "'" + str(facturacionCups) + "'," + "'" + str(cuentaContable) + "'," + "'" + str(requisitos) + "'," + "'" + str(fechaRegistro) + "'," + "'" + str(estadoReg) + "'," + "'" + str(username_id) + "')"



        print(comando)
        curt.execute(comando)
        miConexiont.commit()
        miConexiont.close()



        return JsonResponse({'success': True, 'message': 'Tarifa Creada satisfactoriamente!'})
