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
        if (json['runtime'] > 20) {
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
                '<a href="/test=problem&q=' + json['id']   + '">Problem: ' + json['id']         + '</a><br>' +
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


    var renderGmath = function(json) {
        var $content = $('#content');
        var template = '<div>' + json['calculated'] + '</div>';
        $content.append(template)
    };


    var runAllProblems = function() {
        for (var i=1; i<11; i++) {
            callAjax('/api/problem=' + i, renderProblem);
        }
    };


    var runAllGmath = function() {
        callAjax('/api/gmath=is_prime', renderGmath);
    };


    window.onload = (function() {
        var params = getUrlParameters();
        var test = params['test'];
        var q = params['q'];

        if (test ==='problem' && q === 'all') {
            runAllProblems();
        }
        else if (test ==='problem') {
            callAjax('/api/problem=' + q, renderProblem);
        }
        else if (test ==='gmath' && q === 'all') {
            runAllGmath();
        } 
        else { }
    })();
})();