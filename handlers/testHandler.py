import webapp2


class TestHandler(webapp2.RequestHandler):

    def get(self, problem_id):

        self.response.write(problem_id)