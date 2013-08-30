var GAUSS = (function() {


    var callAjax = function(url, callback) {

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


    var maskAnswer = function(answer) {

        return answer;
    };


    var testProblem = function(json) {

        var $pl = $('#problemList');
        var answerClass;
        var runtimeClass;
        var template;

        // Check answer
        if (json['calculated'] !== json['correct']) {
            answerClass = 'fail';
        }
        else {
            json['calculated'] = maskAnswer(json['calculated']);
            answerClass = 'pass';
        }

        // Check runtime
        if (json['runtime'] > 60) {
            runtimeClass = 'fail';
        }
        else if (json['runtime'] > 10) {
            runtimeClass = 'lowpass';
        }
        else {
            runtimeClass = 'pass';
        }

        template =
            '<li>' +
                '<span>Problem: ' + json['id'] + '</span><br>' +
                '<span class="' + answerClass + '">Answer: ' + json['calculated'] + '</span><br>' +
                '<span class="' + runtimeClass + '">Runtime: ' + json['runtime'] + '</span><br>' +
            '</li>'

        if ($pl.children().length) {
            $pl.children().last().append(template);
        }
        else {
            $pl.append(template);
        }
    };


    var runProblem = function(problem_id) {
        callAjax('/api/problem=' + problem_id, testProblem);
    };


    return {
        runProblem: runProblem
    }
})();