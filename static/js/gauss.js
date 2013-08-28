var GAUSS = (function() {


	//var problemList = document.getElementById('problemList');


	var call_ajax = function(url, callback) {

		var requestObj = new XMLHttpRequest();
		requestObj.onreadystatechange = function() {
			if (requestObj.readyState === 4 && requestObj.status === 200) {
				var json = JSON.parse(requestObj.responseText);

				render_problem(json);
			}
		}
		requestObj.open('GET', url, true);
		requestObj.send();

	};


	var render_problem = function(json) {
		var problemList = document.getElementById('problemList');
		var child = document.createElement('li');
		child.innerHTML = json['answer'];
		problemList.appendChild(child);
	};


	var run_problem = function(problem_id) {
		call_ajax('/api/problem=' + problem_id, render_problem);
	};


	return {
		run_problem: run_problem
	}

})();

window.onload = function() {

	GAUSS.run_problem(2, GAUSS.render_callback);
	//alert(answer);

};