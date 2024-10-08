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
/*	tableActionsApoyoTerapeutico();  */
/*      initTableRasgos(data);   */


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
         var estado = document.getElementById("estado").value;
         var folio = document.getElementById("tipoExamenId").value;
         var interpretacion1 = document.getElementById("interpretacion1").value;
         var medicoInterpretacion1 = document.getElementById("medicoInterpretacion1").value;
         var interpretacion2 = document.getElementById("interpretacion2").value;
	 var medicoInterpretacion2 = document.getElementById("medicoInterpretacion2").value;
         var medicoReporte = document.getElementById("medicoReporte").value;
         var rutaImagen = document.getElementById("rutaImagen").value;
         var rutaVideo = document.getElementById("rutaVideo").value;



	$.ajax({
	           url: '/postConsultaApoyoTerapeutico/',
	            data : {post_id:post_id,
			   tipoExamenId:tipoExamenId,
			   tipoExamen:tipoExamen,
			   CupsId:CupsId,
			   nombreExamen:nombreExamen,
			   cantidad:cantidad,
                           observaciones:observaciones,
			   estado:estado,
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
                        alert("dataResultado1="  + data);
                     alert("dataResultado2="  + data[0]);
                      alert("dataResultado3="  + data[0]['ResultadoApoyoTerapeutico']); // este es el Registro
                      alert("dataResultado4="  + data[0]['ResultadoApoyoTerapeutico'][0]);
                       alert("dataResultado5="  + data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
                         alert("RasgosClinicos="  + data[1]['RasgosClinicos']);  // esye es el combo
                             alert("data[2] ="  + data[2]);  // esye es el combo

                            alert("data[2].MedicoInterpretacion1="  + data[2]['MedicoInterpretacion1'][1]['nombre']);  // esye es el combo
                               alert("MedicoInterpretacion2="  + data[3]['MedicoInterpretacion2'][1]['nombre']);  // esye es el combo
                                  alert("MedicoReporte="  + data[4]['MedicoReporte'][1]['nombre']);  // esye es el combo
                    //alert("MedicoReporte="  + data['MedicoReporte'].nombre');

                        alert("dataResultado6="  + data[1]['RasgosClinicos'][1]);
                        alert("dataResultado7="  + data[1]['RasgosClinicos'][1]['id']);
                        alert("dataResultado8="  + data[1]['RasgosClinicos'][1]['nombre']);



	  		  // var dato = JSON.parse(respuesta);
			 $('#pk').val(data.pk);
	       	        $('#tipoExamenId').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamenId);
        	       	$('#tipoExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].tipoExamen);
	                $('#CupsId').val(data[0]['ResultadoApoyoTerapeutico'][0].CupsId);
	                $('#nombreExamen').val(data[0]['ResultadoApoyoTerapeutico'][0].nombreExamen);
	                $('#cantidad').val(data[0]['ResultadoApoyoTerapeutico'][0].cantidad);
	                $('#observaciones').val(data[0]['ResultadoApoyoTerapeutico'][0].observaciones);
	                $('#estado').val(data[0]['ResultadoApoyoTerapeutico'][0].estado);
	                $('#folio').val(data[0]['ResultadoApoyoTerapeutico'][0].folio);
	                $('#interpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion1);
	                $('#medicoInterpretacion1').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion1);
	                $('#interpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].interpretacion2);
	                $('#medicoInterpretacion2').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoInterpretacion2);
	                $('#medicoReporte').val(data[0]['ResultadoApoyoTerapeutico'][0].medicoReporte);
	                $('#rutaImagen').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaImagen);
	                $('#rutaVideo').val(data[0]['ResultadoApoyoTerapeutico'][0].rutaVideo);

	               //  $('#rasgosClinicos').val(data[1]['RasgosClinicos']);
	                 $('#medicoInterpretacion1').val(data[2]['MedicoInterpretacion1']);
	                 $('#medicoInterpretacion2').val(data[3]['MedicoInterpretacion2']);
	                 $('#medicoReporte').val(data[4]['MedicoReporte']);

           	  		   var options = '<option value="=================="></option>';
	  		          var dato = JSON.parse(data[1]['RasgosClinicos']);
	  		            alert("dato = " + dato);


                     const $id2 = document.querySelector("#rasgosClinicos");
 	      		     $("#rasgosClinicos").empty();

	                 $.each(data[1]['RasgosClinicos'], function(key,value) {
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

// Esta Afuera  del documento.ready

/*------------------------------------------
        --------------------------------------------
        Delete Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostRasgos",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');


		   $.ajax({
	           url: '/postDeleteExamenesRasgos/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			            var table = $('#tablaRasgos').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	           });
	});





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
			btn = btn + " <button class='btn btn-danger deleteRasgos' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";
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
              
                { data: "fields.id"},
                { data: "fields.codigoCups"},
                { data: "fields.nombreRasgo"},
                { data: "fields.unidad"},
                { data: "fields.minimo"},
                { data: "fields.maximo"},
                { data: "fields.valorResultado"},
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

