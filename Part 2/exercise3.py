"""
Финальная задача №3
https://stepik.org/lesson/2022462/step/3?unit=2050885

Легенда:

Вы создаете гибкую систему логирования, которая может отправлять сообщения в разные "обработчики"
(в консоль, в файл и т.д.). Вам нужно спроектировать иерархию классов для этой системы.

Техническое задание:
Ваша задача — реализовать пять классов: Handler, ConsoleHandler, FileHandler, TimeMixin и Logger.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Handler(ABC):
    @abstractmethod
    def emit(self, message: str):
        pass

class ConsoleHandler(Handler):
    def emit(self, message):
        print(message)

class FileHandler(Handler):
    def emit(self, message):
        return f"Запись в файл: {message}"

class TimeMixin:
    def format_with_timestamp(self, message: str):
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{message}]"

class Logger(TimeMixin):
    def __init__(self, handlers: list):
        self._handlers = handlers

    def log(self, message: str):
        tsmp = self.format_with_timestamp(message)
        for handler in self._handlers:
            handler.emit(tsmp)

    def __call__(self, message: str):
        self.log(message)

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))