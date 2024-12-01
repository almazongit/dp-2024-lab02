from abc import ABC, abstractmethod
from datetime import datetime

# Абстрактный класс для стратегии логирования
class LogStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        """Абстрактный метод для записи сообщения."""
        pass

# Стратегия логирования в консоль
class ConsoleLogStrategy(LogStrategy):
    def log(self, message: str):
        """Записывает сообщение в консоль."""
        print(message)

# Стратегия логирования в файл
class FileLogStrategy(LogStrategy):
    def __init__(self, filename: str):
        """Инициализирует стратегию с указанным именем файла."""
        self.filename = filename

    def log(self, message: str):
        """Записывает сообщение в файл."""
        with open(self.filename, "a") as file:
            file.write(message + "\n")

# Стратегия логирования в файл в верхнем регистре
class UpperCaseFileLogStrategy(LogStrategy):
    def __init__(self, filename: str):
        """Инициализирует стратегию с указанным именем файла."""
        self.filename = filename

    def log(self, message: str):
        """Записывает сообщение в файл в верхнем регистре."""
        with open(self.filename, "a") as file:
            file.write(message.upper() + "\n")

# Класс логгера, использующий стратегии логирования
class Logger:
    def __init__(self, strategy: LogStrategy):
        """Инициализирует логгер с заданной стратегией логирования."""
        self.strategy = strategy

    def set_strategy(self, strategy: LogStrategy):
        """Устанавливает новую стратегию логирования."""
        self.strategy = strategy

    def log(self, message: str):
        """Форматирует сообщение с временной меткой и передает его текущей стратегии логирования."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        formatted_message = f"{timestamp} - {message}"
        self.strategy.log(formatted_message)

# Пример использования логгера
if __name__ == "__main__":
    # Логирование в консоль
    console_logger = Logger(ConsoleLogStrategy())
    console_logger.log("Это сообщение для консоли.")

    # Логирование в файл
    file_logger = Logger(FileLogStrategy("log.txt"))
    file_logger.log("Это сообщение для файла.")

    # Логирование в файл в верхнем регистре
    upper_case_file_logger = Logger(UpperCaseFileLogStrategy("upper_log.txt"))
    upper_case_file_logger.log("Это сообщение для файла в верхнем регистре.")