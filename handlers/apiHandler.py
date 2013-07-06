import importlib
import json
import time
import webapp2

class ApiHandler(webapp2.RequestHandler):

	def get(self, problem_id):
		output = self.get_data(problem_id)
		outputJson = json.dumps(output)
		self.response.write(outputJson)

	def get_data(self, problem_id):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'magic')

		# Run and time problem
		s = time.time()
		a = func()
		t = time.time() - s

		return func()