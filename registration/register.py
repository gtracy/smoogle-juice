import os
import logging

from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import webapp

from dataModel import *
import config


class ConfigurePhoneHandler(webapp.RequestHandler):
  """ 
  This handler will accept a user's phone number and generate a secret
  code the user must verify to register their mobile phone number
  """
    def post(self):

## end ValidatePhoneHandler


class ConfigurePhoneHandler(webapp.RequestHandler):
  """ 
  This handler will accept a user's phone number and generate a secret
  code the user must verify to register their mobile phone number
  """
    def post(self):

## end ValidatePhoneHandler

class ValidateCodeHandler(webapp.RequestHandler):
  """ 
  This handler validates the signup code the user entered into the web form.
  It needs to match the code we sent them via SMS
  """
    def post(self):
      code = self.request.get('code')
      
      # find the user
      #  get the user object out of the session
      #  get the smoogler object based on this user
      #  test the code entered in the web form and compare it to the one we have stored
      
      # if it worked, redirect to success screen
      template = 'web/templates/phone-reg-success.html'
      
      # if it failed, redirect to fail screen
      template = 'web/templates/phone-reg-fail.html'

      path = os.path.join(os.path.dirname(__file__), template)
      self.response.out.write(template.render(path, template_values))

## end ValidateCodeHandler


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([('/reg/phone/validate', ValidateCodeHandler),
                                          ('/reg/phone/configure', ConfigurePhoneHandler),
                                          ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
