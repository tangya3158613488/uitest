from common.driver.appium_driver import AppiumDriver
from page.login_page.login_page import LoginPage
from page.objects_controller import ObjectsController


class AgreementPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver


    def agree_tab_click(self):
        """
        同意tab点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("agree_tab")))

    def disagree_tab_click(self):
        """
        不同意tab点击
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("disagree_tab")))