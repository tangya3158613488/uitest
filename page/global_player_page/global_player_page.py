import time

from common.driver.appium_driver import AppiumDriver

from page.objects_controller import ObjectsController


class GlobalPlayerPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_gloabl_play_page(self):
        return self.appium_driver.element_displayed(self.get_object("xiaochang_fm_tab"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def switch_to_my_tab(self):
        """
        切换到我的tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_tab")))
        from page.global_player_page.global_player_my_page import GlobalPlayerMyPage
        return GlobalPlayerMyPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def switch_to_listening_tab(self):
        """
        切换到正在收听tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("listening_tab")))
        from page.global_player_page.global_player_listening_page import GlobalPlayerListeningPage
        return GlobalPlayerListeningPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def switch_to_xiaochang_fm_tab(self):
        """
        切换到小唱FMtab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("xiaochang_fm_tab")))
        from page.global_player_page.global_player_xiaochang_fm_page import GlobalPlayerXiaoChangFMPage
        return GlobalPlayerXiaoChangFMPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_prev_btn(self):
        """
        点击上一首
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("prev_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_next_btn(self):
        """
        点击下一首
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("next_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_play_btn(self):
        """
        点击播放按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_collect_btn(self):
        """
        点击收藏
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("collect_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def collected(self):
        """
        是否收藏
        :return:
        """
        return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("collect_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def player_slider_displayed(self):
        """
        是否播放进度条可以点击,ios不能点时元素不可见
        :return:
        """
        return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("player_slider")))

    def player_slider_can_play(self):
        """
        是否能播放
        :return:
        """
        result = self.slider_label()
        return result[0] and result[1]

    def paused(self):
        """
        是否是暂停中
        :return:
        """
        cur = self.curTime()
        print(cur)
        time.sleep(2)
        print(self.curTime())
        return cur == self.curTime()

    def slider_label(self):
        # 当前是0分45秒，总时长5分14秒
        player_slider = self.appium_driver.find_element(self.get_object("player_slider"))
        txts = player_slider.get_attribute("label").split("，")
        print(txts)
        txts[0] = txts[0][3::]
        labels = [0, 0]
        labels[0] = int(txts[0].split("分")[0]) * 60 + int(txts[0].split("分")[1].split("秒")[0])
        txts[1] = txts[1][3::]
        labels[1] = int(txts[1].split("分")[0]) * 60 + int(txts[1].split("分")[1].split("秒")[0])
        return labels

    def curTime(self):
        i = self.slider_label()[0]
        return i

    def pause_utils(self):
        if not self.paused():
            self.click_play_btn()
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def collected(self):
        collect_btn = self.appium_driver.find_element(self.get_object("collect_btn"))
        label = collect_btn.get_attribute("label")
        return label == "取消收藏"

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def xiaochang_fm_tab_selected(self):
        selected_tab = self.appium_driver.find_element(self.get_object("selected_tab"))
        label = selected_tab.get_attribute("label")
        return label == "小唱FM"

    def get_play_model(self):
        play_model = self.appium_driver.find_element(self.get_object("play_model"))
        label = play_model.get_attribute("label")
        print(label)
        return label.split("-")[-1]

    def click_play_model(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_model")))
        return self
