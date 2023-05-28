import logging
import time
import os
import inspect
import sys

import importlib

importlib.reload(sys)
current_file_path = os.path.dirname(os.path.realpath(__file__))
father_file_path = current_file_path + os.path.sep + ".."
# log_save_file_path是存放log文件的路径
log_save_file_path = os.path.join(father_file_path, "logs")


# if not os.path.exists(log_save_file_path) : os.mkdir(log_save_file_path)


class Log:
    cur_time = time.strftime("→ %Y-%m-%d %Hh : %Mm : %Ss")

    def __init__(self, class_name=None):
        # 文件的命名 className:{} + %Y-%m-%d %H:%M:%S 格式
        # 调用该脚本的脚本文件的路径
        if class_name:
            called_class_name = class_name
        else:
            called_class_name = str(inspect.stack()[1][1]).split("/")[-1]
        self.log_name = os.path.join(log_save_file_path, '%s.txt' % (called_class_name + self.cur_time))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __print(self, level, message):
        # 创建一个FileHandler，写文件到log_name
        # fh = logging.FileHandler(self.log_name)
        # fh.setLevel(logging.DEBUG)
        # fh.setFormatter(self.formatter)
        # self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "fatal":
            self.logger.fatal(message)
        self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # fh.close()

    def debug(self, message):
        self.__print("debug", message)

    def info(self, message):
        self.__print("info", message)

    def warning(self, message):
        self.__print("warning", message)

    def error(self, message):
        self.__print("error", message)

    def fatal(self, message):
        self.__print("fatal", message)


if __name__ == "__main__":
    log = Log()
    log.info("----info----")
    log.warning("----warning----")
    log.error("----error----")
    log.fatal("----fatal----")
