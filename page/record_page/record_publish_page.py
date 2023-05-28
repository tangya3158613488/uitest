from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class RecordPublishPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver,song_name=""):
        super().__init__()
        self.song_name= song_name
        self.appium_driver = appium_driver

    def click_publish_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("publish_btn")))

    def get_song_name(self):
        return self.appium_driver.find_element(self.get_object("song_name")).text

    def is_publish_text_shown(self):
        self.appium_driver.element_displayed(self.get_object("publish_text"))

    def get_publish_text(self):
        return self.appium_driver.find_element(self.get_object("publish_text")).text

    def click_public_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("public_btn")))

    def is_process_view_shown(self):
        return self.appium_driver.element_displayed(self.get_object("upload_process_view"))

    def is_cover_img_shown(self):
        return self.appium_driver.element_displayed(self.get_object("cover_img"))

    def is_change_cover_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("change_cover_btn"))

    def is_tip_shown(self):
        return self.appium_driver.element_displayed(self.get_object("tip"))

    def is_add_tread_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("add_tread_btn"))

    def is_choose_competition_view_shown(self):
        return self.appium_driver.element_displayed(self.get_object("choose_competition_view"))

    def is_who_can_see_view_shown(self):
        return self.appium_driver.element_displayed(self.get_object("who_can_see_view"))

    def is_select_area_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("select_area_btn"))

    def is_able_join_chorus_view_shown(self):
        return self.appium_driver.element_displayed(self.get_object("able_join_chorus_view"))

    def is_save_and_exit_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("save_and_exit_btn"))

    def click_save_and_exit_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("save_and_exit_btn")))

    def get_publish_button_text(self):
        return self.appium_driver.find_element(self.get_object("publish_button")).text
