import time
import unittest

from src.testcase.android.case.test_joinmeet import TestJoinMeet
from src.testcase.android.page.page_join_meet import PageJoinMeet
from src.testcase.android.page.meeting.page_meeting_home import PageMeetingHome
from src.testcase.common.util_element import UtilElement
from src.testcase.android.page.page_index import PageIndex
from utils.logger import logger
from utils.test_data_config import TestDataConfig

"""
自动入退会
"""


class TestAutoEnterExitMeeting(unittest.TestCase):

    def test_pageIndex(self):
        c = TestDataConfig().get('homePage')
        isJoinMeeting = c.get("isJoinMeeting")
        if not UtilElement.is_element_found(PageIndex().getHomeJoinMeetBtn()):
            logger.info("非首页")
            # 判断是否是加入会议页面
        else:
            number = TestDataConfig().get('enterExitMeet').get("number")
            for i in range(0, number):
                if isJoinMeeting:
                    # 开始加入会议
                    TestJoinMeet().TestJoinMeeting()
                else:
                    # 开始会议
                    TestJoinMeet().TestStartMeeting()
                # 等待几秒后 退会
                wait_time = TestDataConfig().get('enterExitMeet').get("waitTime")
                time.sleep(wait_time)
                # 退出会议
                UtilElement.elementClick(PageMeetingHome().getLeaveHeadBtn())
                time.sleep(1)
                UtilElement.elementClick(PageMeetingHome().getLeaveBtn())
                time.sleep(2)
                if isJoinMeeting:
                    # 加入会议退出到首页
                    UtilElement.elementClick(PageJoinMeet().getJoinBackBtn())
