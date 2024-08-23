var $ = jQuery;
console.log('Hola Alberto Hi!')

var datavta;
var seriali = new Array();
var serialiLab = new Array();
var serialiRad = new Array();
var serialiTer = new Array();
var serialiDiag = new Array();
var serialiAnt = new Array();
var serialiInt = new Array();


var seriali2 = new Array();
var envio = new FormData()
var envio1 = new FormData()
var envio2 = new FormData()
var envioLab = new FormData()
var envioRad = new FormData()
var envioTer = new FormData()

var envioDiag = new FormData()
var formData = new FormData()
var envio_final = new FormData()
var envio_finalRad = new FormData()
var envio_final1 = new FormData()

var x=0
var  folio_final =0

const form = document.getElementById('formHistoria')

const form2 = document.getElementById('formClinicos')
console.log(form)
console.log(form2)


function valida(forma)
{



	};


$('.editPostar').on('click',function(event)
{
 	 alert("Entre a editPostt"); 
	 var post_id = $(this).data('pk');
          alert("pk1 = " + $(this).data('pk'));


	});


