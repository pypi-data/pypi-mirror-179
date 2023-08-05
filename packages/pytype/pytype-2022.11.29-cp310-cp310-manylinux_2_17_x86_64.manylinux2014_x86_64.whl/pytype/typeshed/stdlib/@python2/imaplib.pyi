import subprocess
import time
from builtins import list as List  # alias to avoid name clashes with `IMAP4.list`
from socket import socket as _socket
from ssl import SSLSocket
from typing import IO, Any, Callable, Pattern, Text
from typing_extensions import Literal

# TODO: Commands should use their actual return types, not this type alias.
#       E.g. tuple[Literal["OK"], list[bytes]]
_CommandResults = tuple[str, list[Any]]

_AnyResponseData = list[None] | list[bytes | tuple[bytes, bytes]]

class IMAP4:
    error: type[Exception] = ...
    abort: type[Exception] = ...
    readonly: type[Exception] = ...
    mustquote: Pattern[Text] = ...
    debug: int = ...
    state: str = ...
    literal: Text | None = ...
    tagged_commands: dict[bytes, List[bytes] | None]
    untagged_responses: dict[str, List[bytes | tuple[bytes, bytes]]]
    continuation_response: str = ...
    is_readonly: bool = ...
    tagnum: int = ...
    tagpre: str = ...
    tagre: Pattern[Text] = ...
    welcome: bytes = ...
    capabilities: tuple[str, ...] = ...
    PROTOCOL_VERSION: str = ...
    def __init__(self, host: str = ..., port: int = ...) -> None: ...
    def open(self, host: str = ..., port: int = ...) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    file: IO[Text] | IO[bytes] = ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def recent(self) -> _CommandResults: ...
    def response(self, code: str) -> _CommandResults: ...
    def append(self, mailbox: str, flags: str, date_time: str, message: str) -> str: ...
    def authenticate(self, mechanism: str, authobject: Callable[[bytes], bytes | None]) -> tuple[str, str]: ...
    def capability(self) -> _CommandResults: ...
    def check(self) -> _CommandResults: ...
    def close(self) -> _CommandResults: ...
    def copy(self, message_set: str, new_mailbox: str) -> _CommandResults: ...
    def create(self, mailbox: str) -> _CommandResults: ...
    def delete(self, mailbox: str) -> _CommandResults: ...
    def deleteacl(self, mailbox: str, who: str) -> _CommandResults: ...
    def expunge(self) -> _CommandResults: ...
    def fetch(self, message_set: str, message_parts: str) -> tuple[str, _AnyResponseData]: ...
    def getacl(self, mailbox: str) -> _CommandResults: ...
    def getannotation(self, mailbox: str, entry: str, attribute: str) -> _CommandResults: ...
    def getquota(self, root: str) -> _CommandResults: ...
    def getquotaroot(self, mailbox: str) -> _CommandResults: ...
    def list(self, directory: str = ..., pattern: str = ...) -> tuple[str, _AnyResponseData]: ...
    def login(self, user: str, password: str) -> tuple[Literal["OK"], List[bytes]]: ...
    def login_cram_md5(self, user: str, password: str) -> _CommandResults: ...
    def logout(self) -> tuple[str, _AnyResponseData]: ...
    def lsub(self, directory: str = ..., pattern: str = ...) -> _CommandResults: ...
    def myrights(self, mailbox: str) -> _CommandResults: ...
    def namespace(self) -> _CommandResults: ...
    def noop(self) -> tuple[str, List[bytes]]: ...
    def partial(self, message_num: str, message_part: str, start: str, length: str) -> _CommandResults: ...
    def proxyauth(self, user: str) -> _CommandResults: ...
    def rename(self, oldmailbox: str, newmailbox: str) -> _CommandResults: ...
    def search(self, charset: str | None, *criteria: str) -> _CommandResults: ...
    def select(self, mailbox: str = ..., readonly: bool = ...) -> tuple[str, List[bytes | None]]: ...
    def setacl(self, mailbox: str, who: str, what: str) -> _CommandResults: ...
    def setannotation(self, *args: str) -> _CommandResults: ...
    def setquota(self, root: str, limits: str) -> _CommandResults: ...
    def sort(self, sort_criteria: str, charset: str, *search_criteria: str) -> _CommandResults: ...
    def status(self, mailbox: str, names: str) -> _CommandResults: ...
    def store(self, message_set: str, command: str, flags: str) -> _CommandResults: ...
    def subscribe(self, mailbox: str) -> _CommandResults: ...
    def thread(self, threading_algorithm: str, charset: str, *search_criteria: str) -> _CommandResults: ...
    def uid(self, command: str, *args: str) -> _CommandResults: ...
    def unsubscribe(self, mailbox: str) -> _CommandResults: ...
    def xatom(self, name: str, *args: str) -> _CommandResults: ...
    def print_log(self) -> None: ...

class IMAP4_SSL(IMAP4):
    keyfile: str = ...
    certfile: str = ...
    def __init__(self, host: str = ..., port: int = ..., keyfile: str | None = ..., certfile: str | None = ...) -> None: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    sslobj: SSLSocket = ...
    file: IO[Any] = ...
    def open(self, host: str = ..., port: int | None = ...) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def ssl(self) -> SSLSocket: ...

class IMAP4_stream(IMAP4):
    command: str = ...
    def __init__(self, command: str) -> None: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    file: IO[Any] = ...
    process: subprocess.Popen[bytes] = ...
    writefile: IO[Any] = ...
    readfile: IO[Any] = ...
    def open(self, host: str | None = ..., port: int | None = ...) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...

class _Authenticator:
    mech: Callable[[bytes], bytes] = ...
    def __init__(self, mechinst: Callable[[bytes], bytes]) -> None: ...
    def process(self, data: str) -> str: ...
    def encode(self, inp: bytes) -> str: ...
    def decode(self, inp: str) -> bytes: ...

def Internaldate2tuple(resp: str) -> time.struct_time: ...
def Int2AP(num: int) -> str: ...
def ParseFlags(resp: str) -> tuple[str, ...]: ...
def Time2Internaldate(date_time: float | time.struct_time | str) -> str: ...
