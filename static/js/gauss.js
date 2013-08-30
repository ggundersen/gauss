var GAUSS = (function() {


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
        var answerClass1;
        var answerClass2;
        var template;

        if (json['calculated'] !== json['correct']) {
            answerClass1 = 'fail';
        }
        if (json['runtime'] > 100) {
            answerClass2 = 'fail'
        }
        else {
            answerClass1 = 'pass';
        }

        template =
            '<li>' +
                '<span>Problem: ' + json['id'] + '</span><br>' +
                '<span class="' + answerClass1 + '">Answer: ' + json['calculated'] + '</span><br>' +
                '<span class="' + answerClass2 + '">Runtime: ' + json['runtime'] + '</span><br>' +
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


    return {
        run_problem: run_problem
    }
})();