import os
import logging

from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import webapp

from twilio import twiml, TwilioRestException
from twilio.rest import TwilioRestClient

from data_model import *
import config

class RequestHandler(webapp.RequestHandler):

  def post(self):
  
      # validate it is in fact coming from twilio
      if config.ACCOUNT_SID != self.request.get('AccountSid'):
        logging.error("Inbound request was NOT VALID.  It might have been spoofed!")
        self.response.out.write(errorResponse("Illegal caller"))
        return

      # who called? and what did they ask for?
      phone = self.request.get("From")
      msg = self.request.get("Body")
      logging.info("New inbound request from %s with message, %s" % (self.request.get('From'),msg))
      
      # validate the user
      smoogler = db.GqlQuery("select * from Smoogler where phone = :1", phone)
      if user is None:
        logging.error('Unknown user accessing the juice from %s' % phone)
        return
      
      # interrogate the message body to determine what to do 
      # assume the command is the first word
      feature = msg.lower().split()[0]
      cmd = msg.lower().split()[1]
      if feature.find('t') > -1 or feature.find('task') > -1:
          # it's a task request
          if cmd.find('l') > -1 or cmd.find('list') > -1:
            logging.debug('task list')
      else:
          logging.error('unsupported command. doing nothing with this...')
          
## end RequestHandler

class MainHandler(webapp.RequestHandler):
    """ 
    The MainHandler manages the default landing page - '/index.html'
    """
    def get(self):
      user = users.get_current_user()
      if user:
          greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                      (user.nickname(), users.create_logout_url("/")))
      else:
          greeting = ("<a href=\"%s\">Sign in or register</a>." %
                      users.create_login_url("/"))

      # generate the html
      template_values = {'greeting':greeting}
      path = os.path.join(os.path.dirname(__file__), 'web/templates/index.html')
      self.response.out.write(template.render(path, template_values))

## end MainHandler

def OutboundSMSHandler(phone,msg):
    """
    Convenience method to send an SMS
    """
    phone = self.request.get('target_phone')
    msg = self.request.get('message')
    
    # bail if there is no message defined
    if msg is None:
      logging.error('caller (incorrectly) asked to send a message without text in it');
      return
    
    try:
        client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
                                  config.TWILIO_AUTH_TOKEN)
        logging.debug('sending message - %s - to %s' % (msg,phone))
        message = client.sms.messages.create(to=phone,
                                             from_=config.TWILIO_CALLER_ID,
                                             body=msg)
    except TwilioRestException,te:
        logging.error('Unable to send SMS message! %s'%te)
        
## end OutboundSMSHandler()

class EventLoggingHandler(webapp.RequestHandler):
    """
    Audit trail for all SMS interactions with users
    """
    def post(self):
      if config.AUDITING_ENABLED is 'true':        
		  # normalize the XMPP requests
		  if self.request.get('phone').find('@'):
			  caller = self.request.get('phone').split('/')[0]
		  else:
			  caller = self.request.get('phone')
		  # log this event...
		  log = AuditLog()
		  log.phone = caller
		  log.request = self.request.get('request')
		  log.response = self.request.get('response')
		  log.service = 'fixme'
		  log.sid = self.request.get('sid')
		  
		  # put it into the datastore...
		  log.put()
    
## end EventLoggingHandler


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/request', RequestHandler),
                                          ('/sms/outbound', OutboundSMSHandler),
                                          ('/logger', EventLoggingHandler),
                                         ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
