var totalDeuda=0;

$(".subtotal").each(function(){ //subtotal poner en la fila monto como class
	totalDeuda+=parseInt($(this).html()) || 0;
});
$('#resultado_total').html(totalDeuda.toFixed(2)); //id="resultado_total"  dodne lo muestro