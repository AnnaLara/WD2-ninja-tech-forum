from handlers.base import BaseHandler
from models.subscriptor import Subscriptor
from google.appengine.api import users

class SubscribeHandler(BaseHandler):
    def post(self):

        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        subscriptors = Subscriptor.query(Subscriptor.email == logged_user.email()).fetch()
        print subscriptors

        if subscriptors:
            text = "You are already subscribed!"
        else:
            Subscriptor.create(user=logged_user)
            text = "Success! You have subscribed to the latest topics."

        param = {
         text: text,
        }

        self.render_template('subscription.html', param = param)
