GAUSS.setup_canvas = function() {
	var chart = d3.select('#canvas')
		.append('svg')
		.attr('width', 1000)
		.attr('height', 300);  
};

GAUSS.get_all_runtimes = function(json) {

};

GAUSS.render_answer = function(json_response) {

	var objJSON = eval('(function(){return ' + json_response + ';})()');
	
	/*var data = GAUSS.get_all_runtimes(objJSON);

	d3.select('#canvas').selectAll('div')
			.data(data)
		.enter().append('div')
			.style('width', function(d) { return d * 10 + "px"; })
			.text(function(d) { return d; });*/

	var canvas = document.getElementById('canvas');
	var div = document.createElement('div');
	div.style.width  = '8px'; //Math.ceil((objJSON.runtime * 3000)) + 'px';
	div.style.height = Math.ceil((objJSON.runtime * 3000)) + 'px';
	div.style.float  = 'left';
	div.style.background = 'blue';
	div.style.margin = '0 1px';
	//div.innerHTML = objJSON.runtime;

	canvas.appendChild(div);

};

window.onload = function() {

	for (var x=1000; x<50000; x += 1001) {
		//console.log(x);
		GAUSS.request_answer(GAUSS.render_answer, x);
	}

};