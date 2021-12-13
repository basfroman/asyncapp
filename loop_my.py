import asyncio
import random
import time


async def async_print(value):
    await asyncio.sleep(0)
    print(value)


async def get_fib(num):
    if num < 3:
        return 1
    await asyncio.sleep(0)
    return await get_fib(num - 1) + await get_fib(num - 2)


async def run():
    await asyncio.sleep(0)
    print(await get_fib(random.randint(5, 30)))


async def start():
    await asyncio.gather(
        async_print('start'),
        run(),
        run(),
        run(),
        async_print('stop')
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())

    # loop.run_until_complete(async_print('start'))
    # loop.run_until_complete(run())
    # loop.run_until_complete(run())
    # loop.run_until_complete(run())
    # loop.run_until_complete(async_print('stop'))
