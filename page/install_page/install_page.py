import os
import platform
import subprocess
import time
from common.config.read_config import get_value
from common.utils.logger import Log
from common.utils.build_utils import BuildUtils

log = Log()

class AppUtils:
    # todo:修改下root_path
    def __init__(self,root_path="uitest"):
        self.platform = get_value('platform', 'platform')
        self.appPackage = get_value("Android","appPackage")
        self.udid = BuildUtils.get_udid("Android")
        self.root_path = root_path

    def app_packages_three(self):
        packages = os.popen(f"adb -s {self.udid} shell pm list packages -3")  # adb命令查询第三方安装的包名
        app_packages = packages.read()  # 读取第三方安装的app包名
        # print(app_packages)

        app_pack_str = app_packages.replace('\n', '')  # 读取结果把换行符\n替换为空，删除换行符
        app_pack_list = app_pack_str.split("package:")  # 使用split方法切片，得到包名的一个列表
        # print(app_pack_list)

        app_pack_list.pop(0)  # 使用列表的pop方法删除包名列表中的第一个数据
        return app_pack_list  # 返回包名列表


    def uninstall_app(self):
        if self.platform == '2':
            if self.appPackage in self.app_packages_three():
                with subprocess.Popen(
                        f"adb -s {self.udid}  uninstall {self.appPackage}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        encoding="utf-8") as port_process:
                    out_lines = port_process.stdout.readlines()
                    print("卸载中-",out_lines)
                    return True
            else:
                log.info(f"{self.appPackage} is not in this phone")
                return False


    def get_app_size(self):
        """获取安装包大小：xxMB"""
        curent_path = os.path.abspath(__file__)
        apk_path = os.path.join(curent_path.split(f"{self.root_path}")[0], f"{self.root_path}", "common/config/ktv.apk")
        stats = os.stat(apk_path)
        apk_size = stats.st_size
        return round((apk_size/1024/1024),2)

    def install_app(self):
        '''
        安装apk
        :return:
        '''
        curent_path = os.path.abspath(__file__)
        apk_path = os.path.join(curent_path.split(f"{self.root_path}")[0],f"{self.root_path}","common/config/ktv.apk")

        if self.platform == '2':
            with subprocess.Popen(
                    f"adb -s {self.udid} install  -r -g {apk_path}", shell=True, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8") as port_process:
                out_lines = port_process.stdout.readlines()
                print(out_lines)
                log.info(f"----info----{out_lines}")
                if "Success" in out_lines[-1]:
                    return True
                else:
                    return False



    def clear_app(self):
        """
        清除app数据
        :return:
        """
        with subprocess.Popen(
                f"adb -s {self.udid} shell pm clear  {self.appPackage}", shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8") as port_process:
            out_lines = port_process.stdout.readlines()
            print(out_lines)
        log.info(f"----info----清除app数据：{out_lines}")

    def grant_app(self):
        """授权APP"""

        with subprocess.Popen(
                f"adb -s {self.udid} shell appops set --uid  {self.appPackage} MANAGE_EXTERNAL_STORAGE allow", shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8") as port_process:
            out_lines = port_process.stdout.readlines()
            print(out_lines)
        log.info(f"----info----清除app数据：{out_lines}")

if __name__ == '__main__':
    i = AppUtils()
    # i.app_packages_three()
    # i.uninstall_app()
    print(i.get_app_size())
    i.clear_app()

    # i.install_app()
    # In.clear_app()
    # os.system("adb install  -r  ../../common/config/ktv.apk")







