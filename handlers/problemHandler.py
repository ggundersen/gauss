import importlib
import json
import time
import webapp2

class ProblemHandler(webapp2.RequestHandler):

	def get(self, problem_id):
		output = self.get_data(problem_id)
		self.response.write(output)

	def get_data(self, problem_id):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'main')

		# Run and time problem
		s = time.time()
		a = func()
		t = "{0:.10f}".format(time.time() - s)

		return {'id': problem_id, 'answer': answer, 'runtime': t}