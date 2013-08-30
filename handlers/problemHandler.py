import importlib
import json
import pkgutil
import problems
import time
import webapp2
from orm.orm import Orm


class ProblemHandler(webapp2.RequestHandler):

    def get(self, problem_id):

        output = self.run_problem(problem_id)
        self.response.write(output)


    @classmethod
    def get_all_problem_modules(cls):

        """Return a list of integers that represent the completed problems in
        the problem package
        """

        modules = []
        for importer, modname, ispkg in pkgutil.iter_modules(problems.__path__):
            modules.append(int(modname[2:]))
        return modules


    @classmethod
    def run_problem(cls, problem_id):
        
        """Return a JSON object with problem data
        """

        orm = Orm()
        answers = orm.get_canonical_data()
        answer = answers[int(problem_id) - 1][1]

        mod = importlib.import_module('problems.pe' + str(problem_id))
        fn  = getattr(mod, 'main')
        s = time.time()
        a = fn()
        t = '{0:.10f}'.format(time.time() - s)
        return json.dumps({ 'calculated': a , 'runtime': t, 'id': problem_id, 'correct': answer })