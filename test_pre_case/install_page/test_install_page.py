import time

from page.install_page.install_page import AppUtils


def test_uninstall_app(app:AppUtils):
    "卸载APP"
    assert app.uninstall_app()


def test_install_app(app:AppUtils):
    "安装APP"
    app.uninstall_app()
    assert app.install_app()
    time.sleep(3)