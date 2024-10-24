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

    convenios = []

    
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   
    detalle = 'select conv.id id,conv.nombre nombre, "vigenciaDesde" vigenciaDesde, "vigenciaHasta" vigenciaHasta, emp.nombre  empresa, tar.nombre tarifa from contratacion_convenios conv, facturacion_empresas emp, tarifas_tipostarifa tar WHERE emp.id = conv.empresa_id and tar.id = conv."tipoTarifa_id"'

    print(detalle)

    curx.execute(detalle)

    for id, nombre, vigenciaDesde, vigenciaHasta, empresa, tarifa  in curx.fetchall():
        convenios.append(
		{"model":"convenios.convenios","pk":id,"fields":
			{'id':id, 'nombre': nombre, 'vigenciaDesde': vigenciaDesde, 'vigenciaHasta': vigenciaHasta, 'empresa': empresa,
                         'tarifa': tarifa}})

    miConexionx.close()
    print(convenios)
    context['Convenios'] = convenios


    serialized1 = json.dumps(convenios, default=serialize_datetime)


    return HttpResponse(serialized1, content_type='application/json')
