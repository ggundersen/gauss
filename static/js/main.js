var GAUSS = (function() {


    var problemCache = {};


    var cacheProblem = function(json) {

        var i;
        var key;
        var keys = Object.keys(json);
        var obj;

        for (i in keys) {
            key = keys[i]
            problemCache[key] = json[key];
        }

        console.log(problemCache);
    };


    var callAjax = function(url, callback) {

        $.ajax({
            url: url,
            dataType: 'json',
            success: function(response) {
                callback(response);
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


    var renderProblems = function(json) {

        var $content = $('#content');
        var answerClass;
        var i;
        var key;
        var keys = Object.keys(json);
        var obj;
        var runtimeClass;
        var template;
        var $thisLi;

        for (i in keys) {
            key = keys[i]
            obj = json[key];
            if (obj.correct) {
                answerClass = 'pass';
            }
            else {
                answerClass = 'fail';
            }

            // Check runtime
            if (obj.runtime > 20) {
                runtimeClass = 'fail';
            }
            else if (obj.runtime > 10) {
                runtimeClass = 'lowpass';
            }
            else {
                runtimeClass = 'pass';
            }

            if (document.title === 'Gauss - Problems Test Suite') {
                template =
                    '<li>' +
                        '<a href="/test=problem&q=' + key + '">Problem ' + key + '</a><br>' +
                        '<span>Title: ' + obj.title + '</span><br>' +
                        '<span class="' + answerClass  + '">Answer: ' + obj.answer + '</span><br>' +
                        '<span class="' + runtimeClass + '">Runtime: ' + obj.runtime + '</span><br>' +
                    '</li>';
            }
            else {
                 template =
                    '<li>' +
                        '<span>Title: ' + obj.title + '</span><br>' +
                        '<span class="' + answerClass + '">Answer: ' + obj.answer + '</span><br>' +
                        '<span class="' + runtimeClass + '">Runtime: ' + obj.runtime + '</span><br>' +
                    '</li>';           
            }

            if ($content.find('li').length) {
                $thisLi = $content.find('li').last();
                $thisLi.last().after(template);
                $thisLi.show(600);
            }
            else {
                $content.append(template);
                $content.find('li').first().show(600);
            }
        }
    };


    var runAllProblems = function() {

        // fast problems
        callAjax('/api/problems=1,2,5', renderProblems);
        callAjax('/api/problems=6,7,11', renderProblems);
        callAjax('/api/problems=13,14', renderProblems);

        // slow problems
        callAjax('/api/problems=4', renderProblems);
        callAjax('/api/problems=5', renderProblems);
        callAjax('/api/problems=9', renderProblems);
        callAjax('/api/problems=10', renderProblems);
        callAjax('/api/problems=12', renderProblems);

        // broken problems
        //callAjax('/api/problems=8', renderProblems);
    };


    var cacheAllProblems = function() {

        // fast problems
        callAjax('/api/problems=1,2,5', cacheProblem);
    };


    window.onload = (function() {

        var params = getUrlParameters();
        var test = params['test'];
        var q = params['q'];

        if (test ==='problem' && q === 'all') {
            runAllProblems();
        }
        else if (test ==='problem') {
            callAjax('/api/problems=' + q, renderProblems);
        }
        else {
            // test === 'gmath' &c.
        }
    })();


    /*window.onload = (function() {

        cacheAllProblems();

        var params = getUrlParameters();
        var test = params['test'];
        var q = params['q'];
        if (test ==='problem' && q === 'all') {
            while (true) {    // loop forever, check the cache, render problem and remove from cache if complete
                if (problemCache) {
                    for (i in problemCache) {
                        renderProblems(problemCache[i]);
                        delete problemCache[i];
                    }
                }
            }
        }
    })();*/
})();