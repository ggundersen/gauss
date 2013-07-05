$(function() {
	$.ajax({
		dataType: 'html',
		url: '/api/q=pe1'
	}).done(function(data) {
		console.log(data);
	});
});