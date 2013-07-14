import importlib
import json
import time
import webapp2

class ProblemHandler(webapp2.RequestHandler):

	def get(self, problem_id, user_input):
		output = self.get_data(problem_id, user_input)
		self.response.write(output)

	def get_data(self, problem_id, user_input):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'main')

		# Run and time problem
		s = time.time()
		a = func(user_input)
		t = time.time() - s

		return {'answer': a, 'runtime': t}