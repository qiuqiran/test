#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task


class S24h_api(TaskSet):
    @task(2)
    def api_watch1(self):
        a = self.client.get('/3743eb777031bf03aad63d78fa3dd0a0.jpg?details=1')
        print('api图片1压力测试完成')
        assert a.status_code == 200

    @task(1)
    def api_watch2(self):
        b = self.client.get('/5ecbd62ba7efc7a36d53940a96aab683.jpg?details=1')
        print('api图片2压力测试完成')
        assert b.status_code == 200

    @task(3)
    def api_watch3(self):
        c = self.client.get('/bf9051a27b92b2a3f825b66cd972e803.jpg?details=1')
        print('api图片3压力测试完成')
        assert c.status_code == 200






class S24h_api_test(HttpLocust):
    task_set = S24h_api
    min_wait = 1000
    max_wait = 2000
    host = 'http://image.lbiao.net/uploads/st24vip_upload/uploads/20180510/'

