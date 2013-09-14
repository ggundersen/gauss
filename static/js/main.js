(function() {


    var LOW_PASS = 10,
        SOLVED_PROBLEMS = [
        1,2,3,4,5,6,7,9,10,
        11,12,13,14,15,16,17,18,19,20,
        21,
        //22,
        23,24,25,26,27,28,29,30,
        //40,41,42,43,45,46,47,48,49,50,
        //52,
        //62,67
    ];


    var build_template = function(key, obj) {
        
        var answer_class = obj.correct ? 'pass' : 'fail',
            runtime_class = (obj.runtime < LOW_PASS) ? 'pass' : 'fail',
            has_passed = (answer_class === 'pass' && runtime_class === 'pass') ? true : false,
            href = '/test=problem&q=' + key,
            anchor = document.createElement('a'),
            answer = document.createElement('div'),
            runtime = document.createElement('div'),
            template = document.createElement('li'),
            title = document.createElement('div');

        anchor.innerHTML = 'Problem ' + key;
        anchor.setAttribute('href', href);
        title.innerHTML = obj.title;
        answer.innerHTML = 'Answer: ' + obj.answer;
        answer.className = answer_class;
        runtime.innerHTML = 'Runtime: ' + obj.runtime;
        runtime.className = runtime_class;
        
        if (document.title === 'Gauss - Test Suite') {    // TODO : This seems fragile
            template.appendChild(anchor);
            template.appendChild(title);
            template.appendChild(answer);
            template.appendChild(runtime);
            render_progress_bar(key, has_passed, false);
        } else {
            template.appendChild(title);
            template.appendChild(answer);
            template.appendChild(runtime);
        }

        return template;
    };


    var init_progress_bar = function() {

        var div, i,
            DOCUMENT_WIDTH = 400,
            DIV_WIDTH = '19px',
            progress = document.getElementById('progress');

        for (i in SOLVED_PROBLEMS) {
            div = document.createElement('div');
            div.className = 'bar';
            div.id = 'div' + SOLVED_PROBLEMS[i];
            div.style.width = DIV_WIDTH;
            progress.appendChild(div);
        }
    };


    var get_JSON = function(url, callback) {

        var i, problems,
            request = new XMLHttpRequest();
        
        request.timeout = 60000;
        request.onreadystatechange = function() {
            if (request.readyState === 4 && request.status === 200) {
                callback(JSON.parse(request.responseText));
            }
        };
        // assume 505 error caused by GAE timing out Python script
        request.ontimeout = function() {
            problems = url.match(/problems=(.*)/)[1].split(',');
            for (i in problems) {
                console.log(problems[i]);
                render_progress_bar(problems[i], false, true);
            }
        };
        request.open('GET', url);
        request.send();
    };


    var get_url_parameters = function() {

        var i,
            params = {},
            qs = window.location.pathname.replace(/\//, ''),
            pairs = qs.split('&');

        for (i in pairs) {
            var kv = pairs[i].split('=');
            params[kv[0]] = kv[1];
        }
        return params;
    };


    var render_problems = function(json) {

        var i, key, obj, template, 
            keys = Object.keys(json),
            content = document.getElementById('content');

        for (i in keys) {
            key = keys[i];
            obj = json[key];
            template = build_template(key, obj);
            content.appendChild(template);
        }
    };


    var render_progress_bar = function(key, has_passed, has_timedout) {

        var div = document.getElementById('div' + key);
        div.style.background = has_timedout ? '#000000' : (has_passed ? '#2b91af' : '#c82829');
        div.style['border-left'] = '1px solid #fff';
    };


    var run_all_problems = function() {

        var i,
            queries = [
                '/api/problems=1,2,5',
                '/api/problems=6,7,11',
                '/api/problems=13,14,15',
                '/api/problems=16,17,18',
                '/api/problems=19,20,21',
                // where is 22?
                '/api/problems=23,24,25',
                '/api/problems=26,27,28',
                '/api/problems=29,30',
                '/api/problems=3',
                '/api/problems=4',
                '/api/problems=9',
                '/api/problems=10',
                '/api/problems=12',
            ];
        for (i in queries) {
            get_JSON(queries[i], render_problems);
        }
    };


    window.onload = function() {

        var params = get_url_parameters();
        var test = params['test'];
        var q = params['q'];

        if (test ==='problem' && q === 'all') {
            init_progress_bar();
            run_all_problems();
        }
        else if (test ==='problem') {
            get_JSON('/api/problems=' + q, render_problems);
        }
    };
})();