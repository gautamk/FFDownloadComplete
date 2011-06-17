#!/usr/bin/python
import wsgiref.handlers
import md5
from google.appengine.ext import webapp
from time import localtime, strftime

class generateSecretKey(webapp.RequestHandler):
	def get(self):
		self.redirect('../');
	def post(self):
		digest = md5.new( self.request.get('message') + strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()) )
		self.response.out.write( digest.hexdigest() )
			

def main():
	app = webapp.WSGIApplication([('/GenerateSecretKey',generateSecretKey)],debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()
