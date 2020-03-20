# Write an async python function
from datetime import datetime, timedelta
import heapq
import types
import time


class Task:

    def __init__(self, wait_until, coro):
        self.coro = coro
        self.waiting_until = wait_until

    def __eq__(self, other):
        return self.waiting_until == other.waiting_until

    def __lt__(self, other):
        return self.waiting_until < other.waiting_until


class SleepingLoop:
    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))
        while self._waiting:
            now = datetime.now()
            task = heapq.heappop(self._waiting)
            if now < task.waiting_until:
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds())
                now = datetime.now()
            try:
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                pass


@types.coroutine
def sleep(seconds):
    now = datetime.now()
    wait_until = now + timedelta(seconds=seconds)
    actual = yield wait_until
    return actual - now


async def countdown(label, delay=0):
    await sleep(delay)
    print(label, 'waiting', delay, 'seconds')


def main():
    loop = SleepingLoop(countdown('A', delay=1), countdown('B', delay=2),
                        countdown('c', delay=4), countdown('d', delay=8))
    start = datetime.now()
    loop.run_until_complete()
    print('Total elapsed time is', datetime.now() - start)


if __name__ == '__main__':
    main()