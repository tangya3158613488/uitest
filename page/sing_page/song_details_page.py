from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.record_page.audio_record_prepare_page import RecordPreparePage
from page.sing_page.classify_page.classify_details_page import ClassifyDetailsPage


class SongDetailsPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def judge_enter_page(self):
        """
        判断是否进入页面内
        :return:
        """
        return (self.appium_driver.element_displayed(self.get_object("today_best_tab"))
                and self.appium_driver.element_displayed(self.get_object("years_best_tab"))
                and self.appium_driver.element_displayed(self.get_object("add_duet_tab")))

    def get_song_name(self):
        """
        获取页面内歌曲名
        :return:
        """
        el = self.appium_driver.find_elements(self.get_object("song_name"))[0]
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            song_name = self.appium_driver.get_attribute(el, "text").strip()
        else:
            song_name = self.appium_driver.get_attribute(el, "label")
        print("歌曲详情页点击的歌曲名为：", song_name)
        return song_name

    def get_singer_name(self):
        """
        获取页面内歌手名
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            singer_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("singer_name"))[0], "text")
        else:
            singer_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("singer_name"))[0], "label")
        print("歌曲详情页点击的歌手名为：", singer_name)
        return singer_name

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_today_best_tab(self):
        """
        点击-今日最佳
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("today_best_tab")))
        return self

    def judge_today_best_tab_selected(self):
        """
        今日最佳tab是否被选中
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("today_best_tab")).is_selected()
        else:
            return self.appium_driver.find_element(self.get_object("today_best_tab")).get_attribute(
                "name") == "tabBtn已选中"

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_years_best_tab(self):
        """
        点击-年度最佳
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("years_best_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def judge_years_best_tab_selected(self):
        """
        年度最佳tab是否被选中
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("years_best_tab")).is_selected()
        else:
            return self.appium_driver.find_element(self.get_object("years_best_tab")).get_attribute(
                "name") == "tabBtn已选中"

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_history_best_tab(self):
        """
        点击-历史最佳
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("history_best_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def judge_history_best_tab_selected(self):
        """
        历史最佳是否被选中
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("history_best_tab")).is_selected()
        else:
            return str(
                self.appium_driver.find_element(self.get_object("history_best_tab")).get_attribute(
                    "name")) == "tabBtn已选中"

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_add_duet_tab(self):
        """
        点击-加入合唱
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_duet_tab")))
        return self

    def judge_add_duet_tab_selected(self):
        """
        加入合唱tab是否被选中
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("add_duet_tab")).is_selected()
        else:
            return self.appium_driver.find_element(self.get_object("add_duet_tab")).get_attribute("name") == "tabBtn已选中"

    def click_singer_name(self):
        """
        点击歌手名
        :return:
        """
        from page.sing_page.singer_page.singer_details_page import SingerDetailsPage
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("singer_name")))
        return SingerDetailsPage(self.appium_driver)

    def click_sing_btn(self):
        """
        点击演唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sing_btn")))
        return RecordPreparePage(self.appium_driver)

    def judge_singer_name_is_clicked(self):
        """
        判断歌手名是否可点击
        有歌手名时 歌手名text为 歌手名+#
        :return:
        """
        singer_name_txt = self.appium_driver.get_el_text(
            self.appium_driver.find_element(self.get_object("singer_name")),'text')
        return "#" in singer_name_txt

    def click_first_classify(self):
        """
        点击页面内第一个分类
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("song_category_icon")))
        return ClassifyDetailsPage(self.appium_driver)

    def get_first_classify(self):
        """
        获取页面第一个分类
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("song_category_icon")),
                                                'text')

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def swipe_page(self):
        """
        滑动页面
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.5, device_height * 0.8, device_width * 0.5, device_height * 0.4)
        return self

    def swipe_after_sing_btn_displayed(self):
        """
        滑动页面后演唱按钮展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("swipe_after_sing_btn"))
