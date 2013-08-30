(function() {


    var call_ajax = function(url, callback) {

        $.ajax({
            url: url,
            dataType: 'json',
            success: function(response) {
                callback(response);
            },
            error: function(e) {
                console.log(e);
            }
        });
    };

    var render_problem = function(json) {

        var $pl = $('#problemList');
        var answerClass;
        var template;

        if (json['calculated'] === json['correct']) {
            answerClass = 'pass';
        }
        else {
            answerClass = 'fail';
        }

        template =
            '<li>' +
                '<span>Problem: ' + json['id'] + '</span><br>' +
                '<span class="' + answerClass + '">Answer: ' + json['calculated'] + '</span><br>' +
                '<span>Runtime: ' + json['runtime'] + '</span><br>' +
            '</li>'

        if ($pl.children().length) {
            $pl.children().last().append(template);
        }
        else {
            $pl.append(template);
        }
    };


    var run_problem = function(problem_id) {
        call_ajax('/api/problem=' + problem_id, render_problem);
    };


    window.onload = function() {

        run_problem(1);
        run_problem(2);
        run_problem(3);
        run_problem(4);
        run_problem(5);
        run_problem(6);
        run_problem(7);
        run_problem(8);
        run_problem(9);
        run_problem(10);
    };

})();

