import importlib
import jinja2
import os
import webapp2


template_path = os.path.normpath(os.path.dirname(__file__) + "../.." +\
	os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))


class TemplateHandler(webapp2.RequestHandler):

    def get(self, problem_id):
        template_values = {
            'problem_id' : problem_id,
            'problem_num' : problem_id[2:],
            'problem_title' : 'Problem ' + problem_id[2:],
            'js_path' : problem_id + '.js',
            'css_path' : problem_id + '.css'
        }
        template = JINJA_ENV.get_template('pe' + problem_id + '.html')
        self.response.write(template.render(template_values))