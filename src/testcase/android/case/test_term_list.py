import time
import unittest

from provar import var
from src.testcase.android.page.meeting.page_meeting_home import PageMeetingHome
from src.testcase.android.page.meeting.page_term_list import PageTermlist
from src.testcase.common.util_element import UtilElement
from utils.logger import logger
from utils.test_data_config import TestDataConfig


class TestTermList(unittest.TestCase):
    def TestOpenCloseAudio(self):
        logger.info("准备启动开关麦克风测试用例====")
        # 调整参会人界面
        if not UtilElement.is_element_found(PageMeetingHome().getMeetView()):
            logger.info("非会议界面")
        if not UtilElement.is_element_found(PageMeetingHome().getParticipant()):
            logger.info("未显示参会人按键==触发显示按键")
            UtilElement.elementClick(PageMeetingHome().getMeetView())
        UtilElement.elementClick(PageMeetingHome().getParticipant())
        time.sleep(1)
        if not UtilElement.is_element_found(PageTermlist().getTermList()):
            logger.error("非参会人界面")
        else:
            nums = TestDataConfig().get('openCloseAudio').get("nums")
            logger.info("开始麦克风开关操作=====循环次数 : %d" % nums)
            for i in range(0, nums):
                termItems = PageTermlist().getTermListItems()
                if not UtilElement.is_element_found(termItems):
                    logger.error("没有获取到列表item元素====")
                else:
                    termlistLen: int = len(termItems)
                    logger.info("参会人呢个数====%d" % termlistLen)
                    if termlistLen > 0:
                        for item in termItems:
                            UtilElement.elementClick(item)
                            time.sleep(1)
                            logger.info("开关麦克风操作========循环第=%d次" % i)
                            UtilElement.elementClick(PageTermlist().getMuteAudioBtn())
                            time.sleep(0.5)
                    else:
                        logger.info("当前无参会人==循环第=%d次" % i)
