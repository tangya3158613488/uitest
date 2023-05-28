from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class PublicChatPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def clear_charm_btn_displayed(self):
        """
        "清空全部魅力值按钮是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("clear_charm_display"))

    def user_online_list_click(self):
        """
        "点击在线成员列表
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_users_info_id")))
        return SingChatModePage(self.appium_driver)

    def user_online_list_displayed(self):
        """
        "在线成员列表是否可见
        :return:
        """

        return self.appium_driver.element_displayed(self.get_object("room_users_info_title_display"))