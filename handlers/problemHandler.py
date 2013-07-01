import importlib
import os
import jinja2
import time
import webapp2

template_path = os.path.normpath(os.path.dirname(__file__) + "../.." + os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class ProblemHandler(webapp2.RequestHandler):
	def get(self, problem_id):
		result_array = self.get_data(problem_id)
		template_values = {
			'problem_id' : problem_id,
			'result' : result_array[0],
			'time' : result_array[1]
		}
		template = JINJA_ENV.get_template('problem.tpl.html')
		self.response.write(template.render(template_values))

	def get_data(self, problem_id):
		# get function
		mod = importlib.import_module('problems.' + problem_id)
		func = getattr(mod, problem_id)

		# run and time function
		s = time.time()
		result = func()
		t = time.time() - s

		# return data
		return [result, t]