from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic

class TopicDeleteHandler(BaseHandler):
    def get(self, topic_id):

        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        params = {'topic_id': topic_id}

        self.render_template("topic_delete.html", params = params)

    def post(self, topic_id):

        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        topic = Topic.get_by_id(int(topic_id))


        if users.is_current_user_admin() == True or logged_user.email() == topic.author_email:
            topic.deleted = True
            topic.put()
            return self.write("Topic has been deleted")
        else:
            return self.write("You are not allowed to delete this topic")
