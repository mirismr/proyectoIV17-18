$("a").hover(
  	function() {
	  $( this ).rotate({angle:0,animateTo:360})
	},
	function() {
		$( this ).rotate({angle:360,animateTo:0})
	}
);

$("a.unete").hover(
  	function() {
	  $( "#registrate" ).animate({opacity: [ 0, "linear" ]},600, function() { $("#registrate").hide(); });
	},
	function() {
		$( "#registrate" ).animate({opacity: [ 1, "linear" ]},600, function() { $("#registrate").show(); });
	}


);

indice = 1;

function peticion_ajax( num_pagina ) {
  $.ajax({
    
    // The URL for the request
    url: "/obtener_restaurantes",
    

    data: {
      pagina: num_pagina
    },
    // Whether this is a POST or GET request
    type: "GET",
 
    // The type of data we expect back
    dataType : "json",
}).done(function ( json ) {
    indice = num_pagina;
    var lista = '';
    for(i=0; i<10 && i<json.length; i++) {
      var fila = '';
      fila += "<tr>";
      fila += "<td>"+json[i].address.street+"</td>";
      fila += "<td>"+json[i].borough+"</td>";
      fila += "<td>"+json[i].cuisine+"</td>";
      fila += "<td>"+json[i].name+"</td>";
      fila += "<td>"+json[i].restaurant_id+"</td>";
      fila += "</tr>";
      lista += fila;
    }
    $('#listado').html(lista);

  var boton = '';
  var lista_botones = '';

  if (json.length < 10 ) {
    boton = "<li class='page-item active'><a class='page-link' href='#' onclick='peticion_ajax("+(indice)+")'>"+indice+"</a></li>";
    lista_botones+=boton;
  }else {
    boton = "<li class='page-item'><a class='page-link' href='#' onclick='peticion_ajax("+(indice-1)+")'>Anterior</a></li>";
    lista_botones+=boton;
    boton = "<li class='page-item active'><a class='page-link' href='#' onclick='peticion_ajax("+(indice)+")'>"+indice+"</a></li>";
    lista_botones+=boton;
    for(i=indice+1; i<indice+3; i++) {
      boton = "<li class='page-item'><a class='page-link' href='#' onclick='peticion_ajax("+i+")'>"+i+"</a></li>";
      lista_botones += boton;
    }
    
    boton = "<li class='page-item'><a class='page-link' href='#' onclick='peticion_ajax("+(indice+1)+")'>Siguiente</a></li>";
    lista_botones += boton;
  }

  
  $('#botones').html(lista_botones);

  });
}


$("#busqueda").click(function() {
  peticion_ajax(1);
});
  


$(document).ready(function(){
  
  // Donde queremos cambiar el tamaño de la fuente
  var donde = $('p');
  var sizeFuenteOriginal = donde.css('font-size');
  var colorOriginalContainer = $('.container').css('background-color');
  var colorOriginalLink = $('.container').css('background-color');
  
  // Resetear
  $(".resetearFont").click(function(){
  	donde.css('font-size', sizeFuenteOriginal);
	$('.container').css('background-color', colorOriginalContainer);
	$('a').css('background-color', colorOriginalLink);
  });
 
  // Aumentar Font Size
  $(".aumentarFont").click(function(){
  	var sizeFuenteActual = donde.css('font-size');
 	var sizeFuenteActualNum = parseFloat(sizeFuenteActual, 10);
    var sizeFuenteNuevo = sizeFuenteActualNum*1.2;
	donde.css('font-size', sizeFuenteNuevo);
	return false;
  });
 
  // Disminuir Font Size
  $(".disminuirFont").click(function(){
  	var sizeFuenteActual = donde.css('font-size');
 	var sizeFuenteActualNum = parseFloat(sizeFuenteActual, 10);
    var sizeFuenteNuevo = sizeFuenteActualNum*0.8;
	donde.css('font-size', sizeFuenteNuevo);
	return false;
  });

  //Cambiar color
  $(".cambiarColor").click(function(){
  	$('.container').css('background-color', "#ff0000");
  	$('a').css('background-color', "#00ff00");

	return false;
  });
  
});