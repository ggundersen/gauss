from google.appengine.ext import ndb
from orm.dsEntities import *
import importlib
import os
import webapp2

class RefreshHandler(webapp2.RequestHandler):

	def get(self):
		orm = Orm()

		orm.flush_datastore()
		orm.rebuild_datastore()

		sorted_problems = orm.get_sorted_data()
		self.response.write('<h4>Refreshed datastore</h4>')
		self.response.write('<table><tr><td>#</td><td>Answer</td><td>Title</td></tr>')
		for problem in sorted_problems:
			self.response.write('<tr><td>' + str(problem[0]) + '</td><td>' + str(problem[1]) + '</td><td>' + str(problem[2]) + '</td></tr>')
		self.response.write('</table>')