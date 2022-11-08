"""
Prototype Pattern Design
Clone a Object in other Instance
"""

# Modules
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def clone(self):
        raise NotImplementedError()


@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def clone(self):
        return Rectangle(
            width=self.width,
            height=self.height
        )


@dataclass
class Circle(Shape):
    radious: int

    def clone(self) -> Shape:
        return Circle(
            radious=self.radious
        )


# you can use magical method in python
circle = Circle(3)

new_circle = circle.clone()
print("circle - ", id(circle))
same_circle = circle

print("same_circle - ", id(same_circle))
print("new_circle - ", id(new_circle))