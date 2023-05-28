from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.sing_page.singer_page.hot_singer_page import HotSingerPage


class SingerPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("singer_page_title"))

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=True)
    def hot_see_more_btn_click(self):
        """
        点击查看全部按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_singer_see_more")))
        return HotSingerPage(self.appium_driver)
