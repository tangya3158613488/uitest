from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
import time



class SingChatModePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def user_online_list_click(self):
        """
        "点击在线成员列表
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_users_info_id")))
        return SingChatModePage(self.appium_driver)