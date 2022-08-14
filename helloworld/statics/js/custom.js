$("#addForm").submit(function(e){
    e.preventDefault()
	$.ajax({
		data:$(this).serialize(),
		method:'POST',
		url:$(this).attr('action'),
		dataType:'json',
		success:function(res){
			if(res.bool==true){
				$(".ajaxRes").html('Data has been added.');
                $("#reset").trigger('click');
                alert('Your Rate Added!')
                location.reload();
            }
        }
    });
    e.preventDefault();
});