import unittest
import time

from provar import var
from src.testcase.android.case.test_auto_enter_exit_meeting import TestAutoEnterExitMeeting
from src.testcase.android.case.test_joinmeet import TestJoinMeet
from src.testcase.common.util_driver import init_driver
from utils.HTMLTestRunner import HTMLTestRunner


class RunTestPageIndex:

    def __init__(self):
        pass


if __name__ == '__main__':
    # 初始连接
    init_driver()
    time.sleep(3)

    suite = unittest.TestSuite()
    # 添加执行的测试用例
    suite.addTest(TestAutoEnterExitMeeting('test_pageIndex'))


    now = time.strftime("%Y%m%d-%H%M%S")
    report = var.REPORT_PATH + "\\" + now + "-" + "report.html"
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='手机测试', description='修改html报告')
        runner.run(suite)
