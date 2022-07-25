""""
会议主界面
"""
from provar import var
from src.testcase.common.util_element import UtilElement


class PageMeetingHome:
    def __init__(self):
        # 更多
        self.moreBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.Button[5]"
        # 离开会议
        self.leaveHeadBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[3]"
        # 离开会议(弹框)
        self.leaveBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                             ".FrameLayout" \
                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout" \
                             "/android" \
                             ".widget.TextView[3] "
        # 参会人
        self.paritipant = "//android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button[4]"

        self.meetView ='//android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View'

    # 离开会议
    def getLeaveHeadBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.leaveHeadBtn)

    # 离开会议(弹框)
    def getLeaveBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.leaveBtn)

    def getParticipant(self):
        """参会人按钮"""
        return UtilElement.find_elementByXPath(var.driver, self.paritipant)

    def getMeetView(self):
        return UtilElement.find_elementByXPath(var.driver, self.meetView)