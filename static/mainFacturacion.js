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
	data['ingresoId'] = valor;

	// fecha actual
	let date = new Date();

	ano = date.getFullYear();
	mes = date.getMonth();
	dia = date.getDate();

        desdeFecha = ano + '-' + mes + '-' + dia + ' 00:00:00'
        hastaFecha = ano + '-' + mes + '-' + dia + ' 23:59:59'
	alert("desdefecha = "+ desdeFecha);
	alert("hastafecha = "+ hastaFecha);
        desdeFactura=0;
        hastaFactura=0;


	data['desdeFecha'] = desdeFecha;
	data['hastaFecha'] = hastaFecha;
	data['desdeFactura'] = desdeFactura;
	data['hastaFactura'] = hastaFactura;
	data['bandera'] = 'Por Fecha';

        data = JSON.stringify(data);

	initTableLiquidacion(data);
	initTableLiquidacionDetalle(data);
        initTableFacAbonos(data);
        initTableFacturacion(data);

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
		$('#liquidacionId1').val(data.id);
		$('#ingresoId').val(data.ingresoId1);

		$('#fecha').val(data.fecha);
		$('#tipoDoc_id').val(data.tipoDoc_id);
		$('#documento_id').val(data.documento_id);
		$('#tipoDoc').val(data.tipoDocumento);
		$('#pdocumento').val(data.documento);
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
		$('#valorApagar').val(data.totalAPagar);
		$('#anticipos').val(data.totalAnticipos);
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


                     const $id425 = document.querySelector("#lsuministros");


 	      		     $("#lsuministros").empty();

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
			 var ingresoId = document.getElementById("ingresoId").value;

		        data2['valor'] = valor;	
		        data2['ingresoId'] = ingresoId;	

		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	           initTableLiquidacionDetalle(data2);

		    tableA= $("#tablaAbonosFacturacion").dataTable().fnDestroy();	
	           initTableFacAbonos(data2);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

        });

	/*--------------------------------------------
        Click to Edit Button PostFacturacon
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostFacturacion', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));
        var username_id = document.getElementById("username_id").value;

	$.ajax({
	           url: '/postConsultaFacturacion/',
	            data : {post_id:post_id, username_id:username_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);
			// Colocar Encabezadao
	  		// aqui debe llenar el dato parta posible ANULACION , REFACTURACION
		$('#Afactura').val(data.factura);
		$('#AfechaFactura').val(data.fechaFactura);
		$('#AtipoDoc_id').val(data.tipoDoc);
		$('#Adocumento_id').val(data.documento);
		$('#Apaciente').val(data.paciente);
		$('#AconsecAdmision').val(data.consecAdmision);
		$('#AnombreConvenio').val(data.AnombreConvenio);

		$('#Rfactura').val(data.factura);
		$('#RfechaFactura').val(data.fechaFactura);
		$('#RtipoDoc_id').val(data.tipoDoc);
		$('#Rdocumento_id').val(data.documento);
		$('#Rpaciente').val(data.paciente);
		$('#RconsecAdmision').val(data.consecAdmision);
		$('#RnombreConvenio').val(data.AnombreConvenio);

       

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("liquidacionId").value;
			 var ingresoId = document.getElementById("ingresoId").value;

		        data2['valor'] = valor;	
		        data2['ingresoId'] = ingresoId;	

		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	           initTableLiquidacionDetalle(data2);

		    tableA= $("#tablaAbonosFacturacion").dataTable().fnDestroy();	
	           initTableFacAbonos(data2);

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
                      
                       alert("data="  + data);

			 $('#pk').val(data.pk);
	       	        $('#ldconsecutivo').val(data.consecutivo);

			$('#liquidacionDetalleId').val(data.id);

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


                     const $id4256 = document.querySelector("#ldsuministros");


 	      		     $("#ldsuministros").empty();

	                 $.each(data['Suministros'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4256.appendChild(option);
 	      		      });


		 $('#ldcups').val(data.codigoCups_id);
		 $('#ldsuministros').val(data.cums_id);

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

            $('#saveBtnCrearAbonosFacturacion').val("Create Post");
            $('#post_id').val('');
            $('#postFormCrearAbonosFacturacion').trigger("reset");
            $('#modelHeading').html("Creacion Abonos en admision");
	  var liquidacionId = document.getElementById("liquidacionId").value;
	document.getElementById("liquidacionId1").value =liquidacionId;
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
		   $("#mensajes").html(data.message);

                    $('#postFormCrearAbonosFacturacion').trigger("reset");
	 	  var tableA = $('#tablaAbonosFacturacion').DataTable(); 
	          tableA.ajax.reload();
	 	  var tableL = $('#tablaLiquidacionDetalle').DataTable(); 
	          tableL.ajax.reload();
			LeerTotales();
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
	 	  // var tableA = $('#tablaAbonosFacturacion').DataTable(); 
		  // tableA.ajax.reload();
	 	  var tableL = $('#tablaLiquidacionDetalle').DataTable(); 	          
	          tableL.ajax.reload();
			LeerTotales();

		   $("#mensajes").html(data.message);

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
			            var table = $('#tablaAbonosFacturacion').DataTable(); 
		                table.ajax.reload();
			LeerTotales();
			   $("#mensajes").html(data.message);
                    },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	           });
	});

	/*------------------------------------------
        --------------------------------------------
        Delete Post Liquidacion Detalle
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
			LeerTotales();
			   $("#mensajes").html(data.message);
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
                         btn = btn + " <button   class='btn btn-primary editPostLiquidacionDetalle' data-pk='" + row.pk + "'>" + "</button>";
                         btn = btn + " <button   class='btn btn-primary borrarLiquidacionDetalle' data-pk='" + row.pk + "'>" + "</button>";
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
		{ data: "fields.estadoReg"},
        
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
            scrollY: '250px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
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
                { data: "fields.tipoPagoNombre"},
		{ data: "fields.formaPagoNombre"},
                { data: "fields.valor"},
                { data: "fields.descripcion"},
            
            ]
    });

}


function AdicionarLiquidacion()
{

        var cups = document.getElementById("lcups").value;
        var suministros = document.getElementById("lsuministros").value; 
        var cantidad = document.getElementById("cantidad").value;
        var valorUnitario = document.getElementById("valorUnitario").value;
        var valorTotal = document.getElementById("valorTotal").value;
        var observaciones = document.getElementById("lobservaciones").value;
        var username_id = document.getElementById("username_id").value;
        var tipoRegistro = document.getElementById("tipoRegistro").value;
 	var liquidacionId = document.getElementById("liquidacionId").value;


		$.ajax({
	           url: '/guardarLiquidacionDetalle/',
	            data :
	            {'cups':cups, 'suministros':suministros,'cantidad':cantidad,  'valorUnitario':valorUnitario,
			'valorTotal':valorTotal,'observaciones':observaciones,
			    'username_id':username_id, 'liquidacionId':liquidacionId, 'tipoRegistro':tipoRegistro},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {


            	        var data2 =  {}   ;
        		data2['username'] = username;
    		        data2['sedeSeleccionada'] = sedeSeleccionada;
	    	        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
	            	
	                var username_id = document.getElementById("username_id").value;
  	                data2['username_id'] = username_id;
                        alert("numero de la liquidacionId = " + liquidacionId);

		        data2['valor'] = liquidacionId;
		        data2 = JSON.stringify(data2);

		    tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
			alert ("ya la destrui");

	            initTableLiquidacionDetalle(data2);

			LeerTotales();

		 document.getElementById("lcups").value = '';
	         document.getElementById("lsuministros").value = '';
	         document.getElementById("cantidad").value = '';
	         document.getElementById("valorUnitario").value = '';
	         document.getElementById("valorTotal").value = '';
	         document.getElementById("lobservaciones").value = '';



			$("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}




function AFacturar()
{

	alert ("Entre a facturar ");

 	var liquidacionId = document.getElementById("liquidacionId").value;

		$.ajax({
	           url: '/facturarCuenta/',
	            data :
	            {'liquidacionId':liquidacionId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
				$('#imprimir').val(data.Factura);

            	        var data2 =  {}   ;
        		data2['username'] = username;
    		        data2['sedeSeleccionada'] = sedeSeleccionada;
	    	        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
	            	
	                var username_id = document.getElementById("username_id").value;
  	                data2['username_id'] = username_id;
                        alert("numero de la liquidacionId = " + liquidacionId);

		        data2['valor'] = liquidacionId;
		        data2 = JSON.stringify(data2);

		    tableL= $("#tablaLiquidacion").dataTable().fnDestroy();	
	            initTableLiquidacion(data2);


		    // tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	            // initTableLiquidacionDetalle(data2);


			$("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}



function LeerTotales()
{

	alert ("Entre a LeerTotales ");

 	var liquidacionId = document.getElementById("liquidacionId").value;

		$.ajax({
	           url: '/leerTotales/',
	            data :
	            {'liquidacionId':liquidacionId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

		$('#totalCopagos').val(data.totalCopagos);
		$('#totalCuotaModeradora').val(data.totalCuotaModeradora);
		$('#totalProcedimientos').val(data.totalProcedimientos);
		$('#totalSuministros').val(data.totalSuministros);
		$('#totalLiquidacion').val(data.totalLiquidacion);
		$('#valorApagar').val(data.totalAPagar);
		$('#anticipos').val(data.totalAnticipos);
		$('#totalAbonos').val(data.totalAbonos);

			$("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}


function initTableFacturacion(data) {

	return new DataTable('.tablaFacturacion', {
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
                          btn = btn + " <input type='radio'  class='form-check-input editPostFacturacion' data-pk='"  + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 14
               }
            ],
            ajax: {
                 url:"/load_dataFacturacion/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.id"},
                { data: "fields.fechaFactura"},
                { data: "fields.tipoDoc"},
                { data: "fields.documento"},
                { data: "fields.nombre"},
                { data: "fields.consec"},
                { data: "fields.fechaIngreso"},
                { data: "fields.fechaSalida"},
  		{ data: "fields.servicioNombreSalida"},
                { data: "fields.camaNombreSalida"},
		 { data: "fields.dxSalida"},
		 { data: "fields.convenio"},
		 { data: "fields.salidaClinica"},
		 { data: "fields.estadoSalida"},
        
            ]

 });
}



function AnularFactura()
{

	alert ("Entre Anular factura ");

 	var facturacionId = document.getElementById("facturacionId").value;

		$.ajax({
	           url: '/anularFactura/',
	            data :
	            {'facturacionId':facturacionId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
				$('#imprimir').val(data.Factura);

            	        var data2 =  {}   ;
        		data2['username'] = username;
    		        data2['sedeSeleccionada'] = sedeSeleccionada;
	    	        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
	            	
	                var username_id = document.getElementById("username_id").value;
  	                data2['username_id'] = username_id;
                        alert("numero de la liquidacionId = " + liquidacionId);

		        data2['valor'] = liquidacionId;
		        data2 = JSON.stringify(data2);

		    tableL= $("#tablaLiquidacion").dataTable().fnDestroy();	
	            initTableLiquidacion(data2);


		    // tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	            // initTableLiquidacionDetalle(data2);


			$("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}


function reFacturar()
{

	alert ("Entre Refacturar ");

 	var facturacionId = document.getElementById("facturacionId").value;

		$.ajax({
	           url: '/reFacturar/',
	            data :
	            {'facturacionId':facturacionId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
				$('#imprimir').val(data.Factura);

            	        var data2 =  {}   ;
        		data2['username'] = username;
    		        data2['sedeSeleccionada'] = sedeSeleccionada;
	    	        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
	            	
	                var username_id = document.getElementById("username_id").value;
  	                data2['username_id'] = username_id;
                        alert("numero de la liquidacionId = " + liquidacionId);

		        data2['valor'] = liquidacionId;
		        data2 = JSON.stringify(data2);

		    tableL= $("#tablaLiquidacion").dataTable().fnDestroy();	
	            initTableLiquidacion(data2);


		    // tableF= $("#tablaLiquidacionDetalle").dataTable().fnDestroy();	
	            // initTableLiquidacionDetalle(data2);


			$("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}