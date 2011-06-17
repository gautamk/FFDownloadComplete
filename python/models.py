#!/usr/bin/python

from google.appengine.ext import db

class UserDB(db.Model):
	name=db.UserProperty()
	to_send_email=db.EmailProperty()
	secret_key=db.StringProperty()

