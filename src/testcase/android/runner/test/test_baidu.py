import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from provar import var
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import Config
from utils.file_reader import ExcelReader
from utils.logger import logger


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = var.DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver = webdriver.Edge()
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search2(self):
        logger.info("ceshi === test_search2")
        now = time.strftime("%Y%m%d-%H%M%S")
        report_name = var.REPORT_PATH + "\\" + now + "-" + "report.html"
        logger.info("测试报告：" + report_name)
        fp = open(report_name, "wb")
        runner = HTMLTestRunner(stream=fp,title = "测试报告",description = "浏览器测试")
        runner.run(TestBaiDu('test_search'))
        fp.close()


    def test_search(self):
        datas = ExcelReader(self.excel).data
        logger.info(datas)
        for d in datas:
            logger.info(d)
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info("test_search: "+link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()

