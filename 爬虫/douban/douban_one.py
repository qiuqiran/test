#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib import request
import re
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class Douban_Crawl_data():

    """
    ###############################
        自家用的豆瓣电影短评爬虫
        Author: Kew_one
        Version: 2.0.0
        Date: 2018-03-28
    ###############################
    """
    def Douban_1(self):

        #-------豆瓣id
        url = 'https://movie.douban.com/subject/27605698/comments?status=P'
        #--------导航到网页
        print('短评爬虫准备就绪, 准备爬取数据######')
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)#隐藏浏览器
        print('打开短评页面中###################')
        driver.get(url)

        #---------反复爬取
        print('好了，开始抓取###################')
        for a in range(6):
            if a < 5:
                html_data1 = request.urlopen(driver.current_url).read().decode('utf-8')#获取当前数据
                title = re.findall(r'<title>(.*?)</title>', html_data1)  # 标题
                name = re.findall(r'<a.+people.+">(.+)</a>', html_data1)  # 用户名
                duanping = re.findall(r'<p class="">(.+)', html_data1)  # 短评
                duanping_items = dict(zip(name, duanping))#合并数据
                for x in range(len(duanping_items)):
                    with open('E:\kew\kkk\kew-webapp\douban\douban_01.txt', 'a', encoding='utf-8') as f:
                        f.write('\n----------\n'+str(name[x])+'de短评是:'+str(duanping[x]))#写入当前内容
                print('抓取中##########################')
                driver.find_element_by_link_text('后页 >').click()#下一页
                print('OK,下一页#######################')
                time.sleep(5)

            elif a == 5:
                html_data1 = request.urlopen(driver.current_url).read().decode('utf-8')#获取当前数据
                title = re.findall(r'<title>(.*?)</title>', html_data1)  # 标题
                name = re.findall(r'<a.+people.+">(.+)</a>', html_data1)  # 用户名
                duanping = re.findall(r'<p class="">(.+)', html_data1)  # 短评
                duanping_items = dict(zip(name, duanping))#合并数据
                for x in range(len(duanping_items)):
                    with open('E:\kew\kkk\kew-webapp\douban\douban_01.txt', 'a', encoding='utf-8') as f:
                        f.write('\n----------\n' + str(name[x]) + 'de短评是:' + str(duanping[x]))#写入当前内容
                print('好了，短评抓取结束################')
                driver.quit()
            else:
                print('防止触发爬虫机制不爬了#############')
                driver.quit()

    def Douban_2(self):

        # -------豆瓣id
        # url = 'https://movie.douban.com/subject/27605698/comments?status=P'


        a ='26336252'
        b = str(20*2)
        url ='https://movie.douban.com/subject/'+a+'/comments?start='+b+'&limit=20&sort=new_score&status=P'
        # --------导航到网页
        print('短评爬虫准备就绪, 准备爬取数据######')
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)  # 隐藏浏览器
        print('打开短评页面中###################')
        driver.get(url)

        # ---------反复爬取
        print('好了，开始抓取###################')
        page = 1
        while page < 5:

            html = request.urlopen(driver.current_url).read().decode('utf-8')
            title = re.findall(r'<title>(.*?)</title>', html)  # 标题
            name = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
            duanping = re.findall(r'<span class="short">(.*?)</span>', html)  # 短评
            duanping_items = dict(zip(name, duanping))  # 合并数据
            for x in range(len(duanping_items)):
                with open('E:\kew\kew-webapp\爬虫\douban\douban_01.txt', 'a', encoding='utf-8') as f:
                    f.write('\n----------\n' + str(name[x]) + 'de短评是:' + str(duanping[x]))  # 写入当前内容
                    # print(title)
            print('好了，第',page,'页短评抓取结束##########')
            page = page + 1
            driver.find_element_by_link_text('后页 >').click()  # 下一页
            print('OK,下一页#######################')
            time.sleep(5)

    def nowplaying_name(self):
        '''
        最近上映的电影
        :return:
        '''

        url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
        html = request.urlopen(url).read().decode('utf-8')
        nowplaying_name = re.findall(r'alt="(.*?)" rel="nofollow"', html)
        return nowplaying_name

    def nowplaying_link_num(self):
        '''
        最新上架电影id
        '''
        url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
        html = request.urlopen(url).read().decode('utf-8')
        nowplaying_link_num = re.findall(
            r'<a href="https://movie.douban.com/subject/(.*?)/\?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">',
            html)
        return nowplaying_link_num

    def merge(self):
        '''
        合并id名字
        :return:
        '''
        name = Douban_Crawl_data().nowplaying_name()
        id = Douban_Crawl_data().nowplaying_link_num()
        for i in range(len(id)):
            print(name[i],id[i])

    def dddddd(self):
        '''
        指定id爬取
        :return:
        '''
        # https: // movie.douban.com / subject / 1421884 /
        a = '1421884' #黑衣人：全球追缉 19971676
        import random
        lss = [10,20,30,40,50,60,70,80]
        b = str(random.choice(lss))
        url = 'https://movie.douban.com/subject/' + a + '/comments?start=' + b + '&limit=20&sort=new_score&status=P'
        # print(url)


        html = request.urlopen(url).read().decode('utf-8')
        name = re.findall(r'<a.+people.+">(.+)</a>', html)  # 用户名
        duanping = re.findall(r'<span class="short">(.*?)</span>', html)  # 短评
        duanping_items = dict(zip(name, duanping))  # 合并数据
        for x in range(len(duanping_items)):
                print('@@' + str(name[x]) + '===>' + str(duanping[x]) )












if __name__=='__main__':
    Douban_Crawl_data().dddddd()



