from google.appengine.ext import ndb

class Problem(ndb.Model):
	number = ndb.IntegerProperty()
	answer = ndb.IntegerProperty()
	title = ndb.StringProperty()

	@classmethod
	def get_all_problems(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key)