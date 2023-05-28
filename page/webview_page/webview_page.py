from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class WebViewPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_web_view_page(self):
        """
        是否进入webview页面
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("web_view"))
