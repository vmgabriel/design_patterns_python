"""
State Behaviour Design Pattern
Modify your behaviour when your intern state has change
"""

# Modules
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class State(ABC):
    context: Context = None
    @abstractmethod
    def handle1(self):
        raise NotImplementedError()

    @abstractmethod
    def handle2(self):
        raise NotADirectoryError()


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


context = Context(ConcreteStateA())
context.request1()
context.request2()