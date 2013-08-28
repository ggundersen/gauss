import importlib
import os
import webapp2
from google.appengine.ext import ndb
from orm.orm import *

class RefreshPage(webapp2.RequestHandler):

    def get(self):

        orm = Orm()
        orm.flush_datastore()
        orm.rebuild_datastore()

        problem_tuples = orm.get_problems(title=True)

        self.response.write('<h4>Refreshed datastore</h4>')
        self.response.write('<table><tr><td>#</td><td>Answer</td><td>Title</td></tr>')
        for problem in problem_tuples:
            self.response.write('<tr><td>' + str(problem[0]) + '</td><td>' + str(problem[1]) + '</td><td>' + str(problem[2]) + '</td></tr>')
        self.response.write('</table>')