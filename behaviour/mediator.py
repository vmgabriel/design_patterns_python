"""
Mediator Behaviour Pattern Design
Allow reduce chaotic references in objects
"""

# Modules
from abc import ABC, abstractmethod


class Mediator(ABC):
    def notify(self, sender: object, event: str):
        raise NotImplementedError()


class Component:
    dialog: Mediator

    def click(self):
        print("click component")

    def keypress(self):
        print("key_press component")


class Button(Component):
    pass


class TextBox(Component):
    def click(self):
        super().click()
        self.dialog.notify(self, "C")


class Checkbox(Component):
    def check(self):
        pass


class AuthenticationDialog(Mediator):
    def __init__(self, component1: Button, component2: TextBox, component3: Checkbox):
        self._component1 = component1
        self._component1.dialog = self
        self._component2 = component2
        self._component2.dialog = self
        self._component3 = component3
        self._component3.dialog = self

    def notify(self, sender: object, event: str):
        if event == "A":
            print("react in A trigger")
            self._component1.click()
        if event == "B":
            print("react in B trigger")
            self._component2.click()
        if event == "C":
            print("reat in C trigger")
            self._component3.click()


btn = Button()
txt = TextBox()
cb = Checkbox()
mediator = AuthenticationDialog(btn, txt, cb)

print("Client triggers operation A.")
btn.click()

print("\n", end="")

print("Client triggers operation D.")
txt.click()

print("\n", end="")

print("Client triggers operation D.")
cb.click()