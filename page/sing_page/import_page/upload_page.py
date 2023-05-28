from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class UploadPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=True)
    def video_uploaded_displayed(self):
        """
        视频上传完成 tips是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("video_generation_complete"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def save_btn_click(self):
        """
        保存按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("save_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def upload_btn_click(self):
        """
        上传按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("upload_btn")))