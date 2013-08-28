from google.appengine.ext import ndb
from problemModel import ProblemModel


ANCESTOR_KEY = ndb.Key('All', '1')


class Orm:

    def get_problems(self, title=False):

        return ProblemModel.get_sorted_problems(ancestor_key=ANCESTOR_KEY, title=title)


    def flush_datastore(self):

        problems = ProblemModel.get_ndb_problems(ANCESTOR_KEY)
        for p in problems:
            p.key.delete()


    @classmethod
    def rebuild_datastore(cls):

        data = cls.get_canonical_data()
        for p in data:
            problem = ProblemModel(number=p[0], answer=p[1], title=p[2], parent=ANCESTOR_KEY)
            problem.put()


    @classmethod
    def get_canonical_data(cls):

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