import itertools
import jinja2
import os
import problems
import webapp2
from google.appengine.ext import ndb
from orm.orm import *
from handlers.problemHandler import *


TEMPLATE_PATH = os.path.normpath(os.path.dirname(__file__) + "../.." +
   os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


class TestHandler(webapp2.RequestHandler):

    def get(self, problem_range):

        """Render problem template, passing control to JavaScript
        """

        if problem_range == 'all':
            orm = Orm()
            datastore_problems = orm.get_problems()      
            template_values = {}
            template = JINJA_ENV.get_template('test.html')
            self.response.write(template.render(template_values))

        else:
            problem_id = problem_range
            template_values = {
                'problem_title': 'Problem ' + str(problem_id),
                'problem_num': str(problem_id),
                'js_path': 'pe' + str(problem_id) + '.js'
            }
            template = JINJA_ENV.get_template('problem.tpl.html')
            self.response.write(template.render(template_values))