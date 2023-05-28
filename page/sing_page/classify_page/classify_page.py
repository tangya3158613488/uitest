from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.sing_page.classify_page.classify_details_page import ClassifyDetailsPage


class ClassfiyPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("all_classfiy_page_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def mandarin_classify_btn_click(self):
        """
        国语分类btn点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("mandarin_btn")))
        return ClassifyDetailsPage(self.appium_driver)
