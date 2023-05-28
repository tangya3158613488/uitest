from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.me_page import PersonPage
from page.player_page import PlayerCommentTabPage


class PlayerCommentTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def player_comment_tab_text(self):
        """
        当前在评论tab
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("player_comment_tab")).text






