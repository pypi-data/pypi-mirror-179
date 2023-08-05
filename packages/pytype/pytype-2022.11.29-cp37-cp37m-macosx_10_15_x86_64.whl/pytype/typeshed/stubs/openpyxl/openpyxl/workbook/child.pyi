from typing import Any

INVALID_TITLE_REGEX: Any

def avoid_duplicate_name(names, value): ...

class _WorkbookChild:
    HeaderFooter: Any
    def __init__(self, parent: Any | None = ..., title: Any | None = ...) -> None: ...
    @property
    def parent(self): ...
    @property
    def encoding(self): ...
    @property
    def title(self): ...
    @title.setter
    def title(self, value) -> None: ...
    @property
    def oddHeader(self): ...
    @oddHeader.setter
    def oddHeader(self, value) -> None: ...
    @property
    def oddFooter(self): ...
    @oddFooter.setter
    def oddFooter(self, value) -> None: ...
    @property
    def evenHeader(self): ...
    @evenHeader.setter
    def evenHeader(self, value) -> None: ...
    @property
    def evenFooter(self): ...
    @evenFooter.setter
    def evenFooter(self, value) -> None: ...
    @property
    def firstHeader(self): ...
    @firstHeader.setter
    def firstHeader(self, value) -> None: ...
    @property
    def firstFooter(self): ...
    @firstFooter.setter
    def firstFooter(self, value) -> None: ...
    @property
    def path(self): ...
