import configparser
import os


def get_value(section, key):
    config = configparser.ConfigParser()
    current_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_path, "capabilities.ini")
    config.read(path)
    return config.get(section, key)


def get_value_with_path(path, section, key):
    config = configparser.ConfigParser()
    config.read(path)
    return config.get(section, key)


def get_capability(platform, key):
    return get_value(platform.value, key)
