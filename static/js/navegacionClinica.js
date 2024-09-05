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
	tableActionsRadiologia();
	tableActionsTerapias();
	tableActionsNoQx();

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
        Delete Post Code Lab
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostLaboratorio",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el laboratorio Nro" + id);

	     	// var rowIndex = $(this).parent().index('#tablaLaboratorios tbody tr');
	     	var rowIndex = $(this).parent().index('#tablaLaboratorios tbody tr');
            var tdIndex = $(this).index('#tablaLaboratorios tbody tr:eq('+rowIndex+') td');
            alert('Row Number de tabla laboratorios : '+(rowIndex+1)+'\nColumn Number: '+(tdIndex+1));


	     	var table = $('#tablaLaboratorios');
            table.find( 'tbody tr:eq(rowIndex+1)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			             table.ajax.reload();
	});


	/*------------------------------------------
        --------------------------------------------
        Delete Post Code Rx
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostRadiologia",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el radiologia Nro" + id);
	     	var table1 = $('#tablaRadiologia');
            table1.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table1.ajax.reload();
	});

/*------------------------------------------
        --------------------------------------------
        Delete Post Code Terapias
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostTerapias",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el radiologia Nro" + id);
	     	var table2 = $('#tablaTerapias');
            table2.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table2.ajax.reload();
	});

    /*--------------------------------------------
        Delete Post Code NoQx
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostNoQx",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el Noqx Nro" + id);
	     	var table4 = $('#tablaNoQx');
            table4.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table4.ajax.reload();
	});



$('#tablaLaboratorios tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table = $('#tablaLaboratorios').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaLaboratorios").deleteRow(valor3);
         table.row.remove(valor3).draw(false);

        table.ajax.reload();
} );

$('#tablaTerapias tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table3 = $('#tablaTerapias').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaTerapias").deleteRow(valor3);
         table3.row.remove(valor3).draw(false);

        table3.ajax.reload();
} );

$('#tablaNoQx tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table4 = $('#tablaNoQx').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaTerapias").deleteRow(valor3);
         table4.row.remove(valor3).draw(false);

        table4.ajax.reload();
} );


        /*------------------------------------------
        --------------------------------------------
        Create Post Code Radiologia
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarRadiologia').click(function (e) {
            e.preventDefault();
           // $(this).html('Sending..');
	  //      $('#crearLaboratoriosModel').modal('hide');
         //   $('.success-msg').css('display','block');
         //   $('.success-msg').text('Dato actualizado');
   	   var table1 = $('#tablaRadiologia').DataTable();   // accede de nuevo a la DataTable.

   	   //var TipoDocPaciente = document.getElementById("tipoDocPaciente3").value;
	   // var documentoPaciente = document.getElementById("documentoPaciente3").value;
	   // var IngresoPaciente = document.getElementById("ingresoPaciente3").value;
	   // var tiposExamen_Id  = document.getElementById("tiposExamen_Id3").value;
	   var cantidad = document.getElementById("cantidad3").value;
       var observa = document.getElementById("observa3").value;
           var select = document.getElementById("rad"); /*Obtener el SELECT */
      	   var rad = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

	        table1.row.add([
                    rad, text,  cantidad, observa, ""
                ]).draw(false);
        });

        /*------------------------------------------
        --------------------------------------------
        Create Post Code Terapias
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarTerapias').click(function (e) {
            e.preventDefault();
           // $(this).html('Sending..');
	  //      $('#crearLaboratoriosModel').modal('hide');
         //   $('.success-msg').css('display','block');
         //   $('.success-msg').text('Dato actualizado');
   	   var table3 = $('#tablaTerapias').DataTable();   // accede de nuevo a la DataTable.

   	   //var TipoDocPaciente = document.getElementById("tipoDocPaciente3").value;
	   // var documentoPaciente = document.getElementById("documentoPaciente3").value;
	   // var IngresoPaciente = document.getElementById("ingresoPaciente3").value;
	   // var tiposExamen_Id  = document.getElementById("tiposExamen_Id3").value;
	   var cantidad = document.getElementById("cantidad4").value;
       var observa = document.getElementById("observa4").value;
           var select = document.getElementById("ter"); /*Obtener el SELECT */
      	   var ter = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

	        table3.row.add([
                    ter, text,  cantidad, observa, ""
                ]).draw(false);
        });

/*------------------------------------------
        --------------------------------------------
        Create Post Code NoQx
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarNoQx').click(function (e) {
            e.preventDefault();
           // $(this).html('Sending..');
	  //      $('#crearLaboratoriosModel').modal('hide');
         //   $('.success-msg').css('display','block');
         //   $('.success-msg').text('Dato actualizado');
   	   var table4 = $('#tablaNoQx').DataTable();   // accede de nuevo a la DataTable.

   	   //var TipoDocPaciente = document.getElementById("tipoDocPaciente3").value;
	   // var documentoPaciente = document.getElementById("documentoPaciente3").value;
	   // var IngresoPaciente = document.getElementById("ingresoPaciente3").value;
	   // var tiposExamen_Id  = document.getElementById("tiposExamen_Id3").value;
	   var cantidad = document.getElementById("cantidad5").value;
       var observa = document.getElementById("observa5").value;
           var select = document.getElementById("noQx"); /*Obtener el SELECT */
      	   var noQx = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

	        table4.row.add([
                    noQx, text,  cantidad, observa, ""
                ]).draw(false);
        });


});  // Aquip fin del document.ready


        /*------------------------------------------
        --------------------------------------------
        Create Post Code Laboratorios
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarLaboratorio').click(function (e) {
            e.preventDefault();
           // $(this).html('Sending..');
	  //      $('#crearLaboratoriosModel').modal('hide');
         //   $('.success-msg').css('display','block');
         //   $('.success-msg').text('Dato actualizado');

   	   var table = $('#tablaLaboratorios').DataTable();   // accede de nuevo a la DataTable.
   	   var TipoDocPaciente = document.getElementById("tipoDocPaciente1").value;
	   var documentoPaciente = document.getElementById("documentoPaciente1").value;
	   var IngresoPaciente = document.getElementById("ingresoPaciente1").value;
	   var tiposExamen_Id  = document.getElementById("tiposExamen_Id").value;
	   var cantidad = document.getElementById("cantidad").value;
       var observa = document.getElementById("observa").value;
           var select = document.getElementById("lab"); /*Obtener el SELECT */
      	   var lab = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada
	        table.row.add([
                    lab, text,  cantidad, observa, ""
                ]).draw(false);
        });


// I. LABORATORIOS

function tableActionsLaboratorios() {


   var table= $('#tablaLaboratorios').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostLaboratorio1' id='borraLab'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 4
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 4
            ],
    });
}

// II. RADIOLOGIA


function tableActionsRadiologia() {

      var table1= $('#tablaRadiologias').DataTable({
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
			   btn = btn + " <button class='btn btn-danger deletePostRadiologia' id='borraRad'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 4
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 4
            ],
    });
}
// FIN RADIOLOGIA


// III. TERAPIAS

function tableActionsTerapias() {


   var table3 = $('#tablaTerapias').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostLaboratorio1' id='borraLab'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 4
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 4
            ],
    });
}

// FIN TERAPIAS

// III. NOQX

function tableActionsNoQx() {


   var table4 = $('#tablaNoQx').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostLaboratorio1' id='borraLab'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 4
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 4
            ],
    });
}

// FIN NOQX


formHistoriaClinica.addEventListener('submit', e=>{
            confirm("Confirma Guardar Folio !");
         alert("Entre Form formHistoriaClinica");
        e.preventDefault()
        // Ah peros si se puede solo hay que recorrer y yap

        // LABORATORIO

        const table = $('#tablaLaboratorios').DataTable();
        var datos_tabla = table.rows().data().toArray();


        laboratorios=[]
        cadenas = {}

    	alert("longitud d ela tabla = " + datos_tabla.length);


	for(var i= 0; i < datos_tabla.length; i++) {

	    laboratorios.push({
        	"tiposExamen_Id"    : "1",
	        "cups"  : datos_tabla[i][0],
	        "cantidad"    : datos_tabla[i][2] ,
		"observa"    : datos_tabla[i][3] 
	      });
	   };

	laboratorios  = JSON.stringify(laboratorios);
        alert("asi quedo laboratorios  " + laboratorios);

        // FIN LABORATORIO


        // RADIOLOGIA

                const table1 = $('#tablaRadiologia').DataTable();
                var datos_tabla1 = table1.rows().data().toArray();

        radiologia=[]
        cadenas = {}

    	alert("longitud d ela tabla = " + datos_tabla1.length);



	for(var i= 0; i < datos_tabla1.length; i++) {

	    radiologia.push({
        	"tiposExamen_Id"    : "3",
	        "cups"  : datos_tabla1[i][0],
	        "cantidad"    : datos_tabla1[i][2] ,
		"observa"    : datos_tabla1[i][3]
	      });
	   };

	    radiologia  = JSON.stringify(radiologia);
        alert("asi quedo radiologia  " + radiologia);


        // FIN RADIOLOGIA


        // TERAPIAS

                const table3 = $('#tablaTerapias').DataTable();
                var datos_tabla3 = table3.rows().data().toArray();

        terapias=[]


    	alert("longitud d ela tabla = " + datos_tabla3.length);



	for(var i= 0; i < datos_tabla3.length; i++) {

	    terapias.push({
        	"tiposExamen_Id"    : "2",
	        "cups"  : datos_tabla3[i][0],
	        "cantidad"    : datos_tabla3[i][2] ,
		"observa"    : datos_tabla3[i][3]
	      });
	   };

	    terapias  = JSON.stringify(terapias);
        alert("asi quedo terapisa  " + terapias);


        // FIN TERAPIAS


        // NoQx

                const table4 = $('#tablaNoQx').DataTable();
                var datos_tabla4 = table3.rows().data().toArray();

        noQx=[]


    	alert("longitud d ela tabla = " + datos_tabla4.length);



	for(var i= 0; i < datos_tabla4.length; i++) {

	    noQx.push({
        	"tiposExamen_Id"    : "4",
	        "cups"  : datos_tabla3[i][0],
	        "cantidad"    : datos_tabla3[i][2] ,
		"observa"    : datos_tabla3[i][3]
	      });
	   };

	    noQx  = JSON.stringify(noQx);
        alert("asi quedo noQx  " + noQx);


        // FIN noQx


         var tipoDocPaciente    =  document.getElementById("tipoDocPaciente1").value
         var documentoPaciente  =  document.getElementById("documentoPaciente1").value;
         var folio      = "0";
         alert("tipoDoc y documento = " + tipoDocPaciente + " " + documentoPaciente )
         var fecha      =  document.getElementById("fecha").value;
         var motivo     =  document.getElementById("id_motivo").value;
         var subjetivo  =  document.getElementById("id_subjetivo").value;
         var objetivo   =  document.getElementById("id_objetivo").value;
         var analisis   =  document.getElementById("id_analisis").value;
         var plan =           document.getElementById("id_plann").value;
         var causasExterna = document.getElementById("causasExterna").value;
         var dependenciasRealizado = document.getElementById("dependenciasRealizado").value;
         var usuarioRegistro = document.getElementById("usuarioRegistro").value;
         var ingresoPaciente=document.getElementById("ingresoPaciente1").value;
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
             var planta = document.getElementById("username").value;
             alert("planta =" + planta);
             var fechaRegistro = document.getElementById("fechaRegistro").value;
             var estadoReg = "A"
            // var diagnosticos = document.getElementById("diagnosticos").value;

            var form_valido;

               $.ajax({
            	   type: 'POST',
 	               url: '/crearHistoriaClinica/',
  	               data: { 'tipoDocPaciente':tipoDocPaciente,
  	                      'documentoPaciente':documentoPaciente,
  	                      'ingresoPaciente':ingresoPaciente,
  	               		  'folio':folio,
			               'motivo':motivo,
			                'subjetivo':subjetivo,
			                'objetivo':objetivo,
                            'analisis':analisis,
                            'plan':plan,
	                        'causasExterna':causasExterna,
	                        'dependenciasRealizado':dependenciasRealizado,
			                'usuarioRegistro':usuarioRegistro,
			                'ingresoPaciente':ingresoPaciente,
				            'tiposFolio':tiposFolio,
				            'profesional':profesional,
				            'espMedico':espMedico,
				            'planta':planta,
				            'estadoReg':estadoReg,
				           'laboratorios':laboratorios,
				           'radiologia':radiologia,
				           'terapias':terapias,
				           'noQx':noQx},
 	      		success: function (respuesta2) {
 	      		       // var data = JSON.parse(respuesta2);
 	      		        alert("Esto llega :  " + JSON.stringify(respuesta2));

 	      		        mensaje1 = JSON.parse(respuesta2);
 	      		        alert("Esto llega el Mensaje :  " + mensaje1['Mensaje']);
 	      		        mensaje =  mensaje1['Mensaje'];

				        if (mensaje == "OK")
				            {

				            $("#formHistoriaClinicaT").submit();
				            }
				        else
				            {
				            $("#mensajes").html(mensaje);
				            }
 	      		        //return true;
 	      		}, // cierra function sucess
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);

 	      		}, // cierra error function
  	        });  // cierra ajax

});  // cierra commit
