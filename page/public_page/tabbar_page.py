from common.driver.appium_driver import AppiumDriver
from ..my_page.main_my_page import MainMyPage
from ..objects_controller import ObjectsController
from ..ktv_page.ktv_page import KtvPage
from ..home_page.home_page import HomePage
from ..sing_page.sing_page import SingPage
from ..message_page.message_page import MessagePage


class TabBarPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def ktv_tab_click(self):
        """
        KTV tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("ktv_tab")))
        return KtvPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def wait_ktv_tab_displayed(self):
        """
        等待KTV tab出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("ktv_tab"))

    def sing_tab_click(self):
        """
        唱歌（点歌台） tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sing_tab")))
        return SingPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def wait_singing_tab_displayed(self):
        """
        等待唱歌（点歌台） tab出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("sing_tab"))

    def home_tab_click(self):
        """
        首页 tab 点击
        return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("home_tab")))
        # return HomePage(self.appium_driver)
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def wait_home_tab_displayed(self):
        """
        等待首页 tab出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("home_tab"))

    def message_tab_click(self):
        """
        消息 tab 点击
        return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("message_tab")))
        return MessagePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def wait_message_tab_displayed(self):
        """
        等待消息 tab出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("message_tab"))

    def my_tab_click(self):
        """
        我的 tab 点击
        return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("me_tab")))
        return MainMyPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def wait_my_tab_displayed(self):
        """
        等待我的 tab出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("me_tab"))
