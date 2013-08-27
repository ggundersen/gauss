import pkgutil
import problems
import webapp2
from google.appengine.ext import ndb
from orm.orm import *
from handlers.problemHandler import *

#import jinja2
#template_path = os.path.normpath(os.path.dirname(__file__) + "../.." +
#   os.environ["TEMPLATE_PATH"])
#JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))


class TestHandler(webapp2.RequestHandler):

    def get(self):

        orm = Orm()
        ph = ProblemHandler()

        problems_from_ds = orm.get_problems()
        problems_run = ph.run_all_problems()

        self.response.write('<li>' + str(problems_from_ds) + '</li>')
        self.response.write('<li>' + str(problems_run) + '</li>')