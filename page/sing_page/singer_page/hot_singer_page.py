from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.sing_page.singer_page.singer_details_page import SingerDetailsPage


class HotSingerPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("hot_singer_page_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_single_cell(self):
        """
        点击单独的cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("single_singer_cell"))[0])
        return SingerDetailsPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_single_cell_singer_name(self):
        """
        获取单独cell的歌手名txt
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("single_singer_cell")),
                "text")
        else:
            return self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("single_singer_cell")),
                "label")
