from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.public_page.client_utils_page import ClientUtilsPage


class LoginPage(ObjectsController):

    def __init__(self,appium_driver:AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver



    def password_login_click(self):
        """
        点击密码登录
        :return:
        """
        # self.appium_driver.wait_for(3, self.appium_driver.find_element(self.get_object("password_login_tab")))
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("password_login_tab")))


    def input_userid(self,userid):
        self.appium_driver.wait_for(3,self.appium_driver.find_element(self.get_object("changba_id_input")))
        return self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("changba_id_input")),f"{userid}")

    def input_password(self,password):
        self.appium_driver.wait_for(3, self.appium_driver.find_element(self.get_object("password_text_input")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("password_text_input")))
        return self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("password_text_input")),f"{password}")

    def login_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("login_btn")))

    def agree_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("consent_protocol_tab")))
    def login_by_password(self,userid,password):
        self.password_login_click()
        self.input_userid(userid=userid)
        self.input_password(password=password)
        self.agree_btn_click()
        self.login_btn_click()
        return ClientUtilsPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def grant_btn_display(self):
        self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("grant_btn")))
        # return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("grant_btn")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def i_see_btn_display(self):
        self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("i_see_btn")))
        # return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("i_see_btn")))

    def i_see_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_see_btn")))

    def grant_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("grant_btn")))

