

    $(document).ready(function() {
    var $ = jQuery;
    console.log('Hola Alberto Hi!')

	var sede = document.getElementById("sede").value;
        var username_id = document.getElementById("username_id").value;
	var tipoDoc_id = document.getElementById("tipoDoc_id").value;
	var documentoPaciente = document.getElementById("documentoPaciente").value;
	var IngresoPaciente = document.getElementById("IngresoPaciente").value;

        var data =  {}   ;

        data['sede'] = sede;
        data['username_id'] = username_id;
        data['tipoDoc_id'] = tipoDoc_id;
        data['documentoPaciente'] = documentoPaciente;
        data['IngresoPaciente'] = IngresoPaciente;

        data = JSON.stringify(data);


	tableActionsLaboratorios();

	    /*------------------------------------------
        --------------------------------------------
        Click to Button
        --------------------------------------------
        --------------------------------------------*/
        $('#createNewPostLaboratorios').click(function () {

	    //var ingresoId= document.getElementById("ingresoId1").value;
	    //document.getElementById("ingresoId2").value = ingresoId;

            $('#saveBtnCrearLaboratorios').val("Create Post");
            $('#post_id').val('');
            $('#postFormCrearLaboratorios').trigger("reset");
            $('#modelHeadingLaboratorios').html("Creacion Laboratorios");
            $('#crearLaboratoriosModel').modal('show');
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
        $('#saveBtnCrearLaboratorio').click(function (e) {
            e.preventDefault();
            $(this).html('Sending..');
	        $('#crearLaboratoriosModel').modal('hide');
            $('.success-msg').css('display','block');
            $('.success-msg').text('Dato actualizado');
   	   var table = $('#tablaLaboratorios').DataTable();   // accede de nuevo a la DataTable.

   	   var TipoDocPaciente = document.getElementById("TipoDocPaciente").value;
	   var documentoPaciente = document.getElementById("documentoPaciente").value;
	   var IngresoPaciente = document.getElementById("IngresoPaciente").value;
	   var tiposExamen_Id  = document.getElementById("tiposExamen_Id").value;
	   var cantidad = document.getElementById("cantidad").value;

 	       var select = document.getElementById("laboratorios"); /*Obtener el SELECT */
      	   var laboratorios = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

            var x = document.createElement("INPUT");
            x.setAttribute("type", "radio");
            x.setAttribute("id", "laboratorioId");
            t = document.body.appendChild(x);

	table.row
        .add([
            laboratorios, text,  cantidad, ""
        ])
        .draw(false);

    
        });
	/*------------------------------------------
        --------------------------------------------
        Delete Post Code
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostLaboratorio",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');


		   $.ajax({
	           url: '/postDeleteLaboratorios/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			            var table = $('#tablaLaboratorios').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	           });
	});



});  // Aquip fin del document.ready


function tableActionsLaboratorios() {

   // var table = $('#tablaLaboratorios').DataTable();
  //  const table = new DataTable('#tablaLaboratorios');

   var table= $('#tablaLaboratorios').DataTable({
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 4
            ]
    });

}

formHistoriaClinica.addEventListener('submit', e=>{


         alert("Entre Form formHistoriaClinica");
        e.preventDefault()
        // Ah peros si se puede solo hay que recorrer y yap

        const table = $('#tablaLaboratorios').DataTable();
        var datos_tabla = table.rows().data().toArray();
        alert("datos_tabla = " + datos_tabla);  // Este si funcionap
        alert("datos_tabla json = " +  JSON.stringify(datos_tabla));
        alert("datos_tabla json = " +  JSON.stringify(datos_tabla[0]));
        alert("datos_tabla json1 = " +  JSON.stringify(datos_tabla[1]));
        alert("datos_tabla json2 = " +  JSON.stringify(datos_tabla[2]));
        alert("datos_tabla json1 = " +  JSON.stringify(datos_tabla[1][0]));
        alert("datos_tabla json1 = " +  JSON.stringify(datos_tabla[1][1]));
        alert("datos_tabla json1 = " +  JSON.stringify(datos_tabla[1][2]));






         var tipoDoc    =  document.getElementById("tipoDocPaciente").value
         var documento      =  document.getElementById("documentoPaciente").value;
         var folio  = "0";
         var fecha          =  document.getElementById("fecha").value;
         var motivo =          document.getElementById("id_motivo").value;
         var subjetivo =      document.getElementById("id_subjetivo").value;
         var objetivo =       document.getElementById("id_objetivo").value;
         var analisis =        document.getElementById("id_analisis").value;
        // var plan =           document.getElementById("id_plan").value;
         var causasExterna = document.getElementById("causasExterna").value;
         var dependenciasRealizado = document.getElementById("dependenciasRealizado").value;
         var usuarioRegistro = document.getElementById("usuarioRegistro").value;
         var consecAdmision=document.getElementById("IngresoPaciente").value;
         var tiposfolio = 0;
             // Medico Verificar
             if (perfil == 1)
                {
                document.getElementById("tiposFolio").value=1;
                }
                // Enfermeria Verificar
             if (perfil == 2)
                {
                document.getElementById("tiposFolio").value=2;
                }

             var tiposFolio = document.getElementById("tiposFolio").value;
             alert("tiposFolio =" + tiposFolio);
             var profesional = document.getElementById("profesional").value;
             alert("Profesional = ", profesional);
             var espMedico = document.getElementById("espMedico").value;
             var planta = document.getElementById("Username_id").value;
             var fechaRegistro = document.getElementById("fechaRegistro").value;
             var estadoReg = "A"
            // var diagnosticos = document.getElementById("diagnosticos").value;


             envio1.append('tipoDoc', tipoDoc );
             envio1.append( 'documento', documento);
             envio1.append( 'consecAdmision', consecAdmision);
             envio1.append('folio', folio);
             envio1.append('fecha', fecha);
             envio1.append('tiposFolio', tiposFolio);
             envio1.append('profesional', profesional);
             envio1.append('causasExterna', causasExterna);
             envio1.append('dependenciasRealizado', dependenciasRealizado);
             envio1.append('espMedico', espMedico);
             envio1.append('planta', planta);
             envio1.append('motivo' , motivo);
             envio1.append('subjetivo' , subjetivo);
             envio1.append('objetivo' , objetivo);
             envio1.append('analisis' , analisis);
             //envio1.append('plan' , plan);
             envio1.append('fechaRegistro' , fechaRegistro);
             envio1.append('usuarioRegistro' , usuarioRegistro);
             envio1.append('estadoReg' , estadoReg);
             // envio1.append('diagnosticos' , diagnosticos);

             // El serialize de la tabla de laboratorios ASI :

             // var table = $('#tablaLaboratorios').DataTable();
             // var sData = table.$('input').serialize();
		     alert( "The following data would have been submitted to the server: \n\n"+table );


             envio1.append('laboratorios' , laboratorios);
             enviot=[]
             enviot['envio1'] = envio1;

             envio2 = JSON.stringify(enviot);

            alert("Acabo de serializar los Laboratorios y voy AJAX con esta data: ", envio2);
            alert("Acabo de serializar los Laboratorios y voy AJAX con esta data: ", enviot);

            var form_valido;

               $.ajax({
            	   type: 'POST',
 	               url: '/crearHistoriaClinica/',
  	               data: envio2,
 	      		success: function (respuesta2) {
 	      		       // var data = JSON.parse(respuesta2);
 	      		        alert("con stringy = " + JSON.stringify(respuesta2))
 	      		        // alert(data['Tipo']);
 	      		        //alert(data['Mensaje']);

 	      		         if (respuesta2['valido'] == true) {
                               form_valido = true;
                        } else {
                            form_valido = false;
                        }

 	      		        alert(respuesta2.Tipo);
 	      		        alert(respuesta2.Mensaje);

 	      		        if (respuesta2.Tipo != '"Error')
 	      		         {
 	      		        document.getElementById("id_motivo").value = "";
                        document.getElementById("id_subjetivo").value = "";
                        document.getElementById("id_objetivo").value = "";
                        document.getElementById("id_analisis").value = "";
                        document.getElementById("id_plan").value = "";
                        document.getElementById("causasExterna").value = "";
                        document.getElementById("dependenciasRealizado").value = "";
                        document.getElementById("diagnosticos").value = "";

                         const $id2 = document.querySelector("#id_id_medico");

 	      		         //  $("#laboratorios1").empty();
 	      		         //  $("#radiologias1").empty();
 	      		        //   $("#terapias").empty();
 	      		          // $("#tiposAntecedente").empty();
                            //$("#antecedente").empty();
                        //$("#tiposDiagnostico").empty();
                            //$("#diagnostico").empty();
 	      		        }

 	      	 			$("#mensajes").html(respuesta2.Mensaje);


 	      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	        });

 	        if (form_valido) {
                return true;
            }


})
