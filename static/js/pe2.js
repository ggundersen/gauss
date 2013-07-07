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
			.attr('class',
				function(d) {
					return 'cell cell' + d;
			});
	};

	G.make_query = function(divisor) {
		return $.ajax({
			dataType: 'json',
			url: '/api/q=pe2&n=' + divisor
		});
	};

	$(function() {
		$('button.run').on('click', function() {
			var divisor = $('#divisor').val();
			G.make_query(divisor).done(function(response) {
				G.render(response);
			});
		});
	});

})(GAUSS = {});

