

'''
AW大师接口压力测试
https://docs.locust.io/en/stable/quickstart.html

模拟场景 现场100人，每秒10人启动小程序进入精选首页查看，然后进入其中一个楼盘详情页

1.生成100人token和id
2.进入首页
3.进入楼盘详情页

'''



from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(2)
    def view(self):
        '''
        精选-首页 -- v3.0.1-- 杨立伟
        :return:
        '''
        Authorization = "eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiJhNGowcDciLCJzdWIiOiJjbGllbnRJZDp3eDZjNjQyM2M5ZWZiNDRjNzU6NjQ3IiwiZXhwIjoxNTUxNzc4NTc5LCJpYXQiOjE1NTExNzM3Nzl9.egVS7HDbT6dNo4cU36fje1wEHf5gXIQPBSbs5tVbmSwGJ8g7FoY0dGSXdAhPsqjFCNWc13_bUqCb4BqpTHjsNg"
        appId = "wx6c6423c9efb44c75"
        city = "全国"
        header = {"Authorization":Authorization, "appId":appId }
        params = {"city":city}
        r = self.client.get("/miniapp/home/view",headers = header,params=params)
        # json = r.json()
        # print(json)
        print("精选-首页")

    @task(1)
    def linker(self):
        '''
        经纪人详情页楼盘列表 -- v3.0.1-- 郭凯
        :return:
        '''
        Authorization = "eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiJhNGowcDciLCJzdWIiOiJjbGllbnRJZDp3eDZjNjQyM2M5ZWZiNDRjNzU6NjQ3IiwiZXhwIjoxNTUxNzc4NTc5LCJpYXQiOjE1NTExNzM3Nzl9.egVS7HDbT6dNo4cU36fje1wEHf5gXIQPBSbs5tVbmSwGJ8g7FoY0dGSXdAhPsqjFCNWc13_bUqCb4BqpTHjsNg"
        appId = "wx6c6423c9efb44c75"
        agentId = 4773
        header = {"Authorization":Authorization, "appId":appId }
        params = {"agentId":agentId}
        r = self.client.get("/miniapp/linker/agent/info/linker",headers = header,params=params)
        # json = r.json()
        # print(json)
        print("经纪人详情页楼盘列表")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # 等待的最小和最大时间（以毫秒为单位）
    min_wait = 5000
    max_wait = 9000
    host = "https://sit.zooming-data.com/helper-rest/"