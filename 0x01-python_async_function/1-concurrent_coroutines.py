#!/usr/bin/env python3

from typing import List
from my_module import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times with specified max_delay.

    Args:
        n (int): number of times to spawn wait_random coroutine.
        max_delay (int): maximum delay to wait for (inclusive).

    Returns:
        List[float]: list of all the delays waited for (float values).
    """
    # Create a list to store the results of wait_random.
    delays = []

    # Spawn wait_random n times and store the resulting delays.
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Sort the list of delays in ascending order and return it.
    return sorted(delays)
