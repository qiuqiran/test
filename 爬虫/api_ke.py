#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Host: app.api.ke.com

import requests
import time
from bs4 import BeautifulSoup
import re

class Ke:

    def host(self):
        '''
        域名
        :return:
        '''
        url = 'https://app.api.ke.com'
        return url

    def city(self):
        '''
        城市列表
        :return:
        '''
        i = 3
        url = 'https://app.api.ke.com' + '/config/city/selectlist'
        querystring = {"request_ts": "1565836922"}
        headers = {
            'Authorization': "MjAxODAxMTFfaW9zOmFkNDI2OTY1NDliNjcwMjhlMzcxNDc0Mjc1OGE1YzlkZjNmZWMyMjI=",
            'Lianjia-Im-Version': "1",
            'Accept': "*/*",
            'Lianjia-Version': "2.14.0",
            'Device-Info': "scale=3.0;screenwidth=1242;screenheight=2208",
            'Lianjia-Timestamp': "1565836922.695044",
            'Accept-Language': "zh-Hans-CN;q=1",
            'Accept-Encoding': "br, gzip, deflate",
            'Connection': "keep-alive",
            'Referer': "lianjiabeike%3A%2F%2FLJMainViewController",
            'extension': "lj_idfa=7A93D287-F389-441F-B20F-A75D50B1069A&lj_idfv=316330AD-66B4-46A6-8F79-628501D97E91&lj_device_id_ios=5E1A2495-3E45-4E01-89D2-8DC978AF2F70&lj_keychain_id=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E&lj_duid=D2P6wckDajI4qp2GGq29dqzOMwBqqSZu8KXn79RBiTsHYXd7",
            'Page-Schema': "lianjiabeike%3A%2F%2FLJSelecteCityViewController",
            'Lianjia-City-Id': "440300",
            'User-Agent': "Beike 2.14.0;iPhone8,2;iOS 12.3.1;",
            'Cookie': "lianjia_uuid=5E1A2495-3E45-4E01-89D2-8DC978AF2F70; lianjia_ssid=715EEF16-D984-4453-90F3-BAB9EEB55ECF; lianjia_udid=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E, lianjia_uuid=5E1A2495-3E45-4E01-89D2-8DC978AF2F70; lianjia_ssid=715EEF16-D984-4453-90F3-BAB9EEB55ECF; lianjia_udid=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E; lianjia_uuid=266ff033-3fde-4ace-9edc-c05edc49dbc2; app_api_ke_servers=7b19c35c4bc33d9ac872a16269707baf; lianjia_ssid=715EEF16-D984-4453-90F3-BAB9EEB55ECF",
            'Lianjia-Device-Id': "94D38A82-91FE-47CD-9746-C3E9F1EF6D1E",
            'Cache-Control': "no-cache",
            'Postman-Token': "e74cd418-095a-4017-8ef5-c261520c6e73,b7c02bc4-38c8-426d-9744-8fb05241b6a6",
            'Host': "app.api.ke.com",
            'cache-control': "no-cache"
        }
        response = requests.get( url, headers=headers, params=querystring)
        # print(response.json()['data']['tab_list'][0]['title'])
        # print(response.json()['data']['tab_list'][0]['list'][0]['title'])
        # print(response.json()['data']['tab_list'][0]['list'][0]['cities'][3]['id'])
        # print(response.json()['data']['tab_list'][0]['list'][0]['cities'][3]['name'])
        id = response.json()['data']['tab_list'][0]['list']
        # shenzhenid = response.json()['data']['tab_list'][0]['list'][0]['cities'][i]['id']
        # shenzhenname = response.json()['data']['tab_list'][0]['list'][0]['cities'][i]['name']
        # shenzhennameabbr = response.json()['data']['tab_list'][0]['list'][0]['cities'][i]['abbr']
        # print(shenzhenid,shenzhenname,shenzhennameabbr)
        # print(id)
        # return shenzhenid
        for i in id:
            print(i['title'],'标题')
            for jj in range(len(i['cities'])):
                abbr = i['cities'][jj]['abbr']
                print(i['cities'][jj]['name'],abbr,i['cities'][jj]['id'])
                # abbrurl = 'https://{0}.ke.com/xiaoqu/'.format(abbr)
                # print(abbrurl)

    def index(self):
        '''
        新房楼盘
        :return:
        '''
        q = 2
        city_id = self.city()
        url = self.host() +'/newhouse/shellapp/feed/index'
        headers = {"User-Agent": "Beike 2.14.0;iPhone8,2;iOS 12.3.1"}
        params = {'city_id': city_id, 'request_ts': time.time()}
        f = requests.get(url=url,headers=headers, params=params)
        print('新房楼盘第一个楼盘名称：',f.json()['data']['resblock_list']['list'][q]['title'])
        project_name = '新房楼盘第一个楼盘名称：',f.json()['data']['resblock_list']['list'][q]['project_name']
        return project_name

    def detailv1(self):
        '''
        新房详情页
        :return:
        '''
        project_name = self.index()
        city_id = self.city()
        url = self.host() + '/newhouse/shellapp/resblock/detailv1'
        headers = {"User-Agent": "Beike 2.14.0;iPhone8,2;iOS 12.3.1"}
        params = {'city_id': city_id, 'request_ts': time.time(),
                  'page':1,'preload':0,'project_name':project_name}
        f = requests.get(url=url, headers=headers, params=params)
        print(f.json()['data']['data']['base_info']['show_price'],
              f.json()['data']['data']['base_info']['show_price_unit'],
              f.json()['data']['data']['base_info']['address'],)

    def searchv2(self):
        '''
        找小区
        :return:
        '''
        url = self.host() + '/house/community/searchv2'
        city_id = self.city()
        request_ts = "1566201368"
        Authorization = "MjAxODAxMTFfaW9zOjQwYzZhYzZiNWZkY2Q4OGQyYTEyN2JlODc3M2FhOTk3ZjJiZmRkMGI="
        i = 1 # 第几个楼盘
        headers = {
            'Host': "app.api.ke.com",
            'Authorization':Authorization ,
            'Lianjia-Im-Version': "1",
            'Accept': "*/*",
            'Lianjia-Version': "2.14.0",
            'Device-Info': "scale=3.0;screenwidth=1242;screenheight=2208",
            'Lianjia-Timestamp': request_ts,
            'Accept-Language': "zh-Hans-CN;q=1",
            'Accept-Encoding': "br, gzip, deflate",
            'Connection': "keep-alive",
            'Referer': "homepage",
            'extension': "lj_idfa=7A93D287-F389-441F-B20F-A75D50B1069A&lj_idfv=316330AD-66B4-46A6-8F79-628501D97E91&lj_device_id_ios=5E1A2495-3E45-4E01-89D2-8DC978AF2F70&lj_keychain_id=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E&lj_duid=D2P6wckDajI4qp2GGq29dqzOMwBqqSZu8KXn79RBiTsHYXd7",
            'Page-Schema': "community%2Flist",
            'Lianjia-City-Id': city_id,
            'User-Agent': "Beike 2.14.0;iPhone8,2;iOS 12.3.1;",
            'Cookie': "lianjia_uuid=5E1A2495-3E45-4E01-89D2-8DC978AF2F70; lianjia_ssid=24365501-C138-413A-B6CC-B2723D173DCE; lianjia_udid=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E",
            'Lianjia-Device-Id': "94D38A82-91FE-47CD-9746-C3E9F1EF6D1E",
            'cache-control': "no-cache",
        }
        querystring = {"city_id": city_id, "containerType": "0", "limit_count": "20", "limit_offset": "0","request_ts": request_ts}
        f = requests.get(url=url,data="", headers=headers, params=querystring)
        community_id = f.json()['data']['list'][i]['community_id']
        community_name = f.json()['data']['list'][i]['community_name']
        print('找小区第',i,'个楼盘名称：', community_name)
        print('找小区第',i,'个楼盘名称：', community_id)
        lists = [city_id,community_id]
        return lists

    def detailpart1(self):
        '''
        找小区楼盘详情页
        :return:
        '''
        url = self.host() + '/house/resblock/detailpart1'
        searchv2 = self.searchv2()
        city_id = searchv2[0]
        community_id = searchv2[1]
        request_ts = '1566201422'
        Authorization = "MjAxODAxMTFfaW9zOjE4ZDBkNjRiYWYzYTRkZTRjZTMwNDcxMWZjZWNjMDdhNTcwYWQxMDg="
        headers = {
            'Host': "app.api.ke.com",
            'Authorization': Authorization,
            'Lianjia-Im-Version': "1",
            'Accept': "*/*",
            'Lianjia-Version': "2.14.0",
            'Device-Info': "scale=3.0;screenwidth=1242;screenheight=2208",
            'Lianjia-Timestamp': request_ts,
            'Accept-Language': "zh-Hans-CN;q=1",
            'Accept-Encoding': "br, gzip, deflate",
            'Connection': "keep-alive",
            'Referer': "community%2Flist",
            'extension': "lj_idfa=7A93D287-F389-441F-B20F-A75D50B1069A&lj_idfv=316330AD-66B4-46A6-8F79-628501D97E91&lj_device_id_ios=5E1A2495-3E45-4E01-89D2-8DC978AF2F70&lj_keychain_id=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E&lj_duid=D2P6wckDajI4qp2GGq29dqzOMwBqqSZu8KXn79RBiTsHYXd7",
            'Page-Schema': "communitydetail",
            'Lianjia-City-Id': city_id,
            'User-Agent': "Beike 2.14.0;iPhone8,2;iOS 12.3.1;",
            'Cookie': "lianjia_uuid=5E1A2495-3E45-4E01-89D2-8DC978AF2F70; lianjia_ssid=24365501-C138-413A-B6CC-B2723D173DCE; lianjia_udid=94D38A82-91FE-47CD-9746-C3E9F1EF6D1E",
            'Lianjia-Device-Id': "94D38A82-91FE-47CD-9746-C3E9F1EF6D1E",
            'cache-control': "no-cache",
            'Postman-Token': "c8c3f64d-3e36-4244-a033-14281e4a5289"
        }
        querystring = {"id": community_id,"request_ts": request_ts}
        f = requests.get(url=url, data="", headers=headers, params=querystring)

        # print('贝壳指数：', f.json()['data'])
        print('贝壳指数：', f.json()['data']['quotation']['priceInfo']['title'])
        print('贝壳指数：', f.json()['data']['quotation']['priceInfo']['transPrice'],'元/平')


    def get_xiaoqu_city(self):
        '''
        获取所有的小区链接
        :return:
        '''
        url = 'https://www.ke.com/city/'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        l = ['']

        # 按照省份首字母选择
        city_recommend = soup.find_all('div',  {'class': 'city_province'})
        # print('共有国家',len(city_recommend))
        for i in range(len(city_recommend))[0:31]:
            city_list_tit = city_recommend[i].find('div', class_="city_list_tit c_b").get_text().strip().replace("\n", "")
            city_item_id = re.findall(r'a href="//(.*?).ke.com">(.*?)</a>',str(city_recommend[i]))
            city_abbr = re.findall(r'<a href="//(.*?).ke.com">(.*?)</a>',str(city_recommend[i]))
            # print(city_list_tit)
            # print(city_item_id,len(city_item_id))
            for ijkl in city_item_id:

                # 过滤没有小区的地区
                if '.fang' in str(ijkl[0]):
                    pass
                else:

                    abbrurl = 'https://{0}.ke.com/xiaoqu/'.format(ijkl[0])
                    # print(i, city_list_tit, ijkl[0], ijkl[1], abbrurl)
                    l.append(abbrurl)
        # print(l,len(l))
        return l




    def get_xiaoqu_selected(self):
        '''
        获取小区片区
        :return:
        '''
        url = self.get_xiaoqu_city()
        html = requests.get(url[1]).text
        soup = BeautifulSoup(html, 'html.parser')
        l = []

        # 获取所在地区的片区
        house_elems = soup.find_all('a', class_=" CLICKDATA")
        for i in house_elems:
            data_click_evtid = re.findall(r'href="/xiaoqu/(.*?)/" title="',str(i))
            name = i.text.replace("\n", "")


            data_click_evtid_abbrurl = url[1]+ data_click_evtid[0]
            # print(name,data_click_evtid_abbrurl)

            # print(i.text.replace("\n", "").strip())
            l.append(data_click_evtid_abbrurl)
        # print(l)
        return l








    def get_xiaoqu_info(self):
        '''
        爬网页拿到列表
        :return:
        '''

        # u = 'https://sz.ke.com/xiaoqu/huaqiaocheng1/pg1/'
        u = self.get_xiaoqu_selected()[0] + '/pg1/'
        # 写个判断拿到分页，再历遍

        html = requests.get(u).text
        soup = BeautifulSoup(html, 'html.parser')
        l = []

        # 获得有小区信息的panel
        house_elems = soup.find_all('li', class_="xiaoquListItem")
        for house_elem in house_elems:
            price = house_elem.find('div', class_="totalPrice")
            name = house_elem.find('div', class_='title')
            community_id = re.findall(r'ke.com/xiaoqu/(.*?)/" target="_blank"',str(name))
            on_sale = house_elem.find('div', class_="xiaoquListItemSellCount")
            house_url = re.findall(r'href="(.*?)" target="_blank" title="',str(name))
            # 继续清理数据
            price = price.text.strip()
            name = name.text.replace("\n", "")
            community_id = community_id[0]
            house_url = house_url[0]
            on_sale = on_sale.text.replace("\n", "").strip()
            # print(name,community_id,price,on_sale,house_url)
            l.append(house_url)
        # print(l)
        return l

    def get_house_info(self):
        '''
        拿楼盘详情页数据
        :return:
        '''
        u = self.get_xiaoqu_info()[0]
        html = requests.get(u).text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        # 拿到位置

        # 拿到指数
        tabBox = soup.find_all('div', class_="tabBox")
        print(tabBox)




Ke().get_house_info()