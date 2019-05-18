import json
from tornado.web import RequestHandler
import config,os
from tornado.websocket import WebSocketHandler
import json

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')



class ChatHandler(WebSocketHandler):
    users = []
    data = {}
    def open(self):
        self.users.append(self)
        self.data["users"] = [user.request.remote_ip for user in self.users]
        self.data["message"] = "他说：登陆了"
        json_data = json.dumps(self.data)
        for user in self.users:
            user.write_message(json_data, binary=False)

    def on_close(self):
        self.users.remove(self)
        self.data["users"] = [user.request.remote_ip for user in self.users]
        self.data["message"] = "他说：退出了"
        json_data = json.dumps(self.data)
        for user in self.users:
            user.write_message(json_data, binary=False)

    def on_message(self, message):


        for user in self.users:

            if user.request.remote_ip == self.request.remote_ip:
                self.data["message"] = "我说：%s" % message
            else:
                self.data["message"] = "他说：%s" % message
            json_data = json.dumps(self.data)
            user.write_message(json_data, binary=False)

class PersonNumHandler(WebSocketHandler):
    users = []
    def open(self):
        self.users.append(self)
        online_list = [user.request.remote_ip for user in self.users]
        print(online_list)
        for user in self.users:
            user.write_message(str(online_list))

    def on_close(self):
        self.users.remove(self)
        online_list = [user.request.remote_ip for user in self.users]
        for user in self.users:
            user.write_message(str(online_list))
