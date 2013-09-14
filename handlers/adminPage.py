import importlib
import jinja2
import os
import webapp2
from odb.odb import Odb


TEMPLATE_PATH = os.path.normpath(os.path.dirname(__file__) + "../.." +
   os.environ['TEMPLATE_PATH'])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


class AdminPage(webapp2.RequestHandler):

    def get(self, password):


        if password == 'leonhard':
            problem_tuples = Odb().get_canonical_data()
            template_values = {'problems': problem_tuples}
            template = JINJA_ENV.get_template('admin.html')
            self.response.write(template.render(template_values))
        else:
            self.response.write('')