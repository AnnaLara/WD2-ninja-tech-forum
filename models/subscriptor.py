from google.appengine.ext import ndb

class Subscriptor(ndb.Model):
    email = ndb.TextProperty()

    @classmethod
    def create(cls, user):
        subscriptor = cls(email=user.email())
        subscriptor.put()

        return subscribtor
