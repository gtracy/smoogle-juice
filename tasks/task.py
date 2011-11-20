import os
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import config

from apiclient.discovery import build
import httplib2
from oauth2client.appengine import OAuth2Decorator

decorator = OAuth2Decorator(client_id=config.GOOGLE_CLIENT_ID,
                            client_secret=config.GOOGLE_CLIENT_SECRET,
                            scope=config.GOOGLE_SCOPE,
                            )#user_agent='smooglejuice')
class TaskHandler(webapp.RequestHandler):

   @decorator.oauth_required
   def get(self):
     self.response.out.write('<html><body><ul>')
     
     tasks = get_all_tasks()
     for key, list in tasks.iteritems():
       self.response.out.write('<h2>%s</h2><ul>' % key)
       for t in list:
         self.response.out.write('<li>%s</li>' % t)
       self.response.out.write('</ul>')
       
     self.response.out.write('</ul></body><html>')

## end TaskHandler

def get_all_tasks():
    all_tasks = {}
    service = build('tasks', 'v1', http=decorator.http())
    lists = service.tasklists().list().execute()
    for list in lists['items']:
      all_tasks[list['title']] = []
      tasks = service.tasks().list(tasklist=list['id']).execute()
      for (i,task) in enumerate(tasks['items']):
        all_tasks[list['title']].append(task['title'])
        
    return all_tasks
    
## end

def main():
  logging.getLogger().setLevel(logging.INFO)
  application = webapp.WSGIApplication([('/tasks', TaskHandler),
                                        ],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
