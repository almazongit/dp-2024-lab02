
from ILoggerStrategy import ILoggerStrategy
class Logger:
    def __init__(self, logger_strategy: ILoggerStrategy):
        self.logger_strategy = logger_strategy

    def set_logger_strategy(self, logger_strategy: ILoggerStrategy):
        self.logger_strategy = logger_strategy

    def log(self, message: str):
        self.logger_strategy.log(message)