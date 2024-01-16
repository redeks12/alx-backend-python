#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""
from random import uniform
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float]:
    """Write a coroutine called async_generator that takes no arguments."""

    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
