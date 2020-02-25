$(function(){

	var error_area = false;
	var error_room_num = false;
	var error_hall_num = false;

	$('#area').blur(function() {
		check_name();
	});

	$('#room_num').blur(function() {
		check_room_num();
	});

	$('#hall_num').blur(function() {
		check_hall_num();
	});

	function check_name(){
		var area = $('#area').val();
		var re01 = /^\d{2,4}.\d{0,2}$/;
		if(re01.test(area))
		{
			$('#area').next().hide();
			error_area = false;
		}
		else
		{
			$('#area').next().html('请输入正确的面积')
			$('#area').next().show();
			error_area = true;
		}
	}

	function check_room_num(){
		var room_num = $('#room_num').val();
		var re01 = /^\d{1}$/;
		if(re01.test(room_num))
		{
			$('#room_num').next().hide();
			error_room_num = false;
		}
		else
		{
			$('#room_num').next().html('请输入正确的房间数')
			$('#room_num').next().show();
			error_room_num = true;
		}
	}

	function check_hall_num(){
		var hall_num = $('#hall_num').val();
		var re01 = /^\d{1}$/;
		if(re01.test(hall_num))
		{
			$('#hall_num').next().hide();
			error_hall_num = false;
		}
		else
		{
			$('#hall_num').next().html('请输入正确的客厅数')
			$('#hall_num').next().show();
			error_hall_num = true;
		}
	}

})