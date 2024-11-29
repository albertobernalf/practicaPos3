var $ = jQuery;
console.log('Hola Alberto Hi!')

$('.editPostar').on('click',function(event)
{
 	 alert("Entre a editPostt"); 
	 var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));
});

    $(document).ready(function() {

        var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
        var username = document.getElementById("username").value;
        var nombreSede = document.getElementById("nombreSede").value;
    	var sede = document.getElementById("sede").value;
        var username_id = document.getElementById("username_id").value;

        var data =  {}   ;

        data['username'] = username;
        data['sedeSeleccionada'] = sedeSeleccionada;
        data['nombreSede'] = nombreSede;
        data['sede'] = sede;
	data['username_id'] = username_id;
        

        data = JSON.stringify(data);

	initTableApoyoTerapeutico(data);
	initTableTerapeuticoConsulta(data);
	initTableRasgos(data); 

	/*------------------------------------------
        --------------------------------------------
        Delete Post Code Rasgos
        --------------------------------------------
        --------------------------------------------*/

        $("body").on("click",".deletePostRasgos",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');

       var data =  {}   ;

		 data['username'] = username;
        	 data['sedeSeleccionada'] = sedeSeleccionada;
	         data['nombreSede'] = nombreSede;
	         data['sede'] = sede;
		 data['username_id'] = username_id;
	         data['valor'] = examId;

		  data = JSON.stringify(data);


		   $.ajax({
	           url: '/postDeleteExamenesRasgos/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
	  		    alert("vengo de borrar");

	                     tableR= $("#tablaRasgos").dataTable().fnDestroy();

        		   initTableRasgos(data);
	
		  $("#mensajes").html(" ! Registro Borrado !");
	

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





   });  // Aquip fin del document.ready





function initTableRasgos(data) {

	return new DataTable('.tablaRasgos', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '360px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
			btn = btn + " <button class='btn btn-danger deletePostRasgos' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 7
               }
            ],
            ajax: {
                 url:"/load_dataRasgos/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [


                { data: "fields.codigoCups"},
                { data: "fields.nombreRasgo"},
                { data: "fields.unidad"},
                { data: "fields.minimo"},
                { data: "fields.maximo"},
                { data: "fields.valorResultado"},
		{ data: "fields.observa"},
            ]
 });

}



function initTableRasgosConsulta(data) {

	return new DataTable('.tablaRasgosConsulta', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '360px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
		//	 btn = btn + " <button class='btn btn-danger deletePostRasgos' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 6
               }
            ],
            ajax: {
                 url:"/load_dataRasgosConsulta/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [


                { data: "fields.codigoCups"},
                { data: "fields.nombreRasgo"},
                { data: "fields.unidad"},
                { data: "fields.minimo"},
                { data: "fields.maximo"},
                { data: "fields.valorResultado"},
		        { data: "fields.observa"},
            ]
 });

}



	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostApoyoTerapeutico', function () {
          alert ("Entre boton Apoyo Terapeutico");
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

         var tipoExamenId = document.getElementById("tipoExamenId").value;
         var tipoExamen = document.getElementById("tipoExamen").value;
         var CupsId = document.getElementById("CupsId").value;
         var nombreExamen = document.getElementById("nombreExamen").value;
         var cantidad = document.getElementById("cantidad").value;
	 var observaciones = document.getElementById("observaciones").value;
         var estadoExamen = document.getElementById("estadoExamen").value;
         var folio = document.getElementById("tipoExamenId").value;
         var interpretacion1 = document.getElementById("interpretacion1").value;
         var medicoInterpretacion1 = document.getElementById("medicoInterpretacion1").value;
         var interpretacion2 = document.getElementById("interpretacion2").value;
	 var medicoInterpretacion2 = document.getElementById("medicoInterpretacion2").value;
         var medicoReporte = document.getElementById("medicoReporte").value;
         var rutaImagen = document.getElementById("rutaImagen").value;
         var rutaVideo = document.getElementById("rutaVideo").value;
         var username_id = document.getElementById("username_id").value;	

        var data =  {}   ;

	 data['username'] = username;
         data['sedeSeleccionada'] = sedeSeleccionada;
         data['nombreSede'] = nombreSede;
         data['sede'] = sede;
	 data['username_id'] = username_id;
         data['valor'] = post_id;	

	  data = JSON.stringify(data);

          tableR= $("#tablaRasgos").dataTable().fnDestroy();
	alert("username_id ASI VA " + username_id );

           initTableRasgos(data);



	$.ajax({
	           url: '/postConsultaApoyoTerapeutico/',
	            data : {post_id:post_id,
			   tipoExamenId:tipoExamenId,
			   tipoExamen:tipoExamen,
			   CupsId:CupsId,
			   nombreExamen:nombreExamen,
			   cantidad:cantidad,
                           observaciones:observaciones,
			   estadoExamen:estadoExamen,
			   folio:folio,
			   interpretacion1:interpretacion1,
			   medicoInterpretacion1:medicoInterpretacion1,
			   interpretacion2:interpretacion2,
			   medicoInterpretacion2:medicoInterpretacion2,
                           medicoReporte:medicoReporte,
   			   rutaImagen:rutaImagen,
			   rutaVideo:rutaVideo
},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");

                      alert("dataResultado3="  + data[0]['ResultadoApoyoTerapeutico']); // este es el Registro
                       alert("dataResultado5="  + data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
                         alert("RasgosClinicos="  + data[1]['RasgosClinicos']);  // esye es el combo

                            alert("data[2].MedicoInterpretacion1="  + data[2]['MedicoInterpretacion1'][1]['nombre']);  // esye es el combo
                               alert("MedicoInterpretacion2="  + data[3]['MedicoInterpretacion2'][1]['nombre']);  // esye es el combo
                                  alert("MedicoReporte="  + data[4]['MedicoReporte'][1]['nombre']);  // esye es el combo
			alert("dependenciasRealizado1 = " + data[0]['ResultadoApoyoTerapeutico'][0]);
			alert("dependenciasRealizado2 = " + data[0]['ResultadoApoyoTerapeutico'][0].dependencias);
			

	  		  // var dato = JSON.parse(respuesta);
			 $('#pk').val(data.pk);
	       	        $('#tipoExamenId').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
        	       	$('#tipoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamen);
	                $('#CupsId').val(data[0]['ResultadoApoyoTerapeutico'][0].CupsId);
	                $('#nombreExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].nombreExamen);
	                $('#cantidad').val(data[0]['ResultadoApoyoTerapeutico'][0].cantidad);
	                $('#observaciones').val(data[0]['ResultadoApoyoTerapeutico'][0].observaciones);
	                $('#estadoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].estado);
	                $('#folio').val(data[0]['ResultadoApoyoTerapeutico'][0].folio);
	                $('#interpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion1);
	                $('#medicoInterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion1);
	                $('#interpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion2);
	                $('#medicoInterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion2);
	                $('#medicoReporte').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoReporte);
	                $('#rutaImagen').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaImagen);
	                $('#rutaVideo').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaVideo);
			

			 $('#ingresoIdA').val(data[4]['MedicoReporte']);
			 $('#examId').val(data[0]['ResultadoApoyoTerapeutico'][0].examId);
			

           	  		   var options = '<option value="=================="></option>';


                     const $id2 = document.querySelector("#rasgosClinicos");
 	      		     $("#rasgosClinicos").empty();

	                 $.each(data[1]['RasgosClinicos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });


                     const $id3 = document.querySelector("#medicoInterpretacion1");
 	      		     $("#medicoInterpretacion1").empty();

	                 $.each(data[2]['MedicoInterpretacion1'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id3.appendChild(option);
 	      		      });



                     const $id4 = document.querySelector("#medicoInterpretacion2");
 	      		     $("#medicoInterpretacion2").empty();

	                 $.each(data[3]['MedicoInterpretacion2'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4.appendChild(option);
 	      		      });



                     const $id5 = document.querySelector("#medicoReporte");
 	      		     $("#medicoReporte").empty();

	                 $.each(data[4]['MedicoReporte'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id5.appendChild(option);
 	      		      });



                     const $id6 = document.querySelector("#dependenciasRealizado");
 	      		     $("#dependenciasRealizado").empty();

	                 $.each(data[5]['DependenciasRealizado'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id6.appendChild(option);
 	      		      });

	         const $id7 = document.querySelector("#estadoExamen");
 	      		     $("#estadoExamen").empty();

	                 $.each(data[6]['EstadosExamenes'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id7.appendChild(option);
 	      		      });


			
	                 $('#medicoInterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion1);
	                 $('#medicoInterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion2);
	                 $('#medicoReporte').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoReporte);
			  $('#dependenciasRealizado').val(data[0]['ResultadoApoyoTerapeutico'][0].dependencias);
 			 $('#estadoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].estado);








                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });


/*** DESDE AQUI CONSULTA DE RESPUESTAS ***/


	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostTerapeuticoConsulta', function () {
          alert ("Entre boton Apoyo Terapeutico Consulta");
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

         var tipoExamenId = document.getElementById("ztipoExamenId").value;
         var tipoExamen = document.getElementById("ztipoExamen").value;
         var CupsId = document.getElementById("zCupsId").value;
         var nombreExamen = document.getElementById("znombreExamen").value;
         var cantidad = document.getElementById("zcantidad").value;
	 var observaciones = document.getElementById("zobservaciones").value;
         var estadoExamen = document.getElementById("zestadoExamen").value;
         var folio = document.getElementById("ztipoExamenId").value;
         var interpretacion1 = document.getElementById("zinterpretacion1").value;
         var medicoInterpretacion1 = document.getElementById("zmedicoInterpretacion1").value;
         var interpretacion2 = document.getElementById("zinterpretacion2").value;
	 var medicoInterpretacion2 = document.getElementById("zmedicoInterpretacion2").value;
         var medicoReporte = document.getElementById("zmedicoReporte").value;
         var rutaImagen = document.getElementById("zrutaImagen").value;
         var rutaVideo = document.getElementById("zrutaVideo").value;
         var username_id = document.getElementById("username_id").value;

        var data =  {}   ;

	 data['username'] = username;
         data['sedeSeleccionada'] = sedeSeleccionada;
         data['nombreSede'] = nombreSede;
         data['sede'] = sede;
	 data['username_id'] = username_id;
         data['valor'] = post_id;	

	  data = JSON.stringify(data);

          tableR= $("#tablaRasgosConsulta").dataTable().fnDestroy();
	alert("username_id ASI VA " + username_id );

           initTableRasgosConsulta(data);



	$.ajax({
	           url: '/postConsultaApoyoTerapeuticoConsulta/',
	            data : {post_id:post_id,
			   tipoExamenId:tipoExamenId,
			   tipoExamen:tipoExamen,
			   CupsId:CupsId,
			   nombreExamen:nombreExamen,
			   cantidad:cantidad,
                           observaciones:observaciones,
			   estadoExamen:estadoExamen,
			   folio:folio,
			   interpretacion1:interpretacion1,
			   medicoInterpretacion1:medicoInterpretacion1,
			   interpretacion2:interpretacion2,
			   medicoInterpretacion2:medicoInterpretacion2,
                           medicoReporte:medicoReporte,
   			   rutaImagen:rutaImagen,
			   rutaVideo:rutaVideo
},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");

                      alert("dataResultado3="  + data[0]['ResultadoApoyoTerapeutico']); // este es el Registro
                       alert("dataResultado5="  + data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
                         alert("RasgosClinicos="  + data[1]['RasgosClinicos']);  // esye es el combo

                            alert("data[2].MedicoInterpretacion1="  + data[2]['MedicoInterpretacion1'][1]['nombre']);  // esye es el combo
                               alert("MedicoInterpretacion2="  + data[3]['MedicoInterpretacion2'][1]['nombre']);  // esye es el combo
                                  alert("MedicoReporte="  + data[4]['MedicoReporte'][1]['nombre']);  // esye es el combo
			alert("dependenciasRealizado1 = " + data[0]['ResultadoApoyoTerapeutico'][0]);
			alert("dependenciasRealizado2 = " + data[0]['ResultadoApoyoTerapeutico'][0].dependencias);
			

	  		  // var dato = JSON.parse(respuesta);
			 $('#pk').val(data.pk);
	       	        $('#ztipoExamenId').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
        	       	$('#ztipoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamen);
	                $('#zCupsId').val(data[0]['ResultadoApoyoTerapeutico'][0].CupsId);
	                $('#znombreExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].nombreExamen);
	                $('#zcantidad').val(data[0]['ResultadoApoyoTerapeutico'][0].cantidad);
	                $('#zobservaciones').val(data[0]['ResultadoApoyoTerapeutico'][0].observaciones);
	                $('#zestadoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].estado);
	                $('#zfolio').val(data[0]['ResultadoApoyoTerapeutico'][0].folio);
	                $('#zinterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion1);
	                $('#zmedicoInterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion1);
	                $('#zinterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion2);
	                $('#zmedicoInterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion2);
	                $('#zmedicoReporte').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoReporte);
	                $('#zrutaImagen').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaImagen);
	                $('#zrutaVideo').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaVideo);
			

			 $('#zingresoIdA').val(data[4]['MedicoReporte']);
			 $('#zexamId').val(data[0]['ResultadoApoyoTerapeutico'][0].examId);
			

           	  		   var options = '<option value="=================="></option>';


                     const $id2 = document.querySelector("#zrasgosClinicos");
 	      		     $("#zrasgosClinicos").empty();

	                 $.each(data[1]['RasgosClinicos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });


                     const $id3 = document.querySelector("#zmedicoInterpretacion1");
 	      		     $("#zmedicoInterpretacion1").empty();

	                 $.each(data[2]['MedicoInterpretacion1'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id3.appendChild(option);
 	      		      });



                     const $id4 = document.querySelector("#zmedicoInterpretacion2");
 	      		     $("#zmedicoInterpretacion2").empty();

	                 $.each(data[3]['MedicoInterpretacion2'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4.appendChild(option);
 	      		      });



                     const $id5 = document.querySelector("#zmedicoReporte");
 	      		     $("#zmedicoReporte").empty();

	                 $.each(data[4]['MedicoReporte'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id5.appendChild(option);
 	      		      });



                     const $id6 = document.querySelector("#zdependenciasRealizado");
 	      		     $("#zdependenciasRealizado").empty();

	                 $.each(data[5]['DependenciasRealizado'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id6.appendChild(option);
 	      		      });

	         const $id7 = document.querySelector("#zestadoExamen");
 	      		     $("#zestadoExamen").empty();

	                 $.each(data[6]['EstadosExamenes'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id7.appendChild(option);
 	      		      });


			
	                 $('#zmedicoInterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion1);
	                 $('#zmedicoInterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion2);
	                 $('#zmedicoReporte').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoReporte);
			  $('#zdependenciasRealizado').val(data[0]['ResultadoApoyoTerapeutico'][0].dependencias);
 			 $('#zestadoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].estado);








                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });





/**** HASTA AQUI  ***/




    	/*------------------------------------------
        --------------------------------------------
        Click to Button
        --------------------------------------------
        --------------------------------------------*/
        $('#createNewResultadoRasgo').click(function () {

 	alert("Entre a crear un rasgo");
 
	  var valor = document.getElementById("valor").value;
	  var observa = document.getElementById("observa").value;
	  var rasgo = document.getElementById("rasgosClinicos").value;
	  var selectRasgo = document.getElementById("rasgo"); 
	  var examId = document.getElementById("examId").value;

	 $.ajax({
	           url: '/guardarResultadoRasgo/',
	            data : {
			'examId':examId,
  			'rasgo':rasgo,
			'valor':valor,
                        'observa':observa
			},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                        alert("respuesta="  + data);

	                  $("#mensajes").html(" ! Registro Creado !");


                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

		
	        var data =  {}   ;

		 data['username'] = username;
        	 data['sedeSeleccionada'] = sedeSeleccionada;
	         data['nombreSede'] = nombreSede;
	         data['sede'] = sede;
		 data['username_id'] = username_id;
	         data['valor'] = examId;	

		  data = JSON.stringify(data);

	          tableR= $("#tablaRasgos").dataTable().fnDestroy();
		alert("username_id ASI VA " + username_id );
	           initTableRasgos(data);
	           $("#mensajes").html(" ! Registro Guardado !");
  		
        });





// Esta Afuera  del documento.ready




function initTableApoyoTerapeutico(data) {

	return new DataTable('.tablaApoyoTerapeutico', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '360px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                      //    btn = btn + " <button   class='btn btn-primary editPost' data-pk='" + row.pk + "'>" + "</button>";
                         btn = btn + " <input type='radio'  class='form-check-input editPostApoyoTerapeutico' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 11
               }
            ],
            ajax: {
                 url:"/load_dataApoyoTerapeutico/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
              
                { data: "fields.id"},
                { data: "fields.tipoDoc"},
                { data: "fields.documento"},
                { data: "fields.nombre"},
                { data: "fields.consec"},
                { data: "fields.fechaExamen"},
                { data: "fields.tipoExamen"},
	            { data: "fields.examen"},
                { data: "fields.estadoExamen"},
                { data: "fields.cantidad"},
                { data: "fields.folio"},

            ]
 });

}


function initTableTerapeuticoConsulta(data) {

	return new DataTable('.tablaTerapeuticoConsulta', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '360px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                      //    btn = btn + " <button   class='btn btn-primary editPost' data-pk='" + row.pk + "'>" + "</button>";
                         btn = btn + " <input type='radio'  class='form-check-input editPostTerapeuticoConsulta' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 11
               }
            ],
            ajax: {
                 url:"/load_dataTerapeuticoConsulta/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
              
                { data: "fields.id"},
                { data: "fields.tipoDoc"},
                { data: "fields.documento"},
                { data: "fields.nombre"},
                { data: "fields.consec"},
                { data: "fields.fechaExamen"},
                { data: "fields.tipoExamen"},
	            { data: "fields.examen"},
                { data: "fields.estadoExamen"},
                { data: "fields.cantidad"},
                { data: "fields.folio"},

            ]
 });

}



function tableActionsApoyoTerapeutico() {
   var table = initTableApoyoTerapeutico();

    // perform API operations with `table`
    // ...
}

function tableActionsRasgos() {
   var tableR = initTableRasgos();

    // perform API operations with `table`
    // ...
}


$('#tablaApoyoTerapeutico tbody').on('click', 'tr', function () {
    // var data = table.row( this ).data();
    // alert( 'You clicked on '+data[0]+'\'s row' );
} );



function clickEvent() {
  var $ = jQuery;
  console.log("Acabo de entrar en clickEvent");

  // $('input[name="ingresoId"]').prop('checked', true);
  // var valor = $('input[name="ingresoId"]:checked').val();

   var sede = document.getElementById("sede").value;
   table = $("#tablaRasgos").dataTable().fnDestroy();
   initTableRasgos(data);

   $.ajax({
	type : 'POST',
        url  : '//',
        data : {'valor' : valor, 'sede':sede},
        success: function(cambioRasgos) {
             alert("llegue cambio rasgos");
	},
  error: function (request, status, error) {
	   	    	}
         })

}

function guardarResultado() {
          alert ("Entre GUARDAR resultado");
	 var tipoExamenId = document.getElementById("tipoExamenId").value;
         var tipoExamen = document.getElementById("tipoExamen").value;
         var examId = document.getElementById("examId").value;
	 var observaciones = document.getElementById("observaciones").value;
         var interpretacion1 = document.getElementById("interpretacion1").value;
         var medicoInterpretacion1 = document.getElementById("medicoInterpretacion1").value;
         var interpretacion2 = document.getElementById("interpretacion2").value;
	 var medicoInterpretacion2 = document.getElementById("medicoInterpretacion2").value;
         var medicoReporte = document.getElementById("medicoReporte").value;
         var rutaImagen = document.getElementById("rutaImagen").value;
         var rutaVideo = document.getElementById("rutaVideo").value;
	 var dependenciasRealizado = document.getElementById("dependenciasRealizado").value;
	 var username_id = document.getElementById("username_id").value;	
	 var estadoExamen = document.getElementById("estadoExamen").value;


	 $.ajax({
	           url: '/guardarResultado/',
	            data : {
			examId:examId,
  			observaciones:observaciones,
			interpretacion1:interpretacion1,
                        medicoInterpretacion1:medicoInterpretacion1,
			interpretacion2:interpretacion2,
                        medicoInterpretacion2:medicoInterpretacion2,
			medicoReporte:medicoReporte,
                        rutaImagen:rutaImagen,
			rutaVideo:rutaVideo,
			dependenciasRealizado:dependenciasRealizado,
                        usuarioToma: username_id ,
			estadoExamen:estadoExamen
			},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                        alert("respuesta="  + data);

	               // $('#mensajes').val('! Registro Actualizado !');
			  $("#mensajes").html(" ! Registro Actualizado !");
			  window.location.reload();
			  $("#mensajes").html(" ! Registro Actualizado !");

                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

}