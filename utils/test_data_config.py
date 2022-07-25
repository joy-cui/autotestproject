import os

from provar import var
from utils.file_reader import YamlReader


class TestDataConfig:
    def __init__(self, config=var.TEST_DATA_CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)
