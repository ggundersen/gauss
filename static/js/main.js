var GAUSS = (function() {


    var get_JSON = function(url, callback) {

        var request = new XMLHttpRequest();
        request.open('GET', url);
        request.onreadystatechange = function() {
            if (request.readyState === 4 && request.status === 200) {
                callback(JSON.parse(request.responseText));
            }
        };
        request.send();
    };


    var get_url_parameters = function() {

        var params = {};
        var qs = window.location.pathname.replace(/\//, '');
        var pairs = qs.split('&');
        for (var i=0; i<pairs.length; i++) {
            var kv = pairs[i].split('=');
            params[kv[0]] = kv[1];
        }
        return params;
    };


    var render_problems = function(json) {

        var $content = $('#content');
        var content = document.getElementById('content');
        var li = content.getElementsByTagName('li');
        var answer_class;
        var i;
        var key;
        var keys = Object.keys(json);
        var obj;
        var runtime_class;
        var template;
        var $thisLi;
        var thisLi;

        console.log(json);

        for (i in keys) {
            key = keys[i]
            obj = json[key];

            if (obj.correct) {
                answer_class = 'pass';
            } else {
                answer_class = 'fail';
            }
            if (obj.runtime > 20) {
                runtime_class = 'fail';
            } else if (obj.runtime > 10) {
                runtime_class = 'lowpass';
            } else {
                runtime_class = 'pass';
            }

            if (document.title === 'Gauss - Problems Test Suite') {
                //var template = document.createElement('li');
                template =
                    '<li>' +
                        '<a href="/test=problem&q=' + key + '">Problem ' + key + '</a><br>' +
                        '<span>' + obj.title + '</span><br>' +
                        '<span class="' + answer_class  + '">Answer: ' + obj.answer + '</span><br>' +
                        '<span class="' + runtime_class + '">Runtime: ' + obj.runtime + '</span><br>' +
                    '</li>';
            } else {
                 template =
                    '<li>' +
                        '<span>' + obj.title + '</span><br>' +
                        '<span class="' + answer_class + '">Answer: ' + obj.answer + '</span><br>' +
                        '<span class="' + runtime_class + '">Runtime: ' + obj.runtime + '</span><br>' +
                    '</li>';         
            }

            /*if (typeof li !== 'undefined') {
                thisLi = li[li.length - 1];
                thisLi.appendChild(template);
                //$thisLi.last().after(template);
                //$thisLi.show(600);  
            } else {
                content.appendChild(template);
                //thisLi = li[0];
                //$content.find('li').first().show(600);
            }*/

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


    var run_all_problems = function() {

        // fast problems
        get_JSON('/api/problems=1,2,5,6', render_problems);
        get_JSON('/api/problems=7,11,13,14', render_problems);
        get_JSON('/api/problems=14,15,16,17', render_problems);
        get_JSON('/api/problems=18,19,20', render_problems);

        // slow problems
        get_JSON('/api/problems=4', render_problems);
        get_JSON('/api/problems=9', render_problems);
        get_JSON('/api/problems=10', render_problems);
        get_JSON('/api/problems=12', render_problems);

        // broken problems
        //get_JSON('/api/problems=8', render_problems);
    };


    window.onload = function() {

        var params = get_url_parameters();
        var test = params['test'];
        var q = params['q'];

        if (test ==='problem' && q === 'all') {
            run_all_problems();
        }
        else if (test ==='problem') {
            get_JSON('/api/problems=' + q, render_problems);
        }
        else {
            // test === 'gmath' &c.
        }
    };
})();