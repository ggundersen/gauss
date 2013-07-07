(function(G) {

	G.render = function(json_data) {

	var table = d3.select('body').append('table');
	var rows = table.selectAll('tr').data(json_data).enter().append('tr');
	rows.selectAll('td')
		.data(
			function(d) {
				return d;
			})
		.enter()
		.append('td')
		.attr('id',
			function(d) {
				return d;
			})
		.attr('class', 'cell');

	};

	G.make_query = function() {
		return $.ajax({
			dataType: 'json',
			url: '/api/q=pe1'
		});
	};

	$(function() {
		$('button.run').on('click', function() {
			G.make_query().done(function(r) {
				G.render(r);
			});
		});
	});

})(GAUSS = {});