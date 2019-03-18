#腾讯视频投票#

from selenium import webdriver
import unittest
import time

class Tencent_vote(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://v.qq.com/biu/comingone?ptag=jimu.66822.zt')
        time.sleep(1)
        self.title = self.driver.title
        a = self.title
        self.assertAlmostEqual('明日之子勇闯点赞榜',a)
        print('准备开始')

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
        #下面开始写登录授权
        self.driver.find_element_by_xpath('//*[@id="login_win_type"]/div[2]/div/div/div[2]/a[1]').click()#选择qq登录
        time.sleep(2)


        ## 切换到qq登录弹窗授权页面
        self.driver.switch_to.frame('_login_frame_quick_')

        time.sleep(1)
        #------------下面是选择qq快捷登录前提是电脑已经登录了qq----------------
        self.driver.find_element_by_xpath('//*[@id="nick_404657468"]').click()#选择qq快捷登录
        time.sleep(2)

        #------------下面是选择qq账号登录，选择这里就要把上面的qq快捷登录注释掉，2者取其一------------------
        # self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()#选择qq账号登录
        # self.driver.find_element_by_xpath('//*[@id="u"]').clear()#清空账号
        # self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('404657468')#输入qq账号
        # self.driver.find_element_by_xpath('//*[@id="p"]').clear()  # 清空密码
        # self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('404657468@qq.com')  # 输入qq密码
        # self.driver.find_element_by_xpath('//*[@id="login_button"]').click()#点击登录
        # time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/button').click()#重新点击
        time.sleep(1)
        print('点赞一次')



if __name__ == '__main__':
    unittest.main()