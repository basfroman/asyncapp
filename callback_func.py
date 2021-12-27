import asyncio
import random


def callback(result: asyncio.futures):
    print('result:', result.result())
    print('stop')
    asyncio.get_running_loop().stop()


async def start():
    print('start')
    await asyncio.sleep(1)
    print('middle')
    return random.randint(2, 5)


async def main():
    fut = asyncio.futures
    asyncio.create_task(start()).add_done_callback(callback)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
