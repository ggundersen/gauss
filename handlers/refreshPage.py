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

    def get(self):

        orm = Orm()
        orm.flush_datastore()
        orm.rebuild_datastore()
        problem_tuples = orm.get_problems(title=True)

        template_values = {'problems': problem_tuples}
        template = JINJA_ENV.get_template('refresh.html')
        self.response.write(template.render(template_values))