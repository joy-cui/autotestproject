import unittest
import time

from provar import var
from src.testcase.android.case.test_joinmeet import TestJoinMeet
from src.testcase.android.case.test_term_list import TestTermList
from src.testcase.common.util_driver import init_driver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.test_data_config import TestDataConfig


class RunTestPageIndex:

    def __init__(self):
        pass


if __name__ == '__main__':
    init_driver()
    time.sleep(3)
    suite = unittest.TestSuite()
    c = TestDataConfig().get('homePage')
    isJoinMeeting = c.get("isJoinMeeting")
    if isJoinMeeting:
        suite.addTest(TestJoinMeet('TestJoinMeeting'))
    else:
        suite.addTest(TestJoinMeet('TestStartMeeting'))
    time.sleep(5)
    suite.addTest(TestTermList('TestOpenCloseAudio'))

    now = time.strftime("%Y%m%d-%H%M%S")
    report = var.REPORT_PATH + "\\" + now + "-" + "report.html"
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='手机测试', description='修改html报告')
        runner.run(suite)
