import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Chrome()
driver = webdriver.Edge()


# 打开浏览器
def openchrom(ip):
    driver.get("http://%s/webctrl/" % ip)
    driver.maximize_window()
    sleep(0.5)
    print('-------------------------------------------------打开浏览器成功')


##登录会控
def clean_with_send(xpath, text):
    driver.find_element(By.XPATH, xpath).clear()
    driver.find_element(By.XPATH, xpath).send_keys(text)


def login(username, passwd, meetingNum):
    """
    :param username: 会议创建者账号
    :param passwd: 会议创建者密码
    :param meetingNum: 会议号码
    """
    clean_with_send('//*[@id="login"]/div[2]/div/dl/dt[1]/input', '%s' % username)
    clean_with_send('//*[@id="login"]/div[2]/div/dl/dt[2]/input', '%s' % passwd)
    clean_with_send('//*[@id="login"]/div[2]/div/dl/dt[4]/input', '%s' % meetingNum)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/p/a').click()
    print('-------------------------------------------------会控页面登录成功')


##进入参会人页面频繁操作摄像头
def test(num):
    sleep(0.5)
    driver.find_element(By.XPATH, "//a[contains(text(),'参会人')]").click()
    sleep(1)
    get_element_on = driver.find_elements(By.XPATH, "//span[@class='video']")
    get_num_on = len(get_element_on)
    print("get_num_on: ======%d" % get_num_on)
    # 全部打开
    # if get_num_on > 0:
    #     for i in range(0, get_num_on):
    #         driver.find_element(By.XPATH, "(//span[@class='video'])[1]").click()
    #         print('-------------------------------------------------初始化%s个摄像头' % i)
    #         sleep(0.1)
    #     driver.implicitly_wait(3)
    try:
        for a in range(0,num):
            print("准备开始第%d次循环=====" % a)
            get_element_on2 = driver.find_elements(By.XPATH, "//span[@class='video']")
            get_element_off2 = driver.find_elements(By.XPATH, "//span[@class='video videoOff']")
            get_num_on2 = len(get_element_on2)
            get_num_off2 = len(get_element_off2)
            print("get_num_off2: ======%d" % get_num_off2)
            print("get_num_on: ======%d" % get_num_on2)
            if get_num_on2 > 0:
                b = 0
                for on in get_element_on2:
                    try:
                        b = b + 1
                        on.click()
                    except Exception as err:
                        print('-----err----异常 Error: {}'.format(err))
                        continue
                    print('-----------------------------------------------start--循环打开第%s个摄像头' % b)
            if get_num_off2 > 0:
                b = 0
                for off in get_element_off2:
                    try:
                        b = b + 1
                        off.click()
                    except Exception as err:
                        print('-----err----异常 Error: {}'.format(err))
                        continue
                    print('-----------------------------------------------start--循环关闭第%s个摄像头' % b)
            sleep(1)

    except Exception as err:
        print('-----------------------------------------------start--异常 Error: {}'.format(err))


if __name__ == "__main__":
    openchrom('10.10.15.3')
    login('companyadmin', '123456', '1252')
    test(100000)
