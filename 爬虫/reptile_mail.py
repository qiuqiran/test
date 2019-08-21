


import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class Reptile:
    '''
    邮件获取最新文章模块
    '''

    def send_email(self, a ):
        '''发送邮件'''
        # --------填写邮箱信息-----
        me_email = '2167598@163.com'
        me_pass = 'qiuqiran123456'
        kew = '404657468@qq.com'
        kew2 = 'qiuqiran@gmail.com'

        # -----发送信息-----
        msg = MIMEMultipart()  # 附件
        msg['From'] = formataddr(["qiuqiran", me_email])
        msg['To'] = formataddr(["", kew])
        msg['Subject'] = "财富/福布斯每日最新"

        # ----------正文-------
        view = a
        text_plain = MIMEText(view, 'plain', 'utf-8')
        msg.attach(text_plain)

        # ----------发送------------
        try:
            server = smtplib.SMTP_SSL("smtp.163.com", 465)
            server.login(me_email, me_pass)
            server.sendmail(me_email, [kew, kew2, ], msg.as_string())
            server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')

    def fortune(self):
        '''
        财富中文网
        :return:
        '''
        html = urlopen('http://www.fortunechina.com/').read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        # 获取左边头条
        headtitle = soup.find_all('p', {'class': 'headtitle'})
        headtitle_href = re.findall(r'<a href="(.*?)" target="_blank"',str(headtitle))
        headtitle_title = re.findall(r'target="_blank">(.*?)</a>',str(headtitle))
        a = headtitle_title[0]
        a_l = headtitle_href[0]

        # 获取右边3条
        otherhead = soup.find_all('div', {'class': 'otherhead'})

        othertitle_href = re.findall(r'<a href="(.*?)" target="_blank"',str(otherhead))
        othertitle_title = re.findall(r'target="_blank">(.*?)</a>',str(otherhead))
        othertitle_title_1 = othertitle_title[0]
        othertitle_href_1 = othertitle_href[0]
        othertitle_title_2 = othertitle_title[1]
        othertitle_href_2 = othertitle_href[1]
        othertitle_title_3 = othertitle_title[2]
        othertitle_href_3 = othertitle_href[2]
        return a,a_l,othertitle_title_1,othertitle_href_1,othertitle_title_2,othertitle_href_2,othertitle_title_3,othertitle_href_3

    def forbeschina(self):
        '''
        福布斯中文网
        :return:
        '''
        html = urlopen('http://china.forbeschina.com/').read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        # 获取列表
        row = soup.find_all('div', {'class': 'news_center edit_pri'})

        href = re.findall(r'href="(.*?)" style="height:auto;"', str(row))
        title = re.findall(r'>(.*?)</a>', str(row))

        t_0 = title[0]
        h_0 = "http://china" + href[0].strip(" http://www")
        t_1 = title[1]
        h_1 = "http://china" + href[1].strip(" http://www")
        t_2 = title[2]
        h_2 = "http://china" + href[2].strip(" http://www")
        t_3 = title[3]
        h_3 = "http://china" + href[3].strip(" http://www")
        t_4 = title[4]
        h_4 = "http://china" + href[4].strip(" http://www")
        t_5 = title[5]
        h_5 = "http://china" + href[5].strip(" http://www")
        t_6 = title[6]
        h_6 = "http://china" + href[6].strip(" http://www")
        t_7 = title[7]
        h_7 = "http://china" + href[7].strip(" http://www")

        return t_0,h_0,t_1,h_1,t_2,h_2,t_3,h_3,t_4,h_4,t_5,h_5,t_6,h_6,t_7,h_7




    def mail_plain(self):
        '''
        生成每日最新内容
        :return:
        '''
        # a 是财富
        a = Reptile().fortune()

        # b 是福布斯
        b = Reptile().forbeschina()
        # print(b)

        palin = "今日最新\n\n财富中文网：\n1.%s\n%s\n2.%s\n%s\n3.%s\n%s\n4.%s\n%s\n\n福布斯中文网：\n1.%s\n%s\n2.%s\n%s\n3.%s\n%s\n4.%s\n%s\n5.%s\n%s\n6.%s\n%s\n7.%s\n%s\n8.%s\n%s\n"\
                %(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11],b[12],b[13],b[14],b[15])
        print(palin)

        Reptile().send_email(palin)


Reptile().mail_plain()