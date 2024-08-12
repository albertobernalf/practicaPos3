console.log('Hola Alberto Hi!')

var datavta;
var seriali = new Array();
var serialiLab = new Array();
var serialiRad = new Array();
var serialiTer = new Array();
var serialiDiag = new Array();
var serialiAnt = new Array();
var serialiInt = new Array();


var seriali2 = new Array();
var envio = new FormData()
var envio1 = new FormData()
var envio2 = new FormData()
var envioLab = new FormData()
var envioRad = new FormData()
var envioTer = new FormData()

var envioDiag = new FormData()
var formData = new FormData()
var envio_final = new FormData()
var envio_finalRad = new FormData()
var envio_final1 = new FormData()

var x=0
var  folio_final =0

const form = document.getElementById('formHistoria')

const form2 = document.getElementById('formClinicos')
console.log(form)
console.log(form2)


function valida(forma)
{



	};


function CierraModalTriage()
{

       	 $('#modalActualizaTriage').modal().hide();

}

function AUsuarioTriage()
{
	alert("Entre a Grabar Usuario Triage");

	var envios = new FormData();


	var tipoDoc = document.getElementById("tipoDocTriageModal").value;
	alert("tipoDoc = " +  tipoDoc);

	var documento = document.getElementById("documentoTriageModal").value;
        var nombre = document.getElementById("nombre").value;

	alert("Documento = " +  documento);

	var genero = document.getElementById("genero").value;
	var departamentos = document.getElementById("departamentos").value;
	var ciudades = document.getElementById("ciudades").value;
	var direccion = document.getElementById("direccion").value;
        alert("direccion = " +  direccion);
	var telefono = document.getElementById("telefono").value;
	var contacto = document.getElementById("contacto").value;
	var municipio = document.getElementById("municipios").value;
	var localidades = document.getElementById("localidades").value;
	var estadoCivil = document.getElementById("estadoCivil").value;
	var ocupaciones = document.getElementById("ocupaciones").value;
	var correo = document.getElementById("correo").value;
	var fechaNacio = document.getElementById("fechaNacio").value;
	alert("fechaNacio = " + fechaNacio);

	var centrosC = document.getElementById("centrosC").value;
	var tiposUsuario = document.getElementById("tiposUsuario").value;

	alert("centroC = " +  centrosC);

	alert("Voy ajax a Grabar Usuario Triage");

	$.ajax({
		type: 'POST',
	    	url: '/grabaUsuariosTriage/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'nombre':nombre,'genero':genero,'fechaNacio':fechaNacio,
		    'departamentos':departamentos, 'ciudades':ciudades,    'direccion':direccion,'telefono':telefono,
		     'contacto':contacto, "centrosC":centrosC, 'tiposUsuario':tiposUsuario},
		 //     'municipios':municipios},
		//	 'localidades':localidades, 'estadoCivil':estadoCivil, 'ocupaciones':ocupaciones, 'correo':correo},
		success: function (respuesta) {

		alert ("REGRESE DE GRABAR");

                $('#mensaje1').html('<span> respuesta</span>');
                $('#usuariosModalTriage').modal().hide();
		        window.location.reload();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};

///// Aqui la para buscar Usuario Triage ////

$(document).on('change', '#busDocumentoSelTriage', function(event) {

        alert("Entre cambio Modal usuarios Triage");

	var envios = new FormData();

	 var select = document.getElementById("tipoDocTriage"); /*Obtener el SELECT */
    var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */

   documento = document.getElementById("busDocumentoSelTriage").value;
   alert( "Este es el documento : " + tipoDoc +  " " + documento);

    alert("Envio a la MOdal Tipo Doc = " + tipoDoc);
    alert("Envio a la MOdal documento = " + documento);


	$.ajax({
		type: 'POST',
	    	url: '/findOneUsuarioTriage/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {

			 alert("REGRESE DATOS MODAL2 = " + Usuarios.tipoDoc + " " +  Usuarios.documento);


				$('#tipoDocTriageModal').val(Usuarios.tipoDoc);
				$('#documentoTriageModal').val(Usuarios.documento);
				$('#nombre').val(Usuarios.nombre);
				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamentos);
				$('#fechaNacio').val(Usuarios.fechaNacio);
				$('#municipios').val(Usuarios.municipios);
				$('#localidades').val(Usuarios.localidades);
				$('#ciudades').val(Usuarios.ciudad);
				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupaciones);
				$('#correo').val(Usuarios.correo);
				$('#centrosC').val(Usuarios.centrosC);
				$('#tiposUsuario').val(Usuarios.tiposUsuario);

				 $('#usuariosModalTriage').modal({show:true});


                    },
	   		    error: function (request, status, error) {
	   	    	}
	});

});




$('#tablaDatosTriage tbody td').click(function(){
      var rowIndex = $(this).parent().index('#tablaDatosTriage tbody tr');
      var tdIndex = $(this).index('#tablaDatosTriage tbody tr:eq('+rowIndex+') td');
   //   alert('Row Number: '+(rowIndex+1)+'\nColumn Number: '+(tdIndex+1));
  //    var celda = $(this);
      //alert("valor celda = " + celda.html());
 //     let obtenerDato = document.getElementsByTagName("td");
      //alert("valores son : " + obtenerDato.innerHTML + " ::::" + obtenerDato[0].innerHTML + " " + obtenerDato[1].innerHTML + " " + obtenerDato[2].innerHTML + " " + obtenerDato[3].innerHTML + " " + obtenerDato[4].innerHTML + " " + obtenerDato[5].innerHTML + " " + obtenerDato[6].innerHTML)
      //alert ("Aquip los valores");

    //  alert ($(this).parents("tr").find("td").eq(0).html());
    //  alert ($(this).parents("tr").find("td").eq(1).html());
    //  alert ($(this).parents("tr").find("td").eq(2).html());
    //  alert ($(this).parents("tr").find("td").eq(3).html());
    //  alert ($(this).parents("tr").find("td").eq(4).html());

      tipoDoc=$(this).parents("tr").find("td").eq(0).html();
      documento=$(this).parents("tr").find("td").eq(1).html();
      var sede = document.getElementById("Sede").value;



      if ((tdIndex+1) == '9')
      {


      $.ajax({
		type: 'POST',
    	url: '/encuentraTriageModal/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'sede':sede},
		success: function (response_data) {


			 alert("entre DATOS MODAL de Triage y el  nombre es = " + response_data['Triage'].tipoDoc + " " +  response_data['Triage'].documento);

		
                $('#busServicioT').val(response_data['Triage'].servicioSedes);
          	    $('#busSubServicioT').val(response_data['Triage'].subServiciosSedes);
				$('#dependenciasP').val(response_data['Triage'].dependencias);
          		$('#tipoDoc').val(response_data['Triage'].tipoDoc);
				$('#busDocumentoSel').val(response_data['Triage'].documento);
				$('#motivo').val(response_data['Triage'].motivo);
				$('#examenFisico').val(response_data['Triage'].examenFisico);
				$('#frecCardiaca').val(response_data['Triage'].frecCardiaca);
				$('#frecRespiratoria').val(response_data['Triage'].frecRespiratoria);
				$('#taSist').val(response_data['Triage'].taSist);
				$('#taDiast').val(response_data['Triage'].taDiast);
				$('#taMedia').val(response_data['Triage'].taMedia);
				$('#glasgow').val(response_data['Triage'].glasgow);
				$('#peso').val(response_data['Triage'].peso);
				$('#temperatura').val(response_data['Triage'].temperatura);
				$('#estatura').val(response_data['Triage'].estatura);
				$('#glucometria').val(response_data['Triage'].glucometria);
				$('#saturacion').val(response_data['Triage'].saturacion);
				$('#escalaDolor').val(response_data['Triage'].escalaDolor);
				$('#tipoIngreso').val(response_data['Triage'].tipoIngreso);
				$('#observaciones').val(response_data['Triage'].observaciones);
				$('#clasificacionTriage').val(response_data['Triage'].clasificacionTriage);

				 $('#modalActualizaTriage').modal({show:true});


                    },
   		    error: function (request, status, error) {
	   	    	}
	});
      }

	// Aqui es la creacion de la Admision para el triage

 if ((tdIndex+1) == '10')
      {
	alert ("Entre a crear la admision Triage");
	$('#tipoDoc').val(tipoDoc);
	$('#documento').val(documento);
	$('#sede').val(sede);
	alert (documento);

	 $('#crearAdmisionTriage').modal({show:true});
      }



});


 $('.eBtn').on('click',function(event)
	        {
			event.preventDefault();
			var href = $(this).attr('href');
			console.log("Entre AlBERTO BERNAL F Cargue la Forma Modal Usuarios");
			alert("Entre carga MODAL");

			$.get(href, function(Usuarios,status)
			 {
			 alert("entre DATOS MODAL y el nombre es = ");


                $('#tipoDoc').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				alert(Usuarios.nombre);

				$('#nombre').val(Usuarios.nombre);
				$('#genero').val(Usuarios.genero);
				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				}
			);

			 $('#usuariosModal').modal({show:true});

			  });


$(document).on('change', '#departamentos', function(event) {

        alert("Entre cambio Departamento");


       var Departamento =   $(this).val()

       alert("Departamento = " + Departamento);



        $.ajax({
	           url: '/buscarCiudades/',
	            data : {Departamento:Departamento},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#ciudades");


 	      		     $("#ciudades").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busServicio', function(event) {

       var Serv =   $(this).val()

    //   alert("Entre para llamar a buscarServiciosTriage : " + Serv)

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServiciosTriage',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busSubServicio");


 	      		     $("#busSubServicio").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});







$(document).on('change', '#busServicioT', function(event) {

       var Serv =   $(this).val()

    //   alert("Entre para llamar a buscarServiciosTriage : " + Serv)

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServiciosTriage',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busSubServicioT");


 	      		     $("#busSubServicioT").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busSubServicioT', function(event) {

        alert("Entre a busSubServicioT");

        var select = document.getElementById("busServicioT"); /*Obtener el SELECT */
        // var Serv = select.options[select.selectedIndex].value; /* Obtener el valor */
       // var Serv = document.getElementById("busServicioT").value;

	var Serv = $("#busSubServicioT").val();



//        alert("Entre para llamar a buscar Nuevo ServiciosTriage : " + Serv);

        var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


//        alert("Entre para llamar a buscar SubServiciosTriage : " + SubServ);
  //      alert("Entre para llamar a buscar Sede : " + Sede);

        $.ajax({
	           url: '/buscarHabitacionesTriage',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

//	  		alert("Me devuelvo pos satisfactorio habitaciones");


	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);

                     const $id2 = document.querySelector("#dependenciasT");

 	      		     $("#dependenciasT").empty();

//                    alert("ya borre ahora a escribir depedencias" + dato);

	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });

                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});





// Para la ventana Moddal

 $('.eBtn').on('click',function(event)
	        {
			event.preventDefault();
			var href = $(this).attr('href');
			console.log("Entre Ventana Modal");

			$.get(href, function(UsuariosHc,status)
			 {
			 alert("entre");


                $('#username').val(UsuariosHc.username);
				$('#password').val(UsuariosHc.password);

				}
			);

			 $('#exampleModal').modal({show:true});

			  });




// FUnciones para Modales

function abrir_modal(url)
        {
            alert ("Entre NModal_0000000000000000000000000001");
            $('#modalActualizaTriage').load(url, function()
            {
            alert ("Entre NModal_001");
            $(this).modal({

                backdrop: 'static',
                keyboard: false
            })
            alert ("Entre NModal_003");

            $('#tipoDoc').val("1");
	    	$('#documento').val("33333333333333333333");



            $(this).modal('show');
            });
            return false;
        }

function cerrar_modalTriage()
        {
        $('#modalActualizaTriage').modal('hide');
return false;
        }


function findOneTriage(tipoDoc , Documento, Nombre, sede)
{
     alert("Entre function finfOneTriage");
     alert("datos0 = " + tipoDoc);
     alert("datos1 = " + Documento);
     alert("datos2 = " + Nombre);
     alert("datos3 = " + sede);
     var envios = new FormData();




};

function guardaTriageModal()
{
	const forma = document.getElementById("guardaTriageModal");

	//var envios = new FormData(forma);
	//var envios2 =  $('#guardaTriageModal').serialize();


	var tipoDoc = document.getElementById("tipoDoc").value;
	alert("tipoDoc = " +  tipoDoc);

	var documento = document.getElementById("busDocumentoSel").value;

  	var busServicioT = document.getElementById("busServicioT").value;
  	var busSubServicioT = document.getElementById("busSubServicioT").value;
  	var dependenciasP = document.getElementById("dependenciasP").value;

  	var motivo = document.getElementById("motivo").value;
  	var examenFisico = document.getElementById("examenFisico").value;
  	var frecCardiaca = document.getElementById("frecCardiaca").value;
  	var frecRespiratoria = document.getElementById("frecRespiratoria").value;
  	var taSist = document.getElementById("taSist").value;
  	var taDiast = document.getElementById("taDiast").value;
  	var taMedia = document.getElementById("taMedia").value;
  	var glasgow = document.getElementById("glasgow").value;
  	var peso = document.getElementById("peso").value;
  	var estatura = document.getElementById("estatura").value;
  	var temperatura = document.getElementById("temperatura").value;
  	var glucometria = document.getElementById("glucometria").value;
  	var escalaDolor = document.getElementById("escalaDolor").value;
  	var tipoIngreso = document.getElementById("tipoIngreso").value;
  	var observaciones = document.getElementById("observaciones").value;
  	var clasificacionTriage = document.getElementById("clasificacionTriage").value;



	$.ajax({
		type: 'POST',
	    url: '/grabaTriageModal/',
	    dataType: 'JSON',
	    data: {'tipoDoc': tipoDoc,
	            'documento': documento,
	            'busServicioT' : busServicioT,
	            'busSubServicioT':busSubServicioT,
	            'dependenciasP':dependenciasP,
	            'motivo':motivo ,
	             'examenFisico':examenFisico,
	             'frecCardiaca':frecCardiaca,
	             'frecRespiratoria':frecRespiratoria,
	             'taSist':taSist,
	             'taDiast':taDiast,
	             'taMedia':taMedia,
	             'glasgow':glasgow,
	             'peso':peso,
	             'temperatura':temperatura ,
	             'estatura':estatura,
	             'glucometria':glucometria,
	             'escalaDolor':escalaDolor,
	             'tipoIngreso':tipoIngreso,
	             'observaciones':observaciones,
	             'clasificaciontriage':clasificacionTriage},

		success: function (respuesta)
		        {
		        alert ("respuesta =" + respuesta);
        		alert ("REGRESE DE GRABAR triage modal");

                $('#mensaje1').html('<span> respuesta</span>');
                $('#modalActualizaTriage').modal().hide();

		        window.location.reload();
		        $('#mensajeria').val("Triage Actualizado ...");

                },
	   		    error: function (request, status, error)
	   		    {
	   	    	}
	});


 //cache: false,
        //	    data: {'tipoDoc': tipoDoc, 'documento': documento, 'busServicioT' : busServicioT, 'busSubServicioT':busSubServicioT,'dependenciasP':dependenciasP,'motivo':motivo , 'examenFisico':examenFisico,'frecCardiaca':frecCardiaca,'frecRespiratoria':frecRespiratoria,
        //             'taSist':taSist, 'taDiast':taDiast, 'taMedia':taMedia,'glasgow':glasgow,'peso':peso,'temperatura':temperatura ,'estatura':estatura,'glucometria':glucometria,'escalaDolor':escalaDolor,'tipoIngreso':tipoIngreso,'observaciones':observaciones},
	//	data:envios,        // {'estatura':estatura,'peso':peso,'documento':documento},
  //		dataType: 'JSON',
		//processData: false,
	    //method: "POST",

   // {'estatura':estatura,'peso':peso,'documento':documento},

};
