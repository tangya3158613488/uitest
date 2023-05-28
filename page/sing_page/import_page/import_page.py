from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.sing_page.import_page.rotate_page import RotatePage


class ImportPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("import_page_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def video_cell_click(self):
        """
        具体视频cell点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("video_cell")))
        return RotatePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def audio_cell_click(self):
        """
        具体音频cell点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("audio_cell"))[3])
