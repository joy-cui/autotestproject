import time
import unittest

from src.testcase.android.page.page_index import PageIndex
from src.testcase.android.page.page_join_meet import PageJoinMeet
from src.testcase.common.util_element import UtilElement
from utils.logger import logger
from utils.test_data_config import TestDataConfig


class TestJoinMeet(unittest.TestCase):
    def TestJoinMeeting(self):
        if not UtilElement.is_element_found(PageIndex().getHomeJoinMeetBtn()):
            logger.info("非首页")
            # 判断是否是加入会议页面
        else:
            logger.info("----启动加入会议用例-----")
            UtilElement.elementClick(PageIndex().getHomeJoinMeetBtn())
            time.sleep(1)
            params = TestDataConfig().get('joinMeetPage')
            confid = params.get("confid")
            nickName = params.get("nickName")
            closeAudio = params.get("closeAudio")
            closeVideo = params.get("closeVideo")
            UtilElement.elementSendKey(PageJoinMeet().getConfIdEdit(), confid)
            UtilElement.elementSendKey(PageJoinMeet().getNickNameEdit(), nickName)
            logger.info("closeAudio %d closeVideo:%d (closeAudio, closeVideo))")
            if closeAudio:
                UtilElement.elementClick(PageJoinMeet().getCloseAudioBtn())
            if closeVideo:
                UtilElement.elementClick(PageJoinMeet().getCloseVideoBtn())
            time.sleep(0.2)
            UtilElement.elementClick(PageJoinMeet().getJoinMeetBtn())

    def TestStartMeeting(self):
        if not UtilElement.is_element_found(PageIndex().getHomeJoinMeetBtn()):
            logger.info("非首页")
        else:
            logger.info("----启动开始会议用例-----")
            # 开始会议
            UtilElement.elementClick(PageIndex().getStartMeetBtn())
            time.sleep(1)
