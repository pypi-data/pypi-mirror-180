import os
import time
from enum import Enum
from typing import Any, Dict

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from roboform import constants

from .form_logs import FormLogs
from .global_configs import GlobalConfigs
from .utils import Utils


class BotProperty(Enum):
    ID = "id"
    CSS_SELECTOR = "css_selector"
    XPATH = "xpath"
    CLASS_NAME = "class_name"
    WAIT = "wait"
    CONTITION = "condition"
    ACTION = "action"
    TEXT = "text"

class BotActionType(Enum):
    INSERT = "insert"
    CLICK = "click"
    CHECK = "check"

class Bot:
    exec_section = None
    configs_section = None

    def __init__(self, name: str, configs: Dict[str, Any]) -> None:
        tmp_path = os.path.join(GlobalConfigs.get_instance().home_path, ".tmp/")
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        os.environ["TMPDIR"] = tmp_path

        profile_path = os.path.join(tmp_path, "roboform_profile")
        if not os.path.exists(profile_path):
            os.mkdir(profile_path)
        options = webdriver.FirefoxOptions()
        options.add_argument("-profile")
        options.add_argument(profile_path)
        options.headless = True

        firefox_service = FirefoxService(executable_path=GeckoDriverManager(
            path=tmp_path).install(), log_path=os.path.join(tmp_path, "geckodriver.log"))

        self.driver = webdriver.Firefox(service=firefox_service, options=options)
        self.all_configs = configs
        self.logs = FormLogs(name)

    def exec(self) -> bool:
        url = Utils.get_url_configs_from_all_configs(self.all_configs)
        self.driver.get(url)
        self.logs.print_log("*** START BOT FORM ***")

        for config in self.all_configs:
            if config == constants.FORM_CONFIGS_HEADER:
                self.configs_section: Dict[str, Any] = self.all_configs[config]
            else:
                try:
                    self.exec_section = config
                    self.__exec_config(self.all_configs[config])
                except Exception as ex:
                    self.logs.print_error(f"Error in form: {config}, cause: {ex}")
                    return False

        self.logs.print_log("*** END BOT FORM ***")
        self.driver.quit()
        return True

    def __exec_config(self, config: Dict[str, Dict[str, Any]]):
        for items in config.items():
            comp = items[1]

            if BotProperty.CONTITION.value in comp:
                try:
                    cond_str = str(comp[BotProperty.CONTITION.value])
                    for item in cond_str.split(" "):
                        if item in self.configs_section:
                            cond_str = cond_str.replace(item, f"self.configs_section['{item}']")

                    if not eval(cond_str):
                        continue
                except:
                    raise Exception(f"bad condition in element {items[0]}!")

            message_log = f"[{self.exec_section}] | {comp.get(BotProperty.ACTION.value, 'unknow').upper()}"
            if comp.get(BotProperty.TEXT.value) is not None:
                message_log = f"{message_log} '{comp.get(BotProperty.TEXT.value)}' on {items[0]}"
            else:
                message_log = f"{message_log} on {items[0]}"
            self.logs.print_log(message_log)

            self.driver.switch_to.window(self.driver.window_handles[-1])

            if BotProperty.WAIT.value in comp:
                time.sleep(comp[BotProperty.WAIT.value])

            try:
                if BotProperty.ID.value in comp:
                    elem = self.driver.find_element_by_id(comp[BotProperty.ID.value])
                if BotProperty.CSS_SELECTOR.value in comp:
                    elem = self.driver.find_element_by_css_selector(comp[BotProperty.CSS_SELECTOR.value])
                if BotProperty.XPATH.value in comp:
                    elem = self.driver.find_element_by_xpath(comp[BotProperty.XPATH.value])
                if BotProperty.CLASS_NAME.value in comp:
                    elem = self.driver.find_element_by_class_name(comp[BotProperty.CLASS_NAME.value])[1]
            except:
                raise Exception(f"element {items[0]} not found!")

            if comp[BotProperty.ACTION.value] == BotActionType.INSERT.value:
                elem.clear()
                elem.send_keys(comp[BotProperty.TEXT.value])

            if comp[BotProperty.ACTION.value] == BotActionType.CLICK.value:
                elem.click()
