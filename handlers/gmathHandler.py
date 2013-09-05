import json
import lib.gmath as g
import os
import webapp2


class GmathHandler(webapp2.RequestHandler):

    def get(self, fn):

        #jsonOutput = self.run_function(fn)
        #self.response.write(jsonOutput)

        if fn == 'get_gcd':
            jsonOutput = self.test_get_gcd()
            self.response.write(jsonOutput)


    def custom_assert(conditional, description):
        pass


    def run_function(self, fn):
        
        fn = getattr(lib.gmath, fn)
        c = fn(13)
        return json.dumps({ 'name': fn, 'calculated': c })


    def test_get_gcd(self):
        asserts = []
        if g.get_gcd(2, 4) == 2:
            asserts.append('The greatest common divisor of 2 and 4 is 2')
        return json.dumps(asserts)