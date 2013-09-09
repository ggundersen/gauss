import importlib
import json
import pkgutil
import problems
import time
import webapp2
from orm.orm import Orm


class ProblemHandler(webapp2.RequestHandler):

    def get(self, problems):

        problems = [int(s) for s in problems.split(',')]
        jsonOutput = self.run_problem_range(problems)
        self.response.write(jsonOutput)


    def mask_answer(self, answer):
        return '***' + str(answer)[:3]


    def run_problem(self, problem_id, answers):
        
        """Return an object with problem data
        This method is always executed via run_problem_range, which performs
        the JSON encoding.
        """

        mod = importlib.import_module('problems.pe' + str(problem_id))
        fn  = getattr(mod, 'main')
        s = time.time()
        answer = fn()
        runtime = '{0:.10f}'.format(time.time() - s)
        correct = True if (answer == answers[problem_id - 1][1]) else False
        if correct:
            answer = self.mask_answer(answer)
        return { 'answer': answer, 'runtime': runtime, 'correct': correct }


    def run_problem_range(self, problems):

        """Return a JSON object with problem objects from run_problem
        """

        orm = Orm()
        answers = orm.get_canonical_data()
        jsonObj = {}
        for problem_id in problems:
            jsonObj[problem_id] = self.run_problem(problem_id, answers)
        return json.dumps(jsonObj)