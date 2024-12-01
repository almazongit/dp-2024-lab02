import unittest
import os
from logger import Logger, ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy

class TestLogger(unittest.TestCase):

    def setUp(self):
        """Создание временных файлов для тестов."""
        self.test_file = "test_log.txt"
        self.upper_case_file = "upper_test_log.txt"

    def tearDown(self):
        """Удаление временных файлов после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.upper_case_file):
            os.remove(self.upper_case_file)

    def test_console_logging(self):
        """Тестирование логирования в консоль."""
        console_logger = Logger(ConsoleLogStrategy())
        
        # Используем контекстный менеджер для перехвата вывода в консоль.
        with self.assertLogs(level='INFO') as log:
            console_logger.log("Тестовое сообщение для консоли.")
            self.assertIn("Тестовое сообщение для консоли.", log.output)

    def test_file_logging(self):
        """Тестирование логирования в файл."""
        file_logger = Logger(FileLogStrategy(self.test_file))
        file_logger.log("Тестовое сообщение для файла.")
        
        with open(self.test_file, "r") as f:
            content = f.read()
            self.assertIn("Тестовое сообщение для файла.", content)

    def test_upper_case_file_logging(self):
        """Тестирование логирования в файл в верхнем регистре."""
        upper_case_logger = Logger(UpperCaseFileLogStrategy(self.upper_case_file))
        upper_case_logger.log("Тестовое сообщение для файла в верхнем регистре.")
        
        with open(self.upper_case_file, "r") as f:
            content = f.read()
            self.assertIn("ТЕСТОВОЕ СООБЩЕНИЕ ДЛЯ ФАЙЛА В ВЕРХНЕМ РЕГИСТРЕ.", content)

if __name__ == "__main__":
    unittest.main()