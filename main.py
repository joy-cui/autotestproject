from selenium import webdriver
from selenium.webdriver.common.by import By
# driver.find_element(By.XPATH, '//*[@id="kw"]')
# # 根据xpath选择元素(万金油)
# driver.find_element(By.CSS_SELECTOR, '#kw')
# # 根据css选择器选择元素
# driver.find_element(By.NAME, 'wd')
# # 根据name属性值选择元素
# driver.find_element(By.CLASS_NAME, 's_ipt')
# # 根据类名选择元素
# driver.find_element(By.LINK_TEXT, 'hao123')
# # 根据链接文本选择元素
# driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')
# # 根据包含文本选择
# driver.find_element(By.TAG_NAME, 'title')
# # 根据标签名选择
# # 目标元素在当前html中是唯一标签或众多标签第一个时候使用
# driver.find_element(By.ID, 'su')
# # 根据id选择
def is_element_exist(driver, by, value):
    try:
        driver.find_element(by, value)
    except Exception as e:
        return False
    else:
        return True
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '10.0'

desire_cap = {}
desire_cap["platformName"] = "Android"
desire_cap["deviceName"] = "1e4218b1"
desire_cap["appPackage"] = "com.example.android.contactmanager"
desire_cap["appActivity"] = "com.example.android.contactmanager.ContactManager"
desire_cap["noReset"] = "true"
# desire_cap["dontStopAppOnReset"] = "true"
desire_cap["skipDeviceInitialization"] = "true"
desire_cap["platformVersion"] = "10.0.0"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(5)
for i in range(0,10):
    # 开始会议
    # org.suirui.huijian.video:id/m_start_meeting_btn
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/m_start_meeting_btn').click()

    # 离开会议 org.suirui.huijian.video:id/btnHeadEnd
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/btnHeadEnd').click()
    # org.suirui.huijian.video:id/btnLMeet
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/btnLMeet').click()
    driver.implicitly_wait(5)
    #预约会议
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/m_order_meeting_btn').click()
    driver.implicitly_wait(5)
    ## 输入会议名称
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/edt_meeting_theme').send_keys("appium创建的会议")
    driver.implicitly_wait(5)
    # 高级选项
    # org.suirui.huijian.video:id/rl_high_option
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/rl_high_option').click()
    driver.implicitly_wait(5)

    # 入会后静音  org.suirui.huijian.video:id/sw_meeting_mute
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/sw_meeting_mute').click()
    driver.implicitly_wait(5)
    #
    #直播选项 org.suirui.huijian.video:id/tv_recording_level
    # driver.find_element(By.ID, 'org.suirui.huijian.video:id/tv_recording_level').click()
    # driver.implicitly_wait(5)
    # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]
    # driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[2]').click()
    # driver.implicitly_wait(5)
    # 高级选项返回 org.suirui.huijian.video:id/btnBack
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/btnBack').click()
    driver.implicitly_wait(5)

    # 预约会议提交 org.suirui.huijian.video:id/btn_submit
    # driver.find_element(By.ID, 'org.suirui.huijian.video:id/btn_submit').click()
    # driver.implicitly_wait(5)

   # 安排会议返回  org.suirui.huijian.video:id/btnBack
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/btnBack').click()
    driver.implicitly_wait(5)


    #通讯录 org.suirui.huijian.video:id/imv_3
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/imv_3').click()
    driver.implicitly_wait(10)
    # 我的 	 org.suirui.huijian.video:id/imv_4
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/imv_4').click()
    driver.implicitly_wait(5)
    # 首页 org.suirui.huijian.video:id/imv_1
    driver.find_element(By.ID, 'org.suirui.huijian.video:id/imv_1').click()
    driver.implicitly_wait(5)



driver.quit()



