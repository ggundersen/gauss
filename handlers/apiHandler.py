import importlib
import json
import time
import webapp2

class ApiHandler(webapp2.RequestHandler):

	def get(self, problem_id, param1):
		output = self.get_data(problem_id, param1)
		outputJson = json.dumps(output)
		self.response.write(outputJson)

	def get_data(self, problem_id, param1):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'magic')

		# Run and time problem
		s = time.time()
		a = func(param1)
		t = time.time() - s

		return func(param1)