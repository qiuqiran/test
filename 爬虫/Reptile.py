

# 所以爬虫脚本都整理到这里
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


class Reptile:
    '''
    整理所有的爬虫到这里
    '''

    def setUp(self):
        print("""
    ###############################
        自家用的爬虫
        Author: Kew
        Version: 1.3.0
    ###############################
        """)

    def baidu_one(self):
        '''baidu 爬虫1'''

        u = 'http://news.baidu.com/finance'
        html = urlopen(u).read().decode('utf-8')
        # print(html)
        k = re.findall(r'target="_blank">(\w.*?)</a></li>',html)

        for i in k:
           print(i)

    def baidu_two(self):
        '''baidu 爬虫2'''

        html = urlopen('http://news.baidu.com/finance').read().decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')

        q = soup.find_all('ul',{'class':'ulist fb-list'})
        print('今天最新百度的财经新闻如下：\n')
        for i in q:
            print(i.get_text())

    def bing_img_dowmload(self):
        u = 'http://www.nationalgeographic.com.cn/animals/'

        html = requests.get(u).text
        soup = BeautifulSoup(html, 'html.parser')
        img_u = soup.find_all('ul', {'class': 'img_list'})
        # img_u = soup.find_all('section',{'class':'showImg-list'})

        for ul in img_u:
            imgs = ul.find_all('img')
            for img in imgs:
                url = img['src']
                r = requests.get(url)
                image_name = url.split('/')[-1]
                with open('./img/%s' % image_name, 'wb') as f:
                    for chunk in r.iter_content():
                        f.write(chunk)
                print('Saved %s' % image_name)

    def dowmload_demo_one(self):
        import os
        os.makedirs('./img/', exist_ok=True)

        img_u = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
        # 方法1
        from urllib.request import urlretrieve
        urlretrieve(img_u, './img/img1.jpg')

    def dowmload_demo_two(self):
        import os
        os.makedirs('./img/', exist_ok=True)

        img_u = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
        # 方法2
        import requests
        r = requests.get(img_u)
        with open('./img/img2.png', 'wb') as f:
            f.write(r.content)

    def FTnews(self):
        html = urlopen('http://www.ftchinese.com/').read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        q = soup.find_all('div', {'class': 'item-lead'})
        for i in q[2:]:
            # print(h[i])
            print(i.get_text())
            # print('--------------------------')

    def vipstation(self):
        '''
        http://www.vipstation.com.hk/
        名人站数据爬取
        使用方法：在self.model_num 输入后台型号，或者名人站貨品編號,运行即可,型号有空格用%20代替
        :return:
        '''
        self.model_num = '3137BA11986'
        self.url = 'http://www.vipstation.com.hk/products/Detailed/' + self.model_num
        self.html_data = urlopen(self.url).read().decode('utf-8')
        self.title = re.findall(r'<div class="col-sm-12 p0 pg_price_top">(.*?)</div>', self.html_data)
        print(self.title[0])
        self.all_data = re.findall(r' <div class="col-md-3 col-sm-4 p0">(.*?)</div>', self.html_data)
        print('共爬取:', len(self.all_data), '参数')
        for i in self.all_data:
            print(i)

        soup = BeautifulSoup(self.html_data, 'html.parser')
        photo = soup.find_all('div', {'class': 'pp_show'})
        photo_num = str(photo)

        print('共看到有：', len(re.findall(r'https://erp.vipstation.com.hk', photo_num)), '张图片')
        price = re.findall(r'<em class="price">(.*?)</em>', self.html_data)
        print('共看到有', len(price), '个价格,分别是', price)
        if len(price) == 1:
            print('原價/商品公价/original_price: ', price[0], 'HKD')

        else:

            print('現價/平台售价/price：', price[1], 'HKD')
            print('原價/商品公价/original_price: ', price[2], 'HKD')

    def fortune(self):
        '''
        财富中文网
        :return:
        '''
        html = urlopen('http://www.fortunechina.com/').read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        # 获取左边头条
        q = soup.find_all('div', {'class': 'toutiao'})
        headtitle = soup.find_all('p', {'class': 'headtitle'})

        # k = re.findall(r'target="_blank">(\w.*?)</a></li>',html)
        headtitle_href = re.findall(r'<a href="(.*?)" target="_blank"',str(headtitle))
        headtitle_title = re.findall(r'target="_blank">(.*?)</a>',str(headtitle))
        # print(headtitle_title[0],headtitle_href[0])

        # 获取右边3条
        otherhead = soup.find_all('div', {'class': 'otherhead'})

        othertitle_href = re.findall(r'<a href="(.*?)" target="_blank"',str(otherhead))
        othertitle_title = re.findall(r'target="_blank">(.*?)</a>',str(otherhead))
        print(othertitle_href,othertitle_title)

        # print(otherhead)


Reptile().fortune()
