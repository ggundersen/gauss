(function() {


    var call_ajax = function(url, callback) {

        $.ajax({
            url: url,
            dataType: 'json',
            success: function(response) {
                callback(response);
            }
        });
    };

    var render_problem = function(json) {

        var $pl = $('#problemList');
        var html = '<li>' +
                '<p>Problem: ' + json['id'] + '</p>' +
                '<p>Answer: ' + json['answer'] + '</p>' +
                '<p>Runtime: ' + json['runtime'] + '</p>' +
            '</li>'

        if ($pl.children().length) {
            $pl.children().last().append(html);
        }
        else {
            $pl.append(html);
        }
    };


    var run_problem = function(problem_id) {

        call_ajax('/api/problem=' + problem_id, render_problem);
    };


    window.onload = function() {

        //run_problem(9);
        for (var i; i<10; i++) (function(n) {
        	setTimeout(function() {
                run_problem(n);
            }, 0)(i);
        });
        
    };

})();