import time

import pytest

from page.install_page.install_page import AppUtils


@pytest.fixture(scope="session",name="app", autouse=True)
def init_app():
    "初始化APP"
    app = AppUtils()
    yield app