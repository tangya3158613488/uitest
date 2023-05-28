import os
import signal
import subprocess
import time

from common.config import read_config
from common.config.read_config import get_value
from common.driver.platform_selector import PlatformSelector


class BuildUtils:
    appium_process = None
    wda_process = None
    CONNECT_TIME_OUT = 90

    @staticmethod
    def wda_build():
        """
        运行wda
        :return:
        """
        from common.driver.appium_driver import AppiumDriver
        wda_path = BuildUtils.get_wda_path()
        BuildUtils.kill_wda_process()
        wda_paths = [wda_path] if isinstance(wda_path, str) else wda_path
        for path in wda_paths:
            print("wda path is %s" % path)
            with subprocess.Popen(
                    "xcodebuild -project %s -scheme WebDriverAgentRunner -destination id=%s test" % (
                            path, BuildUtils.get_udid(AppiumDriver.get_platform())),
                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    encoding="utf-8") as BuildUtils.wda_process:
                for out in BuildUtils.wda_process.stdout:
                    # print(out)
                    if "Using singleton test manager" in out:
                        AppiumDriver.set_global_var("wda", "running")
                if BuildUtils.wda_process.poll() is not None:
                    print(BuildUtils.wda_process.communicate()[1])
                    continue

    @staticmethod
    def appium_connect():
        """
        与appium建立连接
        :return:
        """
        from common.driver.appium_driver import AppiumDriver
        platform = AppiumDriver.get_platform()
        if platform == PlatformSelector.IOS:
            start = int(time.time())
            while True:
                if not AppiumDriver.get_wda_status():
                    end = int(time.time())
                    if end - start >= BuildUtils.CONNECT_TIME_OUT:
                        break
                else:
                    break
        if AppiumDriver.get_wda_status() or platform == PlatformSelector.ANDROID:
            BuildUtils.kill_appium_process(platform)
            with subprocess.Popen(
                    "node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js --session-override",
                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    encoding="utf-8") as BuildUtils.appium_process:
                for out in BuildUtils.appium_process.stdout:
                    # print(out)
                    if "Appium REST http interface listener started on 0.0.0.0:4723" in out:
                        AppiumDriver.set_global_var("appium", "running")
                if BuildUtils.appium_process.poll() is not None:
                    print(BuildUtils.appium_process.communicate()[1])

    @staticmethod
    def get_wda_path():
        """
        获取本地wda路径
        :return:
        """
        from common.driver.appium_driver import AppiumDriver
        with subprocess.Popen(
                "find %s -name WebDriverAgent.xcodeproj && find %s -name WebDriverAgent.xcodeproj" % (
                        "/Applications/Appium.app/Contents/Resources/app/node_modules/appium",
                        "/usr/local/lib/node_modules/appium"),
                shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8") as wda_path_process:
            out_lines = wda_path_process.stdout.readlines()
            if not out_lines:
                final_wda_path = input("未找到默认路径下的WDA路径，请手动输入WDA路径：")
                return final_wda_path
            return [line.strip() for line in out_lines]

    @staticmethod
    def kill_appium_process(platform):
        """
        杀掉appium进程
        :param platform:
        :return:
        """
        with subprocess.Popen(
                "lsof -i:%s" % read_config.get_capability(platform, "host").split(":")[-1].split("/")[0],
                shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8") as port_process:
            out_lines = port_process.stdout.readlines()
            if out_lines:
                appium_pid = out_lines[-1].split()[1]
                print("exist appium process: %s, kill process" % appium_pid)
                os.kill(int(appium_pid), signal.SIGKILL)

    @staticmethod
    def kill_wda_process():
        """
        杀掉wda进程
        :return:
        """
        with subprocess.Popen(
                "ps -ef | grep xcodebuild", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                encoding="utf-8") as port_process:
            out_lines = port_process.stdout.readlines()
            if len(out_lines) > 2:
                for line in out_lines:
                    if "WebDriverAgentRunner" in line:
                        wda_pid = line.split()[1]
                        print("exist WDA process: %s, kill process" % wda_pid)
                        os.kill(int(wda_pid), signal.SIGKILL)

    @staticmethod
    def get_udid(platform):
        """
        获取手机设备id
        :param platform:
        :return:
        """
        cmd = "idevice_id -l" if platform == PlatformSelector.IOS else "adb devices"
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              encoding="utf-8") as udid_process:
            if platform == PlatformSelector.IOS:
                udid = udid_process.stdout.readline().strip()
            else:
                out_line = udid_process.stdout.readlines()[1:-1]
                if len(out_line) == 0:
                    raise Exception("device not found!!!")
                if len(out_line) > 1:
                    # raise Exception("more than one devices!!!")
                    udid = get_value('Android', 'udid')
                status = str(out_line[0]).split("	")[1].strip()
                if status != "device":
                    raise Exception("devices not ready, please check!!! now device status is %s" % status)
                if len(out_line) == 1:
                    udid = str(out_line[0]).split("	")[0].strip()
            # print(udid)
            return udid

    @staticmethod
    def close_build_process():
        from common.driver.appium_driver import AppiumDriver
        BuildUtils.appium_process.terminate()
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            BuildUtils.wda_process.terminate()
