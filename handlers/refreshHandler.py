from google.appengine.ext import ndb
import importlib
import os
import webapp2

PROBLEM_SET = 'problem_set'

#class Problems(nbd.Model):
#	pass

# entity model class
class Problem(ndb.Model):
	number = ndb.IntegerProperty()
	answer = ndb.IntegerProperty()

	@classmethod
	def get_all_problems(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key)

class RefreshHandler(webapp2.RequestHandler):

	def get(self):

		# Set immutable Datastore key for all data
		ancestor_key = ndb.Key('All', '1')

		# Flush Datastore
		problems = Problem.get_all_problems(ancestor_key)
		for problem in problems:
			problem.key.delete()

		# Rebuild Datastore
		data = self.get_canonical_data()
		for i in data:
			this_prb = Problem(number=i[0], answer=i[1], parent=ancestor_key)
			this_key = this_prb.put()

		# Get and sort data
		problem_array = []
		for problem in problems:
			problem_array.append([problem.number, problem.answer])
		problem_array = sorted(problem_array)

		# Write out all problems
		self.response.write('<h4>Refreshed datastore</h4>')
		self.response.write('<ul>')
		for problem in problem_array:
			self.response.write('<li>' + str(problem[0]) + ': ' + str(problem[1]) + '</li>')
		self.response.write('</ul>')

	def get_canonical_data(self):
		return [\
			[1,233168],\
			[2,4613732],\
			[3,6857]\
		]