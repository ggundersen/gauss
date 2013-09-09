import importlib
import json
import pkgutil
import problems
import time
import webapp2
from orm.orm import Orm


class ProblemHandler(webapp2.RequestHandler):

    def get(self, problem_id):

        jsonOutput = self.run_problem(problem_id)
        self.response.write(jsonOutput)


    def run_problem(self, problem_id):
        
        """Return a JSON object with problem data
        """

        orm = Orm()
        answers = orm.get_canonical_data()
        answer = str(answers[int(problem_id) - 1][1])

        mod = importlib.import_module('problems.pe' + str(problem_id))
        fn  = getattr(mod, 'main')
        s = time.time()
        c = str(fn())
        t = '{0:.10f}'.format(time.time() - s)

        return json.dumps({ 'calculated': c, 'runtime': t, 'id': problem_id, 'correct': answer })


    def run_problem_block(self, problem_range):
        pass