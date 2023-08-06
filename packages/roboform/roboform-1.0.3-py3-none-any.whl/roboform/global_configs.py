import os
import configparser
import subprocess

from roboform import constants


class GlobalConfigs:
    __instance = None
    __config = configparser.ConfigParser()
    __config[constants.GLOBAL_CONFIGS_HEADER] = {"editor": "gedit",
                                                 "debug": "false"}

    home_path = os.path.join(os.path.expanduser("~"), "roboform")

    @staticmethod
    def get_instance():
        if GlobalConfigs.__instance is None:
            GlobalConfigs()

        return GlobalConfigs.__instance

    def __init__(self):
        if GlobalConfigs.__instance is not None:
            raise Exception("This class is a singleton class!")
        else:
            GlobalConfigs.__instance = self

        self.path = os.path.join(GlobalConfigs.home_path, constants.GLOBAL_CONFIGS_FILENAME)

    def check_file_global_configs(self):
        if not os.path.exists(self.home_path):
            os.mkdir(self.home_path)

        self.__write_file_global_configs()

    def __write_file_global_configs(self):
        try:
            self.__config.read(self.path)
        except (configparser.MissingSectionHeaderError, configparser.ParsingError):
            pass

        with open(self.path, "w", encoding="utf-8") as file:
            self.__config.write(file)

    def edit_global_configs(self) -> bool:
        if os.path.exists(self.path):
            subprocess.Popen([self.get_default_editor(), self.path])
            return True
        else:
            return False

    def get_default_editor(self) -> str:
        return self.__config[constants.GLOBAL_CONFIGS_HEADER].get("editor")

    def is_debug_mode(self) -> bool:
        return self.__config[constants.GLOBAL_CONFIGS_HEADER].getboolean("debug")
