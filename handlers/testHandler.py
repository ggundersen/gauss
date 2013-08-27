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

        problems_orm = orm.get_problems()
        problems_run = ph.get_all_problem_data()

        self.response.write('<li>' + str(problems_orm) + '</li>')
        self.response.write('<li>' + str(problems_run) + '</li>')