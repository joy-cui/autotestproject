"""
参会人列表页面
"""
from provar import var
from src.testcase.common.util_element import UtilElement


class PageTermlist:
    def __init__(self):
        self.backBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.ImageView"
        #	org.suirui.huijian.video:id/participant_list
        self.temList = "//android.widget.ListView"
        self.termListItem = '//android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout'
        self.muteAudiobtn = "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView"
        self.muteVideoBtn = "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView"
        self.foucsVideoBtn = "//android.widget.ListView/android.widget.LinearLayout[3]"

        # 更多
        self.moreBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button"
        self.allMuteAutoBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]"
        self.allForceMuteBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]"

    def getTermList(self):
        """"参会人列表"""
        return UtilElement.find_elementByXPath(var.driver, self.temList)

    def getTermListItems(self):
        """"参会人列表item"""
        return UtilElement.find_elementsByXPath(var.driver, self.termListItem)

    def getMuteAudioBtn(self):
        """开关麦克风"""
        return UtilElement.find_elementByXPath(var.driver, self.muteAudiobtn)

    def getMuteVideoBtn(self):
        """"开关镜头"""
        return UtilElement.find_elementByXPath(var.driver, self.muteVideoBtn)

    def getFoucsVideoBtn(self):
        """焦点视频"""
        return UtilElement.find_elementByXPath(var.driver, self.foucsVideoBtn)

    def getMoreBtn(self):
        """更多"""
        return UtilElement.find_elementsByXPath(var.driver, self.moreBtn)

    def getAllMuteBtn(self):
        """全体静音"""
        return UtilElement.find_elementByXPath(var.driver, self.allMuteAutoBtn)

    def getForceMuteBtn(self):
        """强制静音"""
        return UtilElement.find_elementByXPath(var.driver, self.allForceMuteBtn)
