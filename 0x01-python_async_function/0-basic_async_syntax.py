#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): maximum delay to wait for (inclusive). Defaults to 10.

    Returns:
        float: the random delay waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
