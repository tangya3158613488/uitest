from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController


class ClassifyDetailsPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("mandarin_classify_page_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_page_title(self):
        """
        获取页分类title
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("page_title_txt")),
                                                    "text")
        else:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("page_title_txt")),
                                                    "label")
