"""
相册（我的/Ta的相册）
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class PhotoAlbumPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_photo_album_page(self):
        """
        判断是否在我的相册页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("photo_album_title"))