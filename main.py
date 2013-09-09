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

"""----------------------------------------------------------------------------
Gauss
Gregory Gundersen

Gauss is a web application for testing, analyzing, and documenting Project
Euler solutions and associated libraries. All calculations are performed at
runtime.

2013-09-05
2.0.0 - Refactored URL-to-handler mapping to be more clear
      - Stubbed out gmathHandler
      - Modified main.css for more clear styling of code blocks; added favicon
1.0.0 - Initial commit
----------------------------------------------------------------------------"""

import jinja2
import os
import webapp2
from handlers import *


template_path = os.path.normpath(os.path.dirname(__file__) +\
    os.environ['TEMPLATE_PATH'])
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))


class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENV.get_template('index.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/api/problem=(.*)', problemHandler.ProblemHandler),
    (r'/api/gmath=(.*)', gmathHandler.GmathHandler),
    (r'/test=(.*)&q=(.*)', testHandler.TestHandler),
    (r'/refresh', refreshPage.RefreshPage)
], debug=True)