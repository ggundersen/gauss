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
		data = self.get_data(problem_id)
		template_values = {
			'problem_id' : problem_id,
			'problem_num' : problem_id[2:],
			'problem_title' : 'Problem ' + problem_id[2:],
			'answer' : data[0],
			'runtime' : data[1],
			'js_path' : problem_id + '.js',
			'css_path' : problem_id + '.css'
		}
		template = JINJA_ENV.get_template(problem_id + '.html')
		self.response.write(template.render(template_values))

	def get_data(self, problem_id):
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, problem_id)

		# Run and time problem
		s = time.time()
		a = func()
		t = time.time() - s

		return [a, t]