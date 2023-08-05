from typing import Any

from . import interaction as interaction
from .input_device import InputDevice as InputDevice
from .interaction import Interaction as Interaction, Pause as Pause

class KeyInput(InputDevice):
    name: Any
    type: Any
    def __init__(self, name) -> None: ...
    def encode(self): ...
    def create_key_down(self, key) -> None: ...
    def create_key_up(self, key) -> None: ...
    def create_pause(self, pause_duration: int = ...) -> None: ...

class TypingInteraction(Interaction):
    type: Any
    key: Any
    def __init__(self, source, type_, key) -> None: ...
    def encode(self): ...
