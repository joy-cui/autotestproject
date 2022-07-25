import os

from provar import var
from utils.file_reader import YamlReader




class Config:
    def __init__(self, config=var.CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

    def getDesire(self):
        """
        获取配置文件中的配置信息
        :return: driver
        """

        c = Config().get('device')
        # devices_list = c.get("devices_list")
        # print("devices_list=%s" %devices_list)
        desire_cap = {}
        desire_cap["platformName"] = c.get("platformName")
        desire_cap["deviceName"] = c.get("deviceName")
        desire_cap["appPackage"] = c.get("appPackage")
        desire_cap["appActivity"] = c.get("appActivity")
        desire_cap["noReset"] = c.get("noReset")
        # desire_cap["skipDeviceInitialization"] = c.get("skipDeviceInitialization")
        desire_cap["platformVersion"] = c.get("platformVersion")
        return desire_cap
