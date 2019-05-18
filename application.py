import tornado.web
from views import index
import config
import os
class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/home", index.HomeHandler),
            (r'/chat', index.ChatHandler),
            (r'/person_num',index.PersonNumHandler)

        ]

        super(Application,self).__init__(handlers, **config.settings)