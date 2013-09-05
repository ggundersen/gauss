import jinja2
import os
import webapp2
import lib.gmath


TEMPLATE_PATH = os.path.normpath(os.path.dirname(__file__) + '../..' +
   os.environ['TEMPLATE_PATH'])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


class GmathHandler(webapp2.RequestHandler):

    def get(self, function_name):

        jsonOutput = self.run_function(function_name)
        self.response.write(jsonOutput)


    @classmethod
    def run_function(cls, function_name):
        
        fn  = getattr(lib.gmath, function_name)
        c = fn(13)
        return json.dumps({ 'name': function_name, 'calculated': c })