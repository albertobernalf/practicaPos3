from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
import psycopg2

import pytz
import tzlocal
import datetime as dt

from sitios.models import  HistorialDependencias, Dependencias
from usuarios.models import Usuarios, TiposDocumento
from planta.models import Planta
from triage.models import Triage



# Create your views here.


def crearTriage(request):

    print("Entre a Crear TRIAGE")

    if request.method == 'POST':
        print("EntrePost Graba Crea TRIAGE ")
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

        Profesional = request.POST["Profesional"]
        print(" Profesional = " , Profesional)
        context['Profesional'] = Profesional

        Username_id = request.POST["Username_id"]
        print("Username_id = ", Username_id)
        context['Username_id'] = Username_id

        busServicioT = request.POST["busServicioT"]
        print(" busServicioT = ", busServicioT)
        context['BusServicioT'] = busServicioT

        busSubServicioT= request.POST["busSubServicioT"]
        print(" busSubServicioT = ", busSubServicioT)
        context['BusSubServicioT'] = busSubServicioT

        dependencias= request.POST["dependenciasT"]
        print(" dependencias= ", dependencias)
        context['Dependencias'] = dependencias


        tipoDoc = request.POST['tipoDocTriage']
       # documento = request.POST['documento']
        documento = request.POST['busDocumentoSelTriage']
        print("tipoDoc = ", tipoDoc)
        print("documento = ", documento)

        # Consigo el Id del Paciente Documento

        DocumentoId = Usuarios.objects.get(documento=documento)
        idPacienteFinal = DocumentoId.id

        print("idPacienteFinal", idPacienteFinal)

       #consec = request.POST['consec']
       # print("consec Ingreso = ", consec)
        motivo= request.POST['motivo']
        print("motivo = ", motivo)
        examenFisico= request.POST['examenFisico']
        print("examenFisico = ", examenFisico)
        frecCardiaca= request.POST['frecCardiaca']
        print("frecCardiaca= ", frecCardiaca)
        frecRespiratoria= request.POST['frecRespiratoria']
        print("frecRespiratoria= ", frecRespiratoria)
        taSist= request.POST['taSist']
        print("taSist= ", taSist)
        taDiast= request.POST['taDiast']
        print("taDiast= ", taDiast)
        taMedia= request.POST['taMedia']
        print("taMedia= ", taMedia)
        glasgow= request.POST['glasgow']
        print("glasgow= ", glasgow)
        peso= request.POST['peso']
        print("peso= ", peso)
        temperatura= request.POST['temperatura']
        print("temperatura= ", temperatura)
        estatura= request.POST['estatura']
        print("estatura= ", estatura)
        glucometria= request.POST['glucometria']
        print("glucometria= ", glucometria)
        saturacion= request.POST['saturacion']
        print("saturacion= ", saturacion)
        escalaDolor= request.POST['escalaDolor']
        print("escalaDolor= ", escalaDolor)

        tipoIngreso= request.POST['tipoIngreso']
        print("tipoIngreso= ", escalaDolor)
        observaciones= request.POST['observaciones']
        print("observaciones= ", observaciones)
        clasificacionTriage= request.POST['clasificacionTriage']
        print("clasificacionTriage= ", clasificacionTriage)


        #fechaRegistro = request.POST['fechaIngreso']
        fechaRegistro = dt.datetime.now()
        print("fechaRegistro  = ", fechaRegistro )

        usuarioRegistro = Username_id

        print("usuarioRegistro =", usuarioRegistro)
        estadoReg = "A"
        print("estadoRegistro =", estadoReg)

        # VAmos a guardar el Traige

        # Consigo ID de Documento

        documento_llave = Usuarios.objects.get(documento=documento)
        print("el id del documento = ", documento_llave.id)

        usernameId = Planta.objects.get(documento=username)
        print("el id del planta = ", usernameId.id)


        grabo = Triage(
                         sedesClinica_id=Sede,
                         tipoDoc_id=tipoDoc,
                         documento_id=documento_llave.id,
                         consec=0,
                         fechaSolicita=fechaRegistro,
                         serviciosSedes_id=  busServicioT,
                         subServiciosSedes_id=busSubServicioT,
                         dependencias_id=dependencias,
                         motivo=motivo,
                         examenFisico=examenFisico,
                         frecCardiaca=frecCardiaca,
                         frecRespiratoria=frecRespiratoria,
                         taSist=taSist,
                         taDiast=taDiast,
                         taMedia=taMedia,
                         glasgow=glasgow,
                         peso=peso,
                         temperatura=temperatura,
                         estatura=estatura,
                         glucometria=glucometria,
                         saturacion=saturacion,
                         escalaDolor=escalaDolor,
                         tipoIngreso=tipoIngreso,
                         observaciones=observaciones,
                         clasificacionTriage_id=clasificacionTriage,
                         fechaRegistro=fechaRegistro,
                         usuarioCrea_id=usernameId.id,
                         #estadoReg=estadoReg,

        )
        print("Voy a guardar la INFO")

        grabo.save()
        print("yA grabe 2", grabo.id)
        grabo.id
        print("yA grabe" , grabo.id)

        # RUTINA ARMADO CONTEXT

        triage1 = []

        # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curx = miConexionx.cursor()

        comando = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , t.consec consec , dep.nombre camaNombre,t."fechaSolicita" solicita,t.motivo motivo, t."clasificacionTriage_id" triage FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" =' + "'" + str(
            Sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and  u.id = t."documento_id"'
        print(comando)

        curx.execute(comando)

        for tipoDoc, documento, nombre, consec, camaNombre, solicita, motivo, triage in curx.fetchall():
            triage1.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                           'camaNombre': camaNombre, 'solicita': solicita, 'motivo': motivo, 'triage': triage})

        miConexionx.close()
        print(triage1)

        context['Triage'] = triage1

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

        # aqui la manada de combos organizarlo segun necesidades


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
                {'id': id, 'nombre': nombre, 'nomenclatura': nomenclatura, 'logo': logo, 'nombreOpcion': nombreOpcion,'nombreElemento': nombreElemento})

        miConexiont.close()
        print(permisosDetalle)

        context['PermisosDetalle'] = permisosDetalle

        # Fin Combo PermisosDetalle


        # FIN RUTINA ARMADO CONTEXT

    print(triage1)

    return render(request, "triage/panelTriage.html", context)



def buscarTriage(request):
    context = {}

    ## ULTIMOS AJUSTES

    print("Entre Buscar Triage" )
    BusTipoDoc = request.POST["busTipoDoc"]
    BusDocumento = request.POST["busDocumento"]
    BusHabitacion = request.POST["busHabitacion"]
    BusDesde = request.POST["busDesde"]
    BusHasta = request.POST["busHasta"]
    BusServicio = request.POST["busServicio"]
    BusSubServicio = request.POST["busSubServicio"]
    BusPaciente = request.POST["busPaciente"]
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

    ## Combos para Contexto



    # aqui la manada de combos organizarlo segun necesidades

    # Combo de Servicios
    # miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    curt = miConexiont.cursor()
    comando = 'SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed."sedesClinica_id" =' + "'" + str(
        sede) + "'" + ' AND sed."servicios_id" = ser.id and ser.nombre=' + "'" + str('TRIAGE') + "'"
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
        sede) + "'" + ' AND sed."servicios_id" = ser.id and  sed."sedesClinica_id" = sub."sedesClinica_id" and sed.id = sub."serviciosSedes_id" and sed.servicios_id = ser.id and sub."serviciosSedes_id" = sed.id  and ser.nombre = ' +  "'" + str('TRIAGE') + "'"
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

    triage1 = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                   password="pass123")
    cur1 = miConexionx.cursor()

    detalle = 'SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , t.consec consec , dep.nombre camaNombre,t."fechaSolicita" solicita,t.motivo motivo, t."clasificacionTriage_id" triage FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd ,sitios_subServiciosSedes sub  WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" =' + "'" + str(Sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and  u.id = t."documento_id"  and sd.id = sub."serviciosSedes_id"     '
    print(detalle)

    if BusServicio != "":
      detalle = detalle + " AND  sd.id = '" + str(BusServicio) + "'"
    print(detalle)

    if BusSubServicio != "":
      detalle = detalle + " AND  sub.id = '" + str(BusSubServicio) + "'"
    print(detalle)


    if BusDesde != "":
        detalle = detalle +  ' AND t."fechaSolicita" >= ' + "'" + str(desdeFecha) +   " " + str(desdeTiempo)  + ":00" + "'"
        print (detalle)

    if BusHasta != "":
        detalle = detalle + ' AND t."fechaSolicita" <=  ' + "'"  + str(hastaFecha) +  " " + str(hastaTiempo) + ":00" +"'"
        print(detalle)

    if BusHabitacion != "":
        detalle = detalle + " AND dep.id = '" + str(BusHabitacion) + "'"
        print(detalle)

    if BusTipoDoc != "":
        detalle = detalle + ' AND t."tipoDoc_id"= ' + "'" +  str(BusTipoDoc) + "'"
        print(detalle)

    if BusDocumento != "":
        detalle = detalle + " AND u.documento= '" + str(BusDocumento) + "'"
        print(detalle)

    if BusPaciente != "":
        detalle = detalle + " AND u.nombre like '%" + str(BusPaciente) + "%'"
        print(detalle)

    cur1.execute(detalle)

    for tipoDoc, documento, nombre, consec, camaNombre, solicita, motivo, triage in cur1.fetchall():
        triage1.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                       'camaNombre': camaNombre, 'solicita': solicita,
                       'motivo': motivo, 'triage': triage})


    miConexionx.close()
    print(triage1)

    context['Triage'] = triage1

    return render(request, "triage/panelTriage.html", context)


def buscarSubServiciosTriage(request):
    context = {}
    Serv = request.GET["Serv"]
    Sede = request.GET["Sede"]
    print ("Entre buscar  Subservicios del servicio  =",Serv)
    print ("Sede = ", Sede)

    # Combo de SubServicios
    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont =psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()
    #comando = 'SELECT sub.id id ,sub.nombre nombre FROM sitios_serviciosSedes sed ,sitios_subserviciossedes sub Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + '  and sed."sedesClinica_id" = sub."sedesClinica_id" and sed.id = sub."serviciosSedes_id" and sub."serviciosSedes_id" = ' + "'" + str(Serv) + "'"
    comando = 'SELECT sub.id id ,sub.nombre nombre FROM sitios_serviciosSedes sed ,sitios_subserviciossedes sub , clinico_servicios serv Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' and sed."sedesClinica_id" = sub."sedesClinica_id" and sed.id = sub."serviciosSedes_id"  and sub."serviciosSedes_id" = sed.id and sed.id= ' + "'" + str(Serv) + "'" + ' and sed.servicios_id=serv.id'
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



def buscarHabitacionesTriage(request):


    context = {}
    Exc = request.GET["Exc"]
    print ("Excluir = ", Exc)
    Serv = request.GET["Serv"]
    SubServ = request.GET["SubServ"]
    Sede = request.GET["Sede"]
    print ("Entre buscar  servicio =",Serv)
    print("Entre buscar Subservicio =", SubServ)
    print ("Sede = ", Sede)


    # Busco la habitaciones de un Servicio

    #miConexiont = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    curt = miConexiont.cursor()

    if Exc == 'N':

      comando = "SELECT dep.id id ,dep.numero nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub , sitios_dependencias dep  Where sed.sedesClinica_id ='" + str(
        Sede) + "' AND sed.servicios_id = ser.id and  sed.sedesClinica_id = sub.sedesClinica_id and sed.servicios_id =sub.servicios_id and  dep.sedesClinica_id=sed.sedesClinica_id and dep.servicios_id = sub.servicios_id and dep.subServicios_id =sub.id  and dep.subServicios_id = '" +str(SubServ) + "'"

    else:


       comando = 'SELECT dep.id id ,dep.numero nombre   FROM sitios_serviciosSedes sed,  sitios_subserviciossedes sub , sitios_dependencias dep Where sed."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND sed."sedesClinica_id" = sub."sedesClinica_id" and sub."serviciosSedes_id" = sed.id and dep."sedesClinica_id"=sed."sedesClinica_id" and dep."serviciosSedes_id"= sed.id and dep."subServiciosSedes_id" = sub.id and dep."subServiciosSedes_id" = ' + "'" + str(SubServ) + "'"

    curt.execute(comando)
    print(comando)

    habitaciones =[]


    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)
    context['Habitaciones'] = habitaciones

    context['Sede'] = Sede



    return JsonResponse(json.dumps(habitaciones), safe=False)

#def encuentraTriageModal(request, tipoDoc, documento, sede):
def encuentraTriageModal(request):

        print("Entre a buscar una Triage Modal")
        Sede = request.POST["sede"]
        tipoDoc = request.POST["tipoDoc"]
        documento = request.POST["documento"]

        print("documento = ", documento)
        print("tipodoc = ", tipoDoc)
        print("Sede = ", Sede)
        consec = 0;
        tipoDoc1 = TiposDocumento.objects.get(nombre=tipoDoc)
        print("tipodoc1 = ", tipoDoc1.id)
        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        #comando = 'SELECT tp.nombre tipoDoc,  u.documento documento, u.nombre  paciente , ser.nombre servicioNombreIng, dep.nombre dependenciasIngreso , t.motivo,t."examenFisico",t."frecCardiaca",t."frecRespiratoria",t."taSist",t."taDiast",t."taMedia",t.glasgow,t.peso,t.temperatura,t.estatura,t.glucometria,t."escalaDolor",t."tipoIngreso",t.observaciones FROM triage_triage t inner join usuarios_usuarios u on (u."tipoDoc_id" = t."tipoDoc_id" and u.id = t."documento_id" ) inner join sitios_dependencias dep on (dep."sedesClinica_id" = t."sedesClinica_id" and dep."tipoDoc_id" =  t."tipoDoc_id" and dep.documento_id =t."documento_id"  and dep.consec = t.consec) inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on (deptip.id = dep."dependenciasTipo_id") inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = t."sedesClinica_id") inner join clinico_servicios ser  on (ser.id = sd.servicios_id  and ser.id = t."serviciosSedes_id" ) WHERE t."sedesClinica_id" = ' + "'" + str(
        #    Sede) + "'" + ' and u."tipoDoc_id" = ' + "'" + str(tipoDoc1.id) + "'" + ' and u.documento = ' + "'" + str(documento) + "'" + ' and t.consec= ' + "'" + str(consec) + "'"
        comando = 'SELECT sd.id servicioSedes, sub.id subServiciosSedes, dep.id dependencias, tp.nombre tipoDoc,  u.documento documento, u.nombre  paciente , dep.nombre dependenciasIngreso , t.motivo,t."examenFisico",t."frecCardiaca",t."frecRespiratoria",t."taSist",t."taDiast",t."taMedia",t.glasgow,t.peso,t.temperatura,t.estatura,t.glucometria,t."escalaDolor",t."tipoIngreso",t.observaciones, t.saturacion, t."clasificacionTriage_id"   clasificacionTriage FROM triage_triage t inner join usuarios_usuarios u on (u."tipoDoc_id" = t."tipoDoc_id" and u.id = t."documento_id" ) inner join sitios_dependencias dep on (dep."sedesClinica_id" = t."sedesClinica_id" and dep."tipoDoc_id" =  t."tipoDoc_id" and dep.documento_id =t."documento_id" ) inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on (deptip.id = dep."dependenciasTipo_id") inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = t."sedesClinica_id" and sd.id = dep."serviciosSedes_id" and sd.id = t."serviciosSedes_id" ) inner join sitios_subServiciosSedes sub on (sub."serviciosSedes_id" = sd.id and   sub."serviciosSedes_id"= dep."serviciosSedes_id"  and sub.id = t."subServiciosSedes_id" and sub."serviciosSedes_id" = dep."serviciosSedes_id"  and sub.id = dep."subServiciosSedes_id" ) inner join clinico_servicios ser  on (ser.id = sd.servicios_id   ) WHERE t."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' and u."tipoDoc_id" = ' + "'" + str(tipoDoc1.id) + "'" + ' and u.documento = ' + "'" + str(documento) + "'" + ' and t.consec = 0'


        print(comando)
        curt.execute(comando)

        Triage = {}

        for servicioSedes, subServiciosSedes,  dependencias, tipoDoc, documento, paciente,  dependenciasIngreso,  motivo,examenFisico,frecCardiaca,frecRespiratoria, taSist,taDiast,taMedia,glasgow,peso,temperatura,estatura,glucometria,escalaDolor,tipoIngreso,observaciones, saturacion, clasificacionTriage in curt.fetchall():
            Triage = {'servicioSedes':servicioSedes,'subServiciosSedes':subServiciosSedes,'dependencias':dependencias,'tipoDoc': tipoDoc1.id, 'documento': documento,'paciente':paciente, 'dependenciasIngreso' : dependenciasIngreso, 'motivo':motivo , 'examenFisico':examenFisico,'frecCardiaca':frecCardiaca,'frecRespiratoria':frecRespiratoria,
                       'taSist':taSist, 'taDiast':taDiast, 'taMedia':taMedia,'glasgow':glasgow,'peso':peso,'temperatura':temperatura ,'estatura':estatura,'glucometria':glucometria,'escalaDolor':escalaDolor,'tipoIngreso':tipoIngreso,'observaciones':observaciones,'saturacion':saturacion, 'clasificacionTriage':clasificacionTriage}


        miConexiont.close()
        print(Triage)


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


        # Fin combo TiposTriage



        response_data = {}
        response_data['Triage'] = Triage
        response_data['TiposTriage'] = tiposTriage


        if Triage == '[]':
            datos = {'Mensaje': 'Triage No existe'}
            return JsonResponse(datos, safe=False)

        else:
            datos = {'Mensaje': 'Triage SIII existe'}
            #return JsonResponse(Triage, safe=False)
            return JsonResponse(response_data, safe=False)


def UsuariosModalTriage(request):
        print("Entre a buscar Usuario para la Modal")

        tipoDoc = request.POST['tipoDoc']
        documento = request.POST['documento']
        print ("documento = " , documento)
        print("tipodoc = " ,tipoDoc)

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
        curt = miConexiont.cursor()
        comando = 'SELECT usu.nombre, usu.documento documento, usu.genero, usu."fechaNacio" fechaNacio,  usu.departamentos_id departamentos, usu.ciudades_id ciudades, usu.direccion direccion, usu.telefono telefono, usu.contacto contacto, usu."centrosC_id" centrosC, usu."tipoDoc_id" tipoDoc , usu."tiposUsuario_id" tiposUsuario, usu.municipio_id municipio, usu.localidad_id localidad, usu."estadoCivil_id" estadoCivil , usu.ocupacion_id ocupacion, correo correo  FROM usuarios_usuarios usu WHERE usu."tipoDoc_id" = ' + "'"  + str(tipoDoc) + "'" + ' AND usu.documento = ' + "'" + str(documento) + "'"
        print(comando)
        curt.execute(comando)

        Usuarios = {}

        for nombre, documento, genero, fechaNacio, departamentos, ciudades, direccion, telefono, contacto, centrosC, tipoDoc, tiposUsuario, municipio, localidad, estadoCivil, ocupacion, correo  in curt.fetchall():
            Usuarios = {'nombre': nombre, 'documento': documento, 'genero': genero, 'fechaNacio': fechaNacio , 'departamentos' : departamentos, 'ciudades': ciudades,  'direccion':  direccion, 'telefono' :telefono, 'contacto': contacto, 'centrosC':centrosC, 'tipoDoc':tipoDoc,'tiposUsuario':tiposUsuario,
                        'municipio':municipio, 'localidad':localidad, 'estadoCivil':estadoCivil, 'ocupacion':ocupacion,'correo':correo}

        miConexiont.close()
        print(Usuarios)

        if Usuarios == '[]':
            datos = {'Mensaje' : 'Usuario No existe'}
            return JsonResponse(datos, safe=False)
        else:
            return JsonResponse(Usuarios, safe=False)

def grabaUsuariosTriage(request):
    print("Entre a grabar Usuarios Modal")
    tipoDoc = request.POST["tipoDoc"]
    documento = request.POST["documento"]
    nombre = request.POST["nombre"]
    print("DOCUMENTO = " ,documento)
    print(nombre)
    genero = request.POST["genero"]
    departamentos = request.POST["departamentos"]
    ciudades = request.POST["ciudades"]
    fechaNacio = request.POST["fechaNacio"]
    print("fechaNacio = ", fechaNacio)
    print ("departamentos = ", departamentos)
    print("ciudad = ", ciudades)
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    contacto = request.POST["contacto"]
    centrosC = request.POST["centrosC"]
    #quemado por el momento mientras encuentor que pasa
    #centrosc_id = 1
    tiposUsuario = request.POST["tiposUsuario"]
    print("DIRECCION = ", direccion)
    print("telefono = ", telefono)
    print("contacto = ", contacto)
    #municipios  = request.POST['municipios']
    #localidad  = request.POST['localidades']
    #estadoCivil  = request.POST['estadoCivil']
    #ocupaciones = request.POST['ocupaciones']
    #correo = request.POST["correo"]
    print("centrosC = ", centrosC)
    municipios  = 0
    localidades  = 0
    estadoCivil  = 0
    ocupaciones = 0
    correo = '0'


    print(documento)
    print(tipoDoc)

    #miConexion11 =  MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexion11 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
    cur11 = miConexion11.cursor()
    comando = 'SELECT usu.id, usu."tipoDoc_id" tipoDoc, usu.documento FROM usuarios_usuarios usu WHERE usu."tipoDoc_id" = ' + "'" + str(tipoDoc) + "'" + ' AND usu.documento = ' + "'" + str(documento) + "'"

    print(comando)
    cur11.execute(comando)

    Usuarios = []

    for id, tipoDoc, documento in cur11.fetchall():
        Usuarios.append({'id': id, 'tipoDoc': tipoDoc, 'documento': documento})

    miConexion11.close()

    fechaRegistro = dt.datetime.now()


    if Usuarios == []:

         print("Entre a crear")
         #miConexion3 = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
         miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
         cur3 = miConexion3.cursor()
         #comando = 'insert into usuarios_usuarios (nombre, documento, genero, "fechaNacio",  departamentos_id, ciudades_id, direccion, telefono, contacto, "centrosC_id", "tipoDoc_id", "tiposUsuario_id", municipio_id, localidad_id, "estadoCivil_id", ocupacion_id, correo ,"fechaRegistro", "estadoReg") values (' + "'" + str(nombre) + "'" + ' , ' + "'" + str(documento) + "'" + ', ' + "'" + str(genero) + "'" + '  , ' + "'" + str(fechaNacio) + "'" +  ', '  + "'" + str(departamentos) + "'" +  '  , ' + "'" +  str(ciudades) + "'" + '  , ' + "'" +  str(direccion) + "'" + ', ' + "'" + str(telefono) + "'" + ', ' + "'" + str(contacto) + "'" + ', ' + "'" + str(centrosC) + "'" +  ', ' + "'" + str(tipoDoc) + "'" + ', ' + "'" + str(tiposUsuario) + "' , " + "'" + str(municipios) + "'" +   ', ' + "'" + str(localidades) + "'" + ", " + "'" + str(estadoCivil) + "'" + ", " + "'" + str(ocupaciones) + "'" + ", " + "'" + str(correo) + "', " +  "'"  + str(fechaRegistro) + "'"  +  ", 'A'"  +      ')'
         comando = 'insert into usuarios_usuarios (nombre, documento, genero, "fechaNacio",  departamentos_id, ciudades_id, direccion, telefono, contacto, "centrosC_id", "tipoDoc_id", "tiposUsuario_id", "fechaRegistro", "estadoReg") values (' + "'" + str(nombre) + "'" + ' , ' + "'" + str(documento) + "'" + ', ' + "'" + str(genero) + "'" + '  , ' + "'" + str(fechaNacio) + "'" + ', ' + "'" + str(departamentos) + "'" + '  , ' + "'" + str(ciudades) + "'" + '  , ' + "'" + str(direccion) + "'" + ', ' + "'" + str(telefono) + "'" + ', ' + "'" + str(contacto) + "'" + ', ' + "'" + str(centrosC) + "'" + ', ' + "'" + str(tipoDoc) + "'" + ', ' + "'" + str(tiposUsuario) + "' , '" + str(fechaRegistro) + "'" + ", 'A'" + ')'

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
        comando = 'update usuarios_usuarios set nombre = ' "'" + str(nombre) +  "'" +  ', direccion  = ' + "'" +  str(direccion) + "'" + ', genero = ' + "'" + str(genero) + "'"  + ', "fechaNacio" = ' + "'" + str(fechaNacio) + "'"   + ', telefono= ' + "'" + str(telefono) + "'" +  ', contacto= ' + "'" +  str(contacto) + "'" +  ', "centrosC_id"= ' + "'" + str(centrosC) + "'" + ', "tiposUsuario_id" = ' + "'" + str(tiposUsuario) + "' , "   + ' municipio_id = ' + "'" + str(municipios) + "'" +  ', localidad_id = ' + "'" + str(localidades) + "'" + ', "estadoCivil_id"= ' + "'" + str(estadoCivil) + "'" + ', ocupacion_id = ' + "'" + str(ocupaciones) + "'"  + ', correo = ' + "'" + str(correo) + "'"  + ' WHERE "tipoDoc_id" = ' + str(tipoDoc) + ' AND documento = ' + "'" + str(documento) + "'"

        print(comando)
        cur3.execute(comando)
        miConexion3.commit()


        miConexion3.close()
        return HttpResponse("Usuario Actualizado ! ")

def grabaTriageModal(request):

        print("Entre a guardaTriageModal")



        #y = json.loads(envios2)

        estatura = request.POST["estatura"]
        peso = request.POST["peso"]
        documento = request.POST["documento"]
        print("estatura = ", estatura)
        print ("peso = " , peso)
        print("documento= ", documento)
        busServicioT = request.POST["busServicioT"]
        busSubServicioT = request.POST["busSubServicioT"]
        dependenciasP = request.POST["dependenciasP"]
        tipoDoc = request.POST["tipoDoc"]
        documento = request.POST["documento"]
        motivo = request.POST["motivo"]
        examenFisico = request.POST["examenFisico"]
        frecCardiaca = request.POST["frecCardiaca"]
        frecRespiratoria = request.POST["frecRespiratoria"]
        taSist = request.POST["taSist"]
        taDiast = request.POST["taDiast"]
        taMedia = request.POST["taMedia"]
        glasgow = request.POST["glasgow"]
        peso = request.POST["peso"]
        temperatura = request.POST["temperatura"]
        glucometria = request.POST["glucometria"]
        escalaDolor = request.POST["escalaDolor"]
        tipoIngreso = request.POST["tipoIngreso"]
        observaciones = request.POST["observaciones"]
        #clasificacionTriage = request.POST["clasificacionTriage"]
        # OJOO QUEMADO POR EL MOMENTo


        documento_llave = Usuarios.objects.get(documento=documento)
        print("el id del documento = ", documento_llave.id)

        print("Entre a actualizar")
        # miConexion3 =  MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
        miConexion3 = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        cur3 = miConexion3.cursor()
        comando = 'update triage_triage set  "serviciosSedes_id" = ' + "'" + str(busServicioT) + "'," + ' "subServiciosSedes_id" = ' + "'" + str(busSubServicioT) + "',"  + ' dependencias_id= ' + "'" +  str(dependenciasP) + "'," +  ' "tipoDoc_id" = ' "'" + str(tipoDoc) + "'" + ', documento_id  = ' + "'" + str(documento_llave.id) + "'" + ', motivo = ' + "'" + str(motivo) + "'" + ', "examenFisico" = ' + "'" + str(examenFisico) + "'" + ', "frecCardiaca"= ' + "'" + str(frecCardiaca) + "'" + ', "frecRespiratoria"= ' + "'" + str(frecRespiratoria) + "'" + ', "taSist"= ' + "'" + str(taSist) + "'" + ', "taDiast" = ' + "'" + str(taDiast) + "' , " + ' "taMedia" = ' + "'" + str(taMedia) + "'" + ', glasgow = ' + "'" + str(glasgow) + "'" + ', "peso"= ' + "'" + str(peso) + "'" + ', temperatura = ' + "'" + str(temperatura) + "'" + ', glucometria = ' + "'" + str(glucometria) + "'" ', "tipoIngreso"= ' + "'" + str(tipoIngreso) + "'" + ', observaciones = ' + "'" + str(observaciones) + "'"  + ' WHERE "tipoDoc_id" = ' + str(tipoDoc) + ' AND documento_id = ' + "'" + str(documento_llave.id) + "';"

        print(comando)
        cur3.execute(comando)
        miConexion3.commit()

        miConexion3.close()
        print("De regreso")
        return JsonResponse("Triage Actualizado ! ", safe=False)

        #return HttpResponse("Triage Actualizado ! ")

