#!/usr/bin/env python3
"""0. Basic annotations - add"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """0. Basic annotations - add"""
    return [(i, len(i)) for i in lst]
