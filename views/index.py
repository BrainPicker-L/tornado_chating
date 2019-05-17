import json
from tornado.web import RequestHandler
import config,os
from tornado.websocket import WebSocketHandler


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')



class ChatHandler(WebSocketHandler):
    users = []
    def open(self):
        self.users.append(self)
        for user in self.users:
            user.write_message("[%s]登陆了"%self.request.remote_ip)

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("[%s]退出了" % self.request.remote_ip)

    def on_message(self, message):
        for user in self.users:
            user.write_message("[%s]说：%s" % (self.request.remote_ip,message))