from collections.abc import Callable
from threading import Thread
from typing import Any, Literal

from .core import Context
from .device import Device

class Monitor:
    def __init__(self, context : Context, monitor_p : Any) -> None: ...

    def __del__(self) -> None: ...

    @classmethod
    def from_netlink(cls, context : Context, source : Literal["udev", "kernel"] = "udev") -> Monitor: ...

    @property
    def started(self) -> bool: ...

    def fileno(self) -> int: ...

    def filter_by(self, subsystem : str | bytes, device_type : str | bytes | None = None) -> None: ...

    def filter_by_tag(self, tag : str | bytes) -> None: ...

    def remove_filter(self) -> None: ...

    def start(self) -> None: ...

    def set_receive_buffer_size(self, size : int) -> None: ...

    def _receive_device(self) -> Device | None: ...

    def poll(self, timeout : float | None = None) -> Device | None: ...

class MonitorObserver(Thread):
    def __init__(self, monitor : Monitor, event_handler : None = None, callback : Callable[[Device], None] | None = None, *args : Any, **kwargs : Any) -> None: ...

    def start(self) -> None: ...

    def run(self) -> None: ...

    def send_stop(self) -> None: ...

    def stop(self) -> None: ...
