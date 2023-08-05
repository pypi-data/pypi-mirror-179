class Options:
    KEY: str
    def __init__(self) -> None: ...
    @property
    def capabilities(self): ...
    def set_capability(self, name, value) -> None: ...
    @property
    def binary_location(self): ...
    @binary_location.setter
    def binary_location(self, value) -> None: ...
    @property
    def arguments(self): ...
    def add_argument(self, argument) -> None: ...
    @property
    def overlay_scrollbars_enabled(self): ...
    @overlay_scrollbars_enabled.setter
    def overlay_scrollbars_enabled(self, value) -> None: ...
    def to_capabilities(self): ...
