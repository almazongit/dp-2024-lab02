import unittest
from logger.ConsoleLogger import ConsoleLogger
from logger.FileLogger import FileLogger
from logger.UpperCaseFileLogger import UpperCaseFileLogger
from logger.Logger import Logger

class TestLogger(unittest.TestCase):
    def test_console_logging(self):
        logger = ConsoleLogger()
        # Здесь можно добавить проверку вывода в консоль, например, с использованием mock

    def test_file_logging(self):
        logger = FileLogger("test_log.txt")
        logger.log("Тестовое сообщение")
        with open("test_log.txt", "r") as f:
            content = f.read()
            self.assertIn("Тестовое сообщение", content)

    def test_uppercase_file_logging(self):
        logger = UpperCaseFileLogger("test_upper_log.txt")
        logger.log("Тестовое сообщение")
        with open("test_upper_log.txt", "r") as f:
            content = f.read()
            self.assertIn("ТЕСТОВОЕ СООБЩЕНИЕ", content)

if __name__ == "__main__":
    unittest.main()