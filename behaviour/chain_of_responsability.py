"""
Chain of Responsability Behaviour Pattern Design
Pass request along of chain of managers, each manager decide if this managed or not and pass to next manager
"""

# Modules
from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request: dict):
        raise NotImplementedError()


class Basehandler(Handler):
    next: Handler = None
    def set_next(self, handler):
        if(self.next):
            self.next.set_next(handler)
        else:
            self.next = handler

    def handle(self, request: Any) -> Any:
        if(self.next):
            return self.next.handle(request)
        return request


class HandlerPattern(Basehandler):
    @abstractmethod
    def can_handle(self, request: Any) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def _handle(self, request: Any) -> Any:
        raise NotImplementedError()

    def handle(self, request: Any) -> Any:
        if self.can_handle(request):
            request = self._handle(request)
        return super().handle(request)


class Login1(HandlerPattern):
    _handle_name: str = "login_handle"

    def can_handle(self, request: Any) -> bool:
        return True

    def _handle(self, request: Any) -> Any:
        if "steps" not in request:
            request["steps"] = []
        request["steps"].append(self._handle_name)
        return request


class UserRequest(HandlerPattern):
    _handle_name: str = "user_handle"

    def can_handle(self, request: dict) -> bool:
        return True

    def _handle(self, request: dict) -> dict:
        if "steps" not in request:
            request["steps"] = []
        request["steps"].append(self._handle_name)
        return request


class ContentRequest(HandlerPattern):
    _handle_name: str = "content_handle"

    def can_handle(self, request: dict) -> bool:
        return True

    def _handle(self, request: dict) -> dict:
        if "steps" not in request:
            request["steps"] = []
        request["steps"].append(self._handle_name)
        return request


h1 = Login1()
h2 = UserRequest()
h3 = ContentRequest()
h1.set_next(h2)
h1.set_next(h3)

handle_converted = h1.handle({"id": "content"})
print("handle_converted - ", handle_converted)