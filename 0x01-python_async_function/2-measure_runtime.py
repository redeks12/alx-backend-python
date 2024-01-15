#!/usr/bin/env python3
"""
Curriculum
Short Specializations
Average: 118.3%
0x01. Python - Async """
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n
import time


def measure_time(n: int, max_index: int) -> float:
    """
    measure_time function
    """
    start = time.time()
    asyncio.run(wait_n(n, max_index))
    end = time.time()
    return (end - start) / n
