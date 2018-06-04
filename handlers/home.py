from handlers.base import BaseHandler
from models.topic import Topic

class HomeHandler(BaseHandler):
    def get(self):

        allTopics = Topic.query(Topic.deleted == False).fetch()
        params = {"allTopics": allTopics}

        return self.render_template("home.html", params = params)
