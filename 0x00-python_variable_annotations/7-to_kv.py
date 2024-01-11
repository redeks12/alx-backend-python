#!/usr/bin/env python3
"""0. Basic annotations - add"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """0. Basic annotations - add"""
    return tuple([k, float(v * v)])
