import os
import time
import allure
import pytest

from common.driver.appium_driver import AppiumDriver
from common.utils.logger import Log
from common.utils.build_utils import BuildUtils
from page.install_page.install_page import AppUtils
from page.public_page.client_utils_page import ClientUtilsPage

report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
result_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "result")

test_case_result = {}
appium_driver = None


@pytest.fixture(scope="session", autouse=True)
def init_app():
    "初始化APP"
    app = AppUtils()
    app.uninstall_app()
    app.install_app()
    time.sleep(3)

@pytest.fixture(scope="session",name="appium_driver")
def init_appium_driver():
    """
    初始化appium_driver
    运行结束后退出appium_driver，同时结束WDA和appium进程
    :return:
    """
    global appium_driver
    try:
        appium_driver = AppiumDriver()
        yield appium_driver
    except Exception as e:
        print(e.args[0])


@pytest.fixture(scope="session")
def platform():
    """
    当前运行系统
    :return:
    """
    return AppiumDriver.get_platform()


@pytest.fixture(scope="session")
def client_utils_page():
    """
    初始化client_utils_page
    :return:
    """
    if isinstance(appium_driver, AppiumDriver):
        client_utils_page = ClientUtilsPage(appium_driver)
        return client_utils_page


@pytest.fixture(scope="session")
def log():
    """
    初始化log
    :return:
    """
    log = Log()
    return log


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     hook pytest失败
#     :param item:
#     :param call:
#     :return:
#     """
#     outcome = yield
#     rep = outcome.get_result()
#     if not rep.passed:
#         with allure.step("失败截图"):
#             if isinstance(appium_driver, AppiumDriver):
#                 allure.attach(appium_driver.screenshot(rep.head_line.split(".")[1]), rep.when,
#                               allure.attachment_type.PNG)


def pytest_terminal_summary(terminalreporter):
    """
    测试结果分类
    :param terminalreporter:
    :return:
    """
    passed = terminalreporter.stats.get("passed", [])
    failed = terminalreporter.stats.get("failed", [])
    error = terminalreporter.stats.get("error", [])
    skipped = terminalreporter.stats.get("skipped", [])
    deselected = terminalreporter.stats.get("deselected", [])
    run_case_count = terminalreporter._numcollected - len(deselected)
    duration = time.time() - terminalreporter._sessionstarttime

    test_case_result["passed"] = filter_test_case_result(passed)
    test_case_result["failed"] = filter_test_case_result(failed)
    test_case_result["error"] = filter_test_case_result(error)
    test_case_result["skipped"] = filter_test_case_result(skipped)
    test_case_result["run_case_count"] = run_case_count
    test_case_result["duration"] = duration


def filter_test_case_result(case_result):
    """
    整理测试结果
    :param case_result:
    :return:
    """
    temp = []
    final_test_case_result = []
    for result in case_result:
        if result.head_line not in temp:
            temp.append(result.head_line)
            final_test_case_result.append(result)
    return final_test_case_result


# def pytest_sessionfinish(session):
#     """
#     测试结束前调用
#     :param session:
#     :return:
#     """
#     if isinstance(appium_driver, AppiumDriver):
#         try:
#             appium_driver.quit()
#         except AttributeError:
#             raise Exception("init appium driver failed!!!")
#     BuildUtils.close_build_process()
