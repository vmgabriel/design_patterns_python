"""
Observer Behaviour Design Pattern
Define mechanism to subscribe for notify several objects over any event
"""

# Modules
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        raise NotImplementedError()


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        raise NotImplementedError()

    @abstractmethod
    def detach(self, observer: Observer):
        raise NotImplementedError()

    @abstractmethod
    def notify(self):
        raise NotImplementedError()


class ConcreteSubject(Subject):
    _state: int = None
    _observers: list[Observer] = []

    def attach(self, observer: Observer):
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        print("Subject ----")
        self._state = randrange(0, 10)
        print("that is changed - ")
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("Concrete 1: reacted to state")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()