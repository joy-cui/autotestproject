"""
工具类
"""
from selenium.webdriver.common.by import By

from utils.logger import logger


class UtilElement:
    def __init__(self):
        pass

    def is_element_exist(driver, by, value):
        """
        判断当前元素是否存在
        :param by: 元素类型
        :param value: 元素属性值
        :return:
        """
        try:
            driver.find_element(by, value)
        except Exception as e:
            print("未找到元素:%s" % value)
            return False
        else:
            return True

    # def find_element(driver, ele_type, value):
    #     """
    #     查询页面元素
    #     :param ele_type: 元素定位类型
    #     :param value:元素定位属性值
    #     :return: 查找到的元素对象
    #     """
    #     ele = None
    #     try:
    #         if ele_type == "id":
    #             ele = driver.find_element(By.ID, value)
    #         if ele_type == "xpath":
    #             ele = driver.find_element(By.XPATH, value)
    #         else:
    #             logger.error("没有找到定位的元素 %s" % value)
    #     except Exception as err:
    #         # logger.error('find_element Error: {}'.format(err))
    #         ele = None
    #     return ele

    def find_elementById(driver, value):
        """
        根据id找对应的元素
        :param value:
        :return:
        """
        ele = None
        try:
            ele = driver.find_element(By.ID, value)
        except Exception as err:
            ele = None
        return ele

    def find_elementByXPath(driver, value):
        """
        根据xpath找对应的元素
        :param value:
        :return:
        """
        ele = None
        try:
            ele = driver.find_element(By.XPATH, value)
        except Exception as err:
            ele = None
        return ele

    def find_elementsByXPath(driver, value):
        """
        根据xpath找对应的元素
        :param value:
        :return:
        """
        ele = None
        try:
            ele = driver.find_elements(By.XPATH, value)
        except Exception as err:
            ele = None
        return ele

    def is_element_found(element):
        """
        判断该元素是否在当前页面
        :return:
        """
        if element is None:
            return False
        else:
            return True

    def elementClick(element):
        """
        点击效果
        :return:
        """
        if element is None:
            logger.error("元素不存在 %s" % element)
        else:
            element.click()

    def elementSendKey(element, value):
        """
        输入元素的参数
        :param value:
        :return:
        """
        if element is None:
            logger.error("没有找到定位的元素value： %s" % value)
        else:
            element.clear()
            element.send_keys(value)
