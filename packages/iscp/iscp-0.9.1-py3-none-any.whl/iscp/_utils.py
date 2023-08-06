import asyncio
from contextlib import suppress


def drain(q: asyncio.Queue):
    with suppress(asyncio.QueueEmpty):
        # drain
        while True:
            q.get_nowait()
            q.task_done()
