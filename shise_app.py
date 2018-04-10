import unittest
from appium import webdriver
import time

class ShiSe(unittest.TestCase):

    # app的配置字典
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'Android Emulator'
    #这两是要改的
    desired_caps['appPackage'] = 'com.kingnez.umasou.app'#包名
    desired_caps['appActivity'] = '.activity.SplashActivity'#启动类名

    def setUp(self):
        # 创建驱动类
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', ShiSe.desired_caps)

    #测试用例
    def test_qidong(self):
        driver=self.driver
        window_size = driver.get_window_size('current');
        print(window_size)
        #点击发现
        driver.find_element_by_id("image_search").click()
        time.sleep(2)
        driver.find_element_by_name(u"撸串的季节又到了").click()
        time.sleep(2)
        driver.find_element_by_id("card_user_name").click()
        time.sleep(2)
        #点击私信
        driver.find_element_by_id("btn_mail").click()
        time.sleep(2)
        driver.find_element_by_id("session_input").send_keys("I love beer")
        time.sleep(2)
        driver.find_element_by_id("session_btn").click()




    def tearDown(self):
        print("tearDown()")
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()

