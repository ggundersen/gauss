var GAUSS = (function() {

	function get_input() {
		var input_value = document.getElementById('user_input').value;
		if (validate_input(input_value)) {
			return input_value;
		} else {
			alert('Please input an integer.');
			return;
		}
	};

	function validate_input(user_input) {
		return user_input % 1 === 0;
	};

	function render_answer(json_response) {
		var objJSON = eval('(function(){return ' + json_response + ';})()');
		document.getElementById('canvas').innerHTML = '<p class="runtime">Runtime: ' + objJSON.runtime + ' seconds</p>';
	};

	return {

		get_input: get_input,

		get_answer: function() {

			var requestObj = new XMLHttpRequest();
			var input = get_input();
			
			if (input === undefined) { return; }

			requestObj.onreadystatechange = function() {
				if (requestObj.readyState === 4 && requestObj.status === 200) {
					console.log(requestObj.responseText);
					render_answer(requestObj.responseText); // document.getElementById('canvas').innerHTML = requestObj.responseText;
				}
			}
			requestObj.open('GET', '/api/q=pe2&n=' + input, true);
			requestObj.send();
		}

	}; // end return object
})(); // end GAUSS module