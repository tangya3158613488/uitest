from common.driver.appium_driver import AppiumDriver
from page.public_page.navigationbar_page import NavigationBarPage


class FindBroadcastPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def find_broadcast_title_displayed(self):
        """
        寻人广播title可见
        model_room_text: collect_room_text、guard_room_text、history_room_text
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("find_broadcast_title"))


