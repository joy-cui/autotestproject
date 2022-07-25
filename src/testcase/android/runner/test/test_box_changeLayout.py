import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


def is_element_exist(driver, by, value):
    try:
        driver.find_element(by, value)
    except Exception as e:
        print("未找到元素:%s" % value)
        return False
    else:
        return True


def click_fun(driver, by, value):
    if is_element_exist(driver, by, value):
        driver.find_element(by, value).click()
        # time.sleep(1)


# def tap_fun(driver, by, value):
#     if is_element_exist(driver, by, value):
#         driver.find_element(by, value).()

# def open_layout_fun(driver, by, content, value):
#     try:
#         driver.find_element(by, value)
#     except Exception as e:
#         # 打开布局页面
#         # 显示foot按钮
#         click_fun(driver, By.ID, content)
#     click_fun(driver, by, value)


def inputtxt_fun(driver: object, by: object, value: object, data: object) -> object:
    if is_element_exist(driver, by, value):
        driver.find_element(by, value).clear()
        driver.find_element(by, value).send_keys(data)
        # time.sleep(1)


# 会议号
meetid = "5457"
# 切换布局间隔时间
changelayout_time = 2
#是否运行开始会议
is_start_meet = False
# 循环入退会次数
run_meet_num = 1000
# 循环切布局的次数
change_layout_num = 100

class TestBox:

    def setup(self):
        desire_cap = {}
        desire_cap["platformName"] = "Android"
        desire_cap["deviceName"] = "10.10.6.12:5555"
        desire_cap["appPackage"] = "org.suirui.huijian.tv"
        desire_cap["appActivity"] = ".activity.WelcomeActivity"
        desire_cap["noReset"] = "true"
        # desire_cap["dontStopAppOnReset"] = "true"
        desire_cap["skipDeviceInitialization"] = "true"
        desire_cap["platformVersion"] = "7.1.1"
        print("开始连接设备===")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)
        print("连接成功===")

    # def teardown(self):
    #     self.driver.quit()

    def exit_fun(self):
        if not is_element_exist(self.driver, By.ID, self.exit_meet):
            click_fun(self.driver, By.ID, self.content)
        click_fun(self.driver, By.ID, self.exit_meet)
        click_fun(self.driver, By.ID, self.leave_meet)

    def test_layout(self):
        # 获取窗口大小
        size = self.driver.get_window_size()
        # 确定要划动的点x轴的位置为屏幕中央
        x = size["width"] * 0.5
        # 确定从下到上划动距离开始和结束位置
        y_start = size["height"] * 0.9
        y_end = size["height"] * 0.1
        # 加入会议
        join_meet = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.ImageView[1]'
        join_meet_back = 'org.suirui.huijian.tv:id/back_btn'
        # 加入会议输入框
        # org.suirui.huijian.tv:id/input_number_tv
        input_number = 'org.suirui.huijian.tv:id/input_number_tv'
        # 确定加入会议
        sure_join_meet = 'org.suirui.huijian.tv:id/num_j'
        # 开始会议
        start_meet = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.ImageView[2]'
        # 布局
        change_layout = 'org.suirui.huijian.tv:id/btn_change_scence'
        # 自动分屏
        auto_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageButton'
        # 1分屏
        one_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageButton'
        two_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.ImageButton'
        three_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.ImageButton'
        four_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.ImageButton'
        five_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.ImageButton'
        six_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.ImageButton'
        seven_layout = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[8]/android.widget.ImageButton'
        # 最外层 android:id/viewo_main_window
        self.content = 'android:id/content'
        # 离开会议
        self.exit_meet = 'org.suirui.huijian.tv:id/btnEnd'
        self.leave_meet = 'org.suirui.huijian.tv:id/tv_leave_meeting_txt'

        for i in range(0, run_meet_num):
            # 在会中，先退会议
            if is_element_exist(self.driver, By.ID, self.content):
                self.exit_fun()

            # 如果在加入会议页面，先返回首页
            if is_element_exist(self.driver, By.ID, sure_join_meet):
               click_fun(self.driver, By.ID, join_meet_back)
            # 加入会议
            if not is_start_meet:
                click_fun(self.driver, By.XPATH, join_meet)
                inputtxt_fun(self.driver, By.ID, input_number, meetid)
                click_fun(self.driver, By.ID, sure_join_meet)
            else:
                # 开始会议
                click_fun(self.driver, By.XPATH, start_meet)
            # 切换布局
            for j in range(0, change_layout_num):
                print("开始选择的布局")
                # ta = TouchAction(self.driver)
                # # 按住起始位置移动到结束位置
                # ta.press(x=x, y=y_start).wait(200)
                #
                # if not is_element_exist(self.driver, By.ID, change_layout):
                #     click_fun(self.driver, By.ID, content)
                # 开始切换布局
                num = random.randint(0, 7)
                print("选择的布局:%d" % num)
                if not is_element_exist(self.driver, By.XPATH, auto_layout):
                    if not is_element_exist(self.driver, By.ID, change_layout):
                        click_fun(self.driver, By.ID, self.content)
                    click_fun(self.driver, By.ID, change_layout)
                if num == 0:
                    click_fun(self.driver, By.XPATH, auto_layout)
                if num == 1:
                    click_fun(self.driver, By.XPATH, one_layout)
                if num == 2:
                    click_fun(self.driver, By.XPATH, two_layout)
                if num == 3:
                    click_fun(self.driver, By.XPATH, three_layout)
                if num == 4:
                    click_fun(self.driver, By.XPATH, four_layout)
                if num == 5:
                    click_fun(self.driver, By.XPATH, five_layout)
                if num == 6:
                    click_fun(self.driver, By.XPATH, six_layout)
                if num == 7:
                    click_fun(self.driver, By.XPATH, seven_layout)
                time.sleep(changelayout_time)

            # 离开会议
            self.exit_fun()

            time.sleep(2)
