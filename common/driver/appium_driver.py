import threading
import time
import os
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.config import read_config
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.command import Command
from enum import Enum
from common.driver.platform_selector import PlatformSelector
from common.utils.build_utils import BuildUtils


def choose_platform():
    """
    选择平台
    :return:
    """
    if not AppiumDriver.get_connect_time():
        AppiumDriver.set_global_var("connect_time", 0)
    while AppiumDriver.get_connect_time() < 3:
        if AppiumDriver.get_server_status():
            break
        # sys_in = input("请输入想要测试的平台序号（1：iOS、2：Android）:")
        sys_in = "2"
        if sys_in == "1":
            AppiumDriver.set_global_var("platform", PlatformSelector.IOS)
            AppiumDriver.set_global_var("is_start", 1)
            break
        elif sys_in == "2":
            AppiumDriver.set_global_var("platform", PlatformSelector.ANDROID)
            AppiumDriver.set_global_var("is_start", 1)
            break
        else:
            print("输入错误，请重试")
            AppiumDriver.set_global_var("connect_time", AppiumDriver.get_connect_time() + 1)
    else:
        raise Exception("输入错误3次，任务终止")


class AppiumDriver:
    global_var = dict()  # 全局变量
    __DEFAULT_TIME = 5  # 默认智能等待时间

    def __init__(self):
        self.driver.implicitly_wait(self.__DEFAULT_TIME)
        self.__action = TouchAction(self.driver)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls.driver = AppiumDriver.init_driver()
            AppiumDriver._instance = super().__new__(cls)
        return AppiumDriver._instance

    @staticmethod
    def get_desired_caps(platform):
        """
        获取设备信息
        :param platform:
        :return:
        """
        common_desired_caps = {
            'platformName': read_config.get_capability(platform, 'platformName'),
            'platformVersion': read_config.get_capability(platform, 'platformVersion'),
            'automationName': read_config.get_capability(platform, 'automationName'),
            'deviceName': read_config.get_capability(platform, 'deviceName'),
            'udid': BuildUtils.get_udid(platform),
            'noReset': True
        }
        special_desired_caps = {
            'bundleId': read_config.get_capability(platform, 'bundleId'),
            'autoAcceptAlerts': True,
        } if platform == PlatformSelector.IOS else {
            'appPackage': read_config.get_capability(platform, 'appPackage'),
            'appActivity': read_config.get_capability(platform, 'appActivity'),
            'waitForIdleTimeout': int(read_config.get_capability(platform, 'waitForIdleTimeout'))
        }
        return {**common_desired_caps, **special_desired_caps}

    @staticmethod
    def init_driver():
        """
        初始化driver
        :return:
        """
        choose_platform()
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            print("now start connecting WDA...")
            wda_thread = threading.Thread(target=BuildUtils.wda_build)
            wda_thread.setDaemon(True)
            wda_thread.start()
        print("now start connecting Appium...")
        appium_thread = threading.Thread(target=BuildUtils.appium_connect)
        appium_thread.setDaemon(True)
        appium_thread.start()
        for i in range(BuildUtils.CONNECT_TIME_OUT):
            if AppiumDriver.get_platform() == PlatformSelector.IOS:
                if AppiumDriver.get_wda_status() and AppiumDriver.get_appium_status():
                    return AppiumDriver.remote_appium_driver(AppiumDriver.get_platform())
            elif AppiumDriver.get_appium_status():
                return AppiumDriver.remote_appium_driver(AppiumDriver.get_platform())
            time.sleep(1)
        if not AppiumDriver.get_wda_status():
            # wda连接失败有可能是WebDriverAgent.xcodeproj路径问题，若路径没问题可以插拔下数据线
            raise Exception("please check wda connect")
        elif not AppiumDriver.get_appium_status():
            raise Exception("please check appium connect")
        return AppiumDriver.remote_appium_driver(AppiumDriver.get_platform())

    @staticmethod
    def remote_appium_driver(platform):
        """
        连接appium_driver
        :param platform:
        :return:
        """
        print("desired_caps is %s" % AppiumDriver.get_desired_caps(platform))
        return webdriver.Remote(read_config.get_capability(platform, 'host'), AppiumDriver.get_desired_caps(platform))

    def quit(self):
        """
        关闭连接
        :return:
        """
        self.driver.quit()

    def screenshot(self, filename):
        """
        截图
        :param filename:
        :return:
        """
        current_file_path = os.path.dirname((os.path.dirname(os.path.dirname(__file__))))
        log_save_file_path = os.path.join(current_file_path, "screenshot")
        get_time = time.strftime("%Y-%m-%d_%H:%M:%S")
        file_path = os.path.join(log_save_file_path, filename + "_" + get_time + ".png")
        if not os.path.exists(log_save_file_path):
            os.mkdir(log_save_file_path)
        self.driver.save_screenshot(file_path)
        with open(file_path, 'rb') as f:
            png_file = f.read()
        return png_file

    def back(self):
        """
        安卓物理返回键
        :return:
        """
        self.driver.press_keycode(4)

    def accept_alert(self):
        """
        系统弹窗：同意
        :return:
        """
        self.driver.execute(Command.ACCEPT_ALERT)

    def dismiss_alert(self):
        """
        系统弹窗：取消
        :return:
        """
        self.driver.execute(Command.DISMISS_ALERT)

    def get_page_source(self):
        """
        获取当前页面的page_source
        :return:
        """
        return self.driver.page_source

    def find_element(self, el_tuple, father_el=None) -> WebElement:
        """
        el_tuple 包含 by: 定位方式，value: 元素字符串，index: 位置（可不传）
        :param father_el: 父元素默认为空，需要在父元素中找子元素时使用
        :param el_tuple:
        :return:
        """
        if len(el_tuple) == 2:
            by, value = el_tuple
            index = 0
        else:
            by, value, index = el_tuple
        try:
            driver = father_el if father_el else self.driver
            el = None
            el = driver.find_element(by, value) if index == 0 else driver.find_elements(by=by, value=value)[
                index]
            print(el_tuple)
        except IndexError as i:
            print("IndexError {}".format(i))
        except NoSuchElementException as no_element:
            print("NoSuchElementException {}".format(no_element))
            raise NoSuchElementException("%s is not found!!!" % value)
        except Exception as e:
            print("find_element {}".format(e))
        return el

    @staticmethod
    def get_attribute(el, name) -> str:
        """
        获取元素属性
        :param el:
        :param name:
        :return:
        """
        if isinstance(el, WebElement):
            txt = el.get_attribute(name)
            print("the %s is %s" % (name, txt))
            return txt

    def element_displayed(self, el_tuple, index=0, father_el=None) -> bool:
        """
        判断元素是否可见，el_tuple 包含 by: 定位方式，value: 元素字符串，index: 位置（可不传）
        :param index:
        :param father_el: 父元素默认为空，需要在父元素中判断子元素是否存在时使用
        :param el_tuple:
        :return:
        """
        try:
            el = self.find_element(el_tuple, father_el) if index == 0 else self.find_elements(el_tuple, father_el)[
                index]
            return el.is_displayed()
        except IndexError as i:
            print("IndexError {}".format(i))
            return False
        except NoSuchElementException as nse:
            print("NoSuchElementException {}".format(nse))
            return False
        except AttributeError as a:
            print("AttributeError {}".format(a))
            return False
    def find_elements(self, el_tuple, father_el=None) -> list:
        """
        获取同一元素id的多个元素，el_tuple 包含 by: 定位方式，value: 元素字符串
        :param father_el: 父元素默认为空，需要在父元素中找子元素时使用
        :param el_tuple:
        :return:
        """
        by, value = el_tuple
        driver = father_el if father_el else self.driver
        return driver.find_elements(by=by, value=value)

    @staticmethod
    def enter_text(el, txt):
        """
        对指定元素输入文案
        :param el:
        :param txt:
        :return:
        """
        if isinstance(el, WebElement):
            el.send_keys(txt)

    @staticmethod
    def clear(el):
        """
        清空
        :param el:
        :return:
        """
        if isinstance(el, WebElement):
            el.clear()

    @staticmethod
    def press_element(el):
        """
        点击元素
        :param el:
        :return:
        """
        print("点击 {}".format(el))
        el.click()

    def press_element_by_location(self, el):
        """
        通过获取指定元素的坐标进行点击
        :param el:
        :return:
        """
        if isinstance(el, WebElement):
            el_x = el.location['x']
            el_y = el.location['y']
            print(" el_x is %s , el_y  is %s " % (el_x, el_y))
            self.press_location(el_x, el_y)
        else:
            raise Exception('%s is not WebElement' % type(el))

    def press_location(self, x, y):
        """
        通过坐标点击
        :param x:
        :param y:
        :return:
        """
        self.__action.tap(x=x, y=y).perform()

    def long_press_element(self, el, duration=1000) -> TouchAction:
        """
        长按
        :param el:
        :param duration: ms
        :return:
        """
        return self.__action.long_press(el, duration=duration).release().perform()

    def swipe(self, start_x, start_y, end_x, end_y, duration=0):
        """
        通过坐标滑动屏幕
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param duration: ms
        :return:
        """
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)

    def device_width(self) -> int:
        """
        获取设备宽度
        :return:
        """
        return self.driver.get_window_size().get("width")

    def device_height(self) -> int:
        """
        获取设备高度
        :return:
        """
        return self.driver.get_window_size().get("height")

    @staticmethod
    def el_location(el) -> dict:
        """
        获取元素位置
        :param el:
        :return:
        """
        return el.location

    def swipe_el(self, el, swipe_direction, duration):
        """
        通过指定元素进行滑动
        :param el:
        :param swipe_direction: LEFT、RIGHT、UP、DOWN
        :param duration: ms
        :return:
        """
        if isinstance(el, WebElement):
            print(el.size)
            el_height = el.size['height'] - 10
            el_width = el.size['width'] - 10
            el_x = el.location['x']
            el_y = el.location['y']
            el_x_center = (el_x + el_width) / 2
            el_y_center = (el_y + el_height) / 2

            if isinstance(swipe_direction, SwipeDirection):
                if swipe_direction == SwipeDirection.LEFT:
                    return self.swipe(start_x=el_x + el_width, start_y=el_y_center, end_x=el_x, end_y=el_y_center,
                                      duration=duration)
                elif swipe_direction == SwipeDirection.RIGHT:
                    return self.swipe(start_x=el_x, start_y=el_y_center, end_x=el_x + el_width, end_y=el_y_center,
                                      duration=duration)
                elif swipe_direction == SwipeDirection.UP:
                    return self.swipe(start_x=el_x_center, start_y=el_y + el_height, end_x=el_x_center, end_y=el_y,
                                      duration=duration)
                elif swipe_direction == SwipeDirection.DOWN:
                    return self.swipe(start_x=el_x_center, start_y=el_y, end_x=el_x_center, end_y=el_y + el_height,
                                      duration=duration)
            return Exception('check swipe_direction instance')

    @staticmethod
    def set_value(el, value):
        """
        给元素传值(例如：搜索、美颜、音量调节等)
        :param el:
        :param value:
        :return:
        """
        if isinstance(el, WebElement):
            el.set_value(value)

    def get_el_text(self, el, attribute_name=None):
        """
        获取元素文案
        :param el:
        :param attribute_name:
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.get_attribute(el, attribute_name)
        return el.text

    @staticmethod
    def get_platform():
        """
        获取当前设备平台
        :return:
        """
        return AppiumDriver.global_var["platform"]

    @staticmethod
    def get_appium_status():
        """
        获取appium启动状态
        :return:
        """
        return AppiumDriver.global_var.get("appium")

    @staticmethod
    def get_wda_status():
        """
        获取wda启动状态
        :return:
        """
        return AppiumDriver.global_var.get("wda")

    @staticmethod
    def get_server_status():
        """
        获取服务启动状态
        :return:
        """
        return AppiumDriver.global_var.get("is_start")

    @staticmethod
    def get_connect_time():
        """
        获取启动前重试的次数
        :return:
        """
        return AppiumDriver.global_var.get("connect_time")

    @staticmethod
    def set_global_var(key, value):
        """
        配置全局变量
        :param key:
        :param value:
        :return:
        """
        AppiumDriver.global_var[key] = value

    def get_page_source(self):
        """
        页面所有元素
        :return:
        """
        return self.driver.page_source

    def get_android_toast(self):
        """
        获取安卓toast提示
        :return:
        """
        toast_el_tuple = ("xpath", "//*[@class='android.widget.Toast']")
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located(toast_el_tuple))
            return self.driver.find_element_by_xpath(toast_el_tuple[1]).text
        except TimeoutException:
            return None

    @staticmethod
    def wait_for(timeout_sec, need_catch):
        """
        智能等待装饰器
        :param timeout_sec:
        :param need_catch:
        :return:
        """

        def outer(func):
            def inner(*args, **kwargs):
                end_time = time.time() + timeout_sec
                while True:
                    try:
                        condition = func(*args, **kwargs)
                        if condition:
                            print("wait_for_true")
                            return condition
                        else:
                            print("wait_for_false condition {} fuc {}".format(condition, func))
                    except NoSuchElementException as e:
                        print("wait_for {}".format(e))
                        pass
                    except StaleElementReferenceException as e:
                        print("StaleElementReferenceException {}".format(e))
                        pass
                    time.sleep(0.5)
                    if time.time() > end_time:
                        break
                if need_catch:
                    return False
                else:
                    raise TimeoutException("TimeoutException! after wait %s s" % timeout_sec)

            return inner

        return outer

    def swipe_up(self,second):
        """
        上滑
        :param second:滑动的时间ms
        :return:
        """
        device_height = self.device_height()
        end_height = device_height * 0.3
        start_height = device_height * 0.7
        width = self.device_width() * 0.5
        return self.swipe(width, start_height, width, end_height, second)


class SwipeDirection(Enum):
    LEFT = "left"
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
