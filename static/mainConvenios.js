var $ = jQuery;
console.log('Hola Alberto Hi!')



$(document).ready(function () {

function checkByDefault(){
	$("input[name=radioSel][value='1']").prop("checked",true)
        let valor = $('input[name="radioSel"]:checked').val();

        alert(" fila seleccionada radio = " + valor );


}


document.addEventListener("DOMContentLoaded", function(event) {
  	
   alert("Entre DOMContentLoaded" );
  checkByDefault();
    
});

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
        data['valor'] = 1

        data = JSON.stringify(data);
   
	// Check #x


	initTableConvenios(data);

	
	 // $('input[name="radioSel"]').prop('checked', true);
	$("input[name=radioSel][value='1']").prop("checked",true)
	var valor = $('input[name="radioSel"]:checked').val();



      alert(" fila seleccionada radio = " + valor );

	
	initTableConveniosProcedimientos(data);


	/*--------------------------------------------
        Click to Edit Button
        --------------------------------------------
        --------------------------------------------*/
        $('body').on('click', '.editPostConvenios', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	 var data =  {}   ;
	data['username'] = username;
        data['sedeSeleccionada'] = sedeSeleccionada;
        data['nombreSede'] = nombreSede;
        data['sede'] = sede;
        data['username_id'] = username_id;
        data['valor'] = post_id;	
        data = JSON.stringify(data);

         tableC= $("#tablaConveniosProcedimientos").dataTable().fnDestroy();
   	 alert("ya destrui tablaConveniosProcedimientos");

           initTableConveniosProcedimientos(data);
           // initTableConveniosSuministros(data);
           // initTableConveniosHonorarios(data);

	$.ajax({
	           url: '/postConsultaConvenios/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);
  
			 $('#pk').val(data.pk);
	       	        $('#convenioId').val(data.pk);
	       	        $('#convenioId1').val(data.pk);
	       	        $('#nombre').val(data.nombre);
        	       	$('#empresa').val(data.empresa);
	                $('#vigenciaDesde').val(data.vigenciaDesde);
	                $('#vigenciaHasta').val(data.vigenciaHasta);
	                $('#porcTarifario').val(data.porcTarifario);
	                $('#porcSuministros').val(data.porcSuministros);
	                $('#valorOxigeno').val(data.valorOxigeno);
	                $('#porcEsterilizacion').val(data.porcEsterilizacion);
	                $('#porcMaterial').val(data.porcMaterial);
	                $('#hospitalario').val(data.hospitalario);
	                $('#urgencias').val(data.urgencias);
	                $('#ambulatorio').val(data.ambulatorio);
	                $('#consultaExterna').val(data.consultaExterna);
	                $('#copago').val(data.copago);
	                $('#moderadora').val(data.moderadora);
			 $('#tipoFactura').val(data.tipoFactura);
			 $('#agrupada').val(data.agrupada);
			
			 $('#facturacionSuministros').val(data.facturacionSuministros);
			 $('#facturacionCups').val(data.facturacionCups);
			 $('#cuentaContable').val(data.cuentaContable);
			 $('#requisitos').val(data.requisitos);

			$('#pnombre').val(data.nombre);
        	       	$('#pempresa').val(data.empresa);
	                $('#pvigenciaDesde').val(data.vigenciaDesde);
	                $('#pvigenciaHasta').val(data.vigenciaHasta);

			 $('#tiposTarifa').val(data.tiposTarifa);
			 $('#cups').val(data.cups);


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
        $('body').on('click', '.editPostConveniosProcedimientos', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	$.ajax({
	           url: '/postConsultaConveniosProcedimientos/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data="  + data);

		

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

                          btn = btn + " <input type='radio' id='radioSel' name='radioSel'  class='form-check-input editPostConvenios' data-pk='" + row.pk + "'>" + "</input>";
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


function initTableConveniosProcedimientos(data) {

	return new DataTable('.tablaConveniosProcedimientos', {
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
                          btn = btn + " <input type='radio'  class='form-check-input editPostConveniosProcedimientos' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 6
               }
            ],
            ajax: {
                 url:"/load_dataConveniosProcedimientos/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.codigoHomologado"},
                { data: "fields.id"},
                { data: "fields.tarifa"},
                { data: "fields.cupsId"},
                { data: "fields.cupsNombre"},
                { data: "fields.valor"},
        
            ]

 });
}



 function tableActionsConvenios() {
   var table = initTableFacturacion();


    // perform API operations with `table`
    // ...
}


function GrabarConvenio()
{
	alert("Entre grabar convenio");
	var username_id = document.getElementById("username_id").value;
        var convenioId1 = document.getElementById("convenioId1").value;
        var nombre = document.getElementById("cnombre").value;
	var empresa = document.getElementById("cempresa").value;
        var vigenciaDesde = document.getElementById("cvigenciaDesde").value;
	var vigenciaHasta = document.getElementById("cvigenciaHasta").value;
	var porcTarifario = document.getElementById("cporcTarifario").value;
	var porcSuministros = document.getElementById("cporcSuministros").value;
	var valorOxigeno = document.getElementById("cvalorOxigeno").value;
	var porcEsterilizacion = document.getElementById("cporcEsterilizacion").value;
	var porcMaterial  = document.getElementById("cporcMaterial").value;
	var hospitalario = document.getElementById("chospitalario").value;
	var urgencias = document.getElementById("curgencias").value;
	var consultaExterna = document.getElementById("cconsultaExterna").value;
	var copago = document.getElementById("ccopago").value;	
	var moderadora = document.getElementById("cmoderadora").value;
	var tipoFactura = document.getElementById("ctipoFactura").value;
	var agrupada = document.getElementById("cagrupada").value;
	var facturacionSuministros = document.getElementById("cfacturacionSuministros").value;
	var facturacionCups = document.getElementById("cfacturacionCups").value;
	var cuentaContable = document.getElementById("ccuentaContable").value;
	var requisitos = document.getElementById("crequisitos").value;

	$.ajax({
           url: '/guardarConvenio/',
            data : {convenioId:convenioId1,
                    username_id:username_id,
		    nombre:nombre,
		    empresa:empresa,
		    vigenciaDesde:vigenciaDesde,
		    vigenciaHasta:vigenciaHasta,
		    porcTarifario:porcTarifario,
		    porcSuministros:porcSuministros,
		    valorOxigeno:valorOxigeno,
		    porcEsterilizacion:porcEsterilizacion,
		    porcMaterial:porcMaterial,
		    hospitalario:hospitalario,
		    urgencias:urgencias,
		    consultaExterna:consultaExterna,
		    copago:copago,
		    moderadora:moderadora,
		    tipoFactura:tipoFactura,
		    agrupada:agrupada,
		    facturacionSuministros:facturacionSuministros,
		    facturacionCups:facturacionCups,
		    cuentaContable:cuentaContable,
		    requisitos:requisitos},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);
			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

}



function GrabarConvenio1()
{
	alert("Entre grabar convenio1");

        var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
        var nombre = document.getElementById("nombre").value;
	var empresa = document.getElementById("empresa").value;
        var vigenciaDesde = document.getElementById("vigenciaDesde").value;
	var vigenciaHasta = document.getElementById("vigenciaHasta").value;
	var porcTarifario = document.getElementById("porcTarifario").value;
	var porcSuministros = document.getElementById("porcSuministros").value;
	var valorOxigeno = document.getElementById("valorOxigeno").value;
	var porcEsterilizacion = document.getElementById("porcEsterilizacion").value;
	var porcMaterial  = document.getElementById("porcMaterial").value;
	var hospitalario = document.getElementById("hospitalario").value;
	var urgencias = document.getElementById("urgencias").value;
	var consultaExterna = document.getElementById("consultaExterna").value;
	var copago = document.getElementById("copago").value;	
	var moderadora = document.getElementById("moderadora").value;
	var tipoFactura = document.getElementById("tipoFactura").value;
	var agrupada = document.getElementById("agrupada").value;
	var facturacionSuministros = document.getElementById("facturacionSuministros").value;
	var facturacionCups = document.getElementById("facturacionCups").value;
	var cuentaContable = document.getElementById("cuentaContable").value;
	var requisitos = document.getElementById("requisitos").value;

	$.ajax({
           url: '/guardarConvenio1/',
            data : {convenioId:convenioId1,
                    username_id:username_id,
		    nombre:nombre,
		    empresa:empresa,
		    vigenciaDesde:vigenciaDesde,
		    vigenciaHasta:vigenciaHasta,
		    porcTarifario:porcTarifario,
		    porcSuministros:porcSuministros,
		    valorOxigeno:valorOxigeno,
		    porcEsterilizacion:porcEsterilizacion,
		    porcMaterial:porcMaterial,
		    hospitalario:hospitalario,
		    urgencias:urgencias,
		    consultaExterna:consultaExterna,
		    copago:copago,
		    moderadora:moderadora,
		    tipoFactura:tipoFactura,
		    agrupada:agrupada,
		    facturacionSuministros:facturacionSuministros,
		    facturacionCups:facturacionCups,
		    cuentaContable:cuentaContable,
		    requisitos:requisitos},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			    $("#mensajes").html(data.message);

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });

}



function BtnAdicionarConvenio()
{
	alert("Entre Adicionar Convenio");

        var codigoHomologado = document.getElementById("codHomologado").value;
        var tiposTarifa = document.getElementById("tiposTarifa"); /*Obtener el SELECT */
        var nombreTiposTarifa = select.options[tiposTarifa.selectedIndex].value; /* Obtener el valor */
        var cups = document.getElementById("cups").value;
	var nombreCups = select.options[cups.selectedIndex].value; /* Obtener el valor */
        var valor = document.getElementById("valor").value;
	var username_id = document.getElementById("username_id").value;
	var convenioId = document.getElementById("convenioId").value;

		$.ajax({
	           url: '/guardarConveniosProcedimientos/',
	            data : {codigoHomologado:codigoHomologado,
			    tiposTarifa:tiposTarifa,
			    nombreTiposTarifa:nombreTiposTarifa,
    			    cups:_cups,
			    nombreCups:nombreCups,
			    valor:valor,
			    username_id:username_id,
			    convenioId:convenioId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);
			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });


}

function GrabarTarifa()
{
	alert("Entre Grabar Tarifa no hago nada");

$.ajax({
	           url: '/grabarTarifa/',
	            data : {},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(data.message);
	   	    	}
	     });



}


