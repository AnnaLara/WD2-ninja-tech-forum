from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic

class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        logged_user = users.get_current_user()

        if not logged_user:
            return self.write("Please, login first")

        title_value = self.request.get("title")
        text_value = self.request.get("text")

        if not title_value:
            return self.write("Title field is requiered")

        if not text_value:
            return self.write("Text field is requiered")

        new_topic = Topic(
            title=title_value,
            content=text_value,
            author_email = logged_user.email(),
        )

        new_topic.put()
        topic = Topic.query(Topic.title == new_topic.title, Topic.content == new_topic.content, Topic.author_email == new_topic.author_email).fetch()

        return self.redirect("/topics/topic.key.id()")
