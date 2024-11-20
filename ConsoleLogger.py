import datetime

class ConsoleLogger(ILoggerStrategy):
    def log(self, message: str):
        print(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f} - {message}")