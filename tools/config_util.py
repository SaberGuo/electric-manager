import copy
import os

import yaml

from constant import constant


ENV = os.environ.get("ENV", "dev")


def _read_config(env):
    with open(
        os.path.join(constant.BASE_DIR, "config", f"config.{env}.yaml"),
        "r",
        encoding="utf-8",
    ) as stream:
        return yaml.full_load(stream)


if os.path.exists(os.path.join(constant.BASE_DIR, "config", "config.local.yaml")):
    content = _read_config("local")
else:
    content = _read_config(ENV)


class Config:
    _config = content

    @property
    def env(self):
        return ENV

    @property
    def base_dir(self):
        return constant.BASE_DIR

    @property
    def content(self):
        return self._config

    @property
    def interface(self):
        return self._config["interface"]

    @property
    def mongodb(self):
        return self._config["sqlit"]


config = Config()
