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
        var answerClass;
        var template;

        if (json['calculated'] !== json['correct'] || json['runtime'] > 100) {
            answerClass = 'fail';
        }
        else {
            answerClass = 'pass';
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


    return {
        run_problem: run_problem
    }
})();