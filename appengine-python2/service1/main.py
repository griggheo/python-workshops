# Copyright 2016 Google Inc.
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

# [START app]
import logging

from flask import Flask

from google.appengine.api import urlfetch


app = Flask(__name__)


@app.route('/')
def hello():
#    return 'Hello World!'
    url = 'https://service2-dot-eduplatform.appspot.com'
    try:
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            return '{}\n'.format(result.content)
            #self.response.write(result.content)
        else:
            return 'got {} from urlfetch\n'.format(result.status_code), 500
    except urlfetch.Error:
        return 'Caught exception when calling urlfetch\n', 500
    #return 'Hello {}!\n'.format(target)



@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
