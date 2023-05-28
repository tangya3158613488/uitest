from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SaveCompletePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def click_re_record(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("re_record_btn")))

    def click_private_publish_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("private_publish_btn")))

    def click_go_local_record_page_check_btn(self):
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("go_local_record_page_check_btn")))

    def click_close_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn")))

    def search_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))

    def is_save_complete_page_title_displayed(self):
        return self.appium_driver.element_displayed(self.get_object("save_complete_page_title"))

    @AppiumDriver.wait_for(timeout_sec=15, need_catch=True)
    def wait_in_save_complete_page(self):
        """
        等待进入保存完成页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("go_local_record_page_check_btn"))
