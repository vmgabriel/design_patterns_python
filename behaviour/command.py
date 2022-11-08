"""
Command Design Pattern Behaviour
Become request to separated object
"""

# Modules
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()

class SaveCommand(Command):
    def execute(self):
        print("Save Command")


class OpenCommand(Command):
    def execute(self):
        print("Open Command")


class PrintCommand(Command):
    def execute(self):
        print("Print Command")


class Invoker:
    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        self._on_start.execute()
        self._on_finish.execute()


invoker = Invoker()
invoker.set_on_start(OpenCommand())
invoker.set_on_finish(PrintCommand())
invoker.do_something_important()