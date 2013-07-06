PXG = {};

PXG.make_query = function() {
	return $.ajax({
		dataType: 'json',
		url: '/api/q=pe1'
	});
};

PXG.render_result = function(magic) {
	var grid = '';
	for (i = 1; i < magic[0].length; i++) {
		if (magic[0].indexOf(i) > -1 && magic[1].indexOf(i) > -1) {
			grid += '<div class="cell highlight both"></div>';
		}
		else if (magic[0].indexOf(i) > -1) {
			grid += '<div class="cell highlight three"></div>';			
		}
		else if (magic[1].indexOf(i) > -1) {
			grid += '<div class="cell highlight five"></div>';			
		}
		else {
			grid += '<div class="cell"></div>';
		}
	}
	$('#content').append(grid);
};

$(function() {
	$('button.run').on('click', function() {
		PXG.make_query().done(function(r) {
			PXG.render_result(r);
		});
	});
});