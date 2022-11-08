"""
Iterator Design Pattern of Behaviour
Allow go to each elements in a collection without expose your representation
"""

# Modules
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def get_next(self):
        raise NotImplementedError()

    @abstractmethod
    def has_more(self) -> bool:
        raise NotImplementedError()


class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        raise NotImplementedError()


class ConcreteCollection(IterableCollection):
    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)


class ConcreteIterator(Iterator):
    collection: ConcreteCollection = None
    iteration_state: int = 0

    def __init__(self, collection: ConcreteCollection):
        self.collection = collection

    def get_next(self):
        return collections

    def has_more(self) -> bool:
        return bool(collections)

