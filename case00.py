from selenium import webdriver
from time import sleep
import unittest,time,random

class IwebshopTest00(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get(r"http://10.10.57.113:8080/iwebshop/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_case00(self):
        """用户注册成功"""
        driver=self.driver
        driver.find_element_by_xpath("//a[@class='reg']").click()
        driver.find_element_by_xpath("//input[@class='gray' and @name='email']").send_keys("1586887900%s@163.com"%(random.randint(1,100)))
        driver.find_element_by_xpath("//input[@class='gray' and @name='username']").send_keys("admin0%s"%(random.randint(1,100)))
        driver.find_element_by_xpath("//input[@class='gray' and @name='password']").send_keys("123456")
        driver.find_element_by_xpath("//input[@class='gray' and @name='repassword']").send_keys("123456")
        sleep(5)
        driver.find_element_by_xpath("//input[@class='submit_reg']").click()
        sleep(3)
        text=driver.find_element_by_xpath("//strong[@class='f14']").text
        try:
            self.assertEqual(text,"恭喜，操作成功！")
        except AssertionError as ae:
            time_style=time.strftime("%Y%m%d%H%M%S")
            test_path="../image/"
            file_name=test_path+time_style+"_registration_failed_"+str(random.randint(1,100))+".jpg"
            driver.get_screenshot_as_file(file_name)
            raise ae

    def tearDown(self):
        sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



