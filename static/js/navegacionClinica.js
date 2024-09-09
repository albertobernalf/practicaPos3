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
	tableActionsAntecedentes();
	tableActionsDiagnosticos();
	tableActionsInterconsultas();

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

        /*--------------------------------------------
        Delete Post Code Antecedentes
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostAntecedentes",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el Noqx Nro" + id);
	     	var table5 = $('#tablaAntecedentes');
            table5.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table5.ajax.reload();
	});


        /*--------------------------------------------
        Delete Post Code Diagnosticos
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostDiagnosticos",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el Noqx Nro" + id);
	     	var table6 = $('#tablaDiagnosticos');
            table6.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table6.ajax.reload();
	});




        /*--------------------------------------------
        Delete Post Code Interconsultas
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostDInterconsultas",function(){
            var current_object = $(this);
            alert("current_object =" +current_object );
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');
	     	alert("Entre a borrar el Interconsultas Nro" + id);
	     	var table7 = $('#tablaInterconsultas');
            table6.find( 'tbody tr:eq(0)' ).remove();

            alert("valores = " + valores);
		        	  $('.success-msg').css('display','block');
                        $('.success-msg').text(data.message);
			              table7.ajax.reload();
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



$('#tablaAntecedentes tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table5 = $('#tablaAntecedentes').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaAntecedentes").deleteRow(valor3);
         table5.row.remove(valor3).draw(false);

        table5.ajax.reload();
} );

$('#tablaDiagnosticos tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table6 = $('#tablaDiagnosticos').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaDiagnosticos").deleteRow(valor3);
         table6.row.remove(valor3).draw(false);

        table6.ajax.reload();
} );


$('#tablaDInterconsultas tbody').on('click', 'tr', function () {
    confirm("Desea eliminar LA FILA: ");
       var table7 = $('#tablaDInterconsultas').DataTable();
      var valor3 = $(this).parents("tr")['prevObject']['0']['_DT_RowIndex'];

      document.getElementById("tablaDInterconsultas").deleteRow(valor3);
         table7.row.remove(valor3).draw(false);

        table7.ajax.reload();
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


    /*------------------------------------------
        --------------------------------------------
        Create Post Code Antecedentes
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarAntecedentes').click(function (e) {
            e.preventDefault();

   	   var table5 = $('#tablaAntecedentes').DataTable();   // accede de nuevo a la DataTable.

       var observa = document.getElementById("observa6").value;

           var select = document.getElementById("antecedentes"); /*Obtener el SELECT */
      	   var antecedentes = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

	        table5.row.add([
                    antecedentes, text,   observa, ""
                ]).draw(false);
        });

    /*------------------------------------------
        --------------------------------------------
        Create Post Code Diagnosticos
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarDiagnosticos').click(function (e) {
            e.preventDefault();

   	   var table6 = $('#tablaDiagnosticos').DataTable();   // accede de nuevo a la DataTable.

       var observa = document.getElementById("observa7").value;

           var select = document.getElementById("diagnosticos"); /*Obtener el SELECT */
      	   var diagnosticos = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   textDiagnosticos = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

            var select1 = document.getElementById("tiposDiagnosticos"); /*Obtener el SELECT */
      	   var tiposDiagnosticos = select1.options[select1.selectedIndex].value; /* Obtener el valor */
      	   textTiposDiagnosticos = select1.options[select1.selectedIndex].innerText; //El texto de la opción seleccionada

	        table6.row.add([
                    tiposDiagnosticos ,  textTiposDiagnosticos  ,diagnosticos,  textDiagnosticos,  observa, ""
                ]).draw(false);
        });

    /*------------------------------------------
        --------------------------------------------
        Create Post Code Interconsultas
        --------------------------------------------
        --------------------------------------------*/
        $('#BtnAdicionarInterconsultas').click(function (e) {
            e.preventDefault();

   	   var table7 = $('#tablaInterconsultas').DataTable();   // accede de nuevo a la DataTable.

       var descripcion = document.getElementById("descripcion").value;

           var select = document.getElementById("diagnosticosI"); /*Obtener el SELECT */
      	   var diagnosticos = select.options[select.selectedIndex].value; /* Obtener el valor */
      	   textDiagnosticos = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada

            var select1 = document.getElementById("tiposInterconsulta"); /*Obtener el SELECT */
      	   var tiposInterconsulta = select1.options[select1.selectedIndex].value; /* Obtener el valor */
      	   texttiposInterconsulta = select1.options[select1.selectedIndex].innerText; //El texto de la opción seleccionada

            var select2 = document.getElementById("especialidadConsultada"); /*Obtener el SELECT */
      	   var especialidadConsultada = select2.options[select2.selectedIndex].value; /* Obtener el valor */
      	   textespecialidadConsultada = select2.options[select2.selectedIndex].innerText; //El texto de la opción seleccionada

            var select3 = document.getElementById("medicoConsultado"); /*Obtener el SELECT */
      	   var medicoConsultado = select3.options[select3.selectedIndex].value; /* Obtener el valor */
      	   textmedicoConsultado = select3.options[select3.selectedIndex].innerText; //El texto de la opción seleccionada


	        table7.row.add([
                 tiposInterconsulta, texttiposInterconsulta,   especialidadConsultada ,  textespecialidadConsultada ,medicoConsultado, textmedicoConsultado  ,diagnosticos,  textDiagnosticos,  descripcion, ""
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
	   //var tiposExamen_Id  = document.getElementById("tiposExamen_Id").value;
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
			  btn = btn + " <button class='btn btn-danger deletePostLaboratorio1' id='borraTer'>" + '<i class="fa fa-trash"></i>' + "</button>";
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
			  btn = btn + " <button class='btn btn-danger deletePostLaboratorio1' id='borraNoQx'>" + '<i class="fa fa-trash"></i>' + "</button>";
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



// III. ANTECEDENTES

function tableActionsAntecedentes() {

   var table5 = $('#tablaAntecedentes').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostAntecedentes1' id='borraAnt'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 3
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
            ],
    });
}

// FIN ANTECEDENTES


// III. DIAGNOSTICOS

function tableActionsDiagnosticos() {

   var table6 = $('#tablaDiagnosticos').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostDiagnosticos1' id='borraDiag'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 5
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3
            ],
    });
}

// FIN DIAGNOSTICOS




// III. INTERCONSULTAS

function tableActionsInterconsultas() {

   var table6 = $('#tablaInterconsultas').DataTable({
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
			  btn = btn + " <button class='btn btn-danger deletePostDiagnosticos1' id='borraDiag'>" + '<i class="fa fa-trash"></i>' + "</button>";
                        return btn;
                    },
                    "targets": 9
               }
            ],
        lengthMenu: [5],
    columns:[
    //"dummy" configuration
        { visible: true }, //col 1
        { visible: true }, //col 2
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3
        { visible: true }, //col 3

            ],
    });
}

// FIN INTERCONSULTAS



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
                var datos_tabla4 = table4.rows().data().toArray();

        noQx=[]


    	alert("longitud d ela tabla = " + datos_tabla4.length);



	for(var i= 0; i < datos_tabla4.length; i++) {

	    noQx.push({
        	"tiposExamen_Id"    : "4",
	        "cups"  : datos_tabla4[i][0],
	        "cantidad"    : datos_tabla4[i][2] ,
		"observa"    : datos_tabla4[i][3]
	      });
	   };

	    noQx  = JSON.stringify(noQx);
        alert("asi quedo noQx  " + noQx);


        // FIN noQx

	// Antecedentes

        const table5 = $('#tablaAntecedentes').DataTable();
                var datos_tabla5 = table5.rows().data().toArray();

        antecedentes=[]


    	alert("longitud d ela tabla = " + datos_tabla5.length);



	for(var i= 0; i < datos_tabla5.length; i++) {

	    antecedentes.push({

	        "id"  : datos_tabla5[i][0],
	        "tipo"    : datos_tabla5[i][1] ,
		"descripcion"    : datos_tabla5[i][2]
	      });
	   };

	    antecedentes  = JSON.stringify(antecedentes);
        alert("asi quedo antecedentes  " + antecedentes);



 	// Fin Antecedentes

	// Diagnosticos

    const table6 = $('#tablaDiagnosticos').DataTable();
     var datos_tabla6 = table6.rows().data().toArray();

        diagnosticos=[]


    	alert("longitud d ela tabla = " + datos_tabla6.length);



	for(var i= 0; i < datos_tabla6.length; i++) {

	    diagnosticos.push({
	        "diagnosticos"    : datos_tabla6[i][2] ,
	        "tiposDiagnosticos"    : datos_tabla6[i][0] ,
	    	"observa"    : datos_tabla6[i][4]
	      });
	   };

	    diagnosticos  = JSON.stringify(diagnosticos);
        alert("asi quedo diagnosticos  " + diagnosticos);


 	// Fin Diagnosticos

	// Cirugias
	// Fin Cirugias


	// Interconsultas


    const table7 = $('#tablaInterconsultas').DataTable();
     var datos_tabla7 = table7.rows().data().toArray();

        interconsultas=[]


    	alert("longitud d ela tabla = " + datos_tabla7.length);



	for(var i= 0; i < datos_tabla7.length; i++) {

	    interconsultas.push({
	        "tiposInterconsulta"    : datos_tabla7[i][0] ,
	        "tiposInterconsultaNombre"    : datos_tabla7[i][1] ,
	        "especialidadConsultada"    : datos_tabla7[i][2] ,
	        "especialidadConsultadaNombre"    : datos_tabla7[i][3] ,
	        "medicoConsultado"    : datos_tabla7[i][4] ,
	        "medicoConsultadoNombre"    : datos_tabla7[i][5] ,
	        "descripcion"    : datos_tabla7[i][8] ,
	        "diagnosticos"    : datos_tabla7[i][7],
	        "diagnosticosNombre"    : datos_tabla7[i][6]
	      });
	   };

	    interconsultas  = JSON.stringify(interconsultas);
        alert("asi quedo interconsultas  " + interconsultas);

    alert("datos_tabla7[i][0]" +  datos_tabla7[1][0]);
    alert("1" +  datos_tabla7[1][1]);
    alert("2" +  datos_tabla7[1][2]);
    alert("3" +  datos_tabla7[1][3]);
    alert("4" +  datos_tabla7[1][4]);
    alert("5" +  datos_tabla7[1][5]);
    alert("6" +  datos_tabla7[1][6]);
    alert("7" +  datos_tabla7[1][7]);
    alert("8" +  datos_tabla7[1][8]);


 	// Fin Interconsulta

	// Incapacidades
 	// Fin Incapacidades


	// Medicamentos
 	// Fin Medicamentos


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

   	     var tiposfolio  =  document.getElementById("tiposFolio1").value;
         alert("tiposFolio =" + tiposFolio);
         var profesional = document.getElementById("profesional").value;
         alert("Profesional = ", profesional);

   	    var espMedico  =  document.getElementById("espMedico").value;
         alert("espMedico =" + espMedico);
       
         var planta = document.getElementById("username").value;
         alert("planta =" + planta);
         var fechaRegistro = document.getElementById("fechaRegistro").value;
         var estadoReg = "A"
         var tipoIng = document.getElementById("tipoIng").value;
        // Provisional
        tiposFolio=1
        // Fin provisinal


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
				           'noQx':noQx,
				           'tipoIng':tipoIng,
				           'antecedentes':antecedentes,
				           'diagnosticos':diagnosticos,
				           'interconsultas':interconsultas},
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
