"""
Strategy Behaviour Design Patterns
Allow generate a family of algorithm, place each in separated classes and change your objects
"""

# Modules
from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, a, b):
        raise NotImplementedError()


class RoadStrategy(RouteStrategy):
    def build_route(self, a, b):
        print("road_strategy")


class WalkingStrategy(RouteStrategy):
    def build_route(self, a, b):
        print("walking_strategy")


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, a, b):
        print("public traffic strategy")


class Context:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def strategy(self) -> RouteStrategy:
        return self._strategy

    def do_some_business_logic(self):
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        self._strategy.build_route([1,2,3], ["a", "c", "v"])
        #print(",".join(result))


context = Context(RoadStrategy())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()
print()

print("Client: Strategy is set to reverse sorting.")
context._strategy = WalkingStrategy()
context.do_some_business_logic()