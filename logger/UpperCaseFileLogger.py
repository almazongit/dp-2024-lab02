import datetime
from ILoggerStrategy import ILoggerStrategy

class UpperCaseFileLogger(ILoggerStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def log(self, message: str):
        with open(self.file_path, 'a') as file:
            file.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f} - {message.upper()}\n")