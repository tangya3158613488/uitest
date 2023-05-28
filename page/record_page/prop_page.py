from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController


class PropPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def is_prop_no_item_showed(self):
        return self.appium_driver.element_displayed(self.get_object("prop_no_item"))

    def click_first_prop(self):
        self.appium_driver.press_element(self.get_object("first_prop"))

    def click_prop_item_and_wait_for_download(self, index):
        prop_list = self.appium_driver.find_elements(self.get_object("prop_items"))
        self.appium_driver.press_element(prop_list[index])
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            status = prop_list[index].get_attribute("value")
            if status == "未下载":
                self.appium_driver.wait_for(10, False)
            else:
                print("道具已下载")

    def swip_prop_list_to_buttom(self):
        self.appium_driver.wait_for(3, False)
        h = self.appium_driver.find_element(self.get_object("prop_broad")).size["height"]
        to_y = self.appium_driver.find_element(self.get_object("prop_broad")).location['y'] + h / 4
        y = self.appium_driver.find_element(self.get_object("prop_broad")).location['y'] + 3 * h / 4
        print("h is {},to_y is {},y is {}".format(h, to_y, y))
        while not self.appium_driver.element_displayed(self.get_object("prop_scare")):
            self.appium_driver.swipe(10, y, 10, to_y, 1000)
        return PropPage(self.appium_driver)

    def close_prop_board(self):
        self.appium_driver.wait_for(3, False)
        device_height = self.appium_driver.device_height()
        device_width = self.appium_driver.device_width()
        self.appium_driver.press_location(device_height / 3, device_width / 2)
