(function(G) {

	/*G.render = function(json_data) {
		$('#canvas').empty(); // clean slate every rendering
		var table = d3.select('#canvas').append('table');
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
	};*/

	G.make_query = function(divisor) {
		return $.ajax({
			dataType: 'json',
			url: '/api/q=pe2&n=' + divisor
		});
	};

	G.validate_input = function(input) {
		return input % 1 === 0;
	};

	$(function() {
		$('button.run').on('click', function() {
			var input = $('input#divisor').val();
			if (G.validate_input(input) === false || input === '') {
				alert('Please enter an integer');
				return;
			}
			G.make_query(input).done(function(response) {
				//G.render(response);
				$('#canvas').append(response);
			});
		});
	});

})(GAUSS = {});

