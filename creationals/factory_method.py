"""
Factory Method Pattern Design
Allow create a object based in a interface, while allow the sub-classes modify the creation
"""

# Libraries
from abc import ABC, abstractmethod
from enum import Enum


# This is the Transport Segment
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        raise NotImplementedError()


class Truck(Transport):
    def deliver(self):
        return "I am a truck and i'm transporting"


class Ship(Transport):
    def deliver(self) -> str:
        return "I'm a Ship and i'm navigating"


class Logistics(ABC):
    @abstractmethod
    def plan_delivery(self):
        raise NotImplementedError()

    @abstractmethod
    def create_transport(self) -> Transport:
        raise NotADirectoryError()


class RoadLogistics(Logistics):
    def plan_delivery(self):
        transport: Transport = self.create_transport()
        print(transport.deliver())
        print("planning for Road Delivery")

    def create_transport(self):
        print("Creating Transport")
        return Truck()


class SeaLogistics(Logistics):
    def plan_delivery(self):
        transport: Transport = self.create_transport()
        print(transport.deliver())
        print("planning for Ship Delivery")

    def create_transport(self) -> Transport:
        print("Creating for Ship Transport")
        return Ship()


# Client Class Implementation

class TypeLogistical(str, Enum):
    road = "road"
    sea = "sea"

    def get_logistical(self) -> Logistics:
        match self.name:
            case "road":
                return RoadLogistics()
            case "sea":
                return SeaLogistics()
        raise NotImplementedError()


LOGISTICAL: str = "sea"
type_logistical: TypeLogistical = TypeLogistical(LOGISTICAL.lower())

logistical: Logistics = type_logistical.get_logistical()
logistical.plan_delivery()
