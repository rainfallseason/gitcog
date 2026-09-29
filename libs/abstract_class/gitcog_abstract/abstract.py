from abc import ABC, abstractmethod


class GitCogAbstract(ABC):
    @abstractmethod
    @staticmethod
    def generate_config():
        pass

    @abstractmethod
    @staticmethod
    def generate_template():
        pass
    