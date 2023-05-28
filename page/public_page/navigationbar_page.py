from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from ..objects_controller import ObjectsController


class NavigationBarPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=False)
    def wait_for_title(self, title):
        """
        等待标题出现
        :param title:
        :return:
        """
        return title == self.title()

    def title(self):
        """
        获取标题
        :return:
        """
        title = self.appium_driver.get_el_text(self.appium_driver.find_element(self.get_object("navigation_bar_title")),
                                               "name")
        print("title is %s " % title)
        return title

    def back_btn_click(self):
        """
        点击导航上返回或安卓虚拟返回键
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            self.appium_driver.press_element(
                self.appium_driver.find_element(self.get_object("back_btn")))
        else:
            self.appium_driver.back()

    def is_dialog_shown(self):
        """
        返回dialog是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("dialog_confirm"))

    def click_dialog_confirm(self):
        """
        点击某个alert的确认按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dialog_confirm")))
