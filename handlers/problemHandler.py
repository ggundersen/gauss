import importlib
import json
import pkgutil
import problems
import time
import webapp2

class ProblemHandler(webapp2.RequestHandler):

	@classmethod
	def get(cls, problem_id):
		output = self.get_data(problem_id)
		cls.response.write(output)

	@classmethod
	def get_problem_data(cls, problem_id):

		# Get specific Python module
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, 'main')

		# Run and time problem
		s = time.time()
		a = func()
		t = '{0:.10f}'.format(time.time() - s)

		return {'id': problem_id, 'answer': answer, 'runtime': t}

	@classmethod
	def get_all_problem_data(cls):
		output = []
		for importer, problem_id, ispkg in pkgutil.iter_modules(problems.__path__):
			mod = importlib.import_module('problems.' + problem_id)
			func = getattr(mod, 'main')
			answer = func()
			output.append((problem_id, answer))

		return output

		#mod = importlib.import_module('problems.' + str(problem_id))
		#func = getattr(mod, 'main')
		#return func()