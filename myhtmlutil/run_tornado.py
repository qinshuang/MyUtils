# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/17/16.
"""
import tornado.websocket
import tornado.ioloop
import tornado.web
import os
import json

CURRENT_PWD = os.path.dirname(os.path.abspath(__file__))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("edit_script.html")


clients = []


class JobProgressHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        if self not in clients:
            clients.append(self)

        self.stream.set_nodelay(True)

    def on_message(self, script_uid):
        print 'Starting verbose for : ', script_uid
        self.send_progress(script_uid)

    def on_close(self):
        print 'Closing: ', self
        if self in clients:
            clients.remove(self)

    def send_progress(self, script_uid):
        """
        Send a fake job progress
        """
        for x in xrange(10):
            self.write_message(json.dumps({script_uid: (x + 1) * 10}))
            # time.sleep(1)
            print script_uid, (x + 1) * 10


def make_app():
    setting = dict(
        template_path=os.path.join(CURRENT_PWD, "templates"),
        static_path=os.path.join(CURRENT_PWD, "statics"),
        debug=True
    )
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/jobprogress', JobProgressHandler),
    ], **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(4001)
    tornado.ioloop.IOLoop.current().start()
