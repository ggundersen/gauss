var GAUSS = (function() {

	function get_problem_id() {
		var m = document.getElementsByTagName('meta');
		return m[0].getAttribute('name');
	};

	/*function get_default_input() {
		return 1;
	};

	function get_input() {
		var input = document.getElementById('user_input').value;
		if (validate_input(input)) {
			return input;
		} else {
			alert('Please input an integer.');
			return;
		}
	};

	function validate_input(user_input) {
		return user_input % 1 === 0 && user_input !== '';
	};*/

	return {

		/*render_answer: function(json_response) {
			var objJSON = eval('(function(){return ' + json_response + ';})()');
			document.getElementById('canvas').innerHTML = '' +
				'<p class"answer">Answer: ' + objJSON.answer + '</p>' + 
				'<p class="runtime">Runtime: ' + objJSON.runtime + ' seconds</p>';
		},*/

		request_answer: function(callback, input) {

			var requestObj = new XMLHttpRequest();
			var problem_id = get_problem_id();
			var url = '/api/q=' + problem_id + '&n=' + input;

			requestObj.onreadystatechange = function() {
				if (requestObj.readyState === 4 && requestObj.status === 200) {
					callback(requestObj.responseText);
				}
			}

			requestObj.open('GET', url, true);
			requestObj.send();
		}

	}; // end return object
})(); // end GAUSS module