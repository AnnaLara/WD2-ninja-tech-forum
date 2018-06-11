from google.appengine.api import users, memcache

import uuid

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment

class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):

        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=logged_user.email(), time=600)

        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == int(topic_id), Comment.deleted == False).order(-Comment.created).fetch()

        params = {
            "topic": topic,
            "comments": comments,
            "csrf_token": csrf_token,
            }

        return self.render_template("topic_details.html", params = params)
