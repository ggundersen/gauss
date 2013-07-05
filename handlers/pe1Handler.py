import json
import time
import webapp2
from handlers.baseHandler import *

class Pe1Handler(BaseHandler):

	def get(self, problem_id):
		output['test'] = 'this is some text!'
		outputJson = json.dumps(output)
		self.response.write(outputJson)