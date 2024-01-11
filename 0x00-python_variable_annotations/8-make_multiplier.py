# !/usr/bin/env python3
"""0. Basic annotations - add"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multi(x: float) -> float:
        return x * multiplier

    return multi


make_multiplier = __import__("8-make_multiplier").make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
