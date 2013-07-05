import importlib
import os
import jinja2
import json
import time
import webapp2

template_path = os.path.normpath(os.path.dirname(__file__) + "../.." + os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class BaseHandler(webapp2.RequestHandler):

	def get(self, problem_id):
		template_values = {
			'problem_id' : problem_id,
			'answer' : self.get_answer(problem_id),
			'runtime' : self.get_runtime(problem_id),
			'js_path' : problem_id + '.js'
		}
		template = JINJA_ENV.get_template('problem.tpl.html')
		self.response.write(template.render(template_values))

	def get_answer(self, problem_id):
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, problem_id)
		return func()

	def get_runtime(self, problem_id):
		s = time.time()
		self.get_answer(problem_id)
		return time.time() - s