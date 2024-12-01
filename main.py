from abc import ABC, abstractmethod
from datetime import datetime

class LogStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

