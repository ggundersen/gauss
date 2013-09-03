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


    var getUrlParameters = function() {

        var params = {};
        var qs = window.location.pathname.replace(/\//, '');
        var pairs = qs.split('&');
        for (var i=0; i<pairs.length; i++) {
            var kv = pairs[i].split('=');
            params[kv[0]] = kv[1];
        }
        return params;
    };


    var maskAnswer = function(answer) {

        var s = answer.slice(0, length-2).replace(/[0-9]/g, '*');
        var e = answer.slice(length-2);
        return s+e;
    };


    var runProblem = function(problem_id, callback) {
        callAjax('/api/problem=' + problem_id, callback);
    };


    var renderProblem = function(json) {

        var $content = $('#content');
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
                '<a href="/test=' + json['id']   + '">Problem: ' + json['id']         + '</a><br>' +
                '<span class="'   + answerClass  + '">Answer: '  + json['calculated'] + '</span><br>' +
                '<span class="'   + runtimeClass + '">Runtime: ' + json['runtime']    + '</span><br>' +
            '</li>'

        if ($content.children().length) {
            $content.children().last().append(template);
        }
        else {
            $content.append(template);
        }
    };


    window.onload = (function() {
        var params = getUrlParameters(); 
        var problem = params['test'];

        if (problem === 'all') {
            runProblem(1, renderProblem);
            runProblem(2, renderProblem);
            runProblem(3, renderProblem);
            runProblem(4, renderProblem);
            runProblem(5, renderProblem);
            runProblem(6, renderProblem);
            runProblem(7, renderProblem);
            runProblem(8, renderProblem);
            runProblem(9, renderProblem);
            runProblem(10, renderProblem);
        }
        else {
            runProblem(problem, renderProblem)
        }
    })();

})();