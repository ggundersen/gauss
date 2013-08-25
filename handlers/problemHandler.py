import importlib
import json
import pkgutil
import problems

import time
import webapp2

class ProblemHandler(webapp2.RequestHandler):

	def get(self, problem_id):
		output = self.get_data(problem_id)
		self.response.write(output)

	@staticmethod
	def get_problem_data(problem_id):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'main')

		# Run and time problem
		s = time.time()
		a = func()
		t = '{0:.10f}'.format(time.time() - s)

		return {'id': problem_id, 'answer': answer, 'runtime': t}

	@staticmethod
	def get_all_problem_data():
		
		output = []
		for importer, problem_id, ispkg in pkgutil.iter_modules(problems.__path__):
			mod = importlib.import_module('problems.' + problem_id)
			func = getattr(mod, 'main')
			answer = func()
			output.append((int(problem_id[2:]), answer))

		return output