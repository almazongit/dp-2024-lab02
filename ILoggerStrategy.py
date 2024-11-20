from abc import ABC, abstractmethod

class ILoggerStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        pass