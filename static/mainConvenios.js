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
	initTableConveniosSuministros(data);
	initTableConveniosHonorarios(data);


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

         tableS= $("#tablaConveniosSuministros").dataTable().fnDestroy();
   	
           initTableConveniosSuministros(data);

           // initTableConveniosHonorarios(data);

	$.ajax({
	           url: '/postConsultaConvenios/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
  
			 $('#pk').val(data.pk);
	       	        $('#convenioId').val(data.pk);
	       	        $('#convenioId1').val(data.pk);
	       	        $('#nombre').val(data.nombre);
			$('#snombre').val(data.nombre);
	       	        $('#lnombre').val(data.nombre);
        	       	$('#empresa').val(data.empresa);
			$('#sempresa').val(data.empresa);
	                $('#vigenciaDesde').val(data.vigenciaDesde);
	                $('#vigenciaHasta').val(data.vigenciaHasta);
	                $('#lvigenciaDesde').val(data.vigenciaDesde);
	                $('#lvigenciaHasta').val(data.vigenciaHasta);

	                $('#svigenciaDesde').val(data.vigenciaDesde);
	                $('#svigenciaHasta').val(data.vigenciaHasta);
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

	                $('#vigenciaDesde').val(data.vigenciaDesde);
	                $('#vigenciaHasta').val(data.vigenciaHasta);

			 $('#tiposTarifa').val(data.tiposTarifa);
			 $('#cups').val(data.cups);

    		         var options = '<option value="=================="></option>';


                     const $id2 = document.querySelector("#tiposTarifa1");


 	      		     $("#tiposTarifa1").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });




                     const $id22 = document.querySelector("#stiposTarifa1");


 	      		     $("#stiposTarifa1").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id22.appendChild(option);
 	      		      });



                     const $id222 = document.querySelector("#ttiposTarifa");


 	      		     $("#ttiposTarifa").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id222.appendChild(option);
 	      		      });



                     const $id3 = document.querySelector("#xtiposTarifa");


 	      		     $("#xtiposTarifa").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id3.appendChild(option);
 	      		      });

                    const $id33 = document.querySelector("#ltiposTarifa1");


 	      		     $("#ltiposTarifa1").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id33.appendChild(option);
 	      		      });


                    const $id339 = document.querySelector("#ltiposTarifa");


 	      		     $("#ltiposTarifa").empty();

	                 $.each(data['TiposTarifa'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id339.appendChild(option);
 	      		      });

		 const $id449 = document.querySelector("#lhonorarios");


 	      		     $("#lhonorarios").empty();

	                 $.each(data['Honorarios'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id449.appendChild(option);
 	      		      });



		 const $id450 = document.querySelector("#llhonorarios");


 	      		     $("#llhonorarios").empty();

	                 $.each(data['Honorarios'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id450.appendChild(option);
 	      		      });


                     const $id4 = document.querySelector("#conceptos");


 	      		     $("#conceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4.appendChild(option);
 	      		      });




                     const $id44 = document.querySelector("#tconceptos");


 	      		     $("#tconceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id44.appendChild(option);
 	      		      });


                     const $id444 = document.querySelector("#sconceptos");


 	      		     $("#sconceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id444.appendChild(option);
 	      		      });

                     const $id4445 = document.querySelector("#lconceptos");


 	      		     $("#lconceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4445.appendChild(option);
 	      		      });


                     const $id4447 = document.querySelector("#llconceptos");


 	      		     $("#llconceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id4447.appendChild(option);
 	      		      });






                     const $id5 = document.querySelector("#xcups");


 	      		     $("#xcups").empty();

	                 $.each(data['Cups'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id5.appendChild(option);
 	      		      });



                     const $id51 = document.querySelector("#lcups");


 	      		     $("#lcups").empty();

	                 $.each(data['Cups'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id51.appendChild(option);
 	      		      });


                     const $id55 = document.querySelector("#llcups");


 	      		     $("#llcups").empty();

	                 $.each(data['Cups'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id55.appendChild(option);
 	      		      });


                     const $id42 = document.querySelector("#tsum");


 	      		     $("#tsum").empty();

	                 $.each(data['Suministras'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id42.appendChild(option);
 	      		      });


                     const $id425 = document.querySelector("#lsum");


 	      		     $("#lsum").empty();

	                 $.each(data['Suministras'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id425.appendChild(option);
 	      		      });


		  const $id6 = document.querySelector("#xconceptos");


 	      		     $("#xconceptos").empty();

	                 $.each(data['Conceptos'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id6.appendChild(option);
 	      		      });


		  const $id7 = document.querySelector("#empresa");


 	      		     $("#empresa").empty();

	                 $.each(data['Empresas'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id7.appendChild(option);
 	      		      });



		  const $id77 = document.querySelector("#sempresa");


 	      		     $("#sempresa").empty();

	                 $.each(data['Sempresas'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id77.appendChild(option);
 	      		      });

		  const $id778 = document.querySelector("#lempresa");


 	      		     $("#lempresa").empty();

	                 $.each(data['Empresas'], function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id778.appendChild(option);
 	      		      });



			 $('#empresa').val(data.empresa);
			$('#sempresa').val(data.empresa);

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
	           url: '/deleteConveniosProcedimientos/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("convenioId").value;

		        data2['valor'] = valor;	
		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableC= $("#tablaConveniosProcedimientos").dataTable().fnDestroy();	
	           initTableConveniosProcedimientos(data2);
			 

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
        $('body').on('click', '.editPostConveniosSuministros', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	$.ajax({
	           url: '/deleteConveniosSuministros/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("convenioId").value;

		        data2['valor'] = valor;	
		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableC= $("#tablaConveniosSuministros").dataTable().fnDestroy();	
	           initTableConveniosSuministros(data2);
			 

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
        $('body').on('click', '.editPostConveniosHonorarios', function () {
	
          var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));

	$.ajax({
	           url: '/deleteConveniosHonorarios/',
	            data : {post_id:post_id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("convenioId").value;

		        data2['valor'] = valor;	
		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableC= $("#tablaConveniosHonorarios").dataTable().fnDestroy();	
	           initTableConveniosHonorarios(data2);
			 

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
            scrollY: '350px',
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
            scrollY: '220px',
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



function initTableConveniosSuministros(data) {

	return new DataTable('.tablaConveniosSuministros', {
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
                          btn = btn + " <input type='radio'  class='form-check-input editPostConveniosSuministros' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 6
               }
            ],
            ajax: {
                 url:"/load_dataConveniosSuministros/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.codigoHomologado"},
                { data: "fields.id"},
                { data: "fields.tarifa"},
                { data: "fields.suministroId"},
                { data: "fields.suministroNombre"},
                { data: "fields.valor"},
        
            ]

 });
}



function initTableConveniosHonorarios(data) {

	return new DataTable('.tablaConveniosHonorarios', {
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
                          btn = btn + " <input type='radio'  class='form-check-input editPostConveniosHonorarios' data-pk='" + row.pk + "'>" + "</input>";
                        return btn;
                    },
                    "targets": 8
               }
            ],
            ajax: {
                 url:"/load_dataConveniosHonorarios/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.codigoHomologado"},
                { data: "fields.id"},
                { data: "fields.tarifa"},
                { data: "fields.suministroId"},
                { data: "fields.suministroNombre"},
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

			    $("#mensajes").html(data.message);


			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;

			 var valor = document.getElementById("convenioId").value;

		        data2['valor'] = valor;	
		        data2 = JSON.stringify(data2);
			   $("#mensajes").html(data.message);
			
		    tableC= $("#tablaConvenios").dataTable().fnDestroy();	
	           initTableConvenios(data2);






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
        var tiposTarifa = document.getElementById("xtiposTarifa").value; /*Obtener el SELECT */
        // var nombreTiposTarifa = tiposTarifa.options[tiposTarifa.selectedIndex].value; /* Obtener el valor */
        var xcups = document.getElementById("xcups").value;
        var valor = document.getElementById("valor").value;
	    var username_id = document.getElementById("username_id").value;
	    var convenioId = document.getElementById("convenioId").value;
	    var xconceptos = document.getElementById("xconceptos").value;





		$.ajax({
	           url: '/guardarConveniosProcedimientos/',
	            data :
	            {'codigoHomologado':codigoHomologado,  'tiposTarifa':tiposTarifa,
			    'xcups':xcups,  'valor':valor,
			    'username_id':username_id,   'convenioId':convenioId, 'xconceptos':xconceptos },
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

		            tableC= $("#tablaConveniosProcedimientos").dataTable().fnDestroy();
		   	        alert("ya destrui tablaConveniosProcedimientos");

	                    initTableConveniosProcedimientos(data2);
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
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("tiposTarifa1").value;
	var conceptos = document.getElementById("conceptos").value;
	var porcentage = document.getElementById("porcentage").value;
	var valorVariacion = document.getElementById("valorVariacion").value;
	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarTarifa/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId1,
			    username_id:username_id,
                            accion:'Crear'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosProcedimientos").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosProcedimientos");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosProcedimientos(data2);


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });



}



function BorrarTarifa()
{
	alert("Entre Borrar Tarifa no hago nada");
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("tiposTarifa1").value;
	var conceptos = document.getElementById("conceptos").value;
	var porcentage = document.getElementById("porcentage").value;
	var valorVariacion = document.getElementById("valorVariacion").value;
	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarTarifa/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId1,
			    username_id:username_id,
                            accion:'Borrar'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosProcedimientos").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosProcedimientos");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosProcedimientos(data2);


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });



}

////////////////////////////////
/// DESDE AQUIP SUMINISTROS
////////////////////////////////

function BtnAdicionarSuministro()
{
	alert("Entre Adicionar Suministro");

        var codigoHomologado = document.getElementById("scodHomologado").value;
        var tiposTarifa = document.getElementById("ttiposTarifa").value; /*Obtener el SELECT */

        var tsum = document.getElementById("tsum").value;
        var svalor = document.getElementById("svalor").value;
	    var username_id = document.getElementById("username_id").value;
	    var convenioId = document.getElementById("convenioId").value;
	    var tconceptos = document.getElementById("tconceptos").value;



		$.ajax({
	           url: '/guardarConveniosSuministros/',
	            data :
	            {'codigoHomologado':codigoHomologado,  'tiposTarifa':tiposTarifa,
			    'sum':tsum,  'valor':svalor,
			    'username_id':username_id,   'convenioId':convenioId, 'conceptos':tconceptos },
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

		            tableC= $("#tablaConveniosSuministros").dataTable().fnDestroy();
		   	        alert("ya destrui tablaConveniosSuministros");

	                    initTableConveniosSuministros(data2);

			document.getElementById("scodHomologado").value = '';
			
			document.getElementById("tsum").value ='';
			document.getElementById("svalor").value ='0';
			document.getElementById("tconceptos").value = '';


			                $("#mensajes").html(data.message);
                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}

function GrabarSuministro()
{
	alert("Entre Grabar Suministro  no hago nada");
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("stiposTarifa1").value;
	var conceptos = document.getElementById("sconceptos").value;
	var porcentage = document.getElementById("sporcentage").value;
	var valorVariacion = document.getElementById("svalorVariacion").value;
	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarSuministro/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId1,
			    username_id:username_id,
                            accion:'Crear'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosSuministros").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosSuministros");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosSuministros(data2);

			
			 document.getElementById("sconceptos").value = '';
			 document.getElementById("sporcentage").value = 0;
			 document.getElementById("svalorVariacion").value=0;


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });



}



function BorrarSuministro()
{
	alert("Entre Borrar Suministro no hago nada");
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("stiposTarifa1").value;
	var conceptos = document.getElementById("sconceptos").value;
	var porcentage = document.getElementById("sporcentage").value;
	var valorVariacion = document.getElementById("svalorVariacion").value;
	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarSuministro/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId,
			    username_id:username_id,
                            accion:'Borrar'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosSuministros").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosSuministros");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosSuministros(data2);


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });



}


////////////////////////////////
/// DESDE AQUIP HONORARIOS
////////////////////////////////

function BtnAdicionarHonorarios()
{
	alert("Entre Adicionar Honorario");

        var codigoHomologado = document.getElementById("lcodHomologado").value;
        var tiposTarifa = document.getElementById("ltiposTarifa").value; /*Obtener el SELECT */

        var lsum = document.getElementById("lsum").value;
        var lvalor = document.getElementById("lvalor").value;
	    var username_id = document.getElementById("username_id").value;
	    var convenioId = document.getElementById("convenioId").value;
	    var llconceptos = document.getElementById("llconceptos").value;
		var llhonorarios = document.getElementById("llhonorarios").value;
		var llcups = document.getElementById("llcups").value;



		$.ajax({
	           url: '/guardarConveniosHonorarios/',
	            data :
	            {'codigoHomologado':codigoHomologado,  'tiposTarifa':tiposTarifa,
			    'sum':lsum,  'valor':lvalor,
			    'username_id':username_id,   'convenioId':convenioId, 'conceptos':llconceptos,
			    honorarios:llhonorarios,
			    cups:llcups},
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

		            tableC= $("#tablaConveniosHonorarios").dataTable().fnDestroy();
		   	        alert("ya destrui tablaConveniosHonorarios");

	                    initTableConveniosHonorarios(data2);

			document.getElementById("lcodHomologado").value = '';
			
			document.getElementById("lsum").value ='';
			document.getElementById("lvalor").value ='0';
			document.getElementById("llconceptos").value = '';


			                $("#mensajes").html(data.message);
                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
	     });
}




function BorrarHonorarios()
{
	alert("Entre Borrar Suministro no hago nada");
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("ltiposTarifa1").value;
	var conceptos = document.getElementById("lconceptos").value;
	var porcentage = document.getElementById("lporcentage").value;
	var valorVariacion = document.getElementById("lvalorVariacion").value;
	var honorarios = document.getElementById("lhonorarios").value;
	var cups = document.getElementById("lcups").value;

	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarHonorarios/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId,
			    username_id:username_id,
			    honorarios:honorarios,
			    cups:cups,
                            accion:'Borrar'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosHonorarios").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosHonorarios");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosHonorarios(data2);


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });
}

function GrabarHonorarios()
{
	alert("Entre Grabar Suministro  no hago nada");
	var convenioId = document.getElementById("convenioId1").value;
          alert("convenio =  " +convenioId1);

	
	var tiposTarifa = document.getElementById("ltiposTarifa1").value;
	var conceptos = document.getElementById("lconceptos").value;
	var porcentage = document.getElementById("lporcentage").value;
	var valorVariacion = document.getElementById("lvalorVariacion").value;
	var honorarios = document.getElementById("lhonorarios").value;
	var cups = document.getElementById("lcups").value;
	var convenioId1 = document.getElementById("convenioId1").value;
	alert("convenioId1 =" + convenioId1);	
	var username_id = document.getElementById("username_id").value;
         

	$.ajax({
	           url: '/grabarHonorarios/',
	            data : {tiposTarifa:tiposTarifa,
			    conceptos:conceptos,
			    porcentage:porcentage,
			    valorVariacion:valorVariacion,
			    convenioId1:convenioId1,
			    username_id:username_id,
			    honorarios:honorarios,
			    cups:cups,

                            accion:'Crear'},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {
                        alert("Regrese");
                       alert("data y escribir en mensajes="  + data);

			 var data2 =  {}   ;
			data2['username'] = username;
		        data2['sedeSeleccionada'] = sedeSeleccionada;
		        data2['nombreSede'] = nombreSede;
		        data2['sede'] = sede;
		        data2['username_id'] = username_id;
		        data2['valor'] = convenioId;	
		        data2 = JSON.stringify(data2);


		    tableC= $("#tablaConveniosHonorarios").dataTable().fnDestroy();
		   	 alert("ya destrui tablaConveniosHonorarios");
			
		alert("DATA CON QUE CREO EL DATATABLE = " + data);


	           initTableConveniosHonorarios(data2);

			
			 document.getElementById("lconceptos").value = '';
			 document.getElementById("lporcentage").value = 0;
			 document.getElementById("lvalorVariacion").value=0;


			    $("#mensajes").html(data.message);
		

                  },
	   		    error: function (request, status, error) {
	   			    $("#mensajes").html("Error:");
	   	    	}
	     });



}









