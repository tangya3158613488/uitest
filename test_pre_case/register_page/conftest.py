import pytest
from common.driver.appium_driver import AppiumDriver
from page.public_page.agreement_page import AgreementPage
from page.register_page.register_page import RegisterPage


@pytest.fixture(scope="session", autouse=True)
def register_page(appium_driver:AppiumDriver):
    "初始化APP"
    register = RegisterPage(appium_driver)
    yield register

@pytest.fixture(scope='session',name='login', autouse=True)
def init_login_page():
    "c初始化login——page"
    AgreementPage(AppiumDriver()).agree_tab_click()
