"""
Abstract Factory Pattern Design
Allow Produce object families related without specific your classes concretes
"""

# Modules
from abc import ABC, abstractmethod
from enum import Enum


class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        raise NotImplementedError()

    @abstractmethod
    def sit_on(self):
        raise NotImplementedError()


class VictorianChair(Chair):
    def has_legs(self):
        return True

    def sit_on(self):
        print("sit_on victorian Chair")


class ModernChair(Chair):
    def has_legs(self):
        return False

    def sit_on(self):
        print("sit_on modern Chair")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        raise NotImplementedError()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()


# Depend of type of Furniture
class TypeFurniture(str, Enum):
    modern = "modern"
    victorian = "victorian"

    def get_factory(self) -> FurnitureFactory:
        match self.name:
            case "modern":
                return ModernFurnitureFactory()
            case "victorian":
                return VictorianFurnitureFactory()
        raise NotImplementedError()


FURNITURE: str = "victorian"
type_furniture: TypeFurniture = TypeFurniture(FURNITURE.lower())
factory: FurnitureFactory = type_furniture.get_factory()
chair = factory.create_chair()
chair.sit_on()
