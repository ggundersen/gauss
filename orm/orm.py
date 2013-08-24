import dsProblem as p
from google.appengine.ext import ndb

ANCESTOR_KEY = ndb.Key('All', '1')

class Orm:

	def flush_datastore(self):
		return 'the database has been flushed'

	"""	problems = Problem.get_all_problems(ANCESTOR_KEY)
		for problem in problems:
			problem.key.delete()

	def rebuild_datastore(self):
		data = self.get_canonical_data()
		for p in data:
			this_prb = Problem(number=p[0], answer=p[1], title=p[2], parent=ancestor_key)
			this_key = this_prb.put()

	def get_sorted_data(self):
		problem_array = []
		problems = Problem.get_all_problems(ANCESTOR_KEY)
		for problem in problems:
			problem_array.append([problem.number, problem.answer, problem.title])
		return sorted(problem_array)

	def get_canonical_data(self):
		return [\
			[1, 233168, 'Multiples of 3 and 5'],\
			[2, 4613732, 'Even Fibonacci numbers'],\
			[3, 6857, 'Largest prime factor'],\
			[4, 906609, 'Largest palindrome product'],\
			[5, 232792560, 'Smallest multiple'],\
			[6, 25164150, 'Sum square difference'],\
			[7, 104743, '10001st prime'],\
			[8, 40824, 'Largest product in a series'],\
			[9, 31875000, 'Special Pythagorean triplet'],\
			[10, 142913828922, 'Summation of primes']\
		]
		"""