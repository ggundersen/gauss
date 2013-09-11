(function() {


    var build_template = function(key, obj) {
        
        var answer_class = obj.correct ? 'pass' : 'fail',
            anchor = document.createElement('a'),
            answer = document.createElement('div'),
            has_passed = answer_class === 'pass' ? true : false,
            href = '/test=problem&q=' + key,
            runtime = document.createElement('div'),
            runtime_class = (obj.runtime < 1) ? 'pass' : 'fail',
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
            render_progress_bar(key, has_passed);
        } else {
            template.appendChild(title);
            template.appendChild(answer);
            template.appendChild(runtime);
        }

        return template;
    };


    var init_progress_bar = function() {

        var div,
            DOCUMENT_WIDTH = 400,
            TOTAL_PROBLEMS = 24,
            progress = document.getElementById('progress'),
            div_width = Math.floor(DOCUMENT_WIDTH / TOTAL_PROBLEMS - 1) + 'px';

        for (var i=1; i<TOTAL_PROBLEMS+1; i++) {
            div = document.createElement('div');
            div.id = 'div' + i;
            div.style.width = div_width;
            progress.appendChild(div);
        }
    };


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

        var params = {},
            qs = window.location.pathname.replace(/\//, ''),
            pairs = qs.split('&');

        for (var i=0; i<pairs.length; i++) {
            var kv = pairs[i].split('=');
            params[kv[0]] = kv[1];
        }
        return params;
    };


    var render_problems = function(json) {

        var answer_class, has_passed, i, key, obj, template, thisLi,
            keys = Object.keys(json),
            content = document.getElementById('content');


        for (i in keys) {
            key = keys[i];
            obj = json[key];
            template = build_template(key, obj);
            content.appendChild(template);
        }
    };


    var render_progress_bar = function(key, has_passed) {

        var div = document.getElementById('div' + key);
        div.style.background = has_passed ? '#2b91af' : '#c82829';
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