import itertools
import os
import problems
import webapp2
from google.appengine.ext import ndb
from orm.orm import *
from handlers.problemHandler import *

import jinja2
template_path = os.path.normpath(os.path.dirname(__file__) + "../.." +
   os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))


class TestPage(webapp2.RequestHandler):

    def get(self):

        orm = Orm()
        datastore_problems = orm.get_problems()

        template_values = {}
        template = JINJA_ENV.get_template('test.html')
        self.response.write(template.render(template_values))


    #def run_all_problems(self, datastore_problems):

        #problemHandler = ProblemHandler()
        #problems = problemHandler.get_all_problem_modules()
        
        #for prob in datastore_problems:
        #    if prob[0] in problems:
        #        prob_data = problemHandler.run_problem(prob[0])


        #for problem in datastore_problems:





        #p = problemRunner.run_problem(problem_id)

        #problems_from_database = orm.get_problems()
        #problems_at_runtime    = ph.run_all_problems()

        #self.response.write(problems_from_database)
        #self.response.write(problems_at_runtime)

        #self.response.write('<li>' + str(problems_from_ds) + '</li>')
        #self.response.write('<li>' + str(problems_run) + '</li>')

        #for p1, p2 in zip(problems_from_ds, problems_run):
        #	print (p1, p2)
            #self.response.write('<tr><td>' + str(pds[0]) + '</td><td>' + str(pds[1]) + '</td></tr>')
            #self.response.write('<tr><td>' + str(pr[0])  + '</td><td>' + str(pr[1])  + '</td></tr>')
        #self.response.write('</table>')