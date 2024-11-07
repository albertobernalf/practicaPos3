var $ = jQuery;
console.log('Hola Alberto Hi!')


$(document).ready(function () {

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
        valor=1
        data['valor'] = valor;

        data = JSON.stringify(data);

		
	initTableLiquidacion(data);
	initTableLiquidacionDetalle(data);
        initTableAbonos(data);
//	tableActionsLiquidacion();


	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostLiquidacion', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));
        var username_id = document.getElementById("username_id").value;


	$.ajax({
	           url: '/postConsultaLiquidacion/',
	            data : {post_id:post_id, username_id:username_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);

			// Colocar Encabezadao
	  		// aqui debe activar un dataTale para liquidacionDetalle
		$('#liquidacionId').val(data.id);
		$('#fecha').val(data.fecha);
		$('#tipoDoc_id').val(data.tipoDoc_id);
		$('#documento_id').val(data.documento_id);
		$('#tipoDoc').val(data.tiposNombre);
		$('#documento').val(data.docPaciente);
		$('#paciente').val(data.paciente);
		$('#consecAdmision').val(data.consecAdmision);
		$('#nombreConvenio').val(data.nombreConvenio);
		$('#convenioId').val(data.convenioId);
		$('#observaciones').val(data.observaciones);

         

			// Colocar Totales

		$('#totalCopagos').val(data.totalCopagos);
		$('#totalCuotaModeradora').val(data.totalCuotaModeradora);
		$('#totalProcedimientos').val(data.totalProcedimientos);
		$('#totalSuministros').val(data.totalSuministros);
		$('#totalLiquidacion').val(data.totalLiquidacion);
		$('#valorApagar').val(data.valorApagar);
		$('#anticipos').val(data.anticipos);



      		 alert("Regrese");


			// Colocar Totales liquidacioon
	  		// aqui debe activar un dataTale para liquidacionDetalle

		$('#totalCopagos').val(data.totalCopagos);
		$('#totalCuotaModeradora').val(data.totalCuotaModeradora);
		$('#totalProcedimientos').val(data.totalProcedimientos);
		$('#totalSuministros').val(data.totalSuministros);
		$('#totalLiquidacion').val(data.totalLiquidacion);
		$('#valorApagar').val(data.valorApagar);
		$('#anticipos').val(data.anticipos);
		$('#totalAbonos').val(data.totalAbonos);


	     var options = '<option value="=================="></option>';

		    const $id51 = document.querySelector("#lcups");


 	      		     $("#lcups").empty();

	                 $.each(data['Cups'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id51.appendChild(option);
 	      		      });


                     const $id425 = document.querySelector("#lsum");


 	      		     $("#lsum").empty();

	                 $.each(data['Suministros'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id425.appendChild(option);
 	      		      });


                     const $id430 = document.querySelector("#tipoPago");


 	      		     $("#tipoPago").empty();

	                 $.each(data['TiposPagos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id430.appendChild(option);
 	      		      });


                     const $id437 = document.querySelector("#formaPago");


 	      		     $("#formaPago").empty();

	                 $.each(data['FormasPagos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id437.appendChild(option);
 	      		      });




			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("liquidacionId").value;

		        data2['valor'] = valor;	
		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	           initTableLiquidacionDetalle(data2);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });


	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostLiquidacionDetalle', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	$.ajax({
	           url: '/postConsultaLiquidacionDetalle/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);

			// Colocar datos en Ventana Modal
	  		// Nop esto debe abrir una ventana Modal

			 $('#pk').val(data.pk);
	       	        $('#ldconsecutivo').val(data.consecutivo);
	       	        $('#ldcantidad').val(data.cantidad);
	       	        $('#ldvalorUnitario').val(data.valorUnitario);
	       	        $('#ldvalorTotal').val(data.valorTotal);
	       	        $('#ldobservaciones').val(data.observaciones);
	       	        $('#ldtipoRegistro').val(data.tipoRegistro);




	     var options = '<option value="=================="></option>';

		    const $id511 = document.querySelector("#ldcups");


 	      		     $("#ldcups").empty();

	                 $.each(data['Cups'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id511.appendChild(option);
 	      		      });


                     const $id4256 = document.querySelector("#ldsum");


 	      		     $("#ldsum").empty();

	                 $.each(data['Suministros'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4256.appendChild(option);
 	      		      });





            $('#postFormLiquidacionDetalle').trigger("reset");
            $('#modelHeadingLiquidacionDetalle').html("Edicion Liquidacion");
            $('#crearModelLiquidacionDetalle').modal('show');


                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });


    	/*------------------------------------------
        --------------------------------------------
        Click to Button
        --------------------------------------------
        --------------------------------------------*/
        $('#createNewPostAbonosFacturacion').click(function () {

	  /*  var ingresoId= document.getElementById("ingresoId1").value;
	    document.getElementById("ingresoId2").value = ingresoId; */

            $('#saveBtnCrearAbonosFacturacion').val("Create Post");
            $('#post_id').val('');
            $('#postFormCrearAbonosFacturacion').trigger("reset");
            $('#modelHeading').html("Creacion Abonos en admision");
            $('#crearAbonosModelFacturacion').modal('show');
        });

       /*------------------------------------------
        --------------------------------------------
        Create Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $('#saveBtnCrearAbonosFacturacion').click(function (e) {
            e.preventDefault();
            $(this).html('Sending..');

            $.ajax({
                data: $('#postFormCrearAbonosFacturacion').serialize(),

		  url: "/guardaAbonosFacturacion/",
                type: "POST",
                dataType: 'json',
                success: function (data) {
			printErrorMsg(data.error)
                    if ($.isEmptyObject(data.error)) {

                        //  $("input[name='description']").val('');
                        $('#crearAbonosModelFacturacion').modal('hide');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
                    }else{
                        printErrorMsg(data.error)
                    }
                    $('#postFormCrearAbonosFacturacion').trigger("reset");
	 	  var tableA = $('#tablaAbonosFacturacion').DataTable(); // accede de nuevo a la DataTable.
	 	  var tableL = $('#tablaLiquidacionDetalle').DataTable(); // accede de nuevo a la DataTable.
	          tableA.ajax.reload();
	          tableL.ajax.reload();

                },
                error: function (data) {
			alert("VENGO CON ERRORES :" , printErrorMsg(data.error));
                   // $('#saveBtnCrearAbonos').html('NOT Save Changes');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.error);

		  var tableA = $('#tablaAbonosFacturacion').DataTable(); // accede de nuevo a la DataTable.
	          tableA.ajax.reload();
                }
            });
        });




       /*------------------------------------------
        --------------------------------------------
        Create Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $('#saveBtnCrearLiquidacionDetalle').click(function (e) {
            e.preventDefault();
            $(this).html('Sending..');

            $.ajax({
                data: $('#postFormLiquidacionDetalle').serialize(),

		  url: "/editarGuardarLiquidacionDetalle/",
                type: "POST",
                dataType: 'json',
                success: function (data) {
			printErrorMsg(data.error)
                    if ($.isEmptyObject(data.error)) {

                        //  $("input[name='description']").val('');
                        $('#crearModelLiquidacionDetalle').modal('hide');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
                    }else{
                        printErrorMsg(data.error)
                    }
                    $('#postFormLiquidacionDetalle').trigger("reset");
	 	  //var tableA = $('#tablaAbonosFacturacion').DataTable(); // accede de nuevo a la DataTable.
	 	  var tableL = $('#tablaLiquidacionDetalle').DataTable(); // accede de nuevo a la DataTable.
	          //tableA.ajax.reload();
	          tableL.ajax.reload();

                },
                error: function (data) {
			alert("VENGO CON ERRORES :" , printErrorMsg(data.error));
                   // $('#saveBtnCrearAbonos').html('NOT Save Changes');
                        $('.success-msg').css('display','block');
                        $('.success-msg').text(data.error);

		  var tableA = $('#tablaAbonosFacturacion').DataTable(); // accede de nuevo a la DataTable.
	          tableA.ajax.reload();
                }
            });
        });



/*------------------------------------------
        --------------------------------------------
        Delete Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostAbonosFacturacion",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');

		   $.ajax({
	           url: '/postDeleteAbonosFacturacion/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			            var table = $('#tablaAbonosFacturacion').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	           });
	});

	/*------------------------------------------
        --------------------------------------------
        Delete Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".borrarLiquidacionDetalle",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');

		   $.ajax({
	           url: '/postDeleteLiquidacionDetalle/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			            var table = $('#tablaLiquidacionDetalle').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
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



});  //// AQUI cierra el document.ready


function initTableLiquidacion(data) {

	return new DataTable('.tablaLiquidacion', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '300px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                      //    btn = btn + " <button   class='btn btn-primary editPost' data-pk='" + row.pk + "'>" + "</button>";
                          btn = btn + " <input type='radio'  class='form-check-input editPostLiquidacion' data-pk='"  + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 10
               }
            ],
            ajax: {
                 url:"/load_dataLiquidacion/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.tipoIng"},
                { data: "fields.id"},
                { data: "fields.tipoDoc"},
                { data: "fields.documento"},
                { data: "fields.nombre"},
                { data: "fields.consec"},
                { data: "fields.fechaIngreso"},
  
		{ data: "fields.servicioNombreIng"},
                { data: "fields.camaNombreIng"},
		 { data: "fields.convenio"},

        
            ]

 });
}



function initTableLiquidacionDetalle(data) {

	return new DataTable('.tablaLiquidacionDetalle', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '220px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                      //    btn = btn + " <button   class='btn btn-primary editPost' data-pk='" + row.pk + "'>" + "</button>";
                          btn = btn + " <input type='radio'  class='form-check-input editPostLiquidacionDetalle' data-pk='" + row.pk + "'>" + "</input>";
			btn = btn + " <input type='radio'  class='form-check-input borrarLiquidacionDetalle' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 9
               }
            ],
            ajax: {
                 url:"/load_dataLiquidacionDetalle/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.consecutivo"},
                { data: "fields.fecha"},
                { data: "fields.nombreExamen"},
                { data: "fields.cantidad"},
                { data: "fields.valorUnitario"},
                { data: "fields.valorTotal"},
                { data: "fields.observaciones"},
                { data: "fields.tipoRegistro"},
        
            ]

 });
}


function initTableFacAbonos(data) {
 
    return new DataTable('.tablaAbonosFacturacion', {
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
                       //   btn = btn + " <button   class='btn btn-primary editPostAbonos' data-pk='" + row.pk + "'>" + "</button>";
			  btn = btn + " <button class='btn btn-danger deletePostAbonosFacturacion' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";

                        return btn;
                    },
                    "targets": 4
               }
            ],
            ajax: {
                 url:"/load_dataAbonosFacturacion/" + data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.tipoPago"},
		{ data: "fields.formaPago"},
                { data: "fields.valor"},
                { data: "fields.descripcion"},
            
            ]
    });

}



 function tableActionsLiquidacion() {
   var table = initTableLiquiacion();


    // perform API operations with `table`
    // ...
}


function AdicionarLiquidacion()
{
	alert("Entre Adicionar Liquidacion");

        var cups = document.getElementById("lcups").value;
        var suministros = document.getElementById("lsuministros").value; 

        var cantidad = document.getElementById("cantidad").value;
        var valorUnitario = document.getElementById("valorUnitario").value;
        var valorTotal = document.getElementById("valorTotal").value;
        var observaciones = document.getElementById("observaciones").value;
	    var username_id = document.getElementById("username_id").value;




		$.ajax({
	           url: '/guardarLiquidacionDetalle/',
	            data :
	            {'cups':cups, 'suministros':suministros,'cantidad':cantidad,  'valorUnitario':valorUnitario,
			'valorTotal':valorTotal,'observaciones':observaciones,
			    'username_id':username_id, 'liquidacionId':liquidacionId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese PRESENTE");

            		 var data2 =  {}   ;
        			data2['username'] = username;
    		        data2['sedeSeleccionada'] = sedeSeleccionada;
	    	        data2['nombreSede'] = nombreSede;
		            data2['sede'] = sede;
	            	var convenioId1 = document.getElementById("convenioId1").value;

	                var username_id = document.getElementById("username_id").value;

		            data2['username_id'] = username_id;
		            data2['valor'] = convenioId;
		            data2 = JSON.stringify(data2);

		            tableC= $("#tablaLiquidacioDetalle").dataTable().fnDestroy();
		   	        alert("ya destrui tablaLiquidacionDetalle");

	                    initTableLiquidacionDetalle(data2);
			                $("#mensajes").html(data.message);
                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}







