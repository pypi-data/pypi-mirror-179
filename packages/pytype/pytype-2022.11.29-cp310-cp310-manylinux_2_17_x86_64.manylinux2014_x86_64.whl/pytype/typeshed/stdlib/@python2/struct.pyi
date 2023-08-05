from array import array
from mmap import mmap
from typing import Any, Text

class error(Exception): ...

_FmtType = bytes | Text
_BufferType = array[int] | bytes | bytearray | buffer | memoryview | mmap
_WriteBufferType = array[Any] | bytearray | buffer | memoryview | mmap

def pack(fmt: _FmtType, *v: Any) -> bytes: ...
def pack_into(fmt: _FmtType, buffer: _WriteBufferType, offset: int, *v: Any) -> None: ...
def unpack(__format: _FmtType, __buffer: _BufferType) -> tuple[Any, ...]: ...
def unpack_from(__format: _FmtType, buffer: _BufferType, offset: int = ...) -> tuple[Any, ...]: ...
def calcsize(__format: _FmtType) -> int: ...

class Struct:
    format: bytes
    size: int
    def __init__(self, format: _FmtType) -> None: ...
    def pack(self, *v: Any) -> bytes: ...
    def pack_into(self, buffer: _WriteBufferType, offset: int, *v: Any) -> None: ...
    def unpack(self, __buffer: _BufferType) -> tuple[Any, ...]: ...
    def unpack_from(self, buffer: _BufferType, offset: int = ...) -> tuple[Any, ...]: ...
