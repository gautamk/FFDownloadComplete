#!/usr/bin/python
import wsgiref.handlers
import python.models
#import json
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db

class register(webapp.RequestHandler):
	def get(self):
		self.response.out.write( json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4) )
	def post(self):
		userDb=python.models.UserDB(
						name = users.get_current_user() ,
						to_send_email = self.request.get('Send2Email') ,
						secret_key =  self.request.get('SecretKey') )

		datastore_userDb = db.GqlQuery("SELECT * FROM UserDB WHERE name=:current_user  ",current_user=users.get_current_user())
		if( datastore_userDb.count() == 0 ):
			userDb.put()
			self.response.out.write( 'Success fully Registered' )
		elif ( datastore_userDb.count() == 1):
			datastore_userDb = datastore_userDb.get()
			datastore_userDb.to_send_email =  self.request.get('Send2Email')
			datastore_userDb.secret_key = self.request.get('SecretKey')
			datastore_userDb.put()
			self.response.out.write(  'Successfully modified' )

		else:
			self.response.out.write( 'Error Too many conflicting Users' )


def main():
	app = webapp.WSGIApplication([('/Register',register)],debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()

