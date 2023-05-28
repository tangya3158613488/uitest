from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

"""
话题广场
"""


class TopicSquarePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.title = "话题广场"

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def topic_square_page_displayed(self):
        """
        话题广场页面是否显示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("page_id"))

    def click_me(self):
        """
        点击我的
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("me")))
        return self

    def click_popular_topics(self):
        """
        点击热门
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("popular_topics")))
        return self

    def click_topic_cell(self, index=0):
        """
        点击右侧话题cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("topic_cell"))[index])
        return self
