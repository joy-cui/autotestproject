# from selenium import webdriver
from appium import webdriver
from provar import var
from utils.config import Config


def init_driver():
    desire_cap = Config().getDesire()
    print(desire_cap)
    driver_path = Config().get('Driver')
    print(driver_path)
    var.driver = webdriver.Remote(driver_path, desire_cap)
    var.driver.launch_app()



class UtilDriver:
    def __init__(self):
        pass

