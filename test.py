from selenium.webdriver.remote import webdriver
from selenium.webdriver.common.by import By
class TestDW:
    def setup(self):

        desire_cap = {}
        desire_cap["platformName"] = "Android"
        desire_cap["deviceName"] = "1e4218b1"
        desire_cap["appPackage"] = "com.example.android.contactmanager"
        desire_cap["appActivity"] = "com.example.android.contactmanager.ContactManager"
        desire_cap["noReset"] = "true"
        # desire_cap["dontStopAppOnReset"] = "true"
        desire_cap["skipDeviceInitialization"] = "true"
        desire_cap["platformVersion"] = "10.0.0"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # def test_touch_action(self):
    #     action = TouchAction(self.driver)
    #     window_ret = self.driver.get_window_rect()  # 获取屏幕的尺寸
    #     width = window_ret['width']
    #     height = window_ret['height']
    #     x1 = int(width / 2)
    #     y_start = int(height * (4/5))  # 向上滑动，起点为屏幕的4/5处
    #     y_end = int(height * (1/5))
    #     action.press(x=x1, y=y_start).wait(500).move_to(x=x1, y=y_end).release().perform()

    # def is_element_exist(driver, by, value):
    #     try:
    #         driver.find_element(by, value)
    #     except  as e:
    #         return ExceptionFalse
    #     else:
    #         return True