from logger.ConsoleLogger import ConsoleLogger
from logger.FileLogger import FileLogger
from logger.UpperCaseFileLogger import UpperCaseFileLogger
from logger.Logger import Logger

if __name__ == "__main__":
    # Логирование в консоль
    console_logger = Logger(ConsoleLogger())
    console_logger.log("Это сообщение для консоли.")

    # Логирование в файл
    file_logger = Logger(FileLogger("log.txt"))
    file_logger.log("Это сообщение для файла.")

    # Логирование в файл в верхнем регистре
    upper_case_file_logger = Logger(UpperCaseFileLogger("upper_log.txt"))
    upper_case_file_logger.log("Это сообщение для файла в КАПСЕ.")
    
    print("Логи записаны.")