import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.config import read_config

__current_path = os.path.dirname(os.path.realpath(__file__))
emailcfg_path = os.path.join(os.path.dirname(__current_path), "config/emailcfg.ini")

# 读取email配置文件信息
section = "changba"
port = read_config.get_value_with_path(emailcfg_path, section, "port")
ssl_port = read_config.get_value_with_path(emailcfg_path, section, "ssl_port")
smtp_sever = read_config.get_value_with_path(emailcfg_path, section, "smtp_sever")
receiver = read_config.get_value_with_path(emailcfg_path, section, "receiver")


def send(receivers, msg_root, user_email, password):
    global smtp_sever
    try:
        # ssl加密 such as QQ邮箱
        smtp = smtplib.SMTP_SSL(smtp_sever, ssl_port)
        smtp.login(user_email, password)
        smtp.sendmail(user_email, receivers, msg_root.as_string())
    except smtplib.SMTPDataError:
        smtp = smtplib.SMTP_SSL(smtp_sever, ssl_port)
        smtp.login(user_email, password)
        smtp.sendmail(user_email, receivers, msg_root.as_string())
    except smtplib.SMTPException:
        # 非ssl加密
        smtp = smtplib.SMTP()
        smtp.connect(smtp_sever, port)
        smtp.login(user_email, password)
        smtp.sendmail(user_email, receivers, msg_root.as_string())
    finally:
        smtp.quit()


def send_email(email_text, user_email, password, successed=True):
    print("正在发送邮件...")
    if successed:
        subject_text = "UI TEST通过"
    else:
        subject_text = "UI TEST部分case校验失败，测试报告查看zip附件"
    fo = open("result.txt", "w")
    fo.seek(0)
    fo.truncate()
    fo.write(subject_text + "\n")
    fo.write(email_text)
    fo.close()
    # 设置邮件信息
    get_time = time.strftime("%Y-%m-%d %H:%M:%S")
    msg_root = MIMEMultipart()
    msg_root["Subject"] = subject_text + get_time
    msg_root["From"] = user_email
    # 注意MIMEText()["To"]应该为Str类型
    msg_root["To"] = read_config.get_value_with_path(emailcfg_path, section, "receiver")


    # 构造附件
    # att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    # att["Content-Type"] = 'application/octet-stream'
    # att["Content-Disposition"] = 'attachment; filename="allure_report.zip"'
    # msg_root.attach(att)

    text = MIMEText(email_text, "plain", "utf-8")
    msg_root.attach(text)
    # 注意sendmail["To"]应该为list类型, 发送多人时注意！
    receivers = receiver.split(",")
    send(receivers, msg_root, user_email, password)
