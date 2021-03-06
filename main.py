#!/usr/bin/env python

import webapp2
from crons.delete_topics import DeleteTopicsCron

from handlers.base import BaseHandler
from handlers.home import HomeHandler
from handlers.cookie_alert import CookieAlertHandler
from handlers.add_topic import TopicAddHandler
from handlers.topic_details import TopicDetailsHandler
from handlers.add_comment import CommentAddHandler
from handlers.delete_topic import TopicDeleteHandler
from handlers.subscribe import SubscribeHandler
from workers.email_new_comment import EmailNewCommentWorker


app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, name="home-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAddHandler, name='topic-add'),
    webapp2.Route('/topics/<topic_id:\d+>', TopicDetailsHandler, name='topic-details'),
    webapp2.Route('/topics/<topic_id:\d+>/comment/add', CommentAddHandler, name="comment-add"),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment"),
    webapp2.Route('/topics/<topic_id:\d+>/delete', TopicDeleteHandler, name="topic-delete"),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron, name="cron-delete-topics"),
    webapp2.Route('/subscribe', SubscribeHandler, name="subscribe"),
], debug=True)
