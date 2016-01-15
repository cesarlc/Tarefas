$(document).ready(function(){
	// setInterval(function(){
		
	// 	if($('#slide .ativo').next().size()) //verifica se existem a próxima imagem
	// 	{	
	// 		//remove a classe ativo e adiciona no próximo
	// 		$(".ativo").fadeOut().removeClass("ativo").next().fadeIn().addClass('ativo');
	// 	}
	// 	else
	// 	{
	// 		//remove a classe a ativo e adiciona no primeira posição
	// 		$(".ativo").fadeOut().removeClass("ativo");
	// 		$("#slide img:eq(0)").fadeIn().addClass("ativo");
	// 	}
	// },2000);
	
	$('#add-img').on('click', function(){
		$('#imagem').clone().insertAfter('#imagem:last');
		$('#imagem:last').prop('class', 'mais_imagens');
		$('#imagem:last').addClass('form-control');
		$('#remove-img').removeClass('disabled');
	});
	$('#remove-img').on('click', function(){
		conta = $('.mais_imagens').length;
		if (conta == 1){
			$('#remove-img').addClass('disabled');
		}
		$('.mais_imagens:last').remove();

	});


});