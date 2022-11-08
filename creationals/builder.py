"""
Builder Pattern Design
Build objects step by step
"""

# Modules
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Manual:
    content: str = "default content"


@dataclass
class Car:
    part1 = None
    part2 = None
    part3 = None
    part4 = None


@dataclass
class Engine:
    force: float = 1.0


class Builder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def set_seats(self, quantity: int):
        raise NotImplementedError()

    @abstractmethod
    def set_engine(self, engine):
        raise NotImplementedError()

    @abstractmethod
    def set_trip_computer(self):
        raise NotImplementedError()

    @abstractmethod
    def set_gps(self):
        raise NotImplementedError()

    @abstractmethod
    def get_result(self):
        raise NotImplementedError()

class CarBuilder(Builder):
    car: Car = ...
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_seats(self, quantity: int):
        self.car.part1 = quantity

    def set_engine(self, engine):
        self.car.part2 = engine

    def set_trip_computer(self):
        self.car.part3 = "trip_computer"

    def set_gps(self):
        self.car.part4 = "gps"

    def get_result(self):
        return self.car


class Director:
    def make_sport_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine(Engine(1.2))
        builder.set_gps()
        builder.set_trip_computer()


# Now i get director
director: Director = Director()
car_builder: CarBuilder = CarBuilder()
director.make_sport_car(car_builder)
car = car_builder.get_result()
print("vars - ", vars(car))
