import time

import requests

from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.public_page.client_utils_page import ClientUtilsPage

class RegisterPage(ObjectsController):

    def __init__(self,appium_driver:AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.phone = "15901096606"
        self.vrify_code = "150917"

    def register_by_phonenumber(self):
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("userid_tab")),self.phone)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("get_verification_code_tab")))
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("verification_code_tab")),self.vrify_code)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("consent_protocol_tab")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("login_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("man_tab")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("open_tab")))
        time.sleep(3)
        return ClientUtilsPage(self.appium_driver)

        # self.appium_driver
        # return

    def clear_phone_register(self):
        res = requests.get(url=f"http://admin.changba.com/innerscript/safety/blacktest_clearphoneregister.php?confirm=do&phone={self.phone}&saveaccount=1")
        if res.status_code == 200:
            return True
        else:
            return False


if __name__ == '__main__':
    RegisterPage(AppiumDriver()).clear_phone_register()
    RegisterPage(AppiumDriver()).register_by_phonenumber()
