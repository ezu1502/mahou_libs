import time
from functools import wraps
import logging
from typing import Callable, ParamSpec, TypeVar

from .colors import painted_string

from.bocca import BoccaFiglia

log = BoccaFiglia("mahou_libs.time_functions", "#FDFF77")

P = ParamSpec("P")
R = TypeVar("R")


def log_delta_time(function: Callable[P, R]) -> Callable[P, R]:
    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        before = time.perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            delta = time.perf_counter() - before
            meantime = painted_string(f"{delta:.6f}", "#FFFB00")
            log.timetracking(
                "%s executed, action took %s seconds",
                function.__qualname__,
                meantime,
                )

    return wrapper

def print_delta_time(function: Callable[P, R]) -> Callable[P, R]:
    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        before = time.perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            delta = time.perf_counter() - before
            meantime = painted_string(f"{delta:.6f}", "#FFFB00")
            print(
                "%s executed, action took %s seconds",
                function.__qualname__,
                meantime,
                )
    return wrapper


def first_point():
    point1 = time.perf_counter()

def second_point(point):
    point2 = time.perf_counter()
    log.timetracking(f"{point2 - point}")