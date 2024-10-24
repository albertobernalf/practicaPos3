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

        data = JSON.stringify(data);


	initTableConvenios(data);


	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostConvenios', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	$.ajax({
	           url: '/creacionHc/postConsultaConvenios/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);

			// Colocar Encabezadao
	  		// aqui debe activar un dataTale para liquidacionDetalle

			// Colocar Totales liquidacioon

			 $('#pk').val(data.pk);
	       	        $('#tipoDocId').val(data.tipoDocId);
        	       	$('#nombreTipoDoc').val(data.nombreTipoDoc);
	                $('#documentoId').val(data.documentoId);
	                $('#documento2').val(data.documento);
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



});  //// AQUI cierra el document.ready


function initTableConvenios(data) {

	return new DataTable('.tablaConvenios', {
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
                          btn = btn + " <input type='radio'  class='form-check-input editPostConvenios' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 6
               }
            ],
            ajax: {
                 url:"/load_dataConvenios/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.nombre"},
                { data: "fields.id"},
                { data: "fields.vigenciaDesde"},
                { data: "fields.vigenciaHasta"},
                { data: "fields.empresa"},
                { data: "fields.tarifa"},
        
            ]

 });
}


 function tableActionsConvenios() {
   var table = initTableFacturacion();


    // perform API operations with `table`
    // ...
}







