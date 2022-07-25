""""
加入会议界面参数
"""
from provar import var
from src.testcase.common.util_element import UtilElement


class PageJoinMeet:
    def __init__(self):
        # 会议输入框
        self.confIdEdit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget' \
                                 '.FrameLayout' \
                                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout' \
                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout' \
                                 '/android' \
                                 '.widget.RelativeLayout[' \
                                 '1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText '
        self.nickNameEdit = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                   ".RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android" \
                                   ".widget" \
                                   ".LinearLayout/android.widget.RelativeLayout[" \
                                   "2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText "
        # 加入会议按钮
        self.joinMeetingBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button"
        # 入会时断开音频
        self.closeAudioBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Switch"
        # 入会时候关闭视频
        self.closeVideoBtn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.Switch"
        # 返回
        self.joinBackBtn= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
                                  ".RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android" \
                                  ".widget" \
                                  ".RelativeLayout/android.widget.LinearLayout[2]/android.widget.ImageView "

    def getConfIdEdit(self):
        return UtilElement.find_elementByXPath(var.driver, self.confIdEdit)

    def getNickNameEdit(self):
        return UtilElement.find_elementByXPath(var.driver, self.nickNameEdit)

    def getJoinMeetBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.joinMeetingBtn)

    def getCloseAudioBtn(self):
        return UtilElement.find_elementByXPath(var.driver, self.closeAudioBtn)

    def getCloseVideoBtn(self): # 入会是否关闭视频
        return UtilElement.find_elementByXPath(var.driver, self.closeVideoBtn)

    def getJoinBackBtn(self):  # 返回
        return UtilElement.find_elementByXPath(var.driver, self.joinBackBtn)
