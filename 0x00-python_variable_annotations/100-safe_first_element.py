#!/usr/bin/env python3
"""0. Basic annotations - add"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """0. Basic annotations - add"""
    if lst:
        return lst[0]
    else:
        return None
