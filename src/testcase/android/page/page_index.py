"""
首页的元素
"""
from provar import var
from src.testcase.common.util_element import UtilElement


class PageIndex:
    def __init__(self):
        # 加入会议
        # self.joinMeetBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
        self.joinMeetBtn = "//android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
        # 开始会议
        self.startMeetBtn = "//android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]"
        # 预约会议
        self.orderMeetBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[3]"
        # 会议记录
        self.meetRecordBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                    ".LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android" \
                                    ".view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                    ".LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android" \
                                    ".widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[1]/android.widget.TextView "
        # 会议日程
        self.meetRecordBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                    ".LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android" \
                                    ".view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                    ".LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android" \
                                    ".widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.TextView "
        # 首页
        self.pageIndexBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ImageView"
        # 通讯录
        self.addressBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ImageView"
        # 我
        self.myBtnBy = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.ImageView"

    def getHomeJoinMeetBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.joinMeetBtn)

    def getStartMeetBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.startMeetBtn)
