from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class GlobalPlayerXiaoChangFMPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def click_play_all_btn(self):
        """
        点击播放全部
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_all_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def click_replace_all_btn(self):
        """
        点击换一批
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("replace_all_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def click_work_by_index(self, index=0):
        """
        点击作品
        :return:
        """
        work_cell_list = self.appium_driver.find_elements(self.get_object("work_cell_list"))
        self.appium_driver.press_element(work_cell_list[index])
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def work_playing_by_index(self, index=0):
        """
        作品是否正在播放
        :return:
        """
        work_cell_list = self.appium_driver.find_elements(self.get_object("work_cell_list"))
        label = work_cell_list[index].get_attribute("label")
        print(label)
        return label.startswith("正在播放")

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def work_name_by_index(self, index=0):
        """
        获取作品名
        :return:
        """
        work_cell_list = self.appium_driver.find_elements(self.get_object("work_cell_list"))
        label = work_cell_list[index].get_attribute("label")
        return label
