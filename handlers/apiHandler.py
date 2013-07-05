import importlib
import json
import time
import webapp2

class ApiHandler(webapp2.RequestHandler):

	def get(self, problem_id):
		output = {}
		output['id'] = problem_id
		output['answer'] = self.get_answer(problem_id)
		output['runtime'] = self.get_runtime(problem_id)
		outputJson = json.dumps(output)
		self.response.write(outputJson)

	def get_answer(self, problem_id):
		mod = importlib.import_module('problems.' + str(problem_id))
		func = getattr(mod, problem_id)
		return func()

	def get_runtime(self, problem_id):
		s = time.time()
		self.get_answer(problem_id)
		return time.time() - s