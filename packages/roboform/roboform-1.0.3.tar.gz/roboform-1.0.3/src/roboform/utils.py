from typing import Any, Dict

from roboform import constants
from roboform import form_configs


class Utils:

    @staticmethod
    def get_url_configs_from_all_configs(configs: Dict[str, Any]) -> str:
        return configs[constants.FORM_CONFIGS_HEADER][form_configs.ConfigsProperty.URL.value]
