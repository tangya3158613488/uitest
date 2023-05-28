#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import zipfile
import pytest
import json
import time
import requests
from common.utils.db_manager import DatabaseManager
from common.utils.send_email import send_email

report_path = os.path.join(os.path.dirname(__file__), "allure_report")
result_path = os.path.join(os.path.dirname(__file__), "allure_result")
zip_file_path = os.path.join(report_path, "allure_report.zip")


def create_zip_file(input_path, file_list):
    """
    对目录进行深度优先遍历
    :param input_path:
    :param file_list:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            file_list.append(input_path + '/' + file)
            create_zip_file(input_path + '/' + file, file_list)
        else:
            file_list.append(input_path + '/' + file)
    with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zp:
        for file in file_list:
            zp.write("/".join(file.split("/")), file.replace(report_path, ""))


def generate_allure_report(result_path):
    """
    生成测试报告
    :param result_path:
    :return:
    """
    print("正在生成测试报告...")
    with subprocess.Popen(
            "allure generate {} -o {} --clean".format(result_path, report_path),
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            encoding="utf-8") as generate_process:
        for out in generate_process.stdout:
            print(out)
        if generate_process.poll() is not None:
            print(generate_process.communicate()[1])


def get_test_case_result_text():
    """
    整合测试结果
    :param test_case_result:
    :return:
    """
    from test_case import conftest
    passed = conftest.test_case_result.get("passed", [])
    failed = conftest.test_case_result.get("failed", [])
    error = conftest.test_case_result.get("error", [])
    skipped = conftest.test_case_result.get("skipped", [])
    run_case_count = conftest.test_case_result.get("run_case_count", 0)
    duration = conftest.test_case_result.get("duration", 0)
    pass_num = len(passed)
    failed_num = len(failed)
    error_num = len(error)
    skipped_num = len(skipped)
    result_text = "run case count: %d\n" % run_case_count
    if failed:
        result_text += "===========================failed: %d===========================\n" % len(failed)
        for failed_case in failed:
            result_text += "%s          %s          FAILED\n" % (failed_case.head_line, failed_case.when)
    if error:
        result_text += "===========================error: %d===========================\n" % len(error)
        for error_case in error:
            result_text += "%s          %s          ERROR\n" % (error_case.head_line, error_case.when)
    if skipped:
        result_text += "===========================skipped: %d===========================\n" % len(skipped)
        for skipped_case in skipped:
            result_text += "%s          %s          SKIPPED\n" % (skipped_case.head_line, skipped_case.when)
    if passed:
        result_text += "===========================passed: %d===========================\n" % len(passed)
        for passed_case in passed:
            result_text += "%s          %s          PASSED\n" % (passed_case.head_line, passed_case.when)
    result_text += "total times: %.2f seconds" % duration
    is_all_success = False if failed or error or skipped else True
    print(result_text)
    return run_case_count, result_text, pass_num, failed_num, error_num, skipped_num


def senTextmessage(run_case_count, pass_num, failed_num, error_num, test_case_result, name):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/d8da9f6c-3e32-41fa-8934-14352dc947a7"
    report = "http://182.150.24.36:7778/job/uitest/ws/allure_report/index.html"
    content = "UI自动化执行完成 <at id=all></at>\n点击查看报告：[执行报告]({})\n\
    共执行case：{}条\n通过case：{}条\n失败case：{}条\n错误case：{}条\n详情：\n{}\n<font color='red'> 注意查看！ ".format(
        report, run_case_count, pass_num, failed_num, error_num, test_case_result)
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    card = json.dumps({
        "elements": [
            {
                "tag": "markdown",
                "content": content
            }
        ],
        "header": {
            "template": "wathet",
            "title": {
                "content": "UI自动化执行报告（{}）".format(name),
                "tag": "plain_text"
            }
        }
    })
    body = json.dumps({"msg_type": "interactive", "card": card})

    res = requests.post(url=url, data=body, headers=headers)
    return res


if __name__ == "__main__":
    # case_dir = ["test_case/my_page/test_main_my_page.py"]
    md_case_name = {
        "test_case/my_page": "个人主页",
        "test_case/message_page": "消息页",
        "test_case/player_page": "播放详情页",
        "test_case/sing_page": "点歌台"
    }
    # case_dir = []
    name = ""
    # case_dir.append(sys.argv[1])
    for i in range(1,len(sys.argv)):
        if i == len(sys.argv)-1:
            name = name + md_case_name[sys.argv[i]]
        else:
            name = name + md_case_name[sys.argv[i]] + "、"
    # print(case_dir, "===")
    del sys.argv[0]
    pytest.main(["--alluredir={}".format(result_path), "--clean-alluredir", "-s"] + sys.argv)  # 执行test_case
    run_case_count, test_case_result, pass_num, failed_num, error_num, skipped_num = get_test_case_result_text()
    print(test_case_result)
    generate_allure_report(result_path)  # 生成report, 需要使用命令 allure open allure_report路径
    senTextmessage(run_case_count, pass_num, failed_num, error_num, test_case_result, name)
    # create_zip_file(report_path, [])  # 压缩
    # send_email(test_case_result, user_email, password, is_all_success)
    # db = DatabaseManager()
    # create_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # sql = "insert into mars_ui_test (author, success_count, error_count," \
    #       " failure_count, skipped_count, case_count, create_at) values " \
    #       "('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(author, len(passed), len(error), len(failed),
    #                                                           len(skipped),
    #                                                           run_case_count,
    #                                                           create_at)
    # db.insert(sql)
