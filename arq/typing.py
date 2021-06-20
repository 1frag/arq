import sys
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Dict, Optional, Sequence, Set, Type, Union, NewType

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol
else:
    from typing_extensions import Literal, Protocol

try:
    from mypy_extensions import Arg, KwArg, VarArg
except ImportError:
    raise ImportError('mypy_extensions', 'mypy_extensions should be installed')

__all__ = (
    'OptionType',
    'WeekdayOptionType',
    'WEEKDAYS',
    'SecondsTimedelta',
    'WorkerCoroutine',
    'StartupShutdown',
    'WorkerSettingsType',
)


if TYPE_CHECKING:
    from .cron import CronJob  # noqa F401
    from .worker import Function  # noqa F401

OptionType = Union[None, Set[int], int]
WEEKDAYS = 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun'
WeekdayOptionType = Union[OptionType, Literal['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']]
SecondsTimedelta = Union[int, float, timedelta]

WorkerCoroutine = Callable[[Arg(Dict[Any, Any], 'ctx'), VarArg(Any), KwArg(Any)], Coroutine[Any, Any, Any]]
StartupShutdown = Callable[[Arg(Dict[Any, Any], 'ctx')], Coroutine[Any, Any, Any]]


class WorkerSettingsBase(Protocol):
    functions: Sequence[Union[WorkerCoroutine, 'Function']]
    cron_jobs: Optional[Sequence['CronJob']] = None
    on_startup: Optional[StartupShutdown] = None
    on_shutdown: Optional[StartupShutdown] = None
    # and many more...


WorkerSettingsType = Union[Dict[str, Any], Type[WorkerSettingsBase]]
