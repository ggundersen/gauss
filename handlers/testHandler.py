from google.appengine.ext import ndb
import jinja2
import webapp2
from problems import *
import unittest

#template_path = os.path.normpath(os.path.dirname(__file__) + "../.." + os.environ["TEMPLATE_PATH"])
#JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class TestHandler(webapp2.RequestHandler):

	def get(self):

		ancestor_key = ndb.Key('All', '1')
		problems = Problem.get_all_problems(ancestor_key)

		self.response.write(problems)
		
		#all_problems = 5;
		#template_values = {all_problems}
		#template = JINJA_ENV.get_template('test.html')
		#self.response.write(template.render(template_values))