from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.sing_page.song_details_page import SongDetailsPage

from page.sing_page.task_center_page import TaskCenterPage
from page.sing_page.search_page.search_page import SearchPage
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.sing_page.bind_tel_page import BindTelPage
from page.sing_page.real_time_chrous_page import RealTimeChrousPage
from page.sing_page.grab_sing_page import GrabSingPage
from page.sing_page.only_sing_page import OnlySingPage
from page.sing_page.live_room_sing_icon.audio_live_prepare_page import AudioLivePreparePage
from page.sing_page.live_room_sing_icon.live_real_name_identify_page import LiveRealNameIdentifyPage
from page.sing_page.ordered_page.ordered_page import OrderedPage
from page.sing_page.singer_page.singer_page import SingerPage
from page.sing_page.classify_page.classify_page import ClassfiyPage
from page.sing_page.mall_page import MallPage
from page.sing_page.drifting_bottle_page import DriftingBottlePage
from page.sing_page.meet_by_sounds_page import MeetBySoundsPage
from page.sing_page.wish_wall_page import WishWallPage
from page.sing_page.import_page.import_page import ImportPage
from page.public_page.navigationbar_page import NavigationBarPage


class SingPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def back_btn_click(self):
        """
        点击返回
        :return:
        """
        NavigationBarPage(self.appium_driver).back_btn_click()

    @AppiumDriver.wait_for(timeout_sec=2, need_catch=True)
    def swipe_function_icon(self):
        """
        滑动功能区icon
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.appium_driver.swipe(device_width * 0.3, device_height * 0.35, device_width * 0.1, device_height * 0.35)
        else:
            el = self.appium_driver.find_element(self.get_object("real_time_chrous_icon"))
            y = el.rect["y"] + int(el.rect["height"] / 2)
            self.appium_driver.swipe(device_width * 0.8, y, device_width * 0.2, y,
                                     500)
    def qqq(self):
        return
    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def swipe_order_song_module(self):
        """
        滑动点歌区数据
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.45, device_height * 0.80, device_width * 0.45, device_height * 0.25)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def task_center_click(self):
        """
        任务中心入口点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("task_center")))
        return TaskCenterPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def search_frame_click(self):
        """
        搜索框点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_frame_loc")))
        return SearchPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def hum_song_btn_click(self):
        """
        识别歌曲按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recog_song_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def start_hum_song_btn_click(self):
        """
        点击开始哼唱歌曲按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("start_hum_sing_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def give_up_recog_displayed(self):
        """
        点击放弃识别按钮是否见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("give_up_recog_btn"))

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=True)
    def re_recog_btn_displayed(self):
        """
        点击重新识别按钮是否见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("re_recog_song_btn"))

    def close_recog_hum_song_pop(self):
        """
        关闭识别哼唱歌曲弹窗
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_recog_pop_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def open_live_room_icon_click(self):
        """
        开歌房icon点击 未绑定手机号，进入榜单手机号页面
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("open_live_room_icon")))
        return BindTelPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def binded_tel_open_live_room_icon_click(self):
        """
        开歌房icon点击 绑定手机号 直接进入包房
        case中会先判断是否进入绑定手机号页面，如果是，那么证明没有绑定手机号，case直接通过。如果不是，此时已经进入包房了，所以此处只需要返回包房页面，不需要再次点击开歌房icon
        :return:
        """
        return BaseLiveRoomPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def real_name_live_room_sing_icon_click(self):
        """
        直播唱icon点击 未实名认证，进入主播实名认证页面
        :return:
        """
        self.swipe_function_icon()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("live_sing_icon")))
        return LiveRealNameIdentifyPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def live_room_sing_icon_click(self):
        """
        直播唱icon点击 未实名认证，进入电台直播准备页
        case中会先判断是否进入绑定手机号页面，如果是，那么证明没有认证过，case直接通过。如果不是，此时已经进入直播准备页了，所以此处只需要返回直播准备页页面，不需要再次点击直播唱icon
        :return:
        """
        return AudioLivePreparePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def small_train_cell_click(self):
        """
        小火车cell点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("small_train_cell")))
        return BaseLiveRoomPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def real_time_chrous_icon_click(self):
        """
        实时合唱icon点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("real_time_chrous_icon")))
        return RealTimeChrousPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def grab_sing_icon_click(self):
        """
        劲爆抢唱icon点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("grab_sing_icon")))
        return GrabSingPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def grab_sing_icon_click(self):
        """
        劲爆抢唱icon点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("grab_sing_icon")))
        return GrabSingPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def only_sing_icon_click(self):
        """
        清唱icon点击
        :return:
        """
        self.swipe_function_icon()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("only_sing_icon")))
        return OnlySingPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def drifting_bottle_icon_click(self):
        """
        漂流瓶icon点击
        :return:
        """
        self.swipe_function_icon()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("drifting_bottle_icon")))
        return DriftingBottlePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def meet_by_sounds_icon_click(self):
        """
        以声相遇icon点击
        :return:
        """
        self.swipe_function_icon()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("meet_by_sounds_icon")))
        return MeetBySoundsPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def wish_wall_icon_click(self):
        """
        心愿墙icon点击
        :return:
        """
        self.swipe_function_icon()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wish_wall_icon")))
        return WishWallPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def import_icon_click(self):
        """
        导入icon点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("import_icon")))
        return ImportPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def import_local_video_click(self):
        """
        导入icon点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("import_local_video")))
        return ImportPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def ordered_btn_click(self):
        """
        已点btn点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("ordered_btn")))
        return OrderedPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def singer_btn_click(self):
        """
        歌手btn点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("singer_btn")))
        return SingerPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def classify_btn_click(self):
        """
        分类btn点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("classify_btn")))
        return ClassfiyPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def mall_btn_click(self):
        """
        商城btn点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("mall_btn")))
        return MallPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def song_cell_click(self):
        """
        点歌区歌曲cell点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("songs_cell")))
        return SongDetailsPage(self.appium_driver)

    def get_click_song_cell_song_name(self):
        """
        获取点歌区所点击的歌曲名
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0],
                "text")
        else:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0],
                "label")
        print("点歌台点击的歌曲名为：", song_name)
        return song_name

    def get_click_song_cell_singer_name(self):
        """
        获取点歌区所点击的歌手名
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            singer_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("singer_name"))[0], "text")
        else:
            singer_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("singer_name"))[0], "label")
        return singer_name

    # @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def sing_btn_click(self):
        """
        点歌区歌曲cell演唱点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("sing_btn"))[0])

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def hum_displayed(self):
        """
        点击放弃识别按钮是否见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("give_up_recog_btn"))

    def is_sing_page(self):
        """
        是否在点歌台
        :return:
        """
        print("判断是否在点歌台")
        return self.appium_driver.element_displayed(self.get_object("classify_btn"))

