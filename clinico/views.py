import json
from django import forms
import cv2
import numpy as np
# import onnx as onnx
# import onnxruntime as ort
import pyttsx3
import speech_recognition as sr
from django.core.serializers import serialize
from django.db.models.functions import Cast, Coalesce
from django.utils.timezone import now
from django.db.models import Avg, Max, Min
from .forms import historiaForm, historiaExamenesForm
from datetime import datetime
from clinico.models import Historia, HistoriaExamenes, Examenes, TiposExamen, EspecialidadesMedicos, Medicos, Especialidades, TiposFolio, CausasExterna, EstadoExamenes
from sitios.models import Dependencias
from planta.models import Planta
from contratacion.models import Procedimientos
from usuarios.models import Usuarios



from clinico.forms import  IncapacidadesForm, HistorialDiagnosticosCabezoteForm
from django.db.models import Avg, Max, Min
from usuarios.models import Usuarios, TiposDocumento

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

def prueba(request):
    return render(request, "index.html")


def resMotivoInvidente(request):
    print("Entre a Reconocer audio Motivo Consulta")
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())

    with sr.Microphone(device_index=0) as source:  # use the default microphone as the audio source
        print("Por Favor cuenteme :")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  # listen for the first phrase and extract it into audio data
        print("pase")
    try:
        print("No haga nada")
        # print("You said " + r.recognize_google(audio , language = 'en-IN', show_all = True))  # recognize speech using Google Speech Recognition
        # text = r.recognize_google(audio, language = 'es-CO', show_all = True )
        text = r.recognize_google(audio, language='es-CO', show_all=True)
        #  jsonToPython = json.loads(format(text))
        print('You said: {}'.format(text))


    except LookupError:  # speech is unintelligible
        print("Could not understand audio")

    # return render(request, "home.html")

    datos = {"Respuesta": format(text)}
    print(datos)

    return HttpResponse(json.dumps(datos))


def motivoInvidente(request):
    print("Entre al Moivo invidente Audio")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    return redirect('/menu/')



def motivoSeñas(request):
    print("Entre Reproduce SeÃ±as")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    texto = step_5_camera()
    print("De devuelta el texto es : ")
    print(texto)

    #  texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    datos = {"mensaje": texto}
    print(datos)

    return HttpResponse(json.dumps(datos))

    return redirect('/menu/')


def subjetivoSeñas(request):
    print("Entre Reproduce SubjetivoSeñas")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    texto = step_5_camera()
    print("De devuelta el texto es : ")
    print(texto)

    #  texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    datos = {"mensaje": texto}
    print(datos)

    return HttpResponse(json.dumps(datos))

    return redirect('/menu/')


def step_5_camera():
    print("Entree a Camara")
    onnx_file = 'C:\\EntornosPython\\vulne\\vulnerable\\signlanguage.onnx'
    onnx_model = onnx.load(onnx_file)
    onnx.checker.check_model(onnx_model)
    print('The model is checked!')

    # constants
    index_to_letter = list('ABCDEFGHIKLMNOPQRSTUVWXY')
    mean = 0.485 * 255.
    std = 0.229 * 255.
    print("Adentro1")
    # create runnable session with exported model
    ort_session = ort.InferenceSession(onnx_file)
    print("Adentro11")
    cap = cv2.VideoCapture(0)
    mensaje = []
    print("Adentro2")

    # while True:
    for t in range(15):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # preprocess data
        frame = center_crop(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        x = cv2.resize(frame, (28, 28))
        x = (x - mean) / std

        x = x.reshape(1, 1, 28, 28).astype(np.float32)
        y = ort_session.run(None, {'input': x})[0]

        index = np.argmax(y, axis=1)
        letter = index_to_letter[int(index)]

        mensaje.append(letter)
        print("las letras son: %s", mensaje)

        cv2.putText(frame, letter, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), thickness=2)
        cv2.imshow("Sign Language Translator", frame)
        print("Adentro3")
        #  if cv2.waitKey(1) & 0xFF == ord('q'):
        #  break

    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()

    print("El mensaje Final es : ")

    resultado = ''

    for x in range(0, len(mensaje)):
        resultado = resultado + mensaje[x]

    return (resultado)


def center_crop(frame):
    h, w, _ = frame.shape
    start = abs(h - w) // 2
    if h > w:
        return frame[start: start + w]
    return frame[:, start: start + h]


def crearHistoriaClinica(request):
    print("Entre crearHistoriaClinica")
    # form = historiaForm(request.POST)

    if request.method == 'POST':
        if request.is_ajax and request.method == "POST":


            print ("envio1 = " , envio2)

            print("Entre Ajax   por POST")
            envio1 = request.POST["envio2"]
            print ("envio1 = " , envio1)

            tipoDoc = request.POST["tipoDocPaciente"]
            print("tipoDoc = ", tipoDoc)
            documento = request.POST["documentoPaciente"]
            consecAdmision = request.POST["ingresoPaciente"]
            #folio = request.POST["folio"]
            #fecha = request.POST["fecha"]
            tiposFolio = request.POST["tiposFolio"]
            #tiposFolio = 1
            print (tiposFolio)
            causasExterna = request.POST["causasExterna"]
            #dependenciasRealizado = request.POST["dependenciasRealizado"]

            espMedico = request.POST["espMedico"]
            #diagnosticos = request.POST["diagnosticos"]

            #planta = request.POST["planta"]
            #planta = 1
            motivo = request.POST["motivo"]
            objetivo = request.POST["objetivo"]
            subjetivo = request.POST["subjetivo"]
            analisis = request.POST["analisis"]
            #plan = request.POST["plan"]
            #usuarioRegistro = request.POST["usuarioRegistro"]
            #now = datetime.now()
            #dnow = now.strftime("%Y-%m-%d %H:%M:%S")
            #print("NOW  = ", dnow)

            #fechaRegistro = dnow
            estadoReg = "A"
            print("estadoRegistro =", estadoReg)
            # Busca el folio a asignar
            # Primero el id del paciente:

            laboratorios = request.POST["FormaLaboratorios"]
            print ("laboratorios =" , laboratorios)



            miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
            curt = miConexiont.cursor()

            comando = "SELECT cast(id as integer) id FROM usuarios_usuarios  WHERE tipoDoc_id = '" + str(tipoDoc) + "' AND documento ='" + str(documento) +"'"

            curt.execute(comando)
            print(comando)

            idPacientes = curt.fetchall()
            for idPaciente in idPacientes:
                print("dato= ", idPaciente)
                idePac= idPaciente



            miConexiont.close()
            print(idPaciente)

            print ("idePAc", idePac )

            print ("idPacienteFinalll", idePac)


            # fIN consegui id del paciente

            #ultimofolio = Historia.objects.all().filter(tipoDoc_id=tipoDoc).filter(documento_id=idPacienteFinal['id']).aggregate(maximo=Coalesce(Max('folio'), 0))
            ultimofolio = Historia.objects.all().filter(tipoDoc_id=tipoDoc).filter(
               documento_id=idePac).aggregate(maximo=Coalesce(Max('folio'), 0 ))


            ## Camio lo anteriro por lo que sigue

            #miConexiont = pyodbc.connect(
            #    'DRIVER={SQL Server};SERVER=CMKSISTEPC07\MEDICAL;DATABASE=vulnerable ;UID=sa;pwd=75AAbb??')
            #curt = miConexiont.cursor()

            #comando = "SELECT max(folio) folio FROM dbo.clinico_historia WHERE tipoDoc_id  = '" + str(tipoDoc) + "' AND documento_id = '" + str(idPacienteFinal) + "'"

            #print(comando)
            #curt.execute(comando)


            #ultimofolio = []

            #for folio in curt.fetchall():
            #    ultimofolio.append({'maximo': folio})

            #miConexiont.close()

            ##########################################


            print("ultimo folio = ", ultimofolio)
            print("ultimo folio = ", ultimofolio[0])
            ultimofolio2 = (ultimofolio[0]) + 1
            print("ultimo folio2 = ", ultimofolio2)

            print ("documento= ", documento)
            print("tipoDoc = ", tipoDoc)
            print ("consec admisione = ", consecAdmision)
            print("folio = ", ultimofolio2)
            print("fecha = ", fecha)
            print("tiposFolio = ", tiposFolio)
            print("causas externa=", causasExterna)
            print("dependenciasrealizado= ", dependenciasRealizado)
            print("especmedico = ", espMedico)
            print("planta = ", planta)
            print("usuarioRegistro = ", usuarioRegistro)



            if (dependenciasRealizado  == '' or causasExterna == ''  or diagnosticos == '' ):



                print("Entre GRAVES campos vacios")
                data1 = {'Tipo' : '"Error', 'Mensaje': 'Favor suministrar causa Externa y/O Dependencia Realiado folio'}
                data2 = json.dumps(data1)

                data2 = data2.replace("\'", "\"")
                data = json.loads(str(data2))


                #return HttpResponse('Favor suministrar causa Externa y/O Dependencia Realiado folio')
                #return HttpResponse(data)
                return JsonResponse(data)

            else:

                # Grabacion Historia

                # Consigo la Especialidad de Evolucion

                miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
                curt = miConexiont.cursor()

                comando = "SELECT e2.id id , e2.nombre nombre FROM clinico_especialidadesMedicos e, clinico_especialidades e2  WHERE e.id = '" +str(espMedico) + "' AND e.especialidades_id = e2.id     "

                curt.execute(comando)
                print(comando)

                especial = []

                for id, nombre in curt.fetchall():
                    especial.append({'id': id, 'nombre': nombre})


                miConexiont.close()
                print(especial)

                jsonEspecial = especial[0]
                campo = jsonEspecial['id']

                # Fin consigo especialidad

                print (campo)
                print("Especial1 = " , campo)

                jsontiposFolio = {'tiposFolio' : tiposFolio}
                print("jsontiposFolio = ", jsontiposFolio)
                print("jsontiposFolio = ", jsontiposFolio ['tiposFolio'])

                jsonPlanta = {'planta': planta}
                jsonUsuarioRegistro = {'usuarioRegistro': usuarioRegistro}

                print ("jsonusuaroregistr= ", jsonUsuarioRegistro ['usuarioRegistro'])
                print ("jsonplanta = ", jsonPlanta ['planta'])

                # Fin Consigo la Especialidad de Evolucion

                # Inicio grabacion Historia Clinica

                #miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')

                miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres", password="pass123")
                curt = miConexiont.cursor()

                # Consigo el Id del Paciente Documento

                DocumentoId = Usuarios.objects.get(documento = documento)
                DocumentoIdFinal = DocumentoId.id
                print ("DocumentoIdFinal", DocumentoIdFinal)


                comando = "INSERT INTO clinico_Historia (tipoDoc_id , documento_id , consecAdmision, folio ,fecha , tiposFolio_id ,causasExterna_id , dependenciasRealizado_id ,especialidades_id ,planta_id, motivo , subjetivo,objetivo, analisis ,plann,fechaRegistro ,usuarioRegistro_id, estadoReg ) VALUES ('" + str(
                    tipoDoc) + "', '" + str(DocumentoIdFinal) + "',  '" + str(consecAdmision) + "', '" + str(
                    ultimofolio2) + "', '" + str(fechaRegistro) + "', '" + str(tiposFolio) + "', '" + str(
                    causasExterna) + "', '" + str(dependenciasRealizado) + "', '" + str(
                    jsonEspecial['id']) + "', '" + str(planta) + "', '" + str(motivo) + "', '" + str(
                    subjetivo) + "', '" + str(objetivo) + "', '" + str(analisis) + "', '" + str(plan) + "', '" + str(
                    fechaRegistro) + "', '" + str(usuarioRegistro) + "', '" + str(estadoReg) + "');"
                
                print(comando)
                resultado = curt.execute(comando)
                print("resultado =", resultado)
                n = curt.rowcount
                print ("Registros commit = " , n)
                #historiaId = miConexiont.insert_id()
                #historiaId = curt.lastrowid

                historiaId = curt.execute('SELECT @@IDENTITY AS id;').fetchone()[0]

                print ("historiaid = ", historiaId)

                miConexiont.commit()

                miConexiont.close()

                print("El id del la hsitoria INSERTADA es ", historiaId)

                # Fingrabacion Historia Clinica


                #nueva_historia = Historia(
                #    tipoDoc= TiposDocumento.objects.get(id = tipoDoc)   ,
                #    documento=Usuarios.objects.get(documento = documento)  ,
                #    consecAdmision=1,
                #    folio=ultimofolio2,
                #    fecha=fechaRegistro,
                #    tiposFolio=TiposFolio.objects.get(id = jsontiposFolio ['tiposFolio'])   ,
                #    causasExterna=CausasExterna.objects.get(id = causasExterna),
                #    dependenciasRealizado=Dependencias.objects.get(id = dependenciasRealizado)   ,
                #    especialidades=Especialidades.objects.get(id = jsonEspecial['id'])   ,
                #    planta=Planta.objects.get(id = jsonPlanta ['planta'])   ,
                #    motivo=motivo,
                #    subjetivo=subjetivo,
                #    objetivo=objetivo,
                #    analisis=analisis,
                #    plan=plan,
                #    fechaRegistro=fechaRegistro,
                #    usuarioRegistro=Usuarios.objects.get(id = jsonUsuarioRegistro ['usuarioRegistro'])   ,
                #    estadoReg=estadoReg)

                #nueva_historia.save()

                #historiaId = nueva_historia.id
                print("Historia No : ", historiaId)
                jsonHistoria = {'id': historiaId}


                # Fin Grabacion Historia


                # Grabacion Laboratorios


                # Fin Grabacion Laboratorios


            data = {'Mensaje': 'Folio exitoso : ' + str(ultimofolio2)}


            #return HttpResponse(json.dumps(data))
            return HttpResponse('Folio Creado')

    else:

        print("Entre por GET Crear Historia Clinica")
        context = {}
        context['title'] = 'Mi gran Template'
        context['historiaForm'] = historiaForm
        context['IncapacidadesForm'] = IncapacidadesForm
        context['HistorialDiagnosticosCabezoteForm'] = HistorialDiagnosticosCabezoteForm

        Sede = request.GET["sede"]
        Username = request.GET["username"]
        Username_id = request.GET["username_id"]
        Profesional = request.GET["profesional"]
        EscogeModulo = request.GET["escogeModulo"]

        NombreSede = request.GET["nombreSede"]
        TipoDocPaciente = request.GET["nombreTipoDoc"]
        DocumentoPaciente = request.GET["documento2"]
        IngresoPaciente = request.GET["consec"]
        EspMedico = request.GET["espMedico"]
        TiposFolio = request.GET["tiposFolio"]
        DocumentoId = request.GET["documentoId"]

        print("especialidad Medico = ", EspMedico)
        print("TipoDocPaciente = ", TipoDocPaciente)
        print("DocumentoPaciente = ", DocumentoPaciente)
        print("IngresoPaciente = ", IngresoPaciente)

        print("Sede = ", Sede)

        print("Username = ", Username)

        context['Sede'] = Sede
        context['Username'] = Username
        context['Username_id'] = Username_id
        context['Profesional'] = Profesional
        context['EscogeModulo'] = EscogeModulo

        context['NombreSede'] = NombreSede
        context['TipoDocPaciente'] = TipoDocPaciente
        context['DocumentoPaciente'] = DocumentoPaciente
        context['IngresoPaciente'] = IngresoPaciente
        context['EspMedico'] = EspMedico
        context['TiposFolio'] = TiposFolio

        # Combo Tipos Diagnostico

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT t.id id, t.nombre  nombre FROM clinico_tiposDiagnostico t"

        curt.execute(comando)
        print(comando)

        tiposDiagnostico = []
        tiposDiagnostico.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposDiagnostico.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposDiagnostico)

        context['TiposDiagnostico'] = tiposDiagnostico

        # Fin combo Tipos Diagnostico

        # Combo Diagnostico

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

        # Combo Especialidades

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT e.id id, e.nombre  nombre FROM clinico_especialidades e"

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

        # Combo TiposFolio

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

        # Combo Laboratorios

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = 'SELECT t.id TipoId, e.id id, e.nombre nombre , e."codigoCups" cups FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e."TiposExamen_id" and t.nombre = ' + "'" + str(
            'LABORATORIO') + "'"
        curt.execute(comando)
        print(comando)

        laboratorios = []
        laboratorios.append({'TipoId': '', 'id': '', 'nombre': '', 'cups': ''})

        for TipoId, id, nombre, cups in curt.fetchall():
            laboratorios.append({'TipoId': TipoId, 'id': id, 'nombre': nombre, 'cups': cups})

        miConexiont.close()
        print(laboratorios)

        context['Laboratorios'] = laboratorios
        context['TipoExamenLab'] = '1'

        # Fin combo Laboratorios

        # Combo Radiologia

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        # comando = "SELECT t.id TipoId, e.id id, e.nombre nombre FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e.TiposExamen_id and t.id ='1'"
        comando = 'SELECT t.id TipoId, e.id id, e.nombre nombre , e."codigoCups" cups FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e."TiposExamen_id" and t.nombre = ' + "'" + str(
            'RADIOLOGIA') + "'"

        curt.execute(comando)
        print(comando)

        radiologias = []
        radiologias.append({'TipoId': '', 'id': '', 'nombre': '', 'cups': ''})

        for TipoId, id, nombre, cups in curt.fetchall():
            radiologias.append({'TipoId': TipoId, 'id': id, 'nombre': nombre, 'cups': cups})

        miConexiont.close()
        print(radiologias)

        context['Radiologias'] = radiologias
        context['TipoExamenRad'] = '3'

        # Fin combo Radiologia

        # Datos Basicos del Paciente

        print("especialidad Medico = ", EspMedico)
        print("TipoDocPaciente = ", TipoDocPaciente)
        print("DocumentoPaciente = ", DocumentoPaciente)
        print("IngresoPaciente = ", IngresoPaciente)
        print("DocumentoId = ", DocumentoId)


        filaTipoDoc = TiposDocumento.objects.get(nombre=TipoDocPaciente)
        print("id tipodoc = " , filaTipoDoc.id)
        print("nombre tipodoc = ", filaTipoDoc.nombre)

        fila = Usuarios.objects.get(tipoDoc_id=filaTipoDoc.id, documento=DocumentoPaciente)
        print("OJO LOS DATOS DESNORMALIOZADOS")

        print(fila.documento)

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",   password="pass123")
        curt = miConexiont.cursor()

       # comando = "select  tipoDoc_id , tip.nombre tipnombre, documento documentoPaciente, u.nombre nombre, case when genero = 'M' then 'Masculino' when genero= 'F' then 'Femenino' end as genero, cen.nombre as centro, tu.nombre as tipoUsuario, fechaNacio, u.direccion direccion, u.telefono telefono  from usuarios_usuarios u, usuarios_tiposUsuario  tu, sitios_centros cen , usuarios_tiposDocumento tip  where tip.id =u.tipoDoc_id  AND u.tipoDoc_id = '" + str(         filaTipoDoc.id) + "' and u.documento = '" + str(fila.documento) + "' and u.tiposUsuario_id = tu.id and u.centrosc_id = cen.id"
        comando = 'select  u."tipoDoc_id" , tip.nombre tipnombre, documento documentoPaciente, u.nombre nombre, case when genero = ' + "'" + str('M') + "'" + ' then ' + "'" + str("Masculino") + "'" + ' when genero= ' + "'" + str('F') + "'" + ' then ' + "'" + str('Femenino') + "'" + ' end as genero, cen.nombre as centro, tu.nombre as tipoUsuario,"fechaNacio", u.direccion direccion, u.telefono telefono from usuarios_usuarios u, usuarios_tiposUsuario tu, sitios_centros cen, usuarios_tiposDocumento tip where tip.id = u."tipoDoc_id"  AND u."tipoDoc_id" = ' +"'" + str(filaTipoDoc.id) + "'" + ' and u.documento = ' + "'" + str(fila.documento) + "'" + ' and u."tiposUsuario_id" = tu.id and u."centrosC_id" = cen.id'

        curt.execute(comando)
        print(comando)

        datosPaciente = []

        for tipoDoc_id, tipnombre, documentoPaciente, nombre, genero, centro, tipoUsuario, fechaNacio, direccion, telefono in curt.fetchall():
            datosPaciente.append(
                {'tipoDoc_id': tipoDoc_id, 'tipnombre': tipnombre, 'documentoPaciente': documentoPaciente,
                 'nombre': nombre, 'genero': genero, 'centro': centro, 'tipoUsuario': tipoUsuario, 'fechaNacio': fechaNacio, 'direccion': direccion,'telefono': telefono})

        miConexiont.close()
        print("OJO ESTOS SON LOS DAOS DEL PACIENTE SELECCIONAO")

        print(datosPaciente)

        context['DatosPaciente'] = datosPaciente

        # Combo Fin Datos BAsicos paciente

        # Combo DependenciasRealizado

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()
        # 3 = Consultorios Verificar

        comando = 'SELECT d.id id, d.nombre nombre FROM sitios_dependencias d WHERE d."sedesClinica_id" = ' + "'" + str( Sede) + "'" +  ' And d."dependenciasTipo_id" = ' + "'" + str('3') + "'"

        curt.execute(comando)
        print(comando)

        dependenciasRealizado = []
        # dependenciasRealizado.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            dependenciasRealizado.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(dependenciasRealizado)

        context['DependenciasRealizado'] = dependenciasRealizado

        # Fin Combo DependenciasRealizado

        # Combo causasExterna

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT d.id id, d.nombre nombre FROM clinico_causasExterna d "
        curt.execute(comando)
        print(comando)

        causasExterna = []
        causasExterna.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            causasExterna.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(causasExterna)

        context['CausasExterna'] = causasExterna

        # Fin Combo causasExterna

        # Combo Tiposantecedentes

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT id,  nombre FROM clinico_tiposAntecedente  "

        curt.execute(comando)
        print(comando)

        tiposAntecedente = []
        tiposAntecedente.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            tiposAntecedente.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(tiposAntecedente)

        context['TiposAntecedente'] = tiposAntecedente

        # Fin Combo Tiposantecedentes

        # Combo antecedentes

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = "SELECT id,  nombre FROM clinico_antecedentes t "

        curt.execute(comando)
        print(comando)

        antecedentes = []
        antecedentes.append({'id': '', 'nombre': ''})

        # Se va en blanco si antecedentes

        print(antecedentes)

        context['Antecedentes'] = antecedentes

        # Fin Combo antecedentes

        # Combo Terapias

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        # comando = "SELECT t.id TipoId, e.id id, e.nombre nombre FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e.TiposExamen_id and t.id ='3'"
        comando = 'SELECT t.id TipoId, e.id id, e.nombre nombre , e."codigoCups" cups FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e."TiposExamen_id" and t.nombre = ' + "'" + str(
            'TERAPIAS') + "'"

        curt.execute(comando)
        print(comando)

        terapias = []
        terapias.append({'TipoId': '', 'id': '', 'nombre': '', 'cups': ''})

        for TipoId, id, nombre, cups in curt.fetchall():
            terapias.append({'TipoId': TipoId, 'id': id, 'nombre': nombre, 'cups': cups})

        miConexiont.close()
        print(terapias)

        context['Terapias'] = terapias
        context['TipoExamenTer'] = '2'

        # Fin combo Terapias

        # Combo No Qx

        miConexiont = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",
                                       password="pass123")
        curt = miConexiont.cursor()

        comando = 'SELECT t.id TipoId, e.id id, e.nombre nombre , e."codigoCups" cups FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e."TiposExamen_id" and t.nombre = ' + "'" + str(
            'PROCEIMIENTOS NO QX') + "'"

        curt.execute(comando)
        print(comando)

        noQx = []
        noQx.append({'TipoId': '', 'id': '', 'nombre': '', 'cups': ''})

        for TipoId, id, nombre, cups in curt.fetchall():
            noQx.append({'TipoId': TipoId, 'id': id, 'nombre': nombre, 'cups': cups})

        miConexiont.close()
        print(noQx)

        context['ProcNoQx'] = noQx
        context['TipoExamenProcNoQx'] = '4'

        # Fin combo No Qx

        return render(request, 'clinico/navegacionClinica.html', context);


#def cargaPanelMedico(request):
#    print("Hola Entre a Cargar el Panel Clinico")

#    Sede = request.POST['Sede']
#    sede = Sede
#    Servicio = request.POST['Servicio']
#    Perfil = request.POST['Perfil']
#    Username = request.POST['Username']
#    username = Username
#    Username_id = request.POST['Username_id']
#    TipoDocPaciente = request.POST['TipoDocPaciente']
#    nombreSede = request.POST['nombreSede']
#    DocumentoPaciente = request.POST['DocumentoPaciente']
#    #espMedico = request.POST['espMedico']
#    IngresoPaciente = request.POST['IngresoPaciente']



def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 



# Create your views here.
def load_dataClinico(request, data):
    print ("Entre load_data Admisiones")

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

    ingresos = []

    # miConexionx = MySQLdb.connect(host='CMKSISTEPC07', user='sa', passwd='75AAbb??', db='vulnerable')
    miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",     password="pass123")
    curx = miConexionx.cursor()
   
    #detalle = 'SELECT i.id id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id"'
    detalle = 'SELECT i.id id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,i.consec consec , i."fechaIngreso" , i."fechaSalida", ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd WHERE sd."sedesClinica_id" = i."sedesClinica_id"  and sd.servicios_id  = ser.id and  i."sedesClinica_id" = dep."sedesClinica_id" AND i."sedesClinica_id" = ' + "'" + str(sede) + "'" + ' AND  deptip.id = dep."dependenciasTipo_id" and i."serviciosActual_id" = ser.id AND dep.disponibilidad = ' + "'" + 'O' + "'" + ' AND i."salidaDefinitiva" = ' + "'" + 'N' + "'" + ' and tp.id = u."tipoDoc_id" and i."tipoDoc_id" = u."tipoDoc_id" and u.id = i."documento_id" and diag.id = i."dxActual_id" and i."fechaSalida" is null and dep."serviciosSedes_id" = sd.id and dep.id = i."dependenciasActual_id" UNION SELECT t.id id, tp.nombre tipoDoc,u.documento documento,u.nombre nombre,t.consec consec , t."fechaSolicita" , cast(' + "'" + str('0001-01-01 00:00:00') + "'" + ' as timestamp) fechaSalida,ser.nombre servicioNombreIng, dep.nombre camaNombreIng , ' + "''" + ' dxActual FROM triage_triage t, usuarios_usuarios u, sitios_dependencias dep , usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  ,sitios_serviciosSedes sd, clinico_servicios ser WHERE sd."sedesClinica_id" = t."sedesClinica_id"  and t."sedesClinica_id" = dep."sedesClinica_id" AND t."sedesClinica_id" = ' "'" + str(sede) + "'" + ' AND dep."sedesClinica_id" =  sd."sedesClinica_id" AND dep.id = t.dependencias_id AND t."serviciosSedes_id" = sd.id  AND deptip.id = dep."dependenciasTipo_id" and  tp.id = u."tipoDoc_id" and t."tipoDoc_id" = u."tipoDoc_id" and u.id = t."documento_id"  and ser.id = sd.servicios_id and dep."serviciosSedes_id" = sd.id and t."serviciosSedes_id" = sd.id and dep."tipoDoc_id" = t."tipoDoc_id" and dep."documento_id" = t."documento_id" and ser.nombre = ' + "'" + str('TRIAGE') + "'"
    print(detalle)

    curx.execute(detalle)

    for id, tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
        ingresos.append(
		{"model":"ingresos.ingresos","pk":id,"fields":
			{'id':id, 'tipoDoc': tipoDoc, 'documento': documento, 'nombre': nombre, 'consec': consec,
                         'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida,
                         'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                         'dxActual': dxActual}})

    miConexionx.close()
    print(ingresos)
    context['Ingresos'] = ingresos


    ## Voy a enviar tickets

    #ingresos['EspecialidadesMedicos'] =

    serialized1 = json.dumps(ingresos, default=serialize_datetime)

    print ("Envio = ", json)

    return HttpResponse(serialized1, content_type='application/json')


def PostConsultaHcli(request):
    print ("Entre PostConsultaHcli ")


    Post_id = request.POST["post_id"]

    print("id = ", Post_id)

    if request.method == 'POST':


        # Abro Conexion

        miConexionx = psycopg2.connect(host="192.168.79.129", database="vulner", port="5432", user="postgres",password="pass123")
        cur = miConexionx.cursor()
        comando = 'SELECT i.id id, i."tipoDoc_id" tipoDocId,td.nombre nombreTipoDoc, i.documento_id documentoId, u.documento documento , i.consec consec FROM admisiones_ingresos i, usuarios_usuarios u, usuarios_tiposDocumento td where i.id=' + "'" +  str(Post_id) + "'" + ' and i."tipoDoc_id" =td.id and i.documento_id=u.id'
        print(comando)

        cur.execute(comando)

        hc = []

        for id, tipoDocId, nombreTipoDoc, documentoId, documento, consec in cur.fetchall():
            hc.append( {"id": id,
                     "tipoDocId": tipoDocId,
                     "nombreTipoDoc": nombreTipoDoc,
                     "documentoId": documentoId, "documento": documento,
                     "consec": consec  })

        miConexionx.close()
        print(hc)

        # Cierro Conexion

        return JsonResponse({'pk':hc[0]['id'],'tipoDocId':hc[0]['tipoDocId'],'nombreTipoDoc':hc[0]['nombreTipoDoc'],
                             'documentoId':hc[0]['documentoId'],  'documento': hc[0]['documento'],
                             'consec': hc[0]['consec']})

    else:
        return JsonResponse({'errors':'Something went wrong!'})

