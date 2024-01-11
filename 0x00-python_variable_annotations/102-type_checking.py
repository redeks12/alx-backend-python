# !/usr/bin/env python3
"""0. Basic annotations - add"""
# filename: 102-type_checking.py

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """0. Basic annotations - add"""
    zoomed_in: Tuple = tuple([item for item in lst for i in range(factor)])
    return list(zoomed_in)


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)


print(zoom_array.__annotations__)
