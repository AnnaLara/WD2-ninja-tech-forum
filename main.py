#!/usr/bin/env python

import webapp2

from handlers.base import BaseHandler
from handlers.home import HomeHandler
from handlers.cookie_alert import CookieAlertHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, name="home-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
], debug=True)
