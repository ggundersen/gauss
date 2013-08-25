from google.appengine.ext import ndb
from orm.orm import *
from handlers.problemHandler import *

import pkgutil
import problems
import webapp2

#import jinja2
#template_path = os.path.normpath(os.path.dirname(__file__) + "../.." + os.environ["TEMPLATE_PATH"])
#JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class TestHandler(webapp2.RequestHandler):

	def get(self):

		orm = Orm()
		ph = ProblemHandler()

		problems_orm = orm.get_problems()
		problems_run = ph.get_all_problem_data()

		self.response.write('<li>' + str(problems_orm) + '</li>')
		self.response.write('<li>' + str(problems_run) + '</li>')

		"""
		solved_problems = []
		for importer, modname, ispkg in pkgutil.iter_modules(problems.__path__):
			if modname in problem_tuples:
				ans = ph.get_answer(modname)
				self.response.write(ans)

				#self.response.write(modname)


			#solved_problems.append(modname)

		#for problem_id in modules:
		#	ans = ph.get_answer(problem_id)
		
		#self.response.write(solved_problems)

		#self.response.write(ds_problems)
		#self.response.write(modules)


		#test3 = help(problems)
		#self.response.write(test3)



		#self.response.write(sorted_problems)
		#all_problems = 5;
		#template_values = {all_problems}
		#template = JINJA_ENV.get_template('test.html')
		#self.response.write(template.render(template_values))"""