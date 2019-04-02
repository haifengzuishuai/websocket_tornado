# coding:utf-8
# 愉快的搞基,利用Python打造上万并发的聊天室tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
from tornado.web import RequestHandler
import json
from tornado.options import define, options
from tornado.websocket import WebSocketHandler
import codecs
import time
from random import choice

uid = ['1474021371', '1474021374', '1474021378', '1474021380',
       '1474021422', '1474021427', '1474021433', '1474021441', '1480384507']
name = ['我是第一', '我是第二', '我是第山', '我是第是', '我是第五', '我是第流', '我是第器', '我是第吧', '我是第久']
see = ['2', '4', '6', '8', '10']
# 导入json文件现在用不上
# 定义端口
define("port", default=8887, type=int)
txt = json.load(codecs.open('./test.json', 'rb'))
name1 = txt['gift']
name2 = txt['gift1']
# 主路由


class IndexHandler(RequestHandler):
    def get(self,account,account1):
        self.render("chat-client.html")

class ChatHandler(WebSocketHandler):
    users = set()  # 用来存放在线用户的容器

    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息
            u.write_message(u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip,
                                                  datetime.datetime.now().strftime("%H:%M:%S")))
            a = json.dumps(name1)
            u.write_message(a)
            for i in range(10):
                time.sleep(0.05)
                sl = i + 1
                # 随机取uid
                user = choice(uid)
                named = choice(name)
                se1 = choice(see)
                gift1 = {"gift1": [{
                    "id": 1112908736500506624,
                    "pr": 2,
                    "u": 0,
                    "nk": "运营后台系统",
                    "ic": 'null',
                    "r": 216261349,
                    "t": 2,
                    "st": 0,
                    "ct": "99009999",
                    "ex": {
                        "broadcastType": 3,
                        "configType": 2,
                        "configId": 6722177923,
                        "chatId": 216261349,
                        "content": "99009999",
                        "displayRuleType": 1,
                        "displayRuleTime": 12,
                        "notifyType": 60100,
                        "praiseTotal": 99019999,
                        "msgId": "20190402104454214DN6J2447"
                    },
                    "ts": 1554173094281,
                    "a": 10000
                }]}
                qc = gift1['gift1']
                u.write_message(json.dumps(qc))
                # 随机取uid
                user = choice(uid)
                named = choice(name)
                se1 = choice(see)
                gift1 = {"gift2": [{
                    "id": 1111197118407278592,
                    "pr": 2,
                    "u": 0,
                    "nk": "sys",
                    "ic": 'null',
                    "r": 276687149,
                    "t": 1,
                    "st": 0,
                    "ct": "礼物",
                    "ex": {
                        "nickname": named,
                        "ge": "青春有我",
                        "co": sl,
                        "he": 30,
                        "se": se1,
                        "gl": 1,
                        "de": 5,
                        "me": 2,
                        "icon": "https://img7.iqiyipic.com/passport/20180724/2b/27/passport_1466309899_153239260645722_130_130.jpg",
                        "uid": user,
                        "dh": "https://pic3.iqiyipic.com/common/20190328/yingyuanbang.png",
                        "gd": 110,
                        "fse": "https://static-s.iqiyi.com/ext/common/yingyuanbang_and.zip",
                        "ifse": "https://static-s.iqiyi.com/ext/common/yingyuanbang_ios.zip",
                        "pfse": "http://effect-live.iqiyi.com/dzb/pcw/yingyuanbang.swf",
                        "gr": 1,
                        "gf": "https://pic0.iqiyipic.com/common/20190328/yingyuanbang.gif\t",
                        "qd": 2230398923,
                        "si": "http://pic3.iqiyipic.com/common/20190304/LOGO.jpg",
                        "sne": "青春有你",
                        "isGroup": 0,
                        "user_name": named,
                        "user_face": "https://img7.iqiyipic.com/passport/20180811/37/5b/passport_1602399285_153391556453306_130_130.jpg",
                        "show_name": "青春有你",
                        "is_group": 0,
                        "product_name": "青春有我",
                        "pic": "https://pic3.iqiyipic.com/common/20190328/yingyuanbang.png",
                        "num": 1,
                        "msgId": "20190328172332722I4E135B8"
                    },
                    "ts": 1553765012727,
                    "a": 10000
                }]}
                qc1 = gift1['gift2']
                a = json.dumps(qc1)
                u.write_message(a)

    def on_message(self, message):
        # 随机取uid
        user = choice(uid)
        named = choice(name)
        g = {
            "gift": [{
                "id": 1107982064669155328,
                "pr": 2,
                "u": user,
                "nk": named,
                "ic": "http://www.iqiyipic.com/common/fix/headicons/male-130.png",
                "r": 274123949,
                "t": 51,
                "st": 0,
                "ct": message,
                "ex": {
                    "fanGrade": "10",
                    "icon": "http://www.iqiyipic.com/common/fix/headicons/male-130.png",
                    "msgId": "20190319202804145F43SIRB0",
                    "fanName": "婧宝宝",
                    "barrageColor": "#23d31e",
                    "anchorId": 2280469905,
                    "roomId": 63925,
                    "uid": user,
                    "userLevel": "51",
                    "nickname": named,
                    "userType": "0",
                },
                "ts": 1552998484184,
                "a": 10000
            }]
        }
        f = g['gift']
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"[%s]-[%s]-说：%s" % (self.request.remote_ip,
                                                 datetime.datetime.now().strftime("%H:%M:%S"), message))
            for i in range(3000):
                print(i)
                time.sleep(0.1)
                sl1 = i + 1
                # 随机取uid
                user = choice(uid)
                named = choice(name)
                se1 = choice(see)
                gift1 = {"gift2": [{
                    "id": 1111197118407278592,
                    "pr": 2,
                    "u": 0,
                    "nk": "sys",
                    "ic": 'null',
                    "r": 276687149,
                    "t": 1,
                    "st": 0,
                    "ct": "礼物",
                    "ex": {
                        "nickname": named,
                        "ge": "青春有我",
                        "co": sl1,
                        "he": 30,
                        "se": se1,
                        "gl": 1,
                        "de": 5,
                        "me": 2,
                        "icon": "https://img7.iqiyipic.com/passport/20180724/2b/27/passport_1466309899_153239260645722_130_130.jpg",
                        "uid": user,
                        "dh": "https://pic3.iqiyipic.com/common/20190328/yingyuanbang.png",
                        "gd": 110,
                        "fse": "https://static-s.iqiyi.com/ext/common/yingyuanbang_and.zip",
                        "ifse": "https://static-s.iqiyi.com/ext/common/yingyuanbang_ios.zip",
                        "pfse": "http://effect-live.iqiyi.com/dzb/pcw/yingyuanbang.swf",
                        "gr": 1,
                        "gf": "https://pic0.iqiyipic.com/common/20190328/yingyuanbang.gif\t",
                        "qd": 2230398923,
                        "si": "http://pic3.iqiyipic.com/common/20190304/LOGO.jpg",
                        "sne": "青春有你",
                        "isGroup": 0,
                        "user_name": named,
                        "user_face": "https://img7.iqiyipic.com/passport/20180811/37/5b/passport_1602399285_153391556453306_130_130.jpg",
                        "show_name": "青春有你",
                        "is_group": 0,
                        "product_name": "青春有我",
                        "pic": "https://pic3.iqiyipic.com/common/20190328/yingyuanbang.png",
                        "num": 1,
                        "msgId": "20190328172332722I4E135B8"
                    },
                    "ts": 1553765012727,
                    "a": 10000
                }]}
                qc1 = gift1['gift2']
                a = json.dumps(qc1)
                b = json.dumps(f)
                u.write_message(a)
                u.write_message(b)

    def on_close(self):
        self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message(u"[%s]-[%s]-离开聊天室" % (self.request.remote_ip,
                                                  datetime.datetime.now().strftime("%H:%M:%S")))

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


# “Make a script both importable and executable”
if __name__ == '__main__':
    # 全局的options对象，所有定义的选项变量都会作为该对象的属性。
    tornado.options.parse_command_line()
    # 创建tornado.web.Application对象，路由映射列表
    app = tornado.web.Application([
        # 主路由
        (r"/", IndexHandler),
        (r"/chat", ChatHandler),
    ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    # 创建一个IO循环的对象
    tornado.ioloop.IOLoop.current().start()
