import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from provar import var
from utils.config import Config
from utils.logger import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = var.DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_report(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()



if __name__ == '__main__':
    print("main")
    now = time.strftime("%Y%m%d-%H%M%S")
    report = var.REPORT_PATH + "\\" + now + "-" + "report.html"
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_report'))





