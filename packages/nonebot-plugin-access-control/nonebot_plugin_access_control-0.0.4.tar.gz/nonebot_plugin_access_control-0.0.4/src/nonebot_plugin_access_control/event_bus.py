from asyncio import gather
from collections import defaultdict
from enum import Enum
from inspect import isawaitable
from typing import Dict, List, Callable, Awaitable, Any, Tuple, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    pass


class EventType(str, Enum):
    service_set_permission = "service_set_permission"
    """
    当某个服务设置权限成功时触发
    """

    service_remove_permission = "service_remove_permission"
    """
    当某个服务删除权限成功时触发
    """

    service_change_permission = "service_change_permission"
    """
    当某个服务权限变更时触发（包括该服务及其所有祖先服务设置、删除权限导致的权限变更）
    """


T_Kwargs = Dict[str, Any]
T_Filter = Callable[[T_Kwargs], bool]
T_Listener = Callable[[...], Awaitable[None]]

_listeners: Dict[EventType, List[Tuple[T_Filter, T_Listener]]] = defaultdict(list)


async def fire_event(event_type: EventType, kwargs: T_Kwargs):
    coros = []

    for filter_func, func in _listeners[event_type]:
        if filter_func(kwargs):
            coro = func(**kwargs)
            if isawaitable(coro):
                coros.append(coro)

    await gather(*coros)


def on_event(event_type: EventType, filter_func: T_Filter, func: Optional[T_Listener] = None):
    def decorator(func):
        _listeners[event_type].append((filter_func, func))
        return func

    if func is None:
        return decorator
    else:
        return decorator(func)
