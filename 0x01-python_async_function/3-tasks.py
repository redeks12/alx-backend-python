#!/usr/bin/env python3
"""
Curriculum
Short Specializations
Average: 118.3%
0x01. Python - Async """
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_integer: int):
    '''Import wait_random from 0-basic_async_syntax.'''
    return asyncio.create_task(wait_random(max_integer))
