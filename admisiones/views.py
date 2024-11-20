from django.shortcuts import render
import MySQLdb
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from django.views.generic import ListView, CreateView, TemplateView
from .forms import crearAdmisionForm
from admisiones.models import Ingresos
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.db.models.functions import Cast, Coalesce
import pyodbc
import psycopg2
from datetime import datetime
from decimal import Decimal

import pytz
import tzlocal
# import datetime as dt


from admisiones.models import Ingresos, Furips
from admisiones.forms import furipsForm
from sitios.models import  HistorialDependencias, Dependencias, ServiciosSedes, SubServiciosSedes
from usuarios.models import Usuarios, TiposDocumento
from planta.models import Planta
from facturacion.models import ConveniosPacienteIngresos
from rips.models import  RipsDestinoEgreso
import datetime

# Create your views here.


def menuAcceso(request):
    print("Ingreso a acceso")

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)
    context = {}
    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes

    return render(request, "inicio/accesoPrincipal1.html", context)

def validaAcceso(request):
    print("Hola Entre a validar el acceso Principal")

    context = {}
    username = request.POST["username"].strip()
    print("username=", username)
    contrasena = request.POST["password"]
    #perfilConseguido = request.POST["seleccion1"]
    sede = request.POST["seleccion2"]
    Sede = sede
    print("Sede Mayuscula = ", Sede)
    print(contrasena)
    #print("perfilConseguido= ", perfilConseguido)
    print("sede= ", sede)
    context = {}
    context['Documento'] = username
    context['Username'] = username
    #context['Perfil'] = perfilConseguido
    context['Sede'] = sede

    # Variables que tengo en context : Documento, Perfil , Sede,   sedes ,NombreSede

    print (context['Documento'])

    # Consigo la sede Nombre

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT id, nombre   FROM sitios_sedesClinica WHERE id ='" + sede + "'"
    cur.execute(comando)
    print(comando)

    nombreSede = []

    for id, nombre  in cur.fetchall():
        nombreSede.append({'id':id , 'nombre' : nombre})

    miConexion.close()
    print("ESTA ES EL NOMBRE DE LA SEDE :")
    print (nombreSede[0]['nombre'])

    context['NombreSede'] =  nombreSede[0]['nombre']

    # esta consulta por que se pierde de otras pantallas

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes


    #miConexion0 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion0 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur0 = miConexion0.cursor()
    comando = 'select p.id  Username_id , p.nombre profesional , p."sedesClinica_id" from planta_planta p where p.documento = ' + "'"  + username + "'"
    cur0.execute(comando)
    print(comando)
    planta = []
    profesional = ''

    for Username_id, profesional, sedesClinica_id in cur0.fetchall():
        planta.append({'Username_id': Username_id, 'profesional': profesional, 'sedesClinica_id': sedesClinica_id})
        context['Username_id'] = Username_id
        profesional = profesional

    context['Profesional'] = profesional
    print ("Profesional = ", context['Profesional'] )
    miConexion0.close()

    if planta == []:


        context['Error'] = "Personal invalido ! "
        print("Entre por personal No encontrado")

        miConexion0.close()

        return render(request, "inicio/accesoPrincipal1.html", context)

    else:


        #miConexion1 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexion1 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        cur1 = miConexion1.cursor()
        comando = "select p.contrasena contrasena from planta_planta p where p.documento ='" + username + "'" + " AND contrasena = '" + contrasena +"'"
        cur1.execute(comando)

        plantaContrasena = []



        for contrasena in cur1.fetchall():
            plantaContrasena.append({'contrasena': contrasena})

        if plantaContrasena == []:
            miConexion1.close()
            context['Error'] = "Contraseña invalida ! "
            return render(request, "inicio/accesoPrincipal1.html", context)
        else:
            print("OJOOO ya valide CONTRASENA")
            #Aqui ya se valido username y contraseña OK

            #miConexion2 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
            miConexion2 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
            cur2 = miConexion2.cursor()
            #comando = "select perf.tiposPlanta_id  perfil from planta_planta p , planta_perfilesplanta perf , planta_tiposPlanta tp where  p.sedesClinica_id = perf.sedesClinica_id and  p.sedesClinica_id ='" + str(sede) + "' AND p.documento =  '" + str(username) + "' AND perf.planta_id = p.id AND  perf.tiposPlanta_id = " + str(perfilConseguido)

            #comando = 'select gralusu."perfilesClinicaId_id"  perfil from planta_planta p, seguridad_perfilesclinica perf, seguridad_perfilesgralusu  gralusu where p."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND p.documento = ' + "'"  +  str(username) + "'" + ' and p.id = gralusu."plantaId_id" AND gralusu."perfilesClinicaId_id" = perf.id AND gralusu."perfilesClinicaId_id" = '  + str(perfilConseguido)
            comando =  'select perfcli.id perfil1 from seguridad_perfilesgralusu gral, sitios_sedesClinica sedes, seguridad_perfilesclinica perfcli, planta_planta planta where planta."sedesClinica_id" = sedes.id and planta.id=gral."plantaId_id" and perfcli.id = gral."perfilesClinicaId_id" and sedes.id = ' + "'" +  str(sede) + "'" +   ' AND  planta.documento = ' + "'" + str(username) + "'"
            print(comando)
            cur2.execute(comando)

            perfil = []

            for perfil1 in cur2.fetchall():
                perfil.append({'perfil1': perfil1})
                
            print ("OJOOO esto es perfil", perfil)
            miConexion2.close()

            if perfil == []:

                print ("Entre Perfil No autorizado para la sede!")
                context['Error'] = "Perfil No autorizado para la sede! "
                return render(request, "inicio/accesoPrincipal1.html", context)

            else:

                ## AQUI BORRRE MUCHOS COMBOS


                # Combo Modulos

                # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
                miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
                curt = miConexiont.cursor()

                comando = "SELECT c.id id,c.nombre nombre, c.nomenclatura nomenclatura, c.logo logo FROM seguridad_modulos c"

                curt.execute(comando)
                print(comando)

                modulos = []

                for id, nombre, nomenclatura, logo in curt.fetchall():
                    modulos.append({'id': id, 'nombre': nombre,'nomenclatura':nomenclatura, 'logo':logo})

                miConexiont.close()
                print(modulos)

                context['Modulos'] = modulos

                # Fin combo Modulos

                # Combo PermisosGrales

                miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
                curt = miConexiont.cursor()

                #comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
                comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(username) + "'"

                curt.execute(comando)
                print(comando)

                permisosGrales = []

                for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
                    permisosGrales.append({'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo,'modulo_id':modulo_id, 'modulo_nombre':modulo_nombre })

                miConexiont.close()
                print(permisosGrales)

                context['PermisosGrales'] = permisosGrales


                # Fin Combo PermisosGrales

                # Combo PermisosDetalle

                miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
                curt = miConexiont.cursor()

                comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo, modeledef.nombre nombreOpcion ,elemen.nombre nombreElemento from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli, seguridad_perfilesclinicaopciones perfopc, seguridad_perfilesusu perfdet, seguridad_moduloselementosdef modeledef, seguridad_moduloselementos elemen where planta.id= 1 and  planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and gral.id = perfdet."plantaId_id" and perfdet."perfilesClinicaOpcionesId_id" = perfopc.id and perfopc."perfilesClinicaId_id" =perfcli.id and  perfopc."modulosElementosDefId_id" = modeledef.id and elemen.id = modeledef."modulosElementosId_id"  and planta.documento = ' + "'"  + username + "'"

                curt.execute(comando)
                print(comando)

                permisosDetalle = []

                for id, nombre, nomenclatura, logo , nombreOpcion , nombreElemento in curt.fetchall():
                    permisosDetalle.append({'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion':nombreOpcion, 'nombreElemento':nombreElemento})

                miConexiont.close()
                print(permisosDetalle)

                context['PermisosDetalle'] = permisosDetalle

                # Fin Combo PermisosDetalle

                print (perfil[0])

    return render(request, "inicio/PantallaPrincipal.html", context)


def escogeAcceso(request, Sede, Username, Profesional, Documento, NombreSede, escogeModulo ):
    print ("Entre Escoge Acceso")

    username = Username
    sede = Sede
    #perfilConseguido = Perfil
    profesional = Profesional
    documento = Documento
    nombreSede = NombreSede
    escogeModulo = escogeModulo

    print("username = ", username)
    print("sede= ", sede)
    print("escogeModulo= ", escogeModulo)
    print("documento= ", documento)
    print("nombreSede= ", nombreSede)
    print("profesional= ", profesional)

    ## username_id
    usernameLlave = Planta.objects.get(documento=username.strip())
    username_id= usernameLlave.id


    ## Fin username_id



    # Combo PermisosGrales

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(username) + "'"

    curt.execute(comando)
    print(comando)

    permisosGrales = []

    for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
        permisosGrales.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
             'modulo_nombre': modulo_nombre})

    miConexiont.close()
    print(permisosGrales)

    # Fin Combo PermisosGrales
    print("permisosGrales= ", permisosGrales)

    context = {}
    context['PermisosGrales'] = permisosGrales
    context['Documento'] = documento
    context['Username'] = username
    context['Profesional'] = profesional
    context['Sede'] = sede
    context['PermisosGrales'] = permisosGrales
    context['NombreSede'] = nombreSede
    context['EscogeModulo'] = escogeModulo
    context['Username_id'] = username_id



    # aqui la manada de combos organizarlo segun necesidades


    # Combo de Servicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id AND ser.nombre != ' + "'" + str('TRIAGE') + "'"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios

    # Fin combo servicios

    # Combo de SubServicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id"'
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)

    context['SubServicios'] = subServicios

    # Fin combo SubServicios

    # Combo TiposDOc
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM usuarios_TiposDocumento "
    curt.execute(comando)
    print(comando)

    tiposDoc = []
    tiposDoc.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDoc.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDoc)

    context['TiposDoc'] = tiposDoc

    # Fin combo TiposDOc

    # Combo Habitaciones
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = ' SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip where dep."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND tip.nombre=' + "'" + str('HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id'
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    context['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    # Combo Especialidades
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Especialidades"
    curt.execute(comando)
    print(comando)

    especialidades = []
    especialidades.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidades)

    context['Especialidades'] = especialidades

    # Fin combo Especialidades

    # Combo EspecialidadesMedicos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT em.id ,e.nombre FROM clinico_Especialidades e, clinico_EspecialidadesMedicos em,planta_planta pl  where em."especialidades_id" = e.id and em."planta_id" = pl.id AND pl.documento = ' + "'" + str(username) + "'"
    curt.execute(comando)
    print(comando)

    especialidadesMedicos = []
    especialidadesMedicos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidadesMedicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidadesMedicos)

    context['EspecialidadesMedicos'] = especialidadesMedicos

    # Fin combo EspecialidadesMedicos

    # Combo Medicos
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT med.id id, med.nombre nombre FROM planta_planta p,clinico_medicos med, planta_tiposPlanta tp WHERE p."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' and p."tiposPlanta_id" = tp.id and tp.nombre = ' + "'" + str('MEDICO') + "'" + ' and med.planta_id = p.id'

    curt.execute(comando)
    print(comando)

    medicos = []
    medicos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        medicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicos)

    context['Medicos'] = medicos

    # Fin combo Medicos

    # Combo TiposFolio

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT e.id id, e.nombre nombre FROM clinico_tiposFolio e"

    curt.execute(comando)
    print(comando)

    tiposFolio = []
    tiposFolio.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposFolio.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposFolio)

    context['TiposFolio'] = tiposFolio

    # Fin combo TiposFolio

    # Combo TiposUsuario

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposusuario p"

    curt.execute(comando)
    print(comando)

    tiposUsuario = []
    # tiposUsuario.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposUsuario.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposUsuario)

    context['TiposUsuario'] = tiposUsuario

    # Fin combo Tipos Usuario

    # Combo TiposDocumento

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposDocumento p"

    curt.execute(comando)
    print(comando)

    tiposDocumento = []
    # tiposDocumento.append({'id': '', 'nombre': ''})

    tiposDocumento.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDocumento.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDocumento)

    context['TiposDocumento'] = tiposDocumento

    # Fin combo TiposDocumento

    # Combo Centros

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM sitios_centros p"

    curt.execute(comando)
    print(comando)

    centros = []

    for id, nombre in curt.fetchall():
        centros.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDocumento)

    context['Centros'] = centros

    # Fin combo Centros

    # Combo Diagnosticos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM clinico_diagnosticos p"

    curt.execute(comando)
    print(comando)

    diagnosticos = []
    diagnosticos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        diagnosticos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(diagnosticos)

    context['Diagnosticos'] = diagnosticos

    # Fin combo Diagnosticos

    # Combo Pais

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_paises d"

    curt.execute(comando)
    print(comando)

    pais = []

    for id, nombre in curt.fetchall():
        pais.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(pais)

    context['Pais'] = pais

    # Fin combo Pais



    # Combo Departamentos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_departamentos d"

    curt.execute(comando)
    print(comando)

    departamentos = []

    for id, nombre in curt.fetchall():
        departamentos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(departamentos)

    context['Departamentos'] = departamentos

    # Fin combo Departamentos

    # Combo Ciudades

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id, c.nombre  nombre FROM sitios_ciudades c"

    curt.execute(comando)
    print(comando)

    ciudades = []

    for id, nombre in curt.fetchall():
        ciudades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ciudades)

    context['Ciudades'] = ciudades

    # Fin combo Ciudades

    # Combo Modulos

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre, c.nomenclatura nomenclatura, c.logo logo FROM seguridad_modulos c"

    curt.execute(comando)
    print(comando)

    modulos = []

    for id, nombre, nomenclatura, logo in curt.fetchall():
        modulos.append({'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo})

    miConexiont.close()
    print(modulos)

    context['Modulos'] = modulos

    # Fin combo Modulos

    # Combo PermisosGrales

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(
        username) + "'"

    curt.execute(comando)
    print(comando)

    permisosGrales = []

    for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
        permisosGrales.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
             'modulo_nombre': modulo_nombre})

    miConexiont.close()
    print(permisosGrales)

    context['PermisosGrales'] = permisosGrales

    # Fin Combo PermisosGrales

    # Combo PermisosDetalle

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo, modeledef.nombre nombreOpcion ,elemen.nombre nombreElemento from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli, seguridad_perfilesclinicaopciones perfopc, seguridad_perfilesusu perfdet, seguridad_moduloselementosdef modeledef, seguridad_moduloselementos elemen where planta.id= 1 and  planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and gral.id = perfdet."plantaId_id" and perfdet."perfilesClinicaOpcionesId_id" = perfopc.id and perfopc."perfilesClinicaId_id" =perfcli.id and  perfopc."modulosElementosDefId_id" = modeledef.id and elemen.id = modeledef."modulosElementosId_id"  and planta.documento = ' + "'" + username + "'"

    curt.execute(comando)
    print(comando)

    permisosDetalle = []

    for id, nombre, nomenclatura, logo, nombreOpcion, nombreElemento in curt.fetchall():
        permisosDetalle.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion': nombreOpcion,
             'nombreElemento': nombreElemento})

    miConexiont.close()
    print(permisosDetalle)

    context['PermisosDetalle'] = permisosDetalle

    # Fin Combo PermisosDetalle

    ## Hasta aquo FIN contexto para todas las Pantallas


    # Combo Vias Ingreso

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_viasingreso c"

    curt.execute(comando)
    print(comando)

    viasIngreso = []

    for id, nombre in curt.fetchall():
        viasIngreso.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(viasIngreso)

    context['ViasIngreso'] = viasIngreso

    # Fin combo vias Ingreso

    # Combo Causas Externa

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_causasExterna c"

    curt.execute(comando)
    print(comando)

    causasExterna = []

    for id, nombre in curt.fetchall():
        causasExterna.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(causasExterna)

    context['CausasExterna'] = causasExterna

    # Fin combo causasExterna

    # Combo Regimenes

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_regimenes c"

    curt.execute(comando)
    print(comando)

    regimenes = []

    for id, nombre in curt.fetchall():
        regimenes.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(regimenes)

    context['Regimenes'] = regimenes

    # Fin combo regimenes


    # Combo Tipos Cotizante

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_tiposcotizante c"

    curt.execute(comando)
    print(comando)

    tiposCotizante = []

    for id, nombre in curt.fetchall():
        tiposCotizante.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposCotizante)

    context['TiposCotizante'] = tiposCotizante

    # Fin combo tiposCotizante

    # Combo municipios

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_municipios c"

    curt.execute(comando)
    print(comando)

    municipios = []

    for id, nombre in curt.fetchall():
        municipios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(municipios)

    context['Municipios'] = municipios

    # Fin combo municipios

    # Combo localidades

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_localidades c"

    curt.execute(comando)
    print(comando)

    localidades = []

    for id, nombre in curt.fetchall():
        localidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(localidades)

    context['Localidades'] = localidades

    # Fin combo localidades


    # Combo estadoCivil

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_estadocivil c"

    curt.execute(comando)
    print(comando)

    estadoCivil = []

    for id, nombre in curt.fetchall():
        estadoCivil.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(estadoCivil)

    context['EstadoCivil'] = estadoCivil

    # Fin combo estadoCivil


    # Combo ocupaciones

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_ocupaciones c"

    curt.execute(comando)
    print(comando)

    ocupaciones = []

    for id, nombre in curt.fetchall():
        ocupaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ocupaciones)

    context['Ocupaciones'] = ocupaciones

    # Fin combo ocupaciones


    # Combo ips

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_ips c"

    curt.execute(comando)
    print(comando)

    ips = []
    ips.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        ips.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ips)

    context['Ips'] = ips

    # Fin combo ips

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

    # Combo Acompanantes

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre nombre FROM usuarios_usuarioscontacto c, basicas_tiposcontacto t where  c."tiposContacto_id" = t.id and t.nombre like (' + "'" + str('%ACOMPA%') + "')"

    curt.execute(comando)
    print(comando)

    acompanantes = []
    acompanantes.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        acompanantes.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(acompanantes)

    context['Acompanantes'] = acompanantes

    # Fin combo Acompanantes

    # Combo responsables

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT c.id id,c.nombre nombre FROM usuarios_usuarioscontacto c, basicas_tiposcontacto t where  c."tiposContacto_id" = t.id and t.nombre like (' + "'" + str('%RESPONSA%') + "')"

    curt.execute(comando)
    print(comando)

    responsables = []
    responsables.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        responsables.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(responsables)

    context['Responsables'] = responsables

    # Fin combo responsables


    ## fin manada de combis


   # Aqui ya vienen las validaciones de permisos de acceso
    # Se valida el aaceso al Modulo


    if (escogeModulo == 'ADMISIONES'):
        print ("WENTRE ADMISIONES 4")
        print("escogeModulo = ", escogeModulo)

        # Combo Convenios

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM contratacion_convenios p"

        curt.execute(comando)
        print(comando)

        convenios = []

        for id, nombre in curt.fetchall():
            convenios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("convenios", convenios)

        context['Convenios'] = convenios

        # Fin combo Convenios

        # Combo TiposPagos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM cartera_tipospagos p"

        curt.execute(comando)
        print(comando)

        tiposPagos = []

        for id, nombre in curt.fetchall():
            tiposPagos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("tiposPagos", tiposPagos)

        context['TiposPagos'] = tiposPagos

        # Fin combo tiposPagos


        # Combo FormasPagos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM cartera_formaspagos p"

        curt.execute(comando)
        print(comando)

        formasPagos = []

        for id, nombre in curt.fetchall():
            formasPagos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("formasPagos", formasPagos)

        context['FormasPagos'] = formasPagos

        # Fin combo tiposPagos


        # Combo ripsServiciosIng

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_RipsServicios  p"

        curt.execute(comando)
        print(comando)

        ripsServiciosIng = []
        ripsServiciosIng.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsServiciosIng.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsServiciosIng", ripsServiciosIng)

        context['RipsServiciosIng'] = ripsServiciosIng

        # Fin combo ripsServiciosIng

        # Combo ripsmodalidadGrupoServicioTecSal

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_RipsModalidadAtencion   p"

        curt.execute(comando)
        print(comando)

        ripsmodalidadGrupoServicioTecSal = []
        ripsmodalidadGrupoServicioTecSal.append({'id': '', 'nombre': ''})


        for id, nombre in curt.fetchall():
            ripsmodalidadGrupoServicioTecSal.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsmodalidadGrupoServicioTecSal", ripsmodalidadGrupoServicioTecSal)

        context['RipsmodalidadGrupoServicioTecSal'] = ripsmodalidadGrupoServicioTecSal

        # Fin combo ripsmodalidadGrupoServicioTecSal

        # Combo ripsViaIngresoServicioSalud

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsviasingresosalud  p"

        curt.execute(comando)
        print(comando)

        ripsViaIngresoServicioSalud = []
        ripsViaIngresoServicioSalud.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsViaIngresoServicioSalud.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsViaIngresoServicioSalud", ripsViaIngresoServicioSalud)

        context['RipsViaIngresoServicioSalud'] = ripsViaIngresoServicioSalud

        # Fin combo ripsViaIngresoServicioSalud

        # Combo ripsGrupoServicios

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsGrupoServicios  p"

        curt.execute(comando)
        print(comando)

        ripsGrupoServicios = []
        ripsGrupoServicios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsGrupoServicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsGrupoServicios", ripsGrupoServicios)

        context['RipsGrupoServicios'] = ripsGrupoServicios

        # Fin combo ripsGrupoServicios

        # Combo ripsCondicionDestinoUsuarioEgreso

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsdestinoegreso  p"

        curt.execute(comando)
        print(comando)

        ripsCondicionDestinoUsuarioEgreso = []
        ripsCondicionDestinoUsuarioEgreso.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsCondicionDestinoUsuarioEgreso.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsCondicionDestinoUsuarioEgreso", ripsCondicionDestinoUsuarioEgreso)

        context['RipsCondicionDestinoUsuarioEgreso'] = ripsCondicionDestinoUsuarioEgreso

        # Fin combo ripsCondicionDestinoUsuarioEgreso

        # Combo ripsCausaMotivoAtencion

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripscausaexterna  p"

        curt.execute(comando)
        print(comando)

        ripsCausaMotivoAtencion = []
        ripsCausaMotivoAtencion.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsCausaMotivoAtencion.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsCausaMotivoAtencion", ripsCausaMotivoAtencion)

        context['RipsCausaMotivoAtencion'] = ripsCausaMotivoAtencion

        # Fin combo ripsCausaMotivoAtencion

        # Combo ripsDestinoUsuarioEgresoRecienNacido

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsdestinoegreso  p"

        curt.execute(comando)
        print(comando)

        ripsDestinoUsuarioEgresoRecienNacido = []
        ripsDestinoUsuarioEgresoRecienNacido.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            ripsDestinoUsuarioEgresoRecienNacido.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsDestinoUsuarioEgresoRecienNacido", ripsDestinoUsuarioEgresoRecienNacido)

        context['RipsDestinoUsuarioEgresoRecienNacido'] = ripsDestinoUsuarioEgresoRecienNacido

        # Fin combo ripsDestinoUsuarioEgresoRecienNacido



        ## Aqui contexto para solo admisiones

        ingresos = []

        # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curx = miConexionx.cursor()

        detalle = 'SELECT i.id id, tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
            Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and ser.nombre != ' + "'" + str('TRIAGE') + "'" + ' AND dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"'
        print(detalle)

        curx.execute(detalle)

        for id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
            ingresos.append({'id':id, 'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                             'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                             'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                             'DxActual': dxActual})

        miConexionx.close()
        print(ingresos)
        context['Ingresos'] = ingresos


        context['EspecialidadesMedicos'] = especialidadesMedicos

        # Fin combo EspecialidadesMedicos
        ## Para los froms FURIPS

        context['FuripsForm'] = furipsForm


        # Combo Indicadores

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        #comando = "SELECT c.id id,c.nombre nombre FROM clinico_viasAdministracion c"
        comando = 'SELECT ser.nombre, count(*) total FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd  WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + str('O') + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' and tp.id = u."tipoDoc_id" and  i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"  group by ser.nombre UNION SELECT ser.nombre, count(*) total FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , sitios_serviciosSedes sd, clinico_servicios ser WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND  t."sedesClinica_id" =  ' + "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND  t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and  t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and  dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and  t."consecAdmision" = 0 and dep."documento_id" = t."documento_id" and ser.nombre = '  + "'" + str('TRIAGE') + "'" + ' group by ser.nombre'

        curt.execute(comando)
        print(comando)

        indicadores = []

        for id, nombre in curt.fetchall():
            indicadores.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(indicadores)

        print("Indicadores = ", indicadores)
        print("Indicadores PRIMERO = ", indicadores[0]['nombre'])

        context['Indicadores'] = indicadores

        total = len(indicadores)

        print ("total ", total)

        if (0<total):
            if (indicadores[0]['id'] == 'HOSPITALIZACION' ):
                context['Hospitalizados'] = indicadores[0]['nombre']
                print("hospitakizado = ", indicadores[0]['nombre'])
        if (1 < total):
            if (indicadores[1]['id'] == 'TRIAGE' ):
                context['Triage'] = indicadores[1]['nombre']
                print("Triage = ", indicadores[1]['nombre'])
        if (2 < total):
            if (indicadores[2]['id'] == 'URGENCIAS' ):
                context['Urgencias']= indicadores[2]['nombre']
                print("URGENCIAS = ", indicadores[2]['nombre'])
        if (3 < total):
            if (indicadores[3]['id'] == 'AMBULATORIO' ):
                context['Ambulatorios'] = indicadores[3]['nombre']
                print("Ambulatorios = ", indicadores[3]['nombre'])



    # Fin combo Indicadores


        ## FIN CONTEXTO solo Admisiones
        return render(request, "admisiones/panelAdmisiones.html", context)

    if (escogeModulo == 'HISTORIA CLINICA'):
        print ("WENTRE PERMSISO HISTORIA CLINICA")
        ## Aqui contexto para solo Historia Clinica


        print("username = ", username)
        username = username.lstrip()

        ingresos = []

        # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curx = miConexionx.cursor()

        detalle = 'SELECT i.id id, tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
            Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'
        print(detalle)

        curx.execute(detalle)

        for id,tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
            ingresos.append({'id':id, 'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                             'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                             'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                             'DxActual': dxActual})

        miConexionx.close()
        print(ingresos)
        context['Ingresos'] = ingresos

        #username = username.lstrip()

        print ("username = ", username)

        documento_llave = Planta.objects.get(documento=username)

        print("el id del dopcumento = ", documento_llave.id)

        # Combo EspecialidadesMedicos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",   password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT e.id ,e.nombre FROM clinico_Especialidades e, clinico_EspecialidadesMedicos em,planta_planta pl  where em."especialidades_id" = e.id and em."planta_id" = pl.id AND pl.documento = ' + "'" + str(username) + "'"
        curt.execute(comando)
        print(comando)

        especialidadesMedicos = []
        especialidadesMedicos.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
             especialidadesMedicos.append({'id': id, 'nombre': nombre})

        miConexiont.close()

        print(especialidadesMedicos)

        context['EspecialidadesMedicos'] = especialidadesMedicos

        print ("especialidadesMedicos =", especialidadesMedicos)


        ## FIN CONTEXTO
        return render(request, "clinico/panelClinico.html", context)

    if (escogeModulo == 'TRIAGE'):
        print ("WENTRE PERMSISO TRIAGE")
        ## Aqui contexto para solo Triage

        # Combo de Servicios
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT sed.id id ,sed.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
            sede) + "'" + ' AND sed."servicios_id" = ser.id AND ser.nombre = ' + "'" + str('TRIAGE') + "'"
        curt.execute(comando)
        print(comando)

        servicios = []
        servicios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            servicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(servicios)

        context['Servicios'] = servicios

        # Fin combo servicios

        # Combo de SubServicios
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        #comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id"'
        comando = 'SELECT sub.id id ,sub.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(Sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sub."serviciosSedes_id" = sed.id AND ser.nombre = ' + "'" + str('TRIAGE') + "'"
        curt.execute(comando)
        print(comando)

        subServicios = []
        subServicios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            subServicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(subServicios)

        context['SubServicios'] = subServicios

        # Fin combo SubServicios

        # Combo de TiposTriage
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        #comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id"'
        comando = 'SELECT id, nombre FROM clinico_tipostriage order by id'
        curt.execute(comando)
        print(comando)

        tiposTriage = []
        tiposTriage.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposTriage.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposTriage)

        context['TiposTriage'] = tiposTriage

        # Fin combo TiposTriage



        # Combo ripsServiciosIng

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_RipsServicios  p"

        curt.execute(comando)
        print(comando)

        ripsServiciosIng = []

        for id, nombre in curt.fetchall():
            ripsServiciosIng.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsServiciosIng", ripsServiciosIng)

        context['RipsServiciosIng'] = ripsServiciosIng

        # Fin combo ripsServiciosIng

        # Combo ripsmodalidadGrupoServicioTecSal

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_RipsModalidadAtencion   p"

        curt.execute(comando)
        print(comando)

        ripsmodalidadGrupoServicioTecSal = []

        for id, nombre in curt.fetchall():
            ripsmodalidadGrupoServicioTecSal.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsmodalidadGrupoServicioTecSal", ripsmodalidadGrupoServicioTecSal)

        context['RipsmodalidadGrupoServicioTecSal'] = ripsmodalidadGrupoServicioTecSal

        # Fin combo ripsmodalidadGrupoServicioTecSal

        # Combo ripsViaIngresoServicioSalud

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsviasingresosalud  p"

        curt.execute(comando)
        print(comando)

        ripsViaIngresoServicioSalud = []

        for id, nombre in curt.fetchall():
            ripsViaIngresoServicioSalud.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsViaIngresoServicioSalud", ripsViaIngresoServicioSalud)

        context['RipsViaIngresoServicioSalud'] = ripsViaIngresoServicioSalud

        # Fin combo ripsViaIngresoServicioSalud

        # Combo ripsGrupoServicios

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsGrupoServicios  p"

        curt.execute(comando)
        print(comando)

        ripsGrupoServicios = []

        for id, nombre in curt.fetchall():
            ripsGrupoServicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsGrupoServicios", ripsGrupoServicios)

        context['RipsGrupoServicios'] = ripsGrupoServicios

        # Fin combo ripsGrupoServicios

        # Combo ripsCondicionDestinoUsuarioEgreso

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsdestinoegreso  p"

        curt.execute(comando)
        print(comando)

        ripsCondicionDestinoUsuarioEgreso = []

        for id, nombre in curt.fetchall():
            ripsCondicionDestinoUsuarioEgreso.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsCondicionDestinoUsuarioEgreso", ripsCondicionDestinoUsuarioEgreso)

        context['RipsCondicionDestinoUsuarioEgreso'] = ripsCondicionDestinoUsuarioEgreso

        # Fin combo ripsCondicionDestinoUsuarioEgreso

        # Combo ripsCausaMotivoAtencion

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripscausaexterna  p"

        curt.execute(comando)
        print(comando)

        ripsCausaMotivoAtencion = []

        for id, nombre in curt.fetchall():
            ripsCausaMotivoAtencion.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsCausaMotivoAtencion", ripsCausaMotivoAtencion)

        context['RipsCausaMotivoAtencion'] = ripsCausaMotivoAtencion

        # Fin combo ripsCausaMotivoAtencion

        # Combo ripsDestinoUsuarioEgresoRecienNacido

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM rips_ripsdestinoegreso  p"

        curt.execute(comando)
        print(comando)

        ripsDestinoUsuarioEgresoRecienNacido = []

        for id, nombre in curt.fetchall():
            ripsDestinoUsuarioEgresoRecienNacido.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print("ripsDestinoUsuarioEgresoRecienNacido", ripsDestinoUsuarioEgresoRecienNacido)

        context['RipsDestinoUsuarioEgresoRecienNacido'] = ripsDestinoUsuarioEgresoRecienNacido

        # Fin combo ripsDestinoUsuarioEgresoRecienNacido



        triage1 = []

        # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curx = miConexionx.cursor()

        #comando = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , t.consec consec , dep.nombre camaNombre,t."fechaSolicita" solicita,t.motivo motivo, t."clasificacionTriage_id" triage FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" =' + "'" + str(Sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and  u.id = t."documento_id"'
        comando = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , t.consec consec , dep.nombre camaNombre,t."fechaSolicita" solicita,t.motivo motivo, t."clasificacionTriage_id" triage FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser  WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" =' + "'" + str(Sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and  u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'"
        print(comando)

        curx.execute(comando)

        for tipoDoc, documento, nombre, consec, camaNombre, solicita, motivo, triage in curx.fetchall():
            triage1.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,'camaNombre': camaNombre, 'solicita': solicita,
                             'motivo': motivo, 'triage': triage})

        miConexionx.close()
        print(triage1)
        context['Triage'] = triage1




        ## FIN CONTEXTO
        return render(request, "triage/panelTriage.html", context)

    if (escogeModulo == 'AUTORIZACIONES'):
        print ("WENTRE PERMSISO AUTORIZACIONES")
        ## Aqui contexto para solo Triage

        ## FIN CONTEXTO
        return render(request, "autorizaciones/panelAutorizaciones.html", context)

    if (escogeModulo == 'FACTURACION'):
        print("WENTRE PERMSISO FACTURACION")
        ## Aqui contexto para solo Facturacion

        ## FIN CONTEXTO

        return render(request, "facturacion/panelFacturacion.html", context)

    if (escogeModulo == 'CONTRATACION'):
        print("WENTRE PERMSISO FACTURACION")
        ## Aqui contexto para solo Facturacion

        ## FIN CONTEXTO

        return render(request, "contratacion/panelConvenios.html", context)


    if (escogeModulo == 'APOYO TERAPEUTICO'):
        print("WENTRE PERMSISO APOYO TERAPEUTICO")
        ## Aqui contexto para solo Triage

        ## FIN CONTEXTO
        return render(request, "apoyoTerapeutico/panelApoyoTerapeutico.html", context)


    if (escogeModulo == 'TARIFAS'):
        print("WENTRE PERMSISO TARIFAS")
        ## Aqui contexto para solo Triage

        ## FIN CONTEXTO
        return render(request, "tarifas/Paneltarifas.html", context)



    return render(request, "panelVacio.html", context)


def retornarAdmision(request, Sede, Perfil, Username, Username_id, NombreSede):


    print ("Entre Retornar Admision")
    #Sede = request.POST["Sede"]
    print ("Sede = ", Sede)
    Sede = Sede.lstrip()
    sede = Sede
    #Perfil = request.POST["Perfil"]
    print ("Perfil = ",Perfil)
    Perfil = Perfil.lstrip()
    print("Perfil = ", Perfil)

    print ("Nombre dede = ", NombreSede)
    username = Username

    context = {}

    context['Sede'] = Sede
    context['Username'] = Username
    context['Username_id'] = Username_id
    context['NombreSede'] = NombreSede


    # Consigo la sede Nombre

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT nombre   FROM sitios_sedesClinica WHERE id ='" + sede + "'"
    cur.execute(comando)
    print(comando)

    nombreSedes = []

    for nombre in cur.fetchall():
        nombreSedes.append({'nombre': nombre})

    miConexion.close()
    print(nombreSedes)
    nombresede1 = nombreSedes[0]

    context['NombreSede'] = nombresede1

    # esta consulta por que se pierde de otras pantallas

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes

    ingresos = []

    #miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curx = miConexionx.cursor()

    detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
        Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'
    print(detalle)

    curx.execute(detalle)

    for tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
        ingresos.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                         'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                         'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                         'DxActual': dxActual})

    miConexionx.close()
    print(ingresos)
    context['Ingresos'] = ingresos

    # Combo de Servicios
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed.sedesClinica_id ='" + str(
        sede) + "' AND sed.servicios_id = ser.id"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios

    # Fin combo servicios

    # Combo de SubServicios
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed.sedesClinica_id ='" + str(
        Sede) + "' AND sed.servicios_id = ser.id and  sed.sedesClinica_id = sub.sedesClinica_id and sed.servicios_id =sub.servicios_id"
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)

    context['SubServicios'] = subServicios

    # Fin combo SubServicios


    # Combo TiposDOc
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM usuarios_TiposDocumento "
    curt.execute(comando)
    print(comando)

    tiposDoc = []
    tiposDoc.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDoc.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDoc)

    context['TiposDoc'] = tiposDoc

    # Fin combo TiposDOc

    # Combo Habitaciones
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = ' SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip where dep."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND tip.nombre=' + "'" + str('HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id'
    curt.execute(comando)
    print(comando)

    habitaciones = []

    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    context['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    # Combo Especialidades
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Especialidades"
    curt.execute(comando)
    print(comando)

    especialidades = []
    especialidades.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidades)

    context['Especialidades'] = especialidades

    # Fin combo Especialidades

    # Combo Medicos
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT p.id id, p.nombre  nombre FROM planta_planta p , planta_perfilesplanta perf WHERE perf.sedesClinica_id = '" + str(
        Sede) + "' AND perf.tiposPlanta_id = 1 and p.id = perf.planta_id"

    curt.execute(comando)
    print(comando)

    medicos = []
    medicos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        medicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicos)

    context['Medicos'] = medicos
    context['Perfil'] = Perfil


    # Combo Vias Ingreso

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_viasingreso c"

    curt.execute(comando)
    print(comando)

    viasIngreso = []

    for id, nombre in curt.fetchall():
        viasIngreso.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(viasIngreso)

    context['ViasIngreso'] = viasIngreso

    # Fin combo vias Ingreso

    # Combo Causas Externa

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_causasExterna c"

    curt.execute(comando)
    print(comando)

    causasExterna = []

    for id, nombre in curt.fetchall():
        causasExterna.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(causasExterna)

    context['CausasExterna'] = causasExterna

    # Fin combo causasExterna

    # Combo Regimenes

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_regimenes c"

    curt.execute(comando)
    print(comando)

    regimenes = []

    for id, nombre in curt.fetchall():
        regimenes.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(regimenes)

    context['Regimenes'] = regimenes

    # Fin combo regimenes


    # Combo Tipos Cotizante

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_tiposcotizante c"

    curt.execute(comando)
    print(comando)

    tiposCotizante = []

    for id, nombre in curt.fetchall():
        tiposCotizante.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposCotizante)

    context['TiposCotizante'] = tiposCotizante

    # Fin combo tiposCotizante


    # Combo municipios

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_municipios c"

    curt.execute(comando)
    print(comando)

    municipios = []

    for id, nombre in curt.fetchall():
        municipios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(municipios)

    context['Municipios'] = municipios

    # Fin combo municipios

    # Combo localidades

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_localidades c"

    curt.execute(comando)
    print(comando)

    localidades = []

    for id, nombre in curt.fetchall():
        localidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(localidades)

    context['Localidades'] = localidades

    # Fin combo localidades


    # Combo estadoCivil

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_estadocivil c"

    curt.execute(comando)
    print(comando)

    estadoCivil = []

    for id, nombre in curt.fetchall():
        estadoCivil.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(estadoCivil)

    context['EstadoCivil'] = estadoCivil

    # Fin combo estadoCivil


    # Combo ocupaciones

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_ocupaciones c"

    curt.execute(comando)
    print(comando)

    ocupaciones = []

    for id, nombre in curt.fetchall():
        ocupaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ocupaciones)

    context['Ocupaciones'] = ocupaciones

    # Fin combo ocupaciones




    # Fin combo Medicos

    if (Perfil == 1):
        return render(request, "menuMedico.html", context)
    if (Perfil == 2):
        return render(request, "menuEnfermero.html", context)
    if (Perfil == 3):
        return render(request, "menuAuxiliar.html", context)
    if (Perfil == 4):
        return render(request, "citasMedicas/menuCitasMedicas.html", context)
    if (Perfil == 5):
        return render(request, "facturacion/menuFacturacion.html", context)
    if (Perfil == 6):
        print ("Entre por dende ERA")
        return render(request, "admisiones/panelAdmisiones.html", context)

    return render(request, "admisiones/panelAdmisiones.html", context)


def retornarMen(request, Sede, Username,  Documento, NombreSede, Profesional):

    print("Voy a RETORNAR AL MENU")


    username = Username.strip()

    documento = Documento
    sede = Sede
    nombreSede = NombreSede
    profesional = Profesional
    context = {}
    print(username)

    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes

    context['Documento'] = username
    context['Username'] = username
    context['Sede'] = sede
    context['NombreSede'] = nombreSede
    context['Profesional'] = profesional


    # Combo PermisosGrales

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(
        username) + "'"

    curt.execute(comando)
    print(comando)

    permisosGrales = []

    for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
        permisosGrales.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
             'modulo_nombre': modulo_nombre})

    miConexiont.close()
    print(permisosGrales)

    context['PermisosGrales'] = permisosGrales

    # Fin Combo PermisosGrales

    # Combo PermisosDetalle

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo, modeledef.nombre nombreOpcion ,elemen.nombre nombreElemento from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli, seguridad_perfilesclinicaopciones perfopc, seguridad_perfilesusu perfdet, seguridad_moduloselementosdef modeledef, seguridad_moduloselementos elemen where planta.id= 1 and  planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and gral.id = perfdet."plantaId_id" and perfdet."perfilesClinicaOpcionesId_id" = perfopc.id and perfopc."perfilesClinicaId_id" =perfcli.id and  perfopc."modulosElementosDefId_id" = modeledef.id and elemen.id = modeledef."modulosElementosId_id"  and planta.documento = ' + "'" + username + "'"

    curt.execute(comando)
    print(comando)

    permisosDetalle = []

    for id, nombre, nomenclatura, logo, nombreOpcion, nombreElemento in curt.fetchall():
        permisosDetalle.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion': nombreOpcion,
             'nombreElemento': nombreElemento})

    miConexiont.close()
    print(permisosDetalle)

    context['PermisosDetalle'] = permisosDetalle

    # Fin Combo PermisosDetalle

    return render(request, "inicio/PantallaPrincipal.html", context)



def validaPassword(request, username, contrasenaAnt,contrasenaNueva,contrasenaNueva2):
    print("Entre ValidaPassword" )
    username = request.POST["username"]
    contrasenaAnt = request.POST["contrasenaAnt"]
    contrasenaNueva = request.POST["contrasenaNueva"]
    contrasenaNueva2 = request.POST["contrasenaNueva2"]

    print(username)
    print(contrasenaAnt)
    print(contrasenaNueva)
    print(contrasenaNueva2)
    context = {}

    if (contrasenaNueva2 != contrasenaNueva):
        dato = "No coinciden las contraseñas ! "
        context['Error'] = "No coincideln las contraseñas ! "
        print(context)

        return HttpResponse(dato)


    #miConexion1 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion1 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur1 = miConexion1.cursor()
    comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "'"
    print(comando)
    cur1.execute(comando)

    UsuariosHc = []

    for documento, contrasena in cur1.fetchall():
        UsuariosHc = {'username': documento, 'contrasena': contrasena}

    miConexion1.close()
    print(UsuariosHc)

    if UsuariosHc == []:

        dato = "Personal invalido ! "
        context['Error'] = "Personal invalido ! "
        print(context)

        return HttpResponse(dato)
        #return render(request, "accesoPrincipal1.html", context)

    else:
        miConexion1 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        cur1 = miConexion1.cursor()
        comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "' AND contrasena = '" + str(contrasenaAnt) + "'"
        print(comando)
        cur1.execute(comando)

        ContrasenaHc = []
        for documento, contrasena in cur1.fetchall():
            ContrasenaHc = {'username': documento, 'contrasena': contrasena}
        miConexion1.close()

        if ContrasenaHc == []:
            dato = "Contraseña Invalida ! "
            context['Error'] = "Contraseña Invalida ! "
            print(context)

            return HttpResponse(dato)

        else:

            miConexion1 =psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
            cur1 = miConexion1.cursor()
            comando = "UPDATE planta_planta SET contrasena = '" +  str(contrasenaNueva) + "' WHERE documento = '" + str(username) + "'"
            print(comando)
            cur1.execute(comando)
            miConexion1.commit()
            miConexion1.close()
            context['Error'] = "Contraseña Actualizada ! "
            dato = "Contraseña Actualizada !"
            print(context)
            #return HttpResponse(context, safe=False)
            return HttpResponse(dato)
            #return render(request, "accesoPrincipal1.html", context)


    #return JsonResponse(UsuariosHc, safe=False)

def Modal(request, username, password):

        print("Entre a Modal")
        print(username)
        print(password)

        #miConexion1 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexion1 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        cur1 = miConexion1.cursor()
        comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "'"
        print(comando)
        cur1.execute(comando)

        UsuariosHc = {}

        for documento, contrasena in cur1.fetchall():
            UsuariosHc = {'username': documento, 'contrasena': contrasena}

        miConexion1.close()
        print(UsuariosHc)
        return JsonResponse(UsuariosHc, safe=False)
        # return HttpResponse(UsuariosHc)



def buscarAdmision(request):
    context = {}

    ## ULTIMOS AJUSTES

    print("Entre Buscar Admision" )
    BusTipoDoc = request.POST["busTipoDoc"]
    BusDocumento = request.POST["busDocumento"]
    BusHabitacion = request.POST["busHabitacion"]
    BusDesde = request.POST["busDesde"]
    BusHasta = request.POST["busHasta"]
    BusEspecialidad = request.POST["busEspecialidad"]
    print ("Especialidad = ", BusEspecialidad )
    BusMedico = request.POST["busMedico"]
    BusServicio = request.POST["busServicio"]
    BusSubServicio = request.POST["busSubServicio"]
    BusPaciente = request.POST["busPaciente"]
    #Perfil = request.POST['Perfil']

    Sede = request.POST["sede"]
    sede = request.POST["sede"]
    context['Sede'] = Sede

    # Consigo la sede Nombre

    #miConexion = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur = miConexion.cursor()
    comando = "SELECT nombre   FROM sitios_sedesClinica WHERE id ='" + Sede + "'"
    cur.execute(comando)
    print(comando)

    nombreSedes = []

    for nombre in cur.fetchall():
        nombreSedes.append({'nombre': nombre})

    miConexion.close()
    print(nombreSedes)
    nombresede1 = nombreSedes[0]

    context['NombreSede'] = nombresede1

    username = request.POST["username"]
    context['Username'] = username
    print("Sede  = ", Sede)
    print("BusHabitacion= ", BusHabitacion)
    print("BusTipoDoc=", BusTipoDoc)
    print("BusDocumento=" , BusDocumento)
    print("BusDesde=", BusDesde)
    print("BusHasta=", BusHasta)
    print("La sede es = " , Sede)
    print("El busServicio = ", BusServicio)
    print("El busSubServicio = ", BusSubServicio)
    print("El busEspecialidad = ", BusEspecialidad)
    print("El busSMedico = ", BusMedico)
    print("El busSMedico = ", BusPaciente)

    ## Combos para Contexto

    # aqui la manada de combos organizarlo segun necesidades

    ingresos = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curx = miConexionx.cursor()


    detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'
    print(detalle)

    curx.execute(detalle)

    for tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
        ingresos.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                         'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                         'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                         'DxActual': dxActual})

    miConexionx.close()
    print(ingresos)
    context['Ingresos'] = ingresos

    # Combo de Servicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id'
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios

    # Fin combo servicios

    # Combo de SubServicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id"'
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)

    context['SubServicios'] = subServicios

    # Fin combo SubServicios

    # Combo TiposDOc
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM usuarios_TiposDocumento "
    curt.execute(comando)
    print(comando)

    tiposDoc = []
    tiposDoc.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDoc.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDoc)

    context['TiposDoc'] = tiposDoc

    # Fin combo TiposDOc

    # Combo Habitaciones
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = ' SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip where dep."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND tip.nombre=' + "'" + str('HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id'
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    context['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    # Combo Especialidades
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Especialidades"
    curt.execute(comando)
    print(comando)

    especialidades = []
    especialidades.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidades)

    context['Especialidades'] = especialidades

    # Fin combo Especialidades

    # Combo EspecialidadesMedicos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT em.id ,e.nombre FROM clinico_Especialidades e, clinico_EspecialidadesMedicos em,planta_planta pl  where em."especialidades_id" = e.id and em."planta_id" = pl.id AND pl.documento = ' + "'" + str(username) + "'"
    curt.execute(comando)
    print(comando)

    especialidadesMedicos = []
    especialidadesMedicos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidadesMedicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidadesMedicos)

    context['EspecialidadesMedicos'] = especialidadesMedicos

    # Fin combo EspecialidadesMedicos

    # Combo Medicos
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT p.id id, p.nombre nombre FROM planta_planta p,clinico_medicos med, planta_tiposPlanta tp WHERE p."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' and p."tiposPlanta_id" = tp.id and tp.nombre = ' + "'" + str('MEDICO') + "'" + ' and med.planta_id = p.id'

    curt.execute(comando)
    print(comando)

    medicos = []
    medicos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        medicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicos)

    context['Medicos'] = medicos

    # Fin combo Medicos

    # Combo TiposFolio

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT e.id id, e.nombre nombre FROM clinico_tiposFolio e"

    curt.execute(comando)
    print(comando)

    tiposFolio = []
    tiposFolio.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposFolio.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposFolio)

    context['TiposFolio'] = tiposFolio

    # Fin combo TiposFolio

    # Combo TiposUsuario

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposusuario p"

    curt.execute(comando)
    print(comando)

    tiposUsuario = []
    # tiposUsuario.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposUsuario.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposUsuario)

    context['TiposUsuario'] = tiposUsuario

    # Fin combo Tipos Usuario

    # Combo TiposDocumento

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposDocumento p"

    curt.execute(comando)
    print(comando)

    tiposDocumento = []
    tiposDocumento.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDocumento.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDocumento)

    context['TiposDocumento'] = tiposDocumento

    # Fin combo TiposDocumento

    # Combo Centros

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM sitios_centros p"

    curt.execute(comando)
    print(comando)

    centros = []

    for id, nombre in curt.fetchall():
        centros.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDocumento)

    context['Centros'] = centros

    # Fin combo Centros

    # Combo Diagnosticos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT p.id id, p.nombre  nombre FROM clinico_diagnosticos p"

    curt.execute(comando)
    print(comando)

    diagnosticos = []
    diagnosticos.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        diagnosticos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(diagnosticos)

    context['Diagnosticos'] = diagnosticos

    # Fin combo Diagnosticos

    # Combo Departamentos

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_departamentos d"

    curt.execute(comando)
    print(comando)

    departamentos = []
    # tiposDocumento.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        departamentos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(departamentos)

    context['Departamentos'] = departamentos

    # Fin combo Departamentos

    # Combo Ciudades

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id, c.nombre  nombre FROM sitios_ciudades c"

    curt.execute(comando)
    print(comando)

    ciudades = []

    for id, nombre in curt.fetchall():
        ciudades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ciudades)

    context['Ciudades'] = ciudades

    # Fin combo Ciudades

    # Combo Modulos

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre, c.nomenclatura nomenclatura, c.logo logo FROM seguridad_modulos c"

    curt.execute(comando)
    print(comando)

    modulos = []

    for id, nombre, nomenclatura, logo in curt.fetchall():
        modulos.append({'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo})

    miConexiont.close()
    print(modulos)

    context['Modulos'] = modulos

    # Fin combo Modulos

    # Combo PermisosGrales

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(
        username) + "'"

    curt.execute(comando)
    print(comando)

    permisosGrales = []

    for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
        permisosGrales.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
             'modulo_nombre': modulo_nombre})

    miConexiont.close()
    print(permisosGrales)

    context['PermisosGrales'] = permisosGrales

    # Fin Combo PermisosGrales

    # Combo PermisosDetalle

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo, modeledef.nombre nombreOpcion ,elemen.nombre nombreElemento from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli, seguridad_perfilesclinicaopciones perfopc, seguridad_perfilesusu perfdet, seguridad_moduloselementosdef modeledef, seguridad_moduloselementos elemen where planta.id= 1 and  planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and gral.id = perfdet."plantaId_id" and perfdet."perfilesClinicaOpcionesId_id" = perfopc.id and perfopc."perfilesClinicaId_id" =perfcli.id and  perfopc."modulosElementosDefId_id" = modeledef.id and elemen.id = modeledef."modulosElementosId_id"  and planta.documento = ' + "'" + username + "'"

    curt.execute(comando)
    print(comando)

    permisosDetalle = []

    for id, nombre, nomenclatura, logo, nombreOpcion, nombreElemento in curt.fetchall():
        permisosDetalle.append(
            {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion': nombreOpcion,
             'nombreElemento': nombreElemento})

    miConexiont.close()
    print(permisosDetalle)

    context['PermisosDetalle'] = permisosDetalle

    # Fin Combo PermisosDetalle

    # Combo Vias Ingreso

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_viasingreso c"

    curt.execute(comando)
    print(comando)

    viasIngreso = []

    for id, nombre in curt.fetchall():
        viasIngreso.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(viasIngreso)

    context['ViasIngreso'] = viasIngreso

    # Fin combo vias Ingreso

    # Combo Causas Externa

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_causasExterna c"

    curt.execute(comando)
    print(comando)

    causasExterna = []

    for id, nombre in curt.fetchall():
        causasExterna.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(causasExterna)

    context['CausasExterna'] = causasExterna

    # Fin combo causasExterna

    # Combo Regimenes

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_regimenes c"

    curt.execute(comando)
    print(comando)

    regimenes = []

    for id, nombre in curt.fetchall():
        regimenes.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(regimenes)

    context['Regimenes'] = regimenes

    # Fin combo regimenes


    # Combo Tipos Cotizante

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM clinico_tiposcotizante c"

    curt.execute(comando)
    print(comando)

    tiposCotizante = []

    for id, nombre in curt.fetchall():
        tiposCotizante.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposCotizante)

    context['TiposCotizante'] = tiposCotizante

    # Fin combo tiposCotizante

    # Combo municipios

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_municipios c"

    curt.execute(comando)
    print(comando)

    municipios = []

    for id, nombre in curt.fetchall():
        municipios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(municipios)

    context['Municipios'] = municipios

    # Fin combo municipios

    # Combo localidades

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM sitios_localidades c"

    curt.execute(comando)
    print(comando)

    localidades = []

    for id, nombre in curt.fetchall():
        localidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(localidades)

    context['Localidades'] = localidades

    # Fin combo localidades


    # Combo estadoCivil

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_estadocivil c"

    curt.execute(comando)
    print(comando)

    estadoCivil = []

    for id, nombre in curt.fetchall():
        estadoCivil.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(estadoCivil)

    context['EstadoCivil'] = estadoCivil

    # Fin combo estadoCivil


    # Combo ocupaciones

    # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id,c.nombre nombre FROM basicas_ocupaciones c"

    curt.execute(comando)
    print(comando)

    ocupaciones = []

    for id, nombre in curt.fetchall():
        ocupaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ocupaciones)

    context['Ocupaciones'] = ocupaciones

    # Fin combo ocupaciones

    ## fin manada de combis

    ## Fin Combos para contexto

    #miConexion1 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion1 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur1 = miConexion1.cursor()

    detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd , sitios_subServiciosSedes sub  WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and sd."sedesClinica_id" = sub."sedesClinica_id" and  sub."sedesClinica_id" =  i."sedesClinica_id"   and  sub."sedesClinica_id" = dep."sedesClinica_id" and dep.id = i."dependenciasActual_id"  and dep."subServiciosSedes_id" = sub.id  and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
        Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosIng_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'


    print(detalle)

    desdeTiempo = BusDesde[11:16]
    hastaTiempo = BusHasta[11:16]
    desdeFecha = BusDesde[0:10]
    hastaFecha = BusHasta[0:10]

    print ("desdeTiempo = ", desdeTiempo)
    print("desdeTiempo = " ,hastaTiempo)

    print (" desde fecha = " , desdeFecha)
    print("hasta  = ", hastaFecha)


    if BusServicio != "":
      detalle = detalle + " AND  ser.id = '" + str(BusServicio) + "'"
    print(detalle)

    if BusSubServicio != "":
      detalle = detalle + " AND  sub.id = '" + str(BusSubServicio) + "'"
    print(detalle)


    if BusDesde != "":
        detalle = detalle +  ' AND i."fechaIngreso" >= ' + "'" + str(desdeFecha) +   " " + str(desdeTiempo)  + ":00" + "'"
        print (detalle)

    if BusHasta != "":
        detalle = detalle + ' AND i."fechaIngreso" <=  ' + "'"  + str(hastaFecha) +  " " + str(hastaTiempo) + ":00" +"'"
        print(detalle)

    if BusHabitacion != "":
        detalle = detalle + " AND dep.id = '" + str(BusHabitacion) + "'"
        print(detalle)

    if BusTipoDoc != "":
        detalle = detalle + ' AND i."tipoDoc_id"= ' + "'" +  str(BusTipoDoc) + "'"
        print(detalle)

    if BusDocumento != "":
        detalle = detalle + " AND u.documento= '" + str(BusDocumento) + "'"
        print(detalle)

    if BusPaciente != "":
        detalle = detalle + " AND u.nombre like '%" + str(BusPaciente) + "%'"
        print(detalle)

    if BusMedico != "":
        detalle = detalle + ' AND i."medicoActual_id" = ' + "'"   + str(BusMedico) + "'"
        print(detalle)


    if BusEspecialidad != "":
        detalle = detalle + ' AND i."dxIngreso_id" = ' + "'" +  str(BusEspecialidad) + "'"
        print(detalle)


    cur1.execute(detalle)

    ingresos = []

    for tipoDoc, documento_id, nombre , consec, fechaIngreso,  fechaSalida, servicioNombreIng, camaNombreIng, dxActual  in cur1.fetchall():
        ingresos.append ({'tipoDoc' : tipoDoc, 'Documento': documento_id, 'Nombre': nombre , 'Consec': consec, 'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida, 'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng, 'DxActual': dxActual})

    miConexion1.close()


    print(ingresos)
    context['Ingresos'] = ingresos

    return render(request, "admisiones/panelAdmisiones.html", context)

def buscarServicios(request):
    context = {}
    Sede = request.GET["Sede"]
    print("Entre buscar  servicio =", Serv)
    print("Sede = ", Sede)
    # Combo de Servicios

    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT sed.id id ,sed.nombre nombre FROM  sitios_serviciosSedes sed Where sed."sedesClinica_id" =' + "'" + str(Sede) + "'"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios

    context['Sede'] = Sede

    return JsonResponse(json.dumps(servicios), safe=False)



def buscarSubServicios(request):
    context = {}
    Serv = request.GET["serv"]
    Sede = request.GET["sede"]
    print ("Entre buscar  Subservicios del servicio  =",Serv)
    print ("Sede = ", Sede)

    # Combo de SubServicios
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont =psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    #comando = 'SELECT sub.id id ,sub.nombre nombre FROM sitios_serviciosSedes sed ,sitios_subserviciossedes sub Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + '  and sed."sedesClinica_id" = sub."sedesClinica_id" and sed.id = sub."serviciosSedes_id" and sub."serviciosSedes_id" = ' + "'" + str(Serv) + "'"
    comando = 'SELECT sub.id id ,sub.nombre nombre FROM sitios_serviciosSedes sed ,sitios_subserviciossedes sub , clinico_servicios serv Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' and sed."sedesClinica_id" = sub."sedesClinica_id" and sed.id = sub."serviciosSedes_id"  and sed.servicios_id = ' + "'" + str(Serv) + "'" + ' and sub."serviciosSedes_id" = sed.id and serv.id = ' + "'" + str(Serv) + "'"
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)

    context['SubServicios'] = subServicios


    context['Sede'] = Sede


    return JsonResponse(json.dumps(subServicios), safe=False)



def buscarCiudades(request):
    context = {}
    Departamento = request.GET["Departamento"]

    print ("Entre buscar  Ciudades del Depto  =",Departamento)


    # Combo de Medicos Especialidades


    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()

    comando = "SELECT c.id id, c.nombre  nombre FROM sitios_departamentos d, sitios_ciudades c WHERE c.departamentos_id = d.id and d.id = '" + str(Departamento) + "'"

    curt.execute(comando)
    print(comando)

    ciudades = []



    for id, nombre in curt.fetchall():
        ciudades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(ciudades)


    context['Ciudades'] = ciudades


    return JsonResponse(json.dumps(ciudades), safe=False)




def buscarEspecialidadesMedicos(request):
    context = {}
    Esp = request.GET["Esp"]
    Sede = request.GET["Sede"]
    print ("Entre buscar  Servicio =",Esp)
    print ("Sede = ", Sede)

    # Combo de Medicos Especialidades


    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()


    #comando = 'SELECT m.id id, m.nombre nombre from clinico_medicos m, clinico_Especialidadesmedicos medesp,clinico_especialidades esp,sitios_sedesclinica sed,  planta_planta pla where esp.id = ' + "'" + str(Esp) + "'" + ' and esp.id=medesp.especialidades_id and pla."sedesClinica_id" = sed.id and pla.id = medesp.planta_id and pla."sedesClinica_id"=' + "'" + str(Sede) + "'" + ' order by m.nombre'
    comando = 'SELECT m.id id, m.nombre nombre from clinico_medicos m, clinico_Especialidadesmedicos medesp,clinico_especialidades esp,sitios_sedesclinica sed,  planta_planta pla where  pla.id=medesp.planta_id and  medesp.especialidades_id = esp.id and m.planta_id = pla.id and  esp.id = ' + "'" + str(
        Esp) + "'" + ' and esp.id=medesp.especialidades_id and pla."sedesClinica_id" = sed.id and pla.id = medesp.planta_id and pla."sedesClinica_id"=' + "'" + str(
        Sede) + "'" + ' order by m.nombre'

    curt.execute(comando)
    print(comando)

    medicosEspecialidades = []


    for id, nombre in curt.fetchall():
        medicosEspecialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicosEspecialidades)


    context['MedicosEspecialidades'] = medicosEspecialidades

    context['Sede'] = Sede

    return JsonResponse(json.dumps(medicosEspecialidades), safe=False)



def buscarHabitaciones(request):


    context = {}
    Exc = request.GET["Exc"]
    print ("Excluir = ", Exc)
    Serv = request.GET["serv"]
    SubServ = request.GET["subServ"]
    Sede = request.GET["sede"]
    print ("Entre buscar  servicio =",Serv)
    print("Entre buscar Subservicio =", SubServ)
    print ("Sede = ", Sede)


    # Busco la habitaciones de un Servicio

    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()

    if Exc == 'N':

      comando = "SELECT dep.id id ,dep.numero nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub , sitios_dependencias dep  Where sed.sedesClinica_id ='" + str(
        Sede) + "' AND sed.servicios_id = ser.id and  sed.sedesClinica_id = sub.sedesClinica_id and sed.servicios_id =sub.servicios_id and  dep.sedesClinica_id=sed.sedesClinica_id and dep.servicios_id = sub.servicios_id and dep.subServicios_id =sub.id  and dep.subServicios_id = '" +str(SubServ) + "'" + ' and dep.disponibilidad = ' + "'" + 'L' + "'"

    else:

       comando = 'SELECT dep.id id ,dep.numero nombre   FROM sitios_serviciosSedes sed,  sitios_subserviciossedes sub , sitios_dependencias dep ,  sitios_dependenciasTipo tip   Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND sed."sedesClinica_id" = sub."sedesClinica_id" and sub."serviciosSedes_id" = sed.id and dep."sedesClinica_id"=sed."sedesClinica_id" and dep."serviciosSedes_id"= sed.id and dep."subServiciosSedes_id" = sub.id and dep."subServiciosSedes_id" = ' + "'" + str(SubServ) + "'" + ' and dep.disponibilidad = ' + "'" + 'L' +  "'" + ' and tip.id=dep."dependenciasTipo_id" and tip.nombre = ' + "'" + str('HABITACIONES') + "'"
    curt.execute(comando)
    print(comando)

    Habitaciones =[]




    for id, nombre in curt.fetchall():
        Habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(Habitaciones)
    context['Habitaciones'] = Habitaciones

    context['Sede'] = Sede



    return JsonResponse(json.dumps(Habitaciones), safe=False)



# aqui nuevo codigo cvrear admision DEF


def crearAdmisionDef(request):

    print("Entre a Craer Admision definitiva")

    if request.method == 'POST':
        print("EntrePost Graba Admision Def")
        data = {}
        context = {}


        #sedesClinica = request.POST['sedesClinica']
        sedesClinica = request.POST['Sede']
        Sede = request.POST['Sede']
        sede = request.POST['Sede']
        context['Sede'] = Sede

        NombreSede = request.POST['nombreSede']
        nombreSede = request.POST['nombreSede']


        print("Sedes Clinica = ", sedesClinica)
        print ("Sede = ",Sede)


        username = request.POST["username"].strip()
        print(" Username = " , username)
        context['Username'] = username

        Profesional = request.POST["profesional"]
        print(" Profesional = " , Profesional)
        context['Profesional'] = Profesional


        Username_id = request.POST["username_id"]
        print("Username_id = ", Username_id)
        context['Username_id'] = Username_id

        busServicio2 = request.POST["busServicio22"]
        print(" busServicio2 = ", busServicio2)
        context['BusServicio2'] = busServicio2

        tipoDoc = request.POST['tipoDoc22']
        documento = request.POST['busDocumentoSel22'].strip()
        print("tipoDoc = ", tipoDoc)
        print("documento = ", documento)

        # Consigo el Id del Paciente Documento

        DocumentoId = Usuarios.objects.get(documento=documento.strip())
        idPacienteFinal = DocumentoId.id

        print("idPacienteFinal", idPacienteFinal)



        consec = Ingresos.objects.all().filter(tipoDoc_id=tipoDoc).filter(documento_id=idPacienteFinal).aggregate(maximo=Coalesce(Max('consec'), 0))
        print("ultimo Ingreso = ", consec)
        consecAdmision = (consec['maximo'] + 1)
        print("ultimo ingreso = ", consecAdmision)

        now = datetime.datetime.now()
        dnow = now.strftime("%Y-%m-%d %H:%M:%S")
        print("NOW  = ", dnow)

        fechaIngreso = dnow
        print("fechaIngreso = ", fechaIngreso)

        #fechaSalida = "0001-01-01 00:00:00"

        factura = 0
        numcita = 0
        dependenciasIngreso = request.POST['dependenciasIngreso22']
        print("dependenciasIngreso =", dependenciasIngreso)
        #dependenciasActual = dependenciasIngreso
        dependenciasSalida = ""
        dxIngreso = request.POST['dxIngreso']
        print("dxIngreso =", dxIngreso)
        dxActual = dxIngreso
        dxSalida = ""
        estadoSalida = "1"

        medicoIngreso = request.POST['medicoIngreso']
        print("medicoIngreso =", medicoIngreso)
        medicoActual = medicoIngreso
        medicoSalida = ""
        salidaClinica = "N"
        salidaDefinitiva = "N"

        especialidadesMedicos = request.POST['busEspecialidad']

        especialidadesMedicosSalida = ""
        especialidadesMedicosActual = especialidadesMedicos


        usuarioRegistro = Username_id

        print("usuarioRegistro =", usuarioRegistro)


        fechaRegistro = fechaIngreso

        estadoReg = "A"
        print("estadoRegistro =", estadoReg)

        data[0] = "Ha ocurrido un error"

        # VAmos a guardar la Admision

        # Consigo ID de Documento

        documento_llave = Usuarios.objects.get(documento=documento)
        print("el id del dopcumento = ", documento_llave.id)

        usernameId = Planta.objects.get(documento=username)
        print("el id del planta = ", usernameId.id)

        viasIngreso   = request.POST["viasIngreso"]
        context['ViasIngreso'] = viasIngreso
        causasExterna = request.POST["causasExterna"]
        context['CausasExterna'] = causasExterna
        regimenes = request.POST["regimenes"]
        context['Regimenes'] = regimenes
        tiposCotizante = request.POST["tiposCotizante"]
        context['TiposCotizante'] = tiposCotizante
        ipsRemite = request.POST["ips"]
        numManilla = request.POST["numManilla"]
        remitido = request.POST["remitido"]
        #print("empresaId= ", empresaId)
        print("numManilla = ", numManilla)
        print("ipsRemite = ", ipsRemite)
        print("remitido = ", remitido)

        # DATOS DE RIPS
        ripsServiciosIng = request.POST['ripsServiciosIng']
        ripsmodalidadGrupoServicioTecSal = request.POST['ripsmodalidadGrupoServicioTecSal']
        ripsViaIngresoServicioSalud = request.POST['ripsViaIngresoServicioSalud']
        ripsGrupoServicios = request.POST['ripsGrupoServicios']
        ripsCondicionDestinoUsuarioEgreso = request.POST['ripsCondicionDestinoUsuarioEgreso']
        ripsCausaMotivoAtencion = request.POST['ripsCausaMotivoAtencion']
        ripsRecienNacido = request.POST["ripsRecienNacido"]
        ripsPesoRecienNacido = request.POST["ripsPesoRecienNacido"]
        ripsNumConsultasCPrenatal = request.POST["ripsNumConsultasCPrenatal"]
        ripsEdadGestacional = request.POST["ripsEdadGestacional"]
        ripsDestinoUsuarioEgresoRecienNacido = request.POST['ripsDestinoUsuarioEgresoRecienNacido']

        ripsDestinoUsu1 = RipsDestinoEgreso.objects.get(id= ripsDestinoUsuarioEgresoRecienNacido)

        grabo = Ingresos(
                         sedesClinica_id=Sede,
                         tipoDoc_id=tipoDoc,
                         documento_id=documento_llave.id,
                         consec=consecAdmision,
                         fechaIngreso=fechaIngreso,
                         #fechaSalida=NULL,
                         factura=factura,
                         numcita=numcita,
                         serviciosIng_id=  busServicio2,
                         dependenciasIngreso_id=dependenciasIngreso,
                         dxIngreso_id=dxIngreso,
                         medicoIngreso_id=medicoIngreso,
                         especialidadesMedicosIngreso_id=especialidadesMedicos,
                         serviciosActual_id=busServicio2,
                         dependenciasActual_id=dependenciasIngreso,
                         dxActual_id = dxIngreso,
                         medicoActual_id=medicoIngreso,
                         especialidadesMedicosActual_id=especialidadesMedicos,
                         #dependenciasSalida_id = dependenciasSalida,
                         #dxSalida_id = dxSalida,
                         #medicoSalida_id=medicoSalida,
                         #especialidadesMedicosSalida_id="",
                         #estadoSalida_id = estadoSalida,
                         ViasIngreso_id=viasIngreso,
                         causasExterna_id=causasExterna,
                         regimen_id=regimenes,
                         tiposCotizante_id=tiposCotizante,
                         #empresa_id=empresaId,
                         ipsRemite_id=ipsRemite,
                         numManilla=numManilla,
                         #contactoAcompañante_id=contactoAcompanante,
                         #contactoResponsable_id=contactoResponsable,
                         remitido=remitido,
                         #salidaClinica=salidaClinica,
                         #salidaDefinitiva=salidaDefinitiva,
                         ripsServiciosIng_id = ripsServiciosIng,
                         ripsServiciosActual_id=ripsServiciosIng,
                         ripsmodalidadGrupoServicioTecSal_id = ripsmodalidadGrupoServicioTecSal,
                         ripsViaIngresoServicioSalud_id = ripsViaIngresoServicioSalud,
                         ripsGrupoServicios_id = ripsGrupoServicios,
                         ripsCondicionDestinoUsuarioEgreso_id = ripsCondicionDestinoUsuarioEgreso,
                         ripsCausaMotivoAtencion_id = ripsCausaMotivoAtencion,
                         ripsRecienNacido = ripsRecienNacido,
                         ripsPesoRecienNacido = ripsPesoRecienNacido,
                         ripsNumConsultasCPrenatal = ripsNumConsultasCPrenatal,
                         ripsEdadGestacional = ripsEdadGestacional,
                         ripsDestinoUsuarioEgresoRecienNacido =ripsDestinoUsu1,
                         fechaRegistro=fechaRegistro,
                         usuarioRegistro_id=usernameId.id,
                         estadoReg=estadoReg,

        )
        print("Voy a guardar la INFO")

        grabo.save()
        print("yA grabe 2", grabo.id)
        grabo.id
        print("yA grabe" , grabo.id)

        # Grabo Dependencias

        print("Voy a guardar dependencias OJO ESTO ES UN UPDATE")
        # ejemplo
        grabo4 =  Dependencias.objects.filter(id = dependenciasIngreso).update(tipoDoc_id=tipoDoc, documento_id=documento_llave.id, consec=consecAdmision, disponibilidad='O',fechaRegistro=fechaRegistro, fechaOcupacion= fechaRegistro)

        print("Grabe HISTPRICO DEPENDENCIAS")

        # Grabo Dependencia Historico

        print("Voy a guardar HISTORICO dependencias ")

        grabo2 = HistorialDependencias(
            tipoDoc_id=tipoDoc,
            documento_id=documento_llave.id,
            consec=consecAdmision,
            dependencias_id=dependenciasIngreso,
            disponibilidad='O',
            fechaRegistro=fechaRegistro,
            usuarioRegistro_id=usernameId.id,
            #fechaLiberacion=NULL,
            fechaOcupacion=fechaRegistro,
            estadoReg=estadoReg

        )
        grabo2.save()
        print("yA grabe dependencias historico", grabo2.id)

        print("Grabe HISTPRICO DEPENDENCIAS")

        # RUTINA ARMADO CONTEXT

        ingresos = []

        #miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx =  psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        curx = miConexionx.cursor()

        detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
            Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and  i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'

        print(detalle)

        curx.execute(detalle)

        for tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
            ingresos.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                             'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                             'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                             'DxActual': dxActual})

        miConexionx.close()
        print(ingresos)
        context['Ingresos'] = ingresos

        ## ojo desde aquip


        # Combo PermisosGrales

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
        comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(
            username) + "'"

        curt.execute(comando)
        print(comando)

        permisosGrales = []

        for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
            permisosGrales.append(
                {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
                 'modulo_nombre': modulo_nombre})

        miConexiont.close()
        print(permisosGrales)

        # Fin Combo PermisosGrales
        print("permisosGrales= ", permisosGrales)

        context = {}
        context['PermisosGrales'] = permisosGrales
        context['Documento'] = documento
        context['Username'] = username
        context['Profesional'] = Profesional
        context['Sede'] = Sede
        context['PermisosGrales'] = permisosGrales
        context['NombreSede'] = NombreSede
        context['NombreSede'] = nombreSede

        # Combo Accesos usuario

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        # comando = "select opc.id id_opc, opc.perfilesClinicaId_id id_perfilesClinica,opc.modulosElementosDefId_id id_elmentosDef, elem_nombre, elem.url url ,modelem.nombre nombreElemento from seguridad_perfilesusu usu, seguridad_perfilesclinicaopciones opc, planta_planta planta, seguridad_moduloselementosdef elem, seguridad_moduloselementos modelem where usu.estadoReg = 'A' and usu.plantaId_id =  planta.id and planta.documento = '" + str(username) + "' and opc.id = usu.perfilesclinicaOpcionesId_id and elem.id =opc.modulosElementosDefId_id and modelem.id = opc.modulosElementosDefId_id "
        comando = 'select opc.id id_opc, opc."perfilesClinicaId_id" id_perfilesClinica,opc."modulosElementosDefId_id" id_elmentosDef,modulos.nombre nombre_modulo ,elem.nombre nombre_defelemento , elem.url url ,modelem.nombre nombreElemento from seguridad_perfilesusu usu, seguridad_perfilesclinicaopciones opc, planta_planta planta, seguridad_moduloselementosdef elem, seguridad_moduloselementos modelem , seguridad_perfilesclinica perfcli, seguridad_perfilesgralusu gralusu, seguridad_modulos modulos, sitios_sedesClinica  sedes where gralusu."perfilesClinicaId_id" = perfcli.id and usu."plantaId_id" = gralusu."plantaId_id" and usu."plantaId_id" =  planta.id and usu."estadoReg" = ' + "'" + 'A' + "'" + ' and  opc.id = usu."perfilesClinicaOpcionesId_id" and elem.id =opc."modulosElementosDefId_id" and modulos.id = perfcli."modulosId_id" and elem."modulosId_id" = perfcli."modulosId_id"  and sedes.id = planta."sedesClinica_id"  and planta.documento =  ' + "'" + '19465673' + "'"

        curt.execute(comando)
        print(comando)

        accesosUsuario = []

        for id_opc, id_perfilesClinica, id_elmentosDef, nombre_modulo, nombre_defelemento, url, nombreElemento in curt.fetchall():
            accesosUsuario.append(
                {'id_opc': id_opc, 'id_perfilesClinica': id_perfilesClinica, 'id_elmentosDef': id_elmentosDef,
                 'nombre_modulo': nombre_modulo, 'nombre_defelemento': nombre_defelemento, 'url': url,
                 'nombreElemento': nombreElemento})

        miConexiont.close()
        print(accesosUsuario)

        context['AccesosUsuario '] = accesosUsuario

        # Fin Accesos usuario

        # aqui la manada de combos organizarlo segun necesidades

        ingresos = []

        # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curx = miConexionx.cursor()
        #detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(
        #    Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null'
        detalle = 'SELECT i.id id, tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and ser.nombre != ' + "'" + str('TRIAGE') + "'" + ' AND dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"'

        print(detalle)

        curx.execute(detalle)

        for id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
            ingresos.append({'id':id, 'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                             'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                             'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                             'DxActual': dxActual})

        miConexionx.close()
        print(ingresos)
        context['Ingresos'] = ingresos

        # Combo de Servicios
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
            sede) + "'" + ' AND sed."servicios_id" = ser.id'
        curt.execute(comando)
        print(comando)

        servicios = []
        servicios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            servicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(servicios)

        context['Servicios'] = servicios

        # Fin combo servicios

        # Combo de SubServicios
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(
            sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id"'
        curt.execute(comando)
        print(comando)

        subServicios = []
        subServicios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            subServicios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(subServicios)

        context['SubServicios'] = subServicios

        # Fin combo SubServicios

        # Combo TiposDOc
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = "SELECT id ,nombre FROM usuarios_TiposDocumento "
        curt.execute(comando)
        print(comando)

        tiposDoc = []
        # tiposDoc.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposDoc.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposDoc)

        context['TiposDoc'] = tiposDoc

        # Fin combo TiposDOc

        # Combo Habitaciones
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = ' SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip where dep."sedesClinica_id" = ' + "'" + str(
            Sede) + "'" + ' AND tip.nombre=' + "'" + str(
            'HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id'
        curt.execute(comando)
        print(comando)

        habitaciones = []
        habitaciones.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            habitaciones.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(habitaciones)

        context['Habitaciones'] = habitaciones

        # Fin combo Habitaciones

        # Combo Especialidades
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = "SELECT id ,nombre FROM clinico_Especialidades"
        curt.execute(comando)
        print(comando)

        especialidades = []
        especialidades.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            especialidades.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(especialidades)

        context['Especialidades'] = especialidades

        # Fin combo Especialidades

        # Combo EspecialidadesMedicos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT em.id ,e.nombre FROM clinico_Especialidades e, clinico_EspecialidadesMedicos em,planta_planta pl  where em."especialidades_id" = e.id and em."planta_id" = pl.id AND pl.documento = ' + "'" + str(
            username) + "'"
        curt.execute(comando)
        print(comando)

        especialidadesMedicos = []
        especialidadesMedicos.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            especialidadesMedicos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(especialidadesMedicos)

        context['EspecialidadesMedicos'] = especialidadesMedicos

        # Fin combo EspecialidadesMedicos

        # Combo Medicos
        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = 'SELECT p.id id, p.nombre nombre FROM planta_planta p,clinico_medicos med, planta_tiposPlanta tp WHERE p."sedesClinica_id" = ' + "'" + str(
            Sede) + "'" + ' and p."tiposPlanta_id" = tp.id and tp.nombre = ' + "'" + str(
            'MEDICO') + "'" + ' and med.planta_id = p.id'

        curt.execute(comando)
        print(comando)

        medicos = []
        medicos.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            medicos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(medicos)

        context['Medicos'] = medicos

        # Fin combo Medicos

        # Combo TiposFolio

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT e.id id, e.nombre nombre FROM clinico_tiposFolio e"

        curt.execute(comando)
        print(comando)

        tiposFolio = []
        tiposFolio.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposFolio.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposFolio)

        context['TiposFolio'] = tiposFolio

        # Fin combo TiposFolio

        # Combo TiposUsuario

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposusuario p"

        curt.execute(comando)
        print(comando)

        tiposUsuario = []
        # tiposUsuario.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposUsuario.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposUsuario)

        context['TiposUsuario'] = tiposUsuario

        # Fin combo Tipos Usuario

        # Combo TiposDocumento

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM usuarios_tiposDocumento p"

        curt.execute(comando)
        print(comando)

        tiposDocumento = []
        # tiposDocumento.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposDocumento.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposDocumento)

        context['TiposDocumento'] = tiposDocumento

        # Fin combo TiposDocumento

        # Combo Centros

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM sitios_centros p"

        curt.execute(comando)
        print(comando)

        centros = []

        for id, nombre in curt.fetchall():
            centros.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposDocumento)

        context['Centros'] = centros

        # Fin combo Centros

        # Combo Diagnosticos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM clinico_diagnosticos p"

        curt.execute(comando)
        print(comando)

        diagnosticos = []
        diagnosticos.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            diagnosticos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(diagnosticos)

        context['Diagnosticos'] = diagnosticos

        # Fin combo Diagnosticos

        # Combo Departamentos

        # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT d.id id, d.nombre  nombre FROM sitios_departamentos d"

        curt.execute(comando)
        print(comando)

        departamentos = []
        # tiposDocumento.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            departamentos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(departamentos)

        context['Departamentos'] = departamentos

        # Fin combo Departamentos

        # Combo Ciudades

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id, c.nombre  nombre FROM sitios_ciudades c"

        curt.execute(comando)
        print(comando)

        ciudades = []

        for id, nombre in curt.fetchall():
            ciudades.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(ciudades)

        context['Ciudades'] = ciudades

        # Fin combo Ciudades

        # Combo Modulos

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre, c.nomenclatura nomenclatura, c.logo logo FROM seguridad_modulos c"

        curt.execute(comando)
        print(comando)

        modulos = []

        for id, nombre, nomenclatura, logo in curt.fetchall():
            modulos.append({'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo})

        miConexiont.close()
        print(modulos)

        context['Modulos'] = modulos

        # Fin combo Modulos

        # Combo PermisosGrales

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        # comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + username + "'" + ' and  perfcli."sedesClinica_id" = ' + "'" + str(Sede) + "'"
        comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo ,perfcli."modulosId_id" modulo_id , m.nombre modulo_nombre from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli where planta.id = gral."plantaId_id" and  gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and planta.documento =' + "'" + str(
            username) + "'"

        curt.execute(comando)
        print(comando)

        permisosGrales = []

        for id, nombre, nomenclatura, logo, modulo_id, modulo_nombre in curt.fetchall():
            permisosGrales.append(
                {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'modulo_id': modulo_id,
                 'modulo_nombre': modulo_nombre})

        miConexiont.close()
        print(permisosGrales)

        context['PermisosGrales'] = permisosGrales

        # Fin Combo PermisosGrales

        # Combo PermisosDetalle

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = 'select m.id id, m.nombre nombre , m.nomenclatura nomenclatura, m.logo logo, modeledef.nombre nombreOpcion ,elemen.nombre nombreElemento from seguridad_modulos m, seguridad_perfilesgralusu gral, planta_planta planta, seguridad_perfilesclinica perfcli, seguridad_perfilesclinicaopciones perfopc, seguridad_perfilesusu perfdet, seguridad_moduloselementosdef modeledef, seguridad_moduloselementos elemen where planta.id= 1 and  planta.id = gral."plantaId_id" and gral."perfilesClinicaId_id" = perfcli.id and perfcli."modulosId_id" = m.id and gral.id = perfdet."plantaId_id" and perfdet."perfilesClinicaOpcionesId_id" = perfopc.id and perfopc."perfilesClinicaId_id" =perfcli.id and  perfopc."modulosElementosDefId_id" = modeledef.id and elemen.id = modeledef."modulosElementosId_id"  and planta.documento = ' + "'" + username + "'"

        curt.execute(comando)
        print(comando)

        permisosDetalle = []

        for id, nombre, nomenclatura, logo, nombreOpcion, nombreElemento in curt.fetchall():
            permisosDetalle.append(
                {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion': nombreOpcion,
                 'nombreElemento': nombreElemento})

        miConexiont.close()
        print(permisosDetalle)

        context['PermisosDetalle'] = permisosDetalle

        # Fin Combo PermisosDetalle

        # Combo Vias Ingreso

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM clinico_viasingreso c"

        curt.execute(comando)
        print(comando)

        viasIngreso = []

        for id, nombre in curt.fetchall():
            viasIngreso.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(viasIngreso)

        context['ViasIngreso'] = viasIngreso

        # Fin combo vias Ingreso

        # Combo Causas Externa

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM clinico_causasExterna c"

        curt.execute(comando)
        print(comando)

        causasExterna = []

        for id, nombre in curt.fetchall():
            causasExterna.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(causasExterna)

        context['CausasExterna'] = causasExterna

        # Fin combo causasExterna

        # Combo Regimenes

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM clinico_regimenes c"

        curt.execute(comando)
        print(comando)

        regimenes = []

        for id, nombre in curt.fetchall():
            regimenes.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(regimenes)

        context['Regimenes'] = regimenes

        # Fin combo regimenes

        # Combo Tipos Cotizante

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM clinico_tiposcotizante c"

        curt.execute(comando)
        print(comando)

        tiposCotizante = []

        for id, nombre in curt.fetchall():
            tiposCotizante.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposCotizante)

        context['TiposCotizante'] = tiposCotizante

        # Fin combo tiposCotizante

        # Combo municipios

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM sitios_municipios c"

        curt.execute(comando)
        print(comando)

        municipios = []

        for id, nombre in curt.fetchall():
            municipios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(municipios)

        context['Municipios'] = municipios

        # Fin combo municipios

        # Combo localidades

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM sitios_localidades c"

        curt.execute(comando)
        print(comando)

        localidades = []

        for id, nombre in curt.fetchall():
            localidades.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(localidades)

        context['Localidades'] = localidades

        # Fin combo localidades

        # Combo estadoCivil

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM basicas_estadocivil c"

        curt.execute(comando)
        print(comando)

        estadoCivil = []

        for id, nombre in curt.fetchall():
            estadoCivil.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(estadoCivil)

        context['EstadoCivil'] = estadoCivil

        # Fin combo estadoCivil

        # Combo ocupaciones

        # iConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT c.id id,c.nombre nombre FROM basicas_ocupaciones c"

        curt.execute(comando)
        print(comando)

        ocupaciones = []

        for id, nombre in curt.fetchall():
            ocupaciones.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(ocupaciones)

        context['Ocupaciones'] = ocupaciones

        # Fin combo ocupaciones
        # FIN RUTINA ARMADO CONTEXT


    return render(request, "admisiones/panelAdmisiones.html", context)



# fin nuevo mcodigo crear admison DEF



def crearResponsables(request):
    print("Entre crear Responsables")
    pass


def UsuariosModal(request):
        print("Entre a buscar Usuario para la Modal")

        tipoDoc = request.POST['tipoDoc']
        documento = request.POST['documento']

        print ("documento = " , documento)
        print("tipodoc = " ,tipoDoc)



        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT usu.nombre, usu.documento, usu.genero, usu."fechaNacio" fechaNacio, usu.pais_id,  usu.departamentos_id, usu.ciudades_id, usu.direccion, usu.telefono, usu.contacto, usu."centrosC_id", usu."tipoDoc_id", usu."tiposUsuario_id", usu.municipio_id municipio, usu.localidad_id localidad, usu."estadoCivil_id" estadoCivil , usu.ocupacion_id ocupacion, correo correo  FROM usuarios_usuarios usu WHERE usu."tipoDoc_id" = ' + "'"  + str(tipoDoc) + "'" + ' AND usu.documento = ' + "'" + str(documento) + "'"
        print(comando)
        curt.execute(comando)

        Usuarios = {}

        for nombre, documento, genero, fechaNacio, pais_id,  departamentos_id, ciudades_id, direccion, telefono, contacto, centrosc_id, tipoDoc_id, tiposUsuario_id, municipio, localidad, estadoCivil, ocupacion, correo  in curt.fetchall():
            Usuarios = {'nombre': nombre, 'documento': documento, 'genero': genero, 'fechaNacio': fechaNacio , 'pais' : pais,  'departamento' : departamentos_id, 'ciudad': ciudades_id,  'direccion':  direccion, 'telefono' :telefono, 'contacto': contacto, 'centrosc_id':centrosc_id, 'tipoDoc_id':tipoDoc_id,'tiposUsuario_id':tiposUsuario_id,
                        'municipio':municipio, 'localidad':localidad, 'estadoCivil':estadoCivil, 'ocupacion':ocupacion,'correo':correo}

        miConexiont.close()
        print(Usuarios)

        if Usuarios == '[]':
            datos = {'Mensaje' : 'Usuario No existe'}
            return JsonResponse(datos, safe=False)
        else:
            return JsonResponse(Usuarios, safe=False)




def guardarUsuariosModal(request):
    print("Entre a grabar Usuarios Modal")
    tipoDoc_id = request.POST["tipoDoc"]

    documento = request.POST["documento"]
    nombre = request.POST["nombre"]
    print("DOCUMENTO = " ,documento)
    print(nombre)
    genero = request.POST["genero"]
    pais = request.POST["pais"]
    departamento = request.POST["departamentos"]
    ciudad = request.POST["ciudades"]
    fechaNacio = request.POST["fechaNacio"]

    print ("departamento = ", departamento)
    print("ciudad = ", ciudad)
    if (fechaNacio == ''):
         fechaNacio='0001-01-01 00:00:01'
    print("fechaNacio = ", fechaNacio)
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    contacto = request.POST["contacto"]
    #centrosc_id = request.POST["centrosc"]
    #quemado por el momento mientras encuentor que pasa
    centrosc_id = 1
    tiposUsuario_id = request.POST["tiposUsuario"]
    print("DIRECCION = ", direccion)
    print("telefono = ", telefono)
    print("contacto = ", contacto)
    municipio  = request.POST['municipios']
    localidad  = request.POST['localidades']
    estadoCivil  = request.POST['estadoCivil']
    ocupacion = request.POST['ocupaciones']
    correo = request.POST["correo"]

    correo = request.POST["correo"]

    print("centrosc_id = ", centrosc_id)

    print(documento)
    print(tipoDoc_id)

    #miConexion11 =  MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion11 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur11 = miConexion11.cursor()
    comando = 'SELECT usu.id, usu."tipoDoc_id", usu.documento FROM usuarios_usuarios usu WHERE usu."tipoDoc_id" = ' + "'" + str(tipoDoc_id) + "'" + ' AND usu.documento = ' + "'" + str(documento) + "'"

    print(comando)
    cur11.execute(comando)

    Usuarios = []

    for id, tipoDoc_id, documento in cur11.fetchall():
        Usuarios.append({'id': id, 'tipoDoc_id': tipoDoc_id, 'documento': documento})

    miConexion11.close()

    fechaRegistro = datetime.datetime.now()


    if Usuarios == []:

         print("Entre a crear")
         #miConexion3 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
         miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
         cur3 = miConexion3.cursor()
         comando = 'insert into usuarios_usuarios (nombre, documento, genero, "fechaNacio", pais_id,  departamentos_id, ciudades_id, direccion, telefono, contacto, "centrosC_id", "tipoDoc_id", "tiposUsuario_id", municipio_id, localidad_id, "estadoCivil_id", ocupacion_id, correo ,"fechaRegistro", "estadoReg") values (' + "'" + str(nombre) + "'" + ' , ' + "'" + str(documento) + "'" + ', ' + "'" + str(genero) + "'" + '  , ' + "'" + str(fechaNacio) + "'" +  ', ' + "'" + str(pais) + "'" + ', ' + "'" + str(departamento) + "'" +  '  , ' + "'" +  str(ciudad) + "'" + '  , ' + "'" +  str(direccion) + "'" + ', ' + "'" + str(telefono) + "'" + ', ' + "'" + str(contacto) + "'" + ', ' + "'" + str(centrosc_id) + "'" +  ', ' + "'" + str(tipoDoc_id) + "'" + ', ' + "'" + str(tiposUsuario_id) + "' , " + "'" + str(municipio) + "'" +   ', ' + "'" + str(localidad) + "'" + ", " + "'" + str(estadoCivil) + "'" + ", " + "'" + str(ocupacion) + "'" + ", " + "'" + str(correo) + "', " +  "'"  + str(fechaRegistro) + "'"  +  ", 'A'"  +      ')'
         print(comando)
         cur3.execute(comando)
         miConexion3.commit()
         miConexion3.close()
         return HttpResponse("Usuario Creado ! ")
    else:
        print("Entre a actualizar")
        #miConexion3 =  MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        cur3 = miConexion3.cursor()
        comando = 'update usuarios_usuarios set nombre = ' "'" + str(nombre) +  "'" +  ', direccion  = ' + "'" +  str(direccion) + "'" + ', genero = ' + "'" + str(genero) + "'"  + ', "fechaNacio" = ' + "'" + str(fechaNacio) + "'"   + ', telefono= ' + "'" + str(telefono) + "'" +  ', contacto= ' + "'" +  str(contacto) + "'" +  ', "centrosC_id"= ' + "'" + str(centrosc_id) + "'" + ', "tiposUsuario_id" = ' + "'" + str(tiposUsuario_id) + "' , "   + ' municipio_id = ' + "'" + str(municipio) + "'" +  ', localidad_id = ' + "'" + str(localidad) + "'" + ', "estadoCivil_id"= ' + "'" + str(estadoCivil) + "'" + ', ocupacion_id = ' + "'" + str(ocupacion) + "'"  + ', correo = ' + "'" + str(correo) + "'"  + ' WHERE "tipoDoc_id" = ' + str(tipoDoc_id) + ' AND documento = ' + "'" + str(documento) + "'"

        print(comando)
        cur3.execute(comando)
        miConexion3.commit()


        miConexion3.close()
        return HttpResponse("Usuario Actualizado ! ")

def encuentraAdmisionModal(request) : #, tipoDoc, documento, consec, sede):

        tipoDoc = request.POST["tipoDoc"]
        documento = request.POST["documento"]
        sede = request.POST["sede"]
        consec = request.POST["consec"]


        print("Entre a buscar una Admision Modal")
        print("documento = ", documento)
        print("tipodoc = ", tipoDoc)
        print("consecutivoAdmision = ", consec)
        print("Sede = ", sede)
        print("consec = ", consec)

        tipoDoc1 = TiposDocumento.objects.get(nombre=tipoDoc)
        print("tipodoc1 = ", tipoDoc1.id)
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = 'SELECT tp.nombre tipoDoc,  u.documento documento, u.nombre  paciente , i.consec consec , i."fechaIngreso" ingreso , i."fechaSalida" salida, ser.nombre servicioNombreIng, dep.nombre dependenciasIngreso ,med1.nombre medicoIngreso, esp1.nombre espMedico,diag1.nombre diagMedico,vias.nombre viasIngreso, cexterna.nombre causasExterna,reg.nombre regimenes ,cot.nombre cotizante,i.remitido remitido,ips.nombre ips ,i."numManilla" numManilla, diag1.nombre dxIngreso FROM admisiones_ingresos i inner join usuarios_usuarios u on (u."tipoDoc_id" = i."tipoDoc_id" and u.id = i."documento_id" ) inner join sitios_dependencias dep on (dep."sedesClinica_id" = i."sedesClinica_id" and dep."tipoDoc_id" =  i."tipoDoc_id" and dep.documento_id =i."documento_id"  and dep.consec = i.consec) inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on (deptip.id = dep."dependenciasTipo_id") inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = i."sedesClinica_id") inner join clinico_servicios ser  on (ser.id = sd.servicios_id  and ser.id = i."serviciosIng_id" ) left join clinico_especialidades esp1 on (esp1.id = i."especialidadesMedicosIngreso_id" ) left join clinico_diagnosticos diag1 on (diag1.id = i."dxIngreso_id") left join clinico_medicos med1 on (med1.id =i."medicoIngreso_id"  ) inner join clinico_viasIngreso vias on (vias.id = i."ViasIngreso_id") left join clinico_causasExterna cexterna on (cexterna.id = i."causasExterna_id") inner join clinico_regimenes reg on (reg.id = i.regimen_id) inner join clinico_tiposcotizante cot on (cot.id = i."tiposCotizante_id") left  join clinico_ips ips on (ips.id =i."ipsRemite_id") WHERE i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' and u."tipoDoc_id" = ' + "'" + str(tipoDoc1.id) + "'" + ' and u.documento = ' + "'" + str(documento) + "'" + ' and i.consec= ' + "'" + str(consec) + "'" + ' and i."fechaSalida" is null'

        print(comando)
        curt.execute(comando)

        Usuarios = {}

        for tipoDoc,  documento,paciente ,consec ,  ingreso , salida, servicioNombreIng, dependenciasIngreso , medicoIngreso, espMedico,diagMedico, viasIngreso, causasExterna,regimenes, cotizante, remitido,ips , numManilla, dxIngreso  in curt.fetchall():
            Usuarios = {'tipoDoc': tipoDoc, 'documento': documento, 'paciente': paciente, 'ingreso': ingreso,
                        'salida': salida, 'servicioNombreIng': servicioNombreIng, 'dependenciasIngreso': dependenciasIngreso,
                        'medicoIngreso': medicoIngreso, 'espMedico': espMedico, 'diagMedico': diagMedico,
                        'viasIngreso': viasIngreso, 'causasExterna': causasExterna,
                        'regimenes': regimenes, 'cotizante': cotizante, 'remitido': remitido,
                        'ips': ips, 'numManilla': numManilla, 'dxIngreso':dxIngreso}

        miConexiont.close()
        print(Usuarios)

        if Usuarios == '[]':
            datos = {'Mensaje': 'Usuario No existe'}
            return JsonResponse(datos, safe=False)
        else:
            datos = {'Mensaje': 'Usuario SIII existe'}
            return JsonResponse(Usuarios, safe=False)


def cambioServicio(request):

    print("Entre a buscar una Cambio Servicio  Modal")
    sede = request.POST['sede']
    print("sede = ", sede)
    ingreso = request.POST['valor']
    print("ingreso = ", ingreso)



    datos  = Ingresos.objects.get(id=ingreso)


    datosTip = TiposDocumento.objects.get(nombre=datos.tipoDoc)

    datosDoc = Usuarios.objects.get(nombre=datos.documento)
  

    tipoDocPaciente  =  datosTip.id
    documentoPaciente = datosDoc.id
    consecutivo = datos.consec
    print("datos Tipo doc = ", datosTip.id)
    print("datos  documento = ", datosDoc.id)
    print("datos  consecutivo= ", datos.consec)


    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT i."tipoDoc_id" tipoDocId, tp.nombre tipoDoc,  i.documento_id documentoId, u.documento documento, u.nombre  paciente , i.consec consec , i."fechaIngreso" ingreso , i."fechaSalida" salida, ser.nombre servicioNombreIng, dep.nombre dependenciasIngreso ,med1.nombre medicoIngreso, esp1.nombre espMedico,diag1.nombre diagMedico,vias.nombre viasIngreso, cexterna.nombre causasExterna,reg.nombre regimenes ,cot.nombre cotizante,i.remitido remitido,ips.nombre ips ,i."numManilla" numManilla, diag1.nombre dxIngreso, i."contactoResponsable_id" responsable, i."contactoAcompañante_id"  acompanante FROM admisiones_ingresos i inner join usuarios_usuarios u on (u."tipoDoc_id" = i."tipoDoc_id" and u.id = i."documento_id" ) inner join sitios_dependencias dep on (dep."sedesClinica_id" = i."sedesClinica_id" and dep."tipoDoc_id" =  i."tipoDoc_id" and dep.documento_id =i."documento_id"  and dep.consec = i.consec) inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on (deptip.id = dep."dependenciasTipo_id") inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = i."sedesClinica_id") inner join clinico_servicios ser  on (ser.id = sd.servicios_id  and ser.id = i."serviciosIng_id" ) left join clinico_especialidades esp1 on (esp1.id = i."especialidadesMedicosIngreso_id" ) left join clinico_diagnosticos diag1 on (diag1.id = i."dxIngreso_id") left join clinico_medicos med1 on (med1.id =i."medicoIngreso_id"  ) inner join clinico_viasIngreso vias on (vias.id = i."ViasIngreso_id") left join clinico_causasExterna cexterna on (cexterna.id = i."causasExterna_id") inner join clinico_regimenes reg on (reg.id = i.regimen_id) inner join clinico_tiposcotizante cot on (cot.id = i."tiposCotizante_id") left  join clinico_ips ips on (ips.id =i."ipsRemite_id") WHERE i.id = ' + "'" + str(ingreso) + "'"

    print(comando)
    curt.execute(comando)

    usuarios = {}

    for tipoDocId, tipoDoc, documentoId, documento, paciente, consec, ingreso, salida, servicioNombreIng, dependenciasIngreso, medicoIngreso, espMedico, diagMedico, viasIngreso, causasExterna, regimenes, cotizante, remitido, ips, numManilla, dxIngreso, responsable, acompanante in curt.fetchall():
        usuarios = {'tipoDocId':tipoDocId, 'tipoDoc': tipoDoc, 'documentoId':documentoId, 'documento': documento, 'paciente': paciente, 'consec':consec, 'ingreso': ingreso,
                    'salida': salida, 'servicioNombreIng': servicioNombreIng,
                    'dependenciasIngreso': dependenciasIngreso,
                    'medicoIngreso': medicoIngreso, 'espMedico': espMedico, 'diagMedico': diagMedico,
                    'viasIngreso': viasIngreso, 'causasExterna': causasExterna,
                    'regimenes': regimenes, 'cotizante': cotizante, 'remitido': remitido,
                    'ips': ips, 'numManilla': numManilla, 'dxIngreso': dxIngreso, 'responsable':responsable, 'acompanante':acompanante}

    miConexiont.close()
    print(usuarios)

    cambioServicio = {}
    cambioServicio['Usuarios'] = usuarios



    dependenciasActual = {}

    # Ahora llevamos la dependencia Actual

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'select dep.id id , dep.numero numero , dep.nombre depNombre, sd.nombre servicio, sub.nombre subServicio,   dep."tipoDoc_id" tipoDocId, dep.documento_id documentoId, dep."fechaRegistro" fechaRegistro, dep.disponibilidad dispo,dep.consec consec ,dep."fechaOcupacion" ocupacion from sitios_dependencias dep, sitios_serviciosSedes sd, sitios_subServiciosSedes sub where dep."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' and dep."tipoDoc_id"=' + "'" + str(datosTip.id) + "'" + ' and dep.documento_id=' + "'" + str(datosDoc.id) + "'" + ' and dep.consec = ' + str(consec) + '  and dep.disponibilidad = ' + "'" + str('O') + "'" + ' and sub."serviciosSedes_id" = sd.id and sd.id=dep."serviciosSedes_id" and sub.id= dep."subServiciosSedes_id"'

    print(comando)
    curt.execute(comando)

    for id, numero, depNombre, servicio, subServicio, tipoDocId, documentoId, fechaRegistro, dispo, consec, ocupacion in curt.fetchall():
        dependenciasActual = {'id': id, 'numero': numero, 'depNombre': depNombre, 'servicio': servicio,
                    'subServicio': subServicio,
                    'tipoDocId': tipoDocId, 'documentoId': documentoId,
                    'fechaRegistro': fechaRegistro,'dispo':dispo, 'consec':consec,'ocupacion':ocupacion   }

    miConexiont.close()

    cambioServicio['DependenciasActual'] = dependenciasActual
    


    # Combo de Servicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id AND ser.nombre in ( ' + "'" + str('HOSPITALIZACION') + "','" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    cambioServicio['Servicios'] = servicios

    # Fin combo servicios

    # Combo de SubServicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id" AND ser.nombre in ( ' + "'" + str('HOSPITALIZACION') + "','" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)


    cambioServicio['SubServicios'] = subServicios

    # Fin combo SubServicios


    # Combo Habitaciones

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip , sitios_serviciosSedes sd, clinico_servicios ser where dep."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND tip.nombre=' + "'" + str('HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id AND dep.disponibilidad = ' + "'" + str('L') + "'" + ' AND sd.id=dep."serviciosSedes_id" AND ser.id = sd."servicios_id" and ser.nombre in (' + "'" + str('HOSPITALIZACION') + "'," + "'" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    cambioServicio['Habitaciones'] = habitaciones

    # Aqui FURIPS Leer el id y enviar un Furips form por aqui a ver que pasa

    tipoDocPaciente  =  datosTip.id
    documentoPaciente = datosDoc.id
    consecutivo = datos.consec


    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT "consecVictima",  "numeroFactura" ,  "fechaRadicado" ,  "lugarRecogeVictima" ,  "eventoDescripcion" ,  "direccionEvento" ,  "fechaEvento" ,  "documentoInvolucrado" ,  "tipoVehiculo" ,  codigoaseguradora ,   "numeroPlacaTranporto" ,  "fechaIniPoliza" ,  "fechaFinPoliza" ,  "codigoInscripcion" ,  "codigoInscripcionRecibe" ,  "documentoPropietario" , "numeroRadicadoAnterior" ,  "direccionPropietario" ,  "primerApellidoInvolucrado" ,  "cobroExcedentePoliza" ,   "numeroRadicacion" ,  "direccionInvolucrado" ,  "placaVehiculo" ,  "primerApellidoPropietario" ,  "marcaVehiculo" ,  "primerApellidoVictima" ,  "numeroPoliza" ,  "fechaRegistro" ,  "estadoReg" ,   "documentoProfesionalAtendio_id" ,  "dxPrincEgreso_id" ,  "dxPrincIngreso_id" ,  "dxRel1Egreso_id" ,  "dxRel1Ingreso_id" ,  "dxRel2Egreso_id" ,  "dxRel2Ingreso_id" ,  "evento_id" ,  "localidadEvento_id" ,  "municipioEvento_id" ,  "municipioPropietario_id" ,"sedesClinica_id" ,"tipoDocVictima_id" ,  "tipoDocPropietario_id" ,"usuarioCrea_id",  "amparoReclamaAFosygaGastos" ,  "amparoReclamaAFosygaQx" ,  "amparoReclamaFacturadoGastos" , "amparoReclamaFacturadoQx" ,  "certificacionEgreso" ,  "certificacionIngreso" ,  "condicionAccidentado" ,  "departamentoEvento_id" ,  "departamentoInvolucrado_id" ,  "departamentoPropietario_id" ,  "documentoVictima_id" ,  estado,  "fechaAceptacion" ,  "fechaRemision" ,  "intervencionAutoridad" ,  "localidadInvolucrado_id" ,  "localidadPropietario_id" ,  "municipioInvolucrado_id" ,  "prestadorRecibe_id" ,  "prestadorRemite_id" ,  "primerNombreInvolucrado" ,  "primerNombrePropietario" ,  "primerNombreVictima" ,  "profesionalRecibe" ,  "profesionalRemite_id" ,  "segundoApellidoInvolucrado" ,  "segundoApellidoPropietario" ,  "segundoApellidoVictima" ,  "segundoNombreInvolucrado" ,  "segundoNombrePropietario" ,  "segundoNombreVictima" ,  "tipoDocInvolucrado_id" ,  "tipoDocProfesionalAtendio_id" ,  "tipoReferencia" ,  "tipoServicioVehiculo" ,  "tipoTransporteTransporto" ,  "trasportoVictimaDesde" ,  "trasportoVictimaHasta",   "zonaEvento" ,  consec ,  "documento_id" ,  "tipoDoc_id" FROM admisiones_furips where documento_id = ' + "'" + str(tipoDocPaciente) + "'" + ' AND "tipoDoc_id" = ' + "'" + str(documentoPaciente) + "'" + '  AND consec = ' +"'" + str(consecutivo) + "'"


    curt.execute(comando)
    print(comando)

    furips = []
    furips.append({'id': '', 'nombre': ''})

    for  consecVictima,  numeroFactura ,  fechaRadicado ,  lugarRecogeVictima ,  eventoDescripcion ,  direccionEvento ,  fechaEvento ,  documentoInvolucrado ,  tipoVehiculo ,  codigoAseguradora ,  numeroPlacaTranporto ,  fechaIniPoliza ,  fechaFinPoliza ,  codigoInscripcion ,  codigoInscripcionRecibe ,  documentoPropietario , numeroRadicadoAnterior ,  direccionPropietario ,  primerApellidoInvolucrado ,  cobroExcedentePoliza ,  numeroRadicacion ,  direccionInvolucrado ,  placaVehiculo ,  primerApellidoPropietario ,  marcaVehiculo ,  primerApellidoVictima ,  numeroPoliza ,  fechaRegistro ,  estadoReg ,  documentoProfesionalAtendio_id ,  dxPrincEgreso_id ,  dxPrincIngreso_id ,  dxRel1Egreso_id ,  dxRel1Ingreso_id ,  dxRel2Egreso_id ,  dxRel2Ingreso_id ,  evento_id ,  localidadEvento_id ,  municipioEvento_id ,  municipioPropietario_id ,  sedesClinica_id ,  tipoDocVictima_id ,  tipoDocPropietario_id ,  usuarioCrea_id ,  amparoReclamaAFosygaGastos ,  amparoReclamaAFosygaQx ,  amparoReclamaFacturadoGastos ,  amparoReclamaFacturadoQx ,  certificacionEgreso ,  certificacionIngreso ,  condicionAccidentado ,  departamentoEvento_id ,  departamentoInvolucrado_id ,  departamentoPropietario_id ,  documentoVictima_id ,  estado,  fechaAceptacion ,  fechaRemision ,  intervencionAutoridad ,  localidadInvolucrado_id ,  localidadPropietario_id ,  municipioInvolucrado_id ,  prestadorRecibe_id ,  prestadorRemite_id ,  primerNombreInvolucrado ,  primerNombrePropietario ,  primerNombreVictima ,  profesionalRecibe ,  profesionalRemite_id ,  segundoApellidoInvolucrado ,  segundoApellidoPropietario ,  segundoApellidoVictima ,  segundoNombreInvolucrado ,  segundoNombrePropietario ,  segundoNombreVictima ,  tipoDocInvolucrado_id ,  tipoDocProfesionalAtendio_id ,  tipoReferencia ,  tipoServicioVehiculo ,  tipoTransporteTransporto ,  trasportoVictimaDesde ,  trasportoVictimaHasta,  zonaEvento ,  consec ,  documento_id ,  tipoDoc_id  in curt.fetchall():
        furips.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(furips)

    cambioServicio['Furips'] = furips


    # FIN FURIPS

    # Fin combo Habitaciones

    if cambioServicio == '[]':
        datos = {'Mensaje': 'Usuario No existe'}
        return JsonResponse(cambioServicio, safe=False)
    else:
        datos = {'Mensaje': 'Usuario SIII existe'}
        return JsonResponse(cambioServicio, safe=False)



def guardaCambioServicio(request):
    print ("entre guardaCambioServicio")
    CambioServicio = {}
   
    tipoDoc = request.POST['tipoDocx']
    documento = request.POST["documentox"]
    consec = request.POST["consecx"]
    pacientex = request.POST["pacientex"]
    print("tipoDoc  = ", tipoDoc)
    print ("documento = ", documento )
    print("consec = ", consec )
    servicioFin = request.POST["servicioCambio"]
    subServicioFin = request.POST["subServicioCambio"]
    dependenciaFin = request.POST["dependenciaCambio"]
    fechaOcupacion = datetime.now()
    fechaRegistro= fechaOcupacion



    CambioServicio['TipoDocx'] = tipoDoc
    CambioServicio['Documentox'] = documento
    CambioServicio['Consecx'] = consec
    CambioServicio['Pacientex'] = pacientex
    #CambioServicio['ServicioCambio'] = servicioFin
    #CambioServicio['SubServicioCambio'] = subServicioFin
    #CambioServicio['DependenciaCambio'] = dependenciaFin


    username_id = request.POST["username_id"]
    print("servicioFin = ", servicioFin )
    print("subServicioFin = ", subServicioFin )
    print("fechaOcupacion = ", fechaOcupacion)
    print("username_id = ", username_id)
    CambioServicio['Username_id'] = username_id


    # Aqui consigo el servicio Actual

    servicioActualId = ServiciosSedes.objects.get(id=servicioFin)
    print("servicioActualId = ", servicioActualId.id)	

    documentoId = Usuarios.objects.get(documento=documento)
    print("el id del documento es : ", documentoId.id)
    tipoDocId = TiposDocumento.objects.get(nombre=tipoDoc)
    print("el id del tipo del  documento es : ", tipoDocId.id)

    dependenciaActualId = Dependencias.objects.get(documento_id=documentoId.id , tipoDoc_id=tipoDocId.id , consec=consec)
    print("el id del dependenciaActualId es : ", dependenciaActualId.id)
    dependenciaFinalId = Dependencias.objects.get(serviciosSedes_id=servicioFin , subServiciosSedes_id=subServicioFin , id=dependenciaFin)
    print("el id del dependenciaFinalId es : ", dependenciaFinalId.id)
    ingresoActualId = Ingresos.objects.get(documento_id=documentoId.id , tipoDoc_id=tipoDocId.id , consec=consec)
    print("el id del ingresoFinalId es : ", ingresoActualId.id)


    sede = request.POST['sede'] 
    sedeSeleccionada = request.POST['sedeSeleccionada'] 
    numReporte = request.POST['numReporte'] 
    grupo = request.POST['sede']
    subGrupo = request.POST['subGrupo'] 
    nombreSede = request.POST['nombreSede'] 
    profesional = request.POST['profesional'] 
    permisosGrales = request.POST['permisosGrales'] 
    escogeModulo = request.POST['escogeModulo'] 
    permisosDetalle = request.POST['permisosDetalle'] 

    CambioServicio['Sede'] = sede
    CambioServicio['SedeSeleccionada'] = sedeSeleccionada
    CambioServicio['NumReporte'] = numReporte
    CambioServicio['Grupo'] = grupo
    CambioServicio['SubGrupo'] = subGrupo
    CambioServicio['NombreSede'] = nombreSede
    CambioServicio['Profesional'] = profesional
    CambioServicio['PermisosGrales'] = permisosGrales
    CambioServicio['EscogeModulo'] = escogeModulo
    CambioServicio['PermisosDetalle'] = permisosDetalle




    # Actualiza la dependecia Actual

    grabo01 =  Dependencias.objects.filter(id = dependenciaActualId.id).update(tipoDoc_id='', documento_id='', consec=0, disponibilidad='L',fechaRegistro=fechaRegistro, fechaLiberacion= fechaOcupacion)
    print ("pase grabo01", grabo01)

    # Actualiza la dependencia Nueva

    grabo02 =  Dependencias.objects.filter(id = dependenciaFinalId.id).update(tipoDoc_id=tipoDocId.id, documento_id=documentoId.id, consec=consec, disponibilidad='O',fechaRegistro=fechaRegistro, fechaOcupacion= fechaOcupacion)
    print("pase grabo02", grabo02)
    # Inserta en dependeciasHistoricos

    # Actualiza la admision en Ingresos

    grabo03 =  Ingresos.objects.filter(id = ingresoActualId.id).update(dependenciasActual_id=dependenciaFinalId.id, serviciosActual_id = servicioActualId.servicios_id)
    print("pase grabo03", grabo03)

    # Registro el historico de dependencias


    grabo04 = HistorialDependencias(
            tipoDoc_id=tipoDocId.id,
            documento_id=documentoId.id,
            consec=consec,
            dependencias_id=dependenciaActualId.id,
            disponibilidad='L',
            fechaRegistro=fechaRegistro,
            usuarioRegistro_id=username_id,
            fechaLiberacion=fechaRegistro,
            fechaOcupacion=dependenciaActualId.fechaOcupacion,
            estadoReg='A'

        )
    grabo04.save()
    print("yA grabe dependencias historico", grabo04.id)

    # Combo de Servicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id AND ser.nombre in ( ' + "'" + str('HOSPITALIZACION') + "','" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    CambioServicio['Servicios'] = servicios

    # Fin combo servicios


    # Combo de SubServicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed."sedesClinica_id" =' + "'" + str(sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed."servicios_id" = sub."serviciosSedes_id" AND ser.nombre in ( ' + "'" + str('HOSPITALIZACION') + "','" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)


    CambioServicio['SubServicios'] = subServicios

    # Fin combo SubServicios


    # Combo Habitaciones

    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()

    comando = 'SELECT dep.id ,dep.nombre FROM sitios_dependencias dep, sitios_dependenciasTipo tip , sitios_serviciosSedes sd, clinico_servicios ser where dep."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND tip.nombre=' + "'" + str('HABITACIONES') + "'" + ' and dep."dependenciasTipo_id" = tip.id AND dep.disponibilidad = ' + "'" + str('L') + "'" + ' AND sd.id=dep."serviciosSedes_id" AND ser.id = sd."servicios_id" and ser.nombre in (' + "'" + str('HOSPITALIZACION') + "'," + "'" + str('URGENCIAS') + "')"
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    CambioServicio['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    CambioServicio['Mensaje'] = 'Cambio de servicio realizado'

    servicioActualId = ServiciosSedes.objects.get(id=servicioFin)
    subServicioActualId = SubServiciosSedes.objects.get(id=subServicioFin)
    dependenciaActualId = Dependencias.objects.get(id=dependenciaFin)

    ## OJO NO CONFUNDIR ESTE PEDAZO DE CODIGO DE ABAJO CON LO DE ARRIBA SE SOBREESCRIBE
	
    CambioServicio['ServicioActual'] = servicioActualId.nombre
    CambioServicio['SubServicioActual'] = subServicioActualId.nombre
    CambioServicio['DependenciaActual'] = dependenciaActualId.nombre
    CambioServicio['FechaOcupacion'] = fechaOcupacion

    return JsonResponse(CambioServicio, safe=False)
	

def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime):
        return obj.isoformat() 
    raise TypeError("Type not serializable") 


def serialize_datetime1(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Type not serializable")



# Create your views here.
def load_dataConvenioAdmisiones(request, data):
    print ("Entre  load_dataConvenioAdmisiones")

    context = {}
    d = json.loads(data)

    ingresoId = d['ingresoId']
    sede = d['sede']

    print ("sede:", sede)
    print ("ingresoId:", ingresoId)

   

    #print("data = ", request.GET('data'))

    conveniosPacienteIngresos = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   
    detalle = 'SELECT conv.id id,i."tipoDoc_id" tipoDocId , i.documento_id documentoId ,u.documento documento,u.nombre nombre,i.consec consec , contra.nombre convenio, tipdoc.nombre nombreDocumento FROM admisiones_ingresos i, usuarios_usuarios u, facturacion_conveniosPacienteIngresos conv , contratacion_convenios contra , usuarios_tiposdocumento tipdoc WHERE i.id = ' + "'" + str(ingresoId) + "'" + ' and i.documento_id = u.id and i."tipoDoc_id" = conv."tipoDoc_id" and i.documento_id  = conv.documento_id and i.consec = conv."consecAdmision" and contra.id = conv.convenio_id AND tipdoc.id = i."tipoDoc_id"'

    print(detalle)

    curx.execute(detalle)

    for  id, tipoDocId, documentoId, documento, nombre, consec, convenio, nombreDocumento in curx.fetchall():
        conveniosPacienteIngresos.append(
		{"model":"conveniosPacienteIngresos.conveniosPacienteIngresos","pk":id,"fields":
			{'id':id, 'tipoDocId': tipoDocId, 'documentoId': documentoId, 'documento':documento , 'nombre': nombre, 'consec': consec, 'convenio':convenio, 'nombreDocumento':nombreDocumento}})

    miConexionx.close()
    print(conveniosPacienteIngresos )
    context['ConveniosPacienteIngresos '] = conveniosPacienteIngresos

    serialized1 = json.dumps(conveniosPacienteIngresos , default=serialize_datetime)

    print ("Envio = ", serialized1 )

    return HttpResponse(serialized1, content_type='application/json')


def load_dataAbonosAdmisiones(request, data):
    print("Entre  load_dataAbonosAdmisiones")

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

    detalle = 'SELECT pag.id id , i."tipoDoc_id" tipoDoc , i.documento_id documentoId ,u.documento documento,u.nombre nombre,i.consec consec , tipdoc.nombre nombreDocumento , cast(date(pag.fecha) as text)  fecha, pag."tipoPago_id" tipoPago , pag."formaPago_id" formaPago, pag.valor valor, pag.descripcion descripcion FROM admisiones_ingresos i, cartera_pagos pag ,usuarios_usuarios u ,usuarios_tiposdocumento tipdoc, cartera_tiposPagos tip, cartera_formasPagos forma WHERE i.id = ' + "'" + str(ingresoId) + "'" + ' and i.documento_id = u.id and i."tipoDoc_id" = pag."tipoDoc_id" and i.documento_id  = pag.documento_id and  i.consec = pag.consec AND tipdoc.id = i."tipoDoc_id" and pag."tipoPago_id" = tip.id and pag."formaPago_id" = forma.id'
    print(detalle)

    curx.execute(detalle)

    for id, tipoDoc, documentoId, documento, nombre, consec, nombreDocumento , fecha, tipoPago, formaPago, valor, descripcion  in curx.fetchall():
        abonos.append(
            {"model": "cartera_pagos.cartera_pagos", "pk": id, "fields":
                {'id': id, 'tipoDoc': tipoDoc, 'documentoId': documentoId, 'nombre':nombre,'consec':consec,  'nombreDocumento': nombreDocumento,
                 'fecha': fecha, 'tipoPago': tipoPago, 'formaPago': formaPago, 'valor':valor, 'descripcion':descripcion}})

    miConexionx.close()
    print(abonos)
    context['Abonos '] = abonos

    serialized2 = json.dumps(abonos,  default=decimal_serializer)


    print("Envio = ", serialized2)

    return HttpResponse(serialized2, content_type='application/json')



def GuardaConvenioAdmision(request):

    print ("Entre GuardaConvenioAdmision" )

    ingresoId = request.POST["ingresoId2"]
    sede = request.POST["sede2"]
    convenio = request.POST["convenio"]
    print ("ingresoId = ", ingresoId)
    print("sede = ", sede)

    fechaRegistro = datetime.datetime.now()

    registroId = Ingresos.objects.get(id=ingresoId)
    print  ("registroId documento =" , registroId.documento_id)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'insert into facturacion_ConveniosPacienteIngresos ("consecAdmision", "fechaRegistro",  convenio_id, documento_id, "tipoDoc_id" , "usuarioRegistro_id" ,"estadoReg") values (' + "'" + str(registroId.consec) + "'" + ' , ' + "'" + str(fechaRegistro) + "'" + ', ' + "'" + str(convenio) + "'" + '  , ' + "'" + str(registroId.documento_id) + "'" + ', ' + "'" + str(registroId.tipoDoc_id) + "',"  + "'" + str("1") + "'," + "'" +  str("A") + "');"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    #return HttpResponse("Convenio Adicionado", content_type='application/json')

    return JsonResponse({'success': True, 'message': 'Convenio Actualizado satisfactoriamente!'})



def GuardaAbonosAdmision(request):

    print ("Entre GuardaAbonosAdmision" )

    ingresoId = request.POST["ingresoId22"]
    sede = request.POST["sede22"]
    tipoPago = request.POST["tipoPago"]
    formaPago = request.POST["formaPago"]
    valor = request.POST['valorAbono']
    descripcion = request.POST['descripcionAbono']
    print ("ingresoId = ", ingresoId)
    print("sede = ", sede)

    fechaRegistro = datetime.datetime.now()

    registroId = Ingresos.objects.get(id=ingresoId)
    print  ("registroId documento =" , registroId.documento_id)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'insert into cartera_Pagos ("fecha", "tipoDoc_id" , documento_id, consec,  "tipoPago_id" , "formaPago_id", valor, descripcion ,"fechaRegistro","estadoReg") values ('  + "'" + str(fechaRegistro) + "'," +  "'" + str(registroId.tipoDoc_id) + "'" + ' , ' + "'" + str(registroId.documento_id) + "'" + ', ' + "'" + str(registroId.consec) + "'" + '  , ' + "'" + str(tipoPago) + "'" + '  , ' + "'" + str(formaPago) + "'" + ', ' + "'" + str(valor) + "',"   + "'" + str(descripcion) + "','"   + str(fechaRegistro) + "'," + "'" +  str("A") + "');"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    #return HttpResponse("Convenio Adicionado", content_type='application/json')

    return JsonResponse({'success': True, 'message': 'Abono Actualizado satisfactoriamente!'})





def PostDeleteConveniosAdmision(request):

    print ("Entre PostDeleteConveniosAdmision" )
    print ("PostDeleteConveniosAdmision" )

    id = request.POST["id"]
    print ("el id es = ", id)


    post = ConveniosPacienteIngresos.objects.get(id=id)
    post.delete()
    #return HttpResponseRedirect(reverse('index'))
    return JsonResponse({'success': True, 'message': 'Convenio borrado!'})


def PostDeleteAbonosAdmision(request):

    print ("Entre PostDeleteAbonosAdmision" )

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


def GuardarResponsableAdmision(request):

    print ("Entre GuardaConvenioAdmision" )

    ingresoId = request.POST["ingresoId"]
    responsable = request.POST["responsable"]
    print ("ingresoId = ", ingresoId)
    print("responsable  = ", responsable )

    registroId = Ingresos.objects.get(id=ingresoId)
    print  ("registroId documento =" , registroId.documento_id)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'UPDATE admisiones_ingresos set "contactoResponsable_id" = ' + "'" + str(responsable) + "' WHERE id = " + "'" + str(ingresoId) +"'"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Responsable Actualizado satisfactoriamente!'})

def GuardarAcompananteAdmision(request):

    print ("Entre GuardaAcompananteAdmision" )

    ingresoId = request.POST["ingresoId"]
    acompanante = request.POST["acompanante"]
    print ("ingresoId = ", ingresoId)
    print("acompanante  = ", acompanante )

    registroId = Ingresos.objects.get(id=ingresoId)
    print  ("registroId documento =" , registroId.documento_id)

    ## falta usuarioRegistro_id
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'UPDATE admisiones_ingresos set "contactoAcompañante_id" = ' + "'" + str(acompanante) + "' WHERE id = " + "'" + str(ingresoId) +"'"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Responsable Actualizado satisfactoriamente!'})


def GuardaFurips(request):

    print ("Entre GuardaFurips" )

    ingresoId = request.POST["ingresoId"]
    sede = request.POST["sede"]
    print ("ingresoId = ", ingresoId)
    print("sede = ", sede)
    fechaRegistro = datetime.datetime.now()
    registroId = Ingresos.objects.get(id=ingresoId)
    print  ("registroId documento =" , registroId.documento_id)

    primerApellidoVictima = request.POST["primerApellidoVictima"]
    print("primerApellidoVictima = ", primerApellidoVictima)


    numeroRadicacion = request.POST["numeroRadicacion"]
    print ("numeroRadicacion = ", numeroRadicacion)
    fechaRadicado = request.POST["fechaRadicado"]
    print ("fechaRadicado = ", fechaRadicado)
    numeroFactura = request.POST["numeroFactura"]
    print ("numeroFactura = ", numeroFactura)
    primerNombreVictima = request.POST["primerNombreVictima"]
    print ("primerNombreVictima = ", primerNombreVictima)



    
    miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",  password="pass123")
    cur3 = miConexion3.cursor()
    comando = 'insert into admisiones_furips (documento_id,  "tipoDoc_id" , consec , "numeroRadicacion", "fechaRadicado" , "primerNombreVictima", "primerApellidoVictima" , "fechaRegistro" ,"estadoReg") values (' + "'" + str(registroId.documento_id) + "',"   + "'" + str(registroId.tipoDoc_id) + "'," +  "'" + str(registroId.consec) + "'" + ' , ' + "'" + str(numeroRadicacion) + "'" + '  , ' + "'" + str(fechaRadicado) + "'" + ', ' + "'" + str(primerNombreVictima) + "',"   + "'" + str(primerApellidoVictima) + "','"   + str(fechaRegistro) + "'," + "'" +  str("A") + "');"
    print(comando)
    cur3.execute(comando)
    miConexion3.commit()
    miConexion3.close()

    return JsonResponse({'success': True, 'message': 'Furips Actualizado satisfactoriamente!'})

