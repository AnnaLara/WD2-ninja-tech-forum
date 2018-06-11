from google.appengine.api import users, memcache

import uuid

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment

class CommentAddHandler(BaseHandler):
    def post(self, topic_id):
        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        csrf_token = self.request.get('csrf-token')
        mem_token = memcache.get(key=csrf_token)

        if not mem_token or mem_token != logged_user.email():
            return self.write("This website is protected against CSRF")

        comment = self.request.get('comment')
        topic = Topic.get_by_id(int(topic_id))

        if not comment:
            return self.write("Text field is requiered")

        Comment.create(content=comment, user=logged_user, topic=topic)

        # new_comment = Comment(
        #     content = comment,
        #     author_email = logged_user.email(),
        #     topic_id = int(topic_id),
        #     topic_title = Topic.get_by_id(int(topic_id)).title,
        # )

        #new_comment.put()

        return self.redirect_to("topic-details", topic_id=topic_id)
