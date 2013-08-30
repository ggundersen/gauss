import importlib
import jinja2
import os
import webapp2
from google.appengine.ext import ndb
from orm.orm import *


TEMPLATE_PATH = os.path.normpath(os.path.dirname(__file__) + "../.." +
   os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


class RefreshPage(webapp2.RequestHandler):

    """
    def get(self):

        orm = Orm()
        orm.flush_datastore()
        orm.rebuild_datastore()

        problem_tuples = orm.get_problems(title=True)

        self.response.write('<h4>Refreshed datastore</h4>')
        self.response.write('<table><tr><td>#</td><td>Answer</td><td>Title</td></tr>')
        for problem in problem_tuples:
            self.response.write('<tr><td>' + str(problem[0]) + '</td><td>' + str(problem[1]) + '</td><td>' + str(problem[2]) + '</td></tr>')
        self.response.write('</table>')
    """

    def get(self):

        orm = Orm()
        orm.flush_datastore()
        orm.rebuild_datastore()

        problem_tuples = orm.get_problems(title=True)

        template_values = {'problems': problem_tuples}
        template = JINJA_ENV.get_template('refresh.html')
        self.response.write(template.render(template_values))