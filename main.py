#!/usr/bin/env python

import webapp2

from handlers.base import BaseHandler
from handlers.home import HomeHandler
from handlers.cookie_alert import CookieAlertHandler
from handlers.add_topic import TopicAddHandler
from handlers.topic_details import TopicDetailsHandler
from handlers.add_comment import CommentAddHandler
from workers.email_new_comment import EmailNewCommentWorker


app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, name="home-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAddHandler, name='topic-add'),
    webapp2.Route('/topics/<topic_id:\d+>', TopicDetailsHandler, name='topic-details'),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAddHandler, name="comment-add"),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment")
], debug=True)
