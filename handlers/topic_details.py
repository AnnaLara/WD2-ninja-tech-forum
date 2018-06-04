from handlers.base import BaseHandler
from models.topic import Topic

class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):

        topic = Topic.get_by_id(int(topic_id))
        params = {"topic": topic}

        return self.render_template("topic_details.html", params = params)
