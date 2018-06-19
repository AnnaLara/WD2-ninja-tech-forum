from handlers.base import BaseHandler
from models.topic import Topic
from datetime import datetime, timedelta

class DeleteTopicsCron(BaseHandler):
    def get(self):
        deleted_topics = Topic.query(Topic.deleted == True)

        topics_to_be_removed = deleted_topics.filter(Topic.updated < datetime.now() - timedelta(days=30)).fetch()

        for topic in topics_to_be_removed:
            topic.key.delete()

