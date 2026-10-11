from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Windows Button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Windows Checkbox")


class MacButton(Button):
    def render(self):
        print("Mac Button")


class MacCheckbox(Checkbox):
    def render(self):
        print("Mac Checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        self.button.render()
        self.checkbox.render()


factory = WindowsFactory()
app = Application(factory)
app.render()

print("------")

factory = MacFactory()
app = Application(factory)
app.render()
