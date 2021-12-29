import asyncio
import random


def callback(result: asyncio.futures):
    # do something with result
    print('result:', result)
    print('result.result():', result.result())


async def start():
    print('start')
    await asyncio.sleep(1)
    print('middle')
    return random.randint(2, 5)


async def main():
    tasks = [asyncio.create_task(start())]
    tasks[0].add_done_callback(callback)
    await asyncio.gather(*tasks, loop=loop)
    asyncio.get_running_loop().stop()
    print('stop')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon()
    loop.run_until_complete(main())
    loop.run_forever()
