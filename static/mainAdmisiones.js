var $ = jQuery;
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

const get = document.getElementById('dispara');


get.addEventListener('click', e => {});
get.dispatchEvent(new Event('click'));  


function clickEvent() {  

    console.log("The required event is triggered ") ;

	var valor = $('input[name="ingresoId"]:checked').val();
	var sede = document.getElementById("sede").value;

	$.ajax({
		type: 'POST',
    		url: '/cambioServicio/',
		data: {'valor' : valor, 'sede': sede},
		dataType : 'json',
		success: function (cambioServicio) {

                  alert("llegue MODAL cambio Servicio = " + cambioServicio['Usuarios'].tipoDocId);
                  alert("llegue MODAL cambio Servicio = " + cambioServicio['Usuarios'].documento);
                     alert("servicio = " + cambioServicio['DependenciasActual'].servicio);
                      alert("Subservicioio = " + cambioServicio['DependenciasActual'].subServicio);

//		$("#tipoDocx option[value="+ cambioServicio['Usuarios'].tipoDocId +"]").attr("selected",true);
		 $('#tipoDocx').val(cambioServicio['Usuarios'].tipoDoc);
		 $('#documentox').val(cambioServicio['Usuarios'].documento);
		 $('#pacientex').val(cambioServicio['Usuarios'].paciente);
		 $('#consecx').val(cambioServicio['Usuarios'].consec);
		$('#servicioActual').val(cambioServicio['DependenciasActual'].servicio);
		$('#subServicioActual').val(cambioServicio['DependenciasActual'].subServicio);
		$('#dependenciaActual').val(cambioServicio['DependenciasActual'].depNombre);
		$('#fechaOcupacion').val(cambioServicio['DependenciasActual'].ocupacion);
		 $('#servicioCambio').val(cambioServicio['Servicios']);
		 $('#subServicioCambio').val(cambioServicio['SubServicios']);
		 $('#dependenciaCambio').val(cambioServicio['DependenciasActual'].habitaciones);
                    },
	   		    error: function (request, status, error) {
	   	    	}
	}); 
} 



$(document).on('change', '#ingresoId', function(event) {

           document.getElementById("mensajes").innerText="";
           document.getElementById("tipoDocx").value="";
           document.getElementById("documentox").value="";
           document.getElementById("pacientex").value="";
           document.getElementById("consecx").value="";
           document.getElementById("servicioActual").value="";
           document.getElementById("subServicioActual").value="";
           document.getElementById("dependenciaActual").value="";
           document.getElementById("fechaOcupacion").value="";
           document.getElementById("servicioCambio").value="";
           document.getElementById("subServicioCambio").value="";
           document.getElementById("dependenciaCambio").value="";//

	       var data =  {}   ;
           var sede = document.getElementById("sede1").value;
           data['sede'] = sede;
           var ingresoId= document.getElementById("ingresoId1").value;
           data['ingresoId'] = ingresoId;
           data = JSON.stringify(data);
	   table = $("#tablaConveniosAdmisiones").dataTable().fnDestroy();
           initTableConvenios(data);

           // Esta es la parte del cambio de Servicio

           	var valor = $('input[name="ingresoId"]:checked').val();
	var sede = document.getElementById("sede").value;

	$.ajax({
		type: 'POST',
    		url: '/cambioServicio/',
		data: {'valor' : valor, 'sede': sede},
		dataType : 'json',
		success: function (cambioServicio) {

                  alert("llegue MODAL cambio Servicio = " + cambioServicio['Usuarios'].tipoDocId);
                  alert("llegue MODAL cambio Servicio = " + cambioServicio['Usuarios'].documento);
                     alert("servicio = " + cambioServicio['DependenciasActual'].servicio);
                      alert("Subservicioio = " + cambioServicio['DependenciasActual'].subServicio);

//		$("#tipoDocx option[value="+ cambioServicio['Usuarios'].tipoDocId +"]").attr("selected",true);
		 $('#tipoDocx').val(cambioServicio['Usuarios'].tipoDoc);
		 $('#documentox').val(cambioServicio['Usuarios'].documento);
		 $('#pacientex').val(cambioServicio['Usuarios'].paciente);
		 $('#consecx').val(cambioServicio['Usuarios'].consec);
		$('#servicioActual').val(cambioServicio['DependenciasActual'].servicio);
		$('#subServicioActual').val(cambioServicio['DependenciasActual'].subServicio);
		$('#dependenciaActual').val(cambioServicio['DependenciasActual'].depNombre);
		$('#fechaOcupacion').val(cambioServicio['DependenciasActual'].ocupacion);
		 $('#servicioCambio').val(cambioServicio['Servicios']);
		 $('#subServicioCambio').val(cambioServicio['SubServicios']);
		 $('#dependenciaCambio').val(cambioServicio['DependenciasActual'].habitaciones);
                    },
	   		    error: function (request, status, error) {
	   	    	}
	});


           // Fin cambio de servicio


});



function valida(forma)
{



	};



function CierraModal()
{
        alert("A cerrar");
       	 $('#usuariosModal').modal(hide);
           alert("Cerrado");
}

function AUsuario()
{

	var envios = new FormData();


	var tipoDoc = document.getElementById("tipoDoc1").value;
	alert("tipoDoc = " +  tipoDoc);

	var documento = document.getElementById("documento1").value;
		var busDocumentoSel = document.getElementById("busDocumentoSel").value;
   var nombre = document.getElementById("nombre1").value;

   alert("Documento = " +  documento);
 alert("OtorDocumento = " +  busDocumentoSel);

	var genero = document.getElementById("genero").value;
	var departamentos = document.getElementById("departamentos").value;
	var ciudades = document.getElementById("ciudades").value;


	var direccion = document.getElementById("direccion").value;
	 alert("direccion = " +  direccion);
	var telefono = document.getElementById("telefono").value;
	var contacto = document.getElementById("contacto").value;
	var municipio = document.getElementById("municipios").value;
	var localidad = document.getElementById("localidades").value;
	var estadoCivil = document.getElementById("estadoCivil").value;
	var ocupacion = document.getElementById("ocupaciones").value;
	var correo = document.getElementById("correo").value;
	var fechaNacio = document.getElementById("fechaNacio").value;
	alert("fechaNacio = " + fechaNacio);

	var centrosc = document.getElementById("centrosc").value;
	var tiposUsuario = document.getElementById("tiposUsuario").value;
	var centrosC_id = document.getElementById("centrosc").value;

	alert("centroC_id = " +  centrosC_id);


	$.ajax({
		type: 'POST',
    	url: '/guardarUsuariosModal/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'nombre':nombre,'genero':genero,'fechaNacio':fechaNacio, 'departamentos':departamentos, 'ciudades':ciudades,'direccion':direccion,'telefono':telefono, 'contacto':contacto, "centrosC_id":centrosC_id, 'tiposUsuario':tiposUsuario, 'municipios':municipio,'localidades':localidad, 'estadoCivil':estadoCivil,'ocupaciones':ocupacion, 'correo':correo},

		success: function (respuesta) {

			$('#usuariosModal').modal().hide();
            //  document.getElementById("fechaIngreso").value = '2024-01-01';
     


                $('#mensaje1').html('<span> respuesta</span>');
                $('#usuariosModal').modal().hide();
			   
			     window.location.reload();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};


// Aqui combos para Cambio de servicio

$(document).on('change', '#servicioCambio', function(event) {

    alert (" Entre cambio Servicio");
    var serv =   $(this).val()
    var sede =  document.getElementById("sede").value;
    alert ("envio = " + serv + "   " + sede);


        $.ajax({
	           url: '/buscarSubServicios',
	            data : {serv:serv, sede:sede},
	           type: 'GET',
	           dataType : 'json',
	  		success: function (respuesta) {
                        alert("Regrese");

	  		   var options = '<option value="=================="></option>';
	  		  var dato = JSON.parse(respuesta);
                     const $id2 = document.querySelector("#subServicioCambio");
 	      		     $("#subServicioCambio").empty();
				alert("voy a llenar subservicio");
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



$(document).on('change', '#subServicioCambio', function(event) {
    alert (" Entre cambio Habitacion Servicio");
       var select = document.getElementById("servicioCambio"); /*Obtener el SELECT */
       var serv = select.options[select.selectedIndex].value; /* Obtener el valor */
       var subServ =   $(this).val()
       alert("voy a enviar este servicio   = " + serv);
       alert("voy a enviar este Subservicio   = " + subServ);
       var sede =  document.getElementById("sede").value;

        $.ajax({
	           url: '/buscarHabitaciones',
		    data : {serv:serv, sede:sede, subServ:subServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',
	  		success: function (respuesta) {
	  		   var options = '<option value="=================="></option>';
	  		  var dato = JSON.parse(respuesta);
                     const $id2 = document.querySelector("#dependenciaCambio");
 	      		     $("#dependenciaCambio").empty();
			
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

// Fin combios cambios de Servicio


// Aqui la Grabacion del Cambio de Servicio



// Fin grabacion Cambio de Servicio

///// Aqui la para buscar Usuario  Admisiones ////

$(document).on('change', '#busDocumentoSel', function(event) {

        alert("Entre cambio Modal usuarios");

	var envios = new FormData();


   eldocu = document.getElementById("busDocumentoSel").value;
   alert( "Este es el nro del documento : " + eldocu);
   	var busDocumentoSel = document.getElementById("busDocumentoSel").value;
    alert("Documento = " +  eldocu);
    alert("OtorDocumento = " +  busDocumentoSel);
	 var select = document.getElementById("tipoDoc"); /*Obtener el SELECT */
       var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */
	var documento = document.getElementById("busDocumentoSel").value;

    alert("Envio a la MOdal Tipo Doc = " + tipoDoc);
    alert("Envio a la MOdal documento = " + documento);

	$.ajax({
		type: 'POST',
    	url: '/findOneUsuario/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL y el nombre es = " + Usuarios.tipoDoc_id + " " +  Usuarios.documento);

                $('#tipoDoc1').val(Usuarios.tipoDoc_id);
		$('#tipoDoc').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				$('#nombre1').val(Usuarios.nombre);

				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamento);
				$('#municipios').val(Usuarios.municipio);
				$('#localidades').val(Usuarios.localidad);
				$('#ciudades').val(Usuarios.ciudad);

				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupacion);
				$('#correo').val(Usuarios.correo);


				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModal').modal({show:true});
			//	 $('#usuariosModal').modal().hide();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});

});


//  FIN

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

			 alert("entre DATOS MODAL y el nombre es = " + Usuarios.tipoDoc_id + " " +  Usuarios.documento);

                $('#tipoDoc').val(Usuarios.tipoDoc_id);
		$('#tipoDoc').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				$('#nombre1').val(Usuarios.nombre);

				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamento);
				$('#municipios').val(Usuarios.municipio);
				$('#localidades').val(Usuarios.localidad);
				$('#ciudades').val(Usuarios.ciudad);

				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupacion);
				$('#correo').val(Usuarios.correo);


				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModalTriage').modal({show:true});
			//	 $('#usuariosModal').modal().hide();
                    },
	   		    error: function (request, status, error) {
	   	    	}
	});

});


// Aqui usuario para triage

function findOneUsuarioTriage()
{

	var envios = new FormData();

   eldocu = document.getElementById("busDocumentoSelTriage").value;
   alert( "Este es el nro del documento : " + eldocu);
   	var busDocumentoSelTriage = document.getElementById("busDocumentoSeltriage").value;
    alert("Documento = " +  eldocu);
    alert("OtorDocumento = " +  busDocumentoSelTriage);


	 var select = document.getElementById("tipoDoc"); /*Obtener el SELECT */
       var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */
	var documento = document.getElementById("busDocumentoSelTriage").value;

    alert("Envio a la MOdal Tipo Doc = " + tipoDoc);
    alert("Envio a la MOdal documento = " + documento);


	$.ajax({
		type: 'POST',
    	url: '/findOneUsuario/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL y el nombre es = " + Usuarios.tipoDoc_id + " " +  Usuarios.documento);

                $('#tipoDoc1').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				$('#nombre1').val(Usuarios.nombre);

				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamento);
				$('#municipios').val(Usuarios.municipio);
				$('#localidades').val(Usuarios.localidad);
				$('#ciudades').val(Usuarios.ciudad);

				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupacion);
				$('#correo').val(Usuarios.correo);
				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModalTriage').modal({show:true});
			//	 $('#usuariosModal').modal().hide();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};


$(document).on('change', '#busDocumentoSel22', function(event) {

	var envios = new FormData();

     var select = document.getElementById("tipoDoc22"); /*Obtener el SELECT */
       var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */


	var documento = document.getElementById("busDocumentoSel22").value;

    alert("Envio a la MOdal Tipo Doc = " + tipoDoc);
    alert("Envio a la MOdal documento = " + documento);


	$.ajax({
		type: 'POST',
    	url: '/findOneUsuario/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL y el nombre es = " + Usuarios.tipoDoc_id + " " +  Usuarios.documento);

                             $('#tipoDoc1').val(Usuarios.tipoDoc_id);
				$('#documento1').val(Usuarios.documento);
				$('#nombre1').val(Usuarios.nombre);
				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamento);
				$('#municipios').val(Usuarios.municipio);
				$('#localidades').val(Usuarios.localidad);
				$('#ciudades').val(Usuarios.ciudad);

				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupacion);
				$('#correo').val(Usuarios.correo);
				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModal').modal({show:true});





                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
});




function findOneUsuario1()
{

	var envios = new FormData();

   eldocu = document.getElementById("busDocumentoSel").value;
   alert( "Este es el nro del documento : " + eldocu);


   	var busDocumentoSel = document.getElementById("busDocumentoSel").value;
    alert("Documento = " +  eldocu);
    alert("OtorDocumento = " +  busDocumentoSel);

   var select = document.getElementById("tipoDoc"); /*Obtener el SELECT */

       var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */


	var documento = document.getElementById("busDocumentoSel").value;

    alert("Envio a la MOdal Tipo Doc = " + tipoDoc);
    alert("Envio a la MOdal documento = " + documento);


	$.ajax({
		type: 'POST',
    	url: '/findOneUsuario/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL y el nombre es = " + Usuarios.tipoDoc_id + " " +  Usuarios.documento);

                $('#tipoDoc1').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);
				$('#nombre1').val(Usuarios.nombre);
				$('#genero').val(Usuarios.genero);
				$('#departamentos').val(Usuarios.departamento);
				$('#municipios').val(Usuarios.municipio);
				$('#localidades').val(Usuarios.localidad);
				$('#ciudades').val(Usuarios.ciudad);

				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#estadoCivil').val(Usuarios.estadoCivil);
				$('#ocupaciones').val(Usuarios.ocupacion);
				$('#correo').val(Usuarios.correo);


				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModal').modal({show:true});
			//	 $('#usuariosModal').modal().hide();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};






$('#tablaDatos tbody td').click(function(){
      var rowIndex = $(this).parent().index('#tablaDatos tbody tr');
      var tdIndex = $(this).index('#tablaDatos tbody tr:eq('+rowIndex+') td');
   //   alert('Row Number: '+(rowIndex+1)+'\nColumn Number: '+(tdIndex+1));

      tipoDoc=$(this).parents("tr").find("td").eq(0).html();
      documento=$(this).parents("tr").find("td").eq(1).html();
      consec=$(this).parents("tr").find("td").eq(3).html();
      var sede = document.getElementById("sede").value;

     alert("sede = " + sede);
  //    alert("tipoDoc =" + tipoDoc + "documento=" + documento + "ingreso= " + consec);
  //    alert("tdIndex = " + tdIndex);

//    $(this).addClass('selected').siblings().removeClass('selected');    
  //    alert("El valor del botón seleccionado es: " + $(this).find('input:first').val());
  

      if ((tdIndex+1)=='10')
      {
      alert("Entre a Editar AJAX");

      $.ajax({
		type: 'POST',
      	        url: '/encuentraAdmisionModal/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'consec':consec,'sede':sede},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL de Triage y el  nombre es = " + Usuarios.tipoDoc + " " +  Usuarios.documento);

		            $('#tipoDoc').val(Usuarios.tipoDoc_id);
    			    $('#busDocumentoSel').val(Usuarios.documento);
    			    $('#dependenciasIngreso').val(Usuarios.dependenciasIngreso);
    			    $('#busEspecialidad').val(Usuarios.espMedico);
    			    $('#dxIngreso').val(Usuarios.dxIngreso);
    			    $('#medicoIngreso').val(Usuarios.medicoIngreso);
    			    $('#viasIngreso').val(Usuarios.viasIngreso);
    			    $('#causasExterna').val(Usuarios.causasExterna);
    			    $('#regimenes').val(Usuarios.regimenes);
    			    $('#tiposCotizante').val(Usuarios.cotizante);
    			    $('#remitido').val(Usuarios.remitido);
    			    $('#numManilla').val(Usuarios.numManilla);

                            $('#modalActualizaAdmision').modal({show:true});

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
      }

      if ((tdIndex+1)=='11')
      {

      var ingresoId = $('input[name="ingresoId"]:checked').val();
      document.getElementById("sede1").value = sede;
      document.getElementById("ingresoId1").value =ingresoId;
      document.getElementById("sede2").value = sede;
      document.getElementById("ingresoId2").value =ingresoId;

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

				});

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






$(document).on('change', '#busEspecialidad', function(event) {

        alert("Entre cambio especialdiad");


       var Esp =   $(this).val()

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarEspecialidadesMedicos',
	            data : {Esp:Esp, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#medicoIngreso");


 	      		     $("#medicoIngreso").empty();


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



$(document).on('change', '#tiposAntecedente', function(event) {


       var select = document.getElementById("tiposAntecedente"); /*Obtener el SELECT */
       var TiposAntecedente = select.options[select .selectedIndex].value; /* Obtener el valor */
     //  var Antecedentes =   $(this).val()

       // var Sede =  document.getElementById("Sede").value;
        alert("Entre Tipos Antecedente");

        $.ajax({
	           url: '/buscarAntecedentes',
	            data : {TiposAntecedente:TiposAntecedente},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#antecedentes");


      		     $("#antecedentes").empty();

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

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServicios',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busSubServicio");


 	      		     $("#busSubServicio").empty();

				alert("voy a llenar subservicio");
	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });

							alert("ya llene subservicio");



                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busServicioT', function(event) {



       var Serv =   $(this).val()

       alert("Entre para llamar a buscarServiciosTriage : " + Serv)

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



$(document).on('change', '#busSubServicio', function(event) {


       var select = document.getElementById("busSubServicio"); /*Obtener el SELECT */
       var serv = select.options[select.selectedIndex].value; /* Obtener el valor */
       var subServ =   $(this).val()

        var sede =  document.getElementById("sede").value;
        alert("voy a enviar este servicio parea la busqueda de habitaciones  = " + serv);


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {serv:serv, sede:sede, subServ:subServ, Exc:'N'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);

                     const $id2 = document.querySelector("#busHabitacion");
 	      		     $("#busHabitacion").empty();

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



        alert("Entre para llamar a buscar Nuevo ServiciosTriage : " + Serv);

        var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


        alert("Entre para llamar a buscar SubServiciosTriage : " + SubServ);
        alert("Entre para llamar a buscar Sede : " + Sede);

        $.ajax({
	           url: '/buscarHabitacionesTriage',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		alert("Me devuelvo pos satisfactorio habitaciones");


	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);

                     const $id2 = document.querySelector("#dependenciasT");

 	      		     $("#dependenciasT").empty();

                    alert("ya borre ahora a escribir depedencias" + dato);

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







$(document).on('change', '#busServicio22', function(event) {



       var serv =   $(this).val()

        var sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServicios',
	            data : {serv:serv, sede:sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {
				alert("DE REGRESO");


	  		   var options = '<option value="=================="></option>';
	  		  var dato = JSON.parse(respuesta);
			alert("esto devuelve = " + dato);

                     const $id21 = document.querySelector("#busSubServicio22");
 	      		     $("#busSubServicio22").empty();

	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id21.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busSubServicio22', function(event) {

       alert("Entre a cambiar el subservicio");	

       var select = document.getElementById("busServicio22"); /*Obtener el SELECT */
       var serv = select.options[select .selectedIndex].value; /* Obtener el valor */
       var subServ =   $(this).val()

        var sede =  document.getElementById("sede").value;


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {serv:serv, sede:sede, subServ:subServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#dependenciasIngreso22");


 	      		     $("#dependenciasIngreso22").empty();


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






function encuentraAdmisionModal()
{
}

function abrir_modal(url)
        {
            alert ("Entre NModal_0000000000000000000000000001");
            $('#modalActualizaAdmision').load(url, function()
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

function cerrar_modal()
        {
        $('#modalActualizaAdmision').modal('hide');
return false;
        }


function findOneAdmision(tipoDoc,Documento,consec, sede)
{

	var envios = new FormData();


	//var select = document.getElementById("tipoDoc");
    //var tipoDoc = select.options[select.selectedIndex].value;
	//var documento = document.getElementById("busDocumentoSel").value;


    alert("Envio a la MOdal documento = " + documento);

	$.ajax({
		type: 'POST',
    	url: '/encuentraAdmisionModal/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'consec':consec, 'sede':sede},
		success: function (Usuarios) {

			 alert("entre DATOS MODAL de admision y el nombre es = " + Usuarios.tipoDoc + " " +  Usuarios.documento);

	            $('#tipoDoc').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				$('#viasIngreso').val(Usuarios.viasIngreso);

				$('#causasExterna').val(Usuarios.causasExterna);
				$('#regimenes').val(Usuarios.regimenes);
				$('#cotizante').val(Usuarios.cotizante);
				$('#remitido').val(Usuarios.remitido);
				$('#ips').val(Usuarios.ips);

				$('#numManilla').val(Usuarios.numManilla);
				$('#dxIngreso').val(Usuarios.dxIngreso);
				$('#paciente').val(Usuarios.paciente);
				$('#ingreso').val(Usuarios.ingreso);
				$('#salida').val(Usuarios.salida);
				$('#medicoIngreso').val(Usuarios.medicoIngreso);
				$('#espMedico').val(Usuarios.espMedico);
				$('#diagMedico').val(Usuarios.diagMedico);

				 $('#modalActualizaAdmision').modal({show:true});

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};




function guardaCambioServicio()
{


	var tipoDocx = document.getElementById("tipoDocx").value;
	var documentox = document.getElementById("documentox").value;
	var pacientex = document.getElementById("pacientex").value;
	var consecx = document.getElementById("consecx").value;
	var sede= document.getElementById("sede").value;

	var fechaOcupacion = document.getElementById("fechaOcupacion").value;
    var servicioActual = document.getElementById("servicioActual").value;
    var subServicioActual = document.getElementById("subServicioActual").value;
    var dependenciaActual = document.getElementById("dependenciaActual").value;

	var select = document.getElementById("servicioCambio");
    var servicioCambio = select.options[select.selectedIndex].value;
	var select = document.getElementById("subServicioCambio");
    var subServicioCambio = select.options[select.selectedIndex].value;
	var select = document.getElementById("dependenciaCambio");
    var dependenciaCambio = select.options[select.selectedIndex].value;


	var username = document.getElementById("username").value;
	var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
	var numReporte = document.getElementById("numreporte").value;
	var grupo = document.getElementById("grupo").value;
	var subGrupo = document.getElementById("subGrupo").value;
	var sede = document.getElementById("sede").value;
	var documento = document.getElementById("documento").value;
	var nombreSede = document.getElementById("nombreSede").value;
	var profesional = document.getElementById("profesional").value;
	var permisosGrales = document.getElementById("permisosGrales").value;
	var escogeModulo = document.getElementById("escogeModulo").value;
	var username_id = document.getElementById("username_id").value;
	var permisosDetalle = document.getElementById("permisosDetalle").value;

	
    alert("Envio:  " + documentox);

	$.ajax({
		type: 'POST',
    		url: '/guardaCambioServicio/',
		data: {'tipoDocx':tipoDocx,
			'documentox':documentox,
			'consecx':consecx,
             'pacientex':pacientex,
			 'sede':sede,
			 'fechaOcupacion':fechaOcupacion,
			 'servicioActual':servicioActual,
			 'subServicioActual':subServicioActual,
			 'dependenciaActual':dependenciaActual,
			 'servicioCambio':servicioCambio,
			 'subServicioCambio':subServicioCambio,
			 'dependenciaCambio':dependenciaCambio,
			 'username':username,
			 'sedeSeleccionada':sedeSeleccionada,
			 'numReporte':numReporte,
			 'grupo':grupo,
 			 'subGrupo':subGrupo,
             'nombreSede':nombreSede,
			 'profesional':profesional,
			 'permisosGrales':permisosGrales,
			 'escogeModulo':escogeModulo,
			 'username_id':username_id,
			 'permisosDetalle':permisosDetalle},

		success: function (CambioServicio) {

			 alert("DE REGRESO CON CambioServicio = " + CambioServicio);
			 alert("DE REGRESO CON CambioServicio Doc = " + CambioServicio.Documentox);
			 alert("FECHA OCUPACION = " + CambioServicio.FechaOcupacion);

	                       $('#tipoDocx').val(CambioServicio.TipoDocx);
				$('#documentoc').val(CambioServicio.Documentox);
				$('#pacientex').val(CambioServicio.Pacientex);
				$('#servicioActual').val(CambioServicio.ServicioActual);
				$('#subServicioActual').val(CambioServicio.SubServicioActual);
				$('#dependenciaActual').val(CambioServicio.DependenciaActual);
				$('#fechaOcupacion').val(CambioServicio.FechaOcupacion);
		
	  		  var options = '<option value="=================="></option>';
                          const $id2 = document.querySelector("#servicioCambio");
	     		  $("#servicioCambio").empty();

	                 $.each(CambioServicio['Servicios'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });

			  var options = '<option value="=================="></option>';	  	
                          const $id3 = document.querySelector("#subServicioCambio");
	     		  $("#subServicioCambio").empty();

	                 $.each(CambioServicio['SubServicios'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id3.appendChild(option);
 	      		      });

			  var options = '<option value="=================="></option>';	  	
                          const $id4 = document.querySelector("#dependenciaCambio");
	     		  $("#dependenciaCambio").empty();

	                 $.each(CambioServicio['Habitaciones'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4.appendChild(option);
 	      		      });
			
					
                     document.getElementById("mensajes").innerText=CambioServicio.Mensaje;



                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};


const article = document.querySelector('article');
// Print the selected target
article.addEventListener('click', event => {
    // alert("click en article" + event.target);
});

$(document).ready(function () {

	  var data =  {}   ;
          var sede = document.getElementById("sede1").value;
          data['sede'] = sede;
          var ingresoId= document.getElementById("ingresoId1").value;
          data['ingresoId'] = 0  // ingresoId;
          data = JSON.stringify(data);
    

    initTableConvenios(data);

    tableActions();

    	/*------------------------------------------
        --------------------------------------------
        Click to Button
        --------------------------------------------
        --------------------------------------------*/
        $('#createNewPost').click(function () {

	    var ingresoId= document.getElementById("ingresoId1").value;
	    document.getElementById("ingresoId2").value = ingresoId;

            $('#saveBtnCrearConvenio').val("Create Post");
            $('#post_id').val('');
            $('#postFormCrearConvenio').trigger("reset");
            $('#modelHeading').html("Creacion convenios en admision");
            $('#crearConvenioModel').modal('show');
        });
	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostConvenios', function () {

          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

      	$.ajax({
	           url: '/creacionHc/postConsultaHcli/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                        alert("respuesta="  + data);

			 $('#pk').val(data.pk);
        	        $('#tipoDocId').val(data.tipoDocId);
                	$('#nombreTipoDoc').val(data.nombreTipoDoc);
	                $('#documentoId').val(data.documentoId);
	                $('#documento').val(data.documento);
	                $('#consec').val(data.consec);


                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });

        /*------------------------------------------
        --------------------------------------------
        Print Error Msg
        --------------------------------------------
        --------------------------------------------*/
        function printErrorMsg(msg) {
            $('.error-msg').find('ul').html('');
            $('.error-msg').css('display','block');
            $.each( msg, function( key, value ) {
                $(".error-msg").find("ul").append('<li>'+value+'</li>');
            });
        }

        /*------------------------------------------
        --------------------------------------------
        Create Post Code
        --------------------------------------------
        --------------------------------------------*/
        $('#saveBtnCrearConvenio').click(function (e) {
            e.preventDefault();
            $(this).html('Sending..');

            $.ajax({
                data: $('#postFormCrearConvenio').serialize(),
               // url: "{% url '/guardaConvenioAdmision' %}",
		  url: "/guardaConvenioAdmision/",
                type: "POST",
                dataType: 'json',
                success: function (data) {
			printErrorMsg(data.error)
                    if ($.isEmptyObject(data.error)) {

                        //  $("input[name='description']").val('');
                        $('#crearConvenioModel').modal('hide');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
                    }else{
                        printErrorMsg(data.error)
                    }
                    $('#postFormCrearConvenio').trigger("reset");
	 	  var table = $('#tablaConveniosAdmisiones').DataTable(); // accede de nuevo a la DataTable.
	          table.ajax.reload();

                },
                error: function (data) {
			alert("VENGO CON ERRORES :" , printErrorMsg(data.error));
                   // $('#saveBtnCrearConvenio').html('NOT Save Changes');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.error);

		  var table = $('#tablaConveniosAdmisiones').DataTable(); // accede de nuevo a la DataTable.
	          table.ajax.reload();
                }
            });
        });
/*------------------------------------------
        --------------------------------------------
        Delete Post Code
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePost",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');


		   $.ajax({
	           url: '/postDeleteConveniosAdmision/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			            var table = $('#tablaConveniosAdmisiones').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	           });
	});
});

function initTableConvenios(data) {
 
    return new DataTable('.tablaConveniosAdmisiones', {
          "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '130px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                       //   btn = btn + " <button   class='btn btn-primary editPostConvenios' data-pk='" + row.pk + "'>" + "</button>";
			  btn = btn + " <button class='btn btn-danger deletePost' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";

                        return btn;
                    },
                    "targets": 5
               }
            ],
            ajax: {
                 url:"/load_dataConvenioAdmisiones/" + data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.id"},
                { data: "fields.nombreDocumento"},
                { data: "fields.nombre"},
                { data: "fields.consec"},
                { data: "fields.convenio"},
            ]
    });

}

 function tableActions() {
   var table = initTableConvenios();

    // perform API operations with `table`
    // ...
}

$(document).on('click', '#Convenios', function(event) {
  // alert("pique en article Convenios");
});