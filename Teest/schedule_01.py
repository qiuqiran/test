#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 定时任务调度用芹菜celery，或者就写个脚本塞到crontab中，轻量级的定时任务调度的库：schedule。
# 库的安装pip install schedule

import schedule
import time
import threading


def job1():

    print('work1...',time.ctime())

def job2():
    print('work2...',time.ctime())

# 多线程
def job1_task():
    threading.Thread(target=job1).start()

def job2_task():
    threading.Thread(target=job2).start()




schedule.every(10).seconds.do(job1_task)
schedule.every(10).seconds.do(job2_task)


# job()
# schedule.every(10).seconds.do(job)
# schedule.every(1).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)
# # schedule.every(5).to(10).minutes.do(job)
# # schedule.every().monday.do(job)
# # schedule.every().wednesday.at("13:15").do(job)
# # schedule.every().minute.at(":17").do(job)
#

while True:
    schedule.run_pending()
    time.sleep(1)

