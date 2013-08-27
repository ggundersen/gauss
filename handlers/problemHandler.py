import importlib
import json
import pkgutil
#import problems
import time
import webapp2
from problems import *


class ProblemHandler(webapp2.RequestHandler):

    def get(self, problem_id):

        output = self.get_data(problem_id)
        self.response.write(output)


    @staticmethod
    def run_problem(problem_id):

        # Get specific Python module
        mod = importlib.import_module('problems.' + str(problem_id))
        func = getattr(mod, 'main')

        # Run and time problem
        s = time.time()
        a = func()
        t = '{0:.10f}'.format(time.time() - s)

        return {'id': problem_id, 'answer': answer, 'runtime': t}


    #@staticmethod
    def run_all_problems(self):

        output = []

        t = time.time()
        output.append((1, pe1.main(), time.time() - t))

        t = time.time()
        output.append((2, pe2.main(), time.time() - t))

        t = time.time()
        output.append((3, pe3.main(), time.time() - t))

        t = time.time()
        output.append((4, pe4.main(), time.time() - t))

        #t = time.time()
        #output.append((5, pe5.main(), time.time() - t))

        t = time.time()
        output.append((6, pe6.main(), time.time() - t))

        t = time.time()
        output.append((7, pe7.main(), time.time() - t))

        t = time.time()
        output.append((8, pe8.main(), time.time() - t))

        #t = time.time()
        #output.append((9, pe9.main(), time.time() - t))

        #t = time.time()
        #output.append((10, pe10.main(), time.time() - t))
        #for importer, problem_id, ispkg in pkgutil.iter_modules(problems.__path__):
        #    mod = importlib.import_module('problems.' + problem_id)
        #    func = getattr(mod, 'main')
        #    answer = func()
        #    output.append((int(problem_id[2:]), answer))
        return output