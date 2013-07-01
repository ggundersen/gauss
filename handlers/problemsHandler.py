import jinja2
import os
import webapp2

template_path = os.path.normpath(os.path.dirname(__file__) + "../.." + os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class ProblemsHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENV.get_template('problems.html')
		self.response.write(template.render())