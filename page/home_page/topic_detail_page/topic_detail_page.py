from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.public_page.navigationbar_page import NavigationBarPage

"""
话题详情页
"""


class TopicDetailPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_topic_detail_page(self):
        """
        是否在的动态详情页，判断依据是否显示发作品按钮
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("public_work"))

    def get_topic_name(self):
        """
        获取话题详情页话题名字
        :return:
        """
        if self.appium_driver.element_displayed(self.get_object("public_work")):
            text = self.appium_driver.find_element(self.get_object("trend_id")).text[1::]
        else:
            text = self.title()
        return text

