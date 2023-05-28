from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class GrabSingPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def page_title_displayed(self):
        """
        页面标题是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("grab_sing_title"))

    def stop_match_btn(self):
        """
        停止匹配按钮可见
        :return:
        :rtype:
        """
        return self.appium_driver.element_displayed(self.get_object("stop_match_btn"))

    def click_stop_match_btn(self):
        """
        点击停止匹配按钮
        :return:
        :rtype:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("stop_match_btn")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def ranking_icon_displayed(self):
        """
        排行icon是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("ranking_icon"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def new_user_guide_displayed(self):
        """
        抢唱新手引导是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("new_user_guide"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_new_user_guide(self):
        """
        点击抢唱新手引导
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("new_user_guide")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_back_image(self):
        """
        点击返回按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_image")))
