from common.driver.appium_driver import AppiumDriver

from page.objects_controller import ObjectsController


class MyPlayListPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_my_playlist_page(self):
        return self.appium_driver.element_displayed(self.get_object("title"))

