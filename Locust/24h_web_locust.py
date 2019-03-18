#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用python写web性能测试

# from locust import HttpLocust, TaskSet, task
#
# class UserBehavior(TaskSet):
#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         self.login()
#
#     def login(self):
#         self.client.post("/login", {"username":"ellen_key", "password":"education"})
#
#     @task(2)
#     def index(self):
#         self.client.get("/")
#
#     @task(1)
#     def profile(self):
#         self.client.get("/profile")
#
# class WebsiteUser(HttpLocust):
#     task_set = UserBehavior
#     min_wait = 5000
#     max_wait = 9000


# from locust import HttpLocust, TaskSet, task
#
# class WebsiteTasks(TaskSet):#创建UserBehavior()类继承TaskSet类，为用户行为。
#     @task(2)#用@task() 装饰该方法为一个任务。1表示一个Locust实例被挑选执行的权重，数值越大，执行频率越高。在当前UserBehavior()行为下只有一个baidu()任务，所以，这里的权重设置为几，并无影响。
#     def baidu(self):#创建baidu() 方法表示一个行为，访问百度首页。
#         self.client.get("/")
#         print('访问web')
#
#     @task(1)
#     def print(self):
#         print('测试权重')
#
# class WebsiteUser(HttpLocust):#WebsiteUser()类用于设置性能测试。
#     task_set = WebsiteTasks#指向一个定义了的用户行为类。
#     min_wait = 1000#用户执行任务之间等待时间的下界，单位：毫秒。
#     max_wait = 2000#用户执行任务之间等待时间的上界，单位：毫秒。
#     host = 'https://www.baidu.com/'


from locust import HttpLocust, TaskSet, task
# client.get===>requests.get
# client.post===>requests.post

class WebsiteTasks(TaskSet):
    @task(2)
    def swisstime24h(self):

        header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        r = self.client.get('/',headers = header)
        # print(r)
        r_code = r.status_code
        # print(r_code)
        assert r_code == 200
        print('首页加载压力测试')

    @task(1)
    def swisstime24h_login(self):
        b = self.client.post('/login', {"username":"15622518977", "password":"666666"})
        print('登录页面加载压力测试')
        assert b.status_code == 200

    @task(1)
    def swisstime24h_watch(self):
        w = self.client.get('/like/detail?gid=7159a57852b56b320adfd87e15546126e47d0d4e')
        # assert w.status_code == 200
        print('手表详情页加载压力测试')
        if w.status_code == 200:
            print('code ok')
        else:
            print('code no!!!!')


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 2000
    host = 'http://wap.lbiao.net'
