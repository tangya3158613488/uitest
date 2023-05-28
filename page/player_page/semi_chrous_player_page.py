from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SemiChrousPlayerPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def friends_chrous_btn_displayed(self):
        """
        好友合唱title 是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("friends_chrous_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def history_best_chrous_btn_displayed(self):
        """
        历史最佳合唱title 是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("history_best_chrous_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def today_best_chrous_btn_displayed(self):
        """
        今日最佳合唱title 是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("today_best_chrous_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def join_chrous_btn_displayed(self):
        """
        加入合唱btn 是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("join_chrous_btn"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def forwarding_work_btn_displayed(self):
        """
        转发btn 是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("forwarding_work_btn"))
