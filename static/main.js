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

			document.getElementById("busServicio2").value = document.getElementById("bakbusServicio2").value;
             document.getElementById("busSubServicio2").value = document.getElementById("bakbusSubServicio2").value;
         //    document.getElementById("dependenciasIngreso").value = document.getElementById("bakdependenciasIngreso").value;
             document.getElementById("tipoDoc").value = document.getElementById("baktipoDoc").value;
             document.getElementById("busDocumentoSel").value = document.getElementById("bakbusDocumentoSel").value;
            // document.getElementById("fechaIngreso").value = document.getElementById("bakfechaIngreso");
            //  document.getElementById("fechaIngreso").value = '2024-01-01';
             var pase  = document.getElementById("bakbusServicio2").value;
             var pase1 = document.getElementById("bakbusSubServicio2").value;


      //      var  dependenciasIngreso = document.getElementById("bakdependenciasIngreso");
        //    var dxIngreso = document.getElementById("bakdxIngreso");
      //      var especialidadesMedicosIngreso = document.getElementById("bakespecialidadesMedicosIngreso");
     //       var  medicoIngreso = document.getElementById("bakmedicoIngreso");





                $('#mensaje1').html('<span> respuesta</span>');
                $('#usuariosModal').modal().hide();
			    // window.location.reload(document.getElementById("bakbusServicio2").value,document.getElementById("bakbusSubServicio2").value);
			     window.location.reload();

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};




function findOneUsuario1()
{

	var envios = new FormData();


   document.getElementById("baktipoDoc").value  = document.getElementById("tipoDoc").value;
   document.getElementById("bakbusDocumentoSel").value  = document.getElementById("busDocumentoSel").value;
   eldocu = document.getElementById("busDocumentoSel").value;
   alert( "Este es el nro del documento : " + eldocu);


   	var busDocumentoSel = document.getElementById("busDocumentoSel").value;
    alert("Documento = " +  eldocu);
    alert("OtorDocumento = " +  busDocumentoSel);



   document.getElementById("bakfechaIngreso").value  = document.getElementById("fechaIngreso");
   document.getElementById("bakbusServicio2").value  = document.getElementById("busServicio2").value;
   document.getElementById("bakbusSubServicio2").value  = document.getElementById("busSubServicio2").value;


 //   var bakdxIngreso = document.getElementById("dxIngreso").value;
  //  var bakespecialidadesMedicosIngreso = document.getElementById("especialidadesMedicosIngreso").value;
  //  var  bakdependenciasIngreso = document.getElementById("dependenciasIngreso").value;



 //   var  bakmedicoIngreso = document.getElementById("medicoIngreso").value;


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
      alert('Row Number: '+(rowIndex+1)+'\nColumn Number: '+(tdIndex+1));
      var celda = $(this);
      alert("valor celda = " + celda.html());
      let obtenerDato = document.getElementsByTagName("td");
      alert("valores son : " + obtenerDato.innerHTML + " ::::" + obtenerDato[0].innerHTML + " " + obtenerDato[1].innerHTML + " " + obtenerDato[2].innerHTML + " " + obtenerDato[3].innerHTML + " " + obtenerDato[4].innerHTML + " " + obtenerDato[5].innerHTML + " " + obtenerDato[6].innerHTML)
      alert ("Aquip los valores");

      alert ($(this).parents("tr").find("td").eq(0).html());
      alert ($(this).parents("tr").find("td").eq(1).html());
      alert ($(this).parents("tr").find("td").eq(2).html());
      alert ($(this).parents("tr").find("td").eq(3).html());
      alert ($(this).parents("tr").find("td").eq(4).html());
      alert ($(this).parents("tr").find("td").eq(5).html());
      alert ($(this).parents("tr").find("td").eq(6).html());
      alert ($(this).parents("tr").find("td").eq(7).html());
      alert ($(this).parents("tr").find("td").eq(8).html());
      alert ($(this).parents("tr").find("td").eq(9).html());
      alert ($(this).parents("tr").find("td").eq(10).html());

      //var tipoDoc =
      //var documento = document.getElementById("busDocumentoSel").value;
      //var documento=
      //var ingreso=
      //alert("tipoDoc =" + tipoDoc + "documento=" + documento +"ingreso= " + ingreso);


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
       var Serv = select.options[select .selectedIndex].value; /* Obtener el valor */
       var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'N'},
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




$(document).on('change', '#busServicio2', function(event) {



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


                     const $id2 = document.querySelector("#busSubServicio2");


 	      		     $("#busSubServicio2").empty();


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


$(document).on('change', '#busSubServicio2', function(event) {



       var select = document.getElementById("busServicio2"); /*Obtener el SELECT */
       var Serv = select.options[select .selectedIndex].value; /* Obtener el valor */
       var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#dependenciasIngreso");


 	      		     $("#dependenciasIngreso").empty();


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








