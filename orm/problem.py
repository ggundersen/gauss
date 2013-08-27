from google.appengine.ext import ndb
import operator


class Problem(ndb.Model):

    number = ndb.IntegerProperty()
    answer = ndb.IntegerProperty()
    title = ndb.StringProperty()


    @classmethod
    def get_ndb_problems(cls, ancestor_key):

        return cls.query(ancestor=ancestor_key)


    @classmethod
    def get_sorted_problems(cls, ancestor_key, title=False):

        output = []
        problems = cls.query(ancestor=ancestor_key)
        if title == True:
            for problem in problems:
                # call str() on problem.title because it is a unicode string
                output.append(
                    (problem.number, problem.answer, str(problem.title))
                )
        else:
            for problem in problems:
                output.append((problem.number, problem.answer))            
            return sorted(output, key=lambda x: x[0])