console.log('Hola Alberto Hi!')

function miIngreso()
	{
	alert ("Aqui va a estar el AJAX con este ingreso = " );
 	var valor = $('input[name="ingresoId"]:checked').val();
	alert ("Aqui me devuelvo con ingreso = " + valor + " y voy por el ajax");

	$.ajax({
		type: 'POST',
    		url: '/cambioServicioModal/',
		data: {'valor':valor},
		dataType : 'json',
		success: function (Usuarios) {

    	        alert("llegue MODAL cambio Servicio = " + Usuarios.tipoDocId + " " +  Usuarios.documento);

		$("#tipoDocx option[value="+ Usuarios.tipoDocId +"]").attr("selected",true);
		// $('#tipoDocx').val(Usuarios.documento);

		 $('#documentox').val(Usuarios.documento);
		 //$('#cambioServicioModal').modal({show:true});

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
	}
