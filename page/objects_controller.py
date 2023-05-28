import importlib
import inspect
import re

from common.driver.appium_driver import AppiumDriver


class ObjectsController:
    __ORIGIN_PACKAGE = "page"
    __appium_driver = None

    def __init__(self):
        self.module = inspect.currentframe()
        self.module_list = []
        ObjectsController.__appium_driver = AppiumDriver()

    def get_module_list(self) -> list:
        """
        获取module_list，包括子类及父类
        :return:
        """
        for _ in range(50):
            module_dict = dict()
            if self.module is None:
                break
            self.module = self.module.f_back
            search_module_str = re.search("(.+?_page).py", str(self.module).split("/")[-1])
            if search_module_str:
                module_str = search_module_str.group(1)
                if module_str and not str(module_str).startswith("test_"):
                    module_path = "/".join(re.search(".+?'(.+?_page).py", str(self.module)).group(1).split("/")[:-1])
                    module_dict[module_str] = module_path
                    if module_dict not in self.module_list:
                        self.module_list.append(module_dict)
            else:
                return self.module_list
        return self.module_list

    def get_object_class_list(self) -> list:
        """
        获取page_object中对应的类(Android or IOS)
        :return:
        """
        module_page_object_list = []  # 存储page中类的实例
        module_objects_class_list = []  # 存储objects中的类
        module_list = self.get_module_list()
        for module in module_list:
            for module_str, module_path in module.items():
                self.append_module_page_object_list(module_page_object_list, module_str, module_path)
                self.append_module_objects_class_list(module_objects_class_list, module_str, module_path)
        object_class_list = self.sort_module_objects_class_list(module_page_object_list, module_objects_class_list)
        return object_class_list

    def get_object(self, name: str) -> tuple:
        """
        获取元素信息元祖
        :param name:
        :return:
        """
        object_class_list = self.get_object_class_list()
        for object_class in object_class_list:
            try:
                el_tuple = getattr(object_class, name)
                print(el_tuple)
                return el_tuple
            except Exception as e:
                print("get_object {}".format(e))
                continue
        raise Exception("没有找到%s，先确定page和对应的objects文件都已创建" % name)

    def append_module_page_object_list(self, module_page_object_list, module_str, module_path):
        """
        # 存储page中类的实例
        :param module_page_object_list:
        :param module_str:
        :param module_path:
        :return:
        """
        inner_package = module_path.split("/%s" % self.__ORIGIN_PACKAGE)[1]
        module_page_spec = importlib.util.find_spec(".%s" % module_str,
                                                    package=self.__ORIGIN_PACKAGE + inner_package.replace("/",
                                                                                                          "."))
        if module_page_spec:
            module_page_obj = importlib.import_module(module_page_spec.name)
            module_page_class = inspect.getmembers(module_page_obj, inspect.isclass)
            for name, clazz in module_page_class:
                if name.endswith("Page"):
                    module_format = str(module_page_obj).split("/")[-1].replace(".py'>", "").replace("_",
                                                                                                     "").lower()
                    name_format = name.lower()
                    if module_format == name_format and clazz not in module_page_object_list:
                        obj = getattr(module_page_obj, name)
                        module_page_object_list.append(obj(self.__appium_driver))

    def append_module_objects_class_list(self, module_objects_class_list, module_str, module_path):
        """
         存储objects中的类
        :param module_objects_class_list:
        :param module_str:
        :param module_path:
        :return:
        """
        inner_package = module_path.split("/%s" % self.__ORIGIN_PACKAGE)[1]
        module_object = "%s_objects" % module_str
        module_spec = importlib.util.find_spec(".%s" % module_object,
                                               package=self.__ORIGIN_PACKAGE + inner_package.replace("/", "."))
        if module_spec:
            module_obj = importlib.import_module(module_spec.name)
            module_class = getattr(module_obj,
                                   AppiumDriver.get_platform().value[
                                       0].upper() + AppiumDriver.get_platform().value[1:])
            module_objects_class_list.append(module_class)

    @staticmethod
    def sort_module_objects_class_list(module_page_object_list, module_objects_class_list):
        """
        获取排序后的objects类
        :param module_page_object_list:
        :param module_objects_class_list:
        :return:
        """
        normal_list = []
        extend_list = []
        if len(module_page_object_list) < 2:
            return module_objects_class_list
        first_extend_flag = False
        for i in range(len(module_page_object_list)):
            # print(isinstance(module_page_object_list[i + 1], type(module_page_object_list[i])))
            try:
                if isinstance(module_page_object_list[i + 1], type(module_page_object_list[i])):
                    if i == 0:
                        first_extend_flag = True
                    if module_objects_class_list[i] not in extend_list:
                        extend_list.append(module_objects_class_list[i])
                    if module_objects_class_list[i + 1] not in extend_list:
                        extend_list.append(module_objects_class_list[i + 1])
                else:
                    if module_objects_class_list[i] not in normal_list:
                        normal_list.append(module_objects_class_list[i])
                    if module_objects_class_list[i + 1] not in normal_list:
                        normal_list.append(module_objects_class_list[i + 1])
            except IndexError:
                raise Exception("objects文件命名错误或未找到: module_page_object_list: %s, module_objects_class_list: %s" % (
                    module_page_object_list, module_objects_class_list))
            if i == len(module_page_object_list) - 2:
                break
        extend_list.reverse()
        temp_clazz_list = extend_list + normal_list if first_extend_flag else normal_list + extend_list
        clazz_list = []
        for clazz in temp_clazz_list:
            if clazz not in clazz_list:
                clazz_list.append(clazz)
        return clazz_list
