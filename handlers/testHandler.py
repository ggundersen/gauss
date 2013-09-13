import itertools
import jinja2
import os
import webapp2


TEMPLATE_PATH = os.path.normpath(os.path.dirname(__file__) + '../..' +
   os.environ['TEMPLATE_PATH'])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


class TestHandler(webapp2.RequestHandler):

    def get(self, suite, q):

        if suite == 'problem':
            self.get_problems(q)
        elif suite == 'gmath':
            self.get_gmath(q)


    def get_problems(self, q):

        if q == 'all':
            template = JINJA_ENV.get_template('problems.html')
            self.response.write(template.render())
        else:
            problem_id = q
            template_values = {
                'problem_title': 'Problem ' + str(problem_id),
                'problem_num': str(problem_id),
                'js_path': 'pe' + str(problem_id) + '.js'
            }
            template = JINJA_ENV.get_template('problem.tpl.html')
            self.response.write(template.render(template_values))