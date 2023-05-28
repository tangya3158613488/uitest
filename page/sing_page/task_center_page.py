from common.driver.appium_driver import AppiumDriver
from page.ktv_page.my_tab_page import MyTabPage
from page.ktv_page.recommend_tab_page import RecommendTabPage
from page.objects_controller import ObjectsController


class TaskCenterPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        print("任务中心按钮出现了吗？%s" % str(self.appium_driver.element_displayed(self.get_object("task_center_title"))))
        return self.appium_driver.element_displayed(self.get_object("task_center_title"))
