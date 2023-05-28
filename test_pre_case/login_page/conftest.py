import os
import time
import allure
import pytest

from common.config.read_config import get_value
from common.driver.appium_driver import AppiumDriver
from common.utils.logger import Log
from common.utils.build_utils import BuildUtils
from page.install_page.install_page import AppUtils
from page.login_page.login_page import LoginPage
from page.public_page.agreement_page import AgreementPage
from page.public_page.client_utils_page import ClientUtilsPage

@pytest.fixture(scope="session", autouse=True)
def init_app():
    "初始化APP"
    app = AppUtils()
    app.uninstall_app()
    app.install_app()
    time.sleep(3)

@pytest.fixture(scope='session',name='login')
def init_login_page():
    "c初始化login——page"
    AgreementPage(AppiumDriver()).agree_tab_click()
    return LoginPage(appium_driver=AppiumDriver())

