#!/usr/bin/env python3
"""0. Basic annotations - add"""


def to_kv(k: str, v: int | float) -> tuple:
    return tuple([k, float(v * v)])
