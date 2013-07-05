#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import jinja2
import os
import webapp2

from handlers import *

template_path = os.path.normpath(os.path.dirname(__file__) + os.environ["TEMPLATE_PATH"])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENV.get_template('index.html')
		self.response.write(template.render())

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/problems', problemsHandler.ProblemsHandler),
    (r'/problems/(.*)', baseHandler.BaseHandler),
    (r'/api/q=(.*)', apiHandler.ApiHandler)
], debug=True)
