import importlib
import json
import time
import webapp2
from odb.odb import Odb


DB_DATA = Odb().get_canonical_data()

class ProblemHandler(webapp2.RequestHandler):

    def get(self, problems):

        problems = [int(s) for s in problems.split(',')]
        jsonOutput = self.run_problem_range(problems)
        self.response.write(jsonOutput)


    def mask_answer(self, answer):

        return '***' + str(answer)[:3]


    def run_problem(self, problem_id):
        
        """Return an object with problem data
        This method is always executed via run_problem_range, which performs
        the JSON encoding.
        """

        mod = importlib.import_module('problems.pe' + str(problem_id))
        func  = getattr(mod, 'main')
        s = time.time()
        answer = func()
        runtime = '{0:.10f}'.format(time.time() - s)
        correct = True if (answer == DB_DATA[problem_id - 1][1]) else False
        answer = self.mask_answer(answer) if correct else answer
        return { 'answer': answer, 'runtime': runtime, 'correct': correct, 'title' : DB_DATA[problem_id - 1][2] }


    def run_problem_range(self, problems):

        """Return a JSON object with problem objects from run_problem
        """

        jsonObj = {}
        for problem_id in problems:
            jsonObj[problem_id] = self.run_problem(problem_id)
        return json.dumps(jsonObj)