from abc import ABC, abstractmethod
from datetime import datetime

class LogStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogStrategy(LogStrategy):
    def log(self, message: str):
        print(message)
class FileLogStrategy(LogStrategy):
    def __init__(self, filename: str):
        self.filename = filename

    def log(self, message: str):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

class UpperCaseFileLogStrategy(LogStrategy):
    def __init__(self, filename: str):
        self.filename = filename

    def log(self, message: str):
        with open(self.filename, 'a') as file:
            file.write(message.upper() + '\n')