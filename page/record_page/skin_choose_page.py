from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SkinChoosePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver, song_name="", singer=""):
        super().__init__()
        self.appium_driver = appium_driver
        self.song_name = song_name
        self.singer = singer

    def is_title_showed(self):
        return self.appium_driver.element_displayed(self.get_object("title"))