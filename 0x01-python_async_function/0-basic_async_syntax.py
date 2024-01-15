#!/usr/bin/env python3
"""
Curriculum
Short Specializations
Average: 118.3%
0x01. Python - Async """


import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    """0. The basics of async"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
