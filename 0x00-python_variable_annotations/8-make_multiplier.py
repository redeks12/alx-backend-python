#!/usr/bin/env python3
"""0. Basic annotations - add"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """0. Basic annotations - add"""

    def multi(x: float) -> float:
        return x * multiplier

    return multi
