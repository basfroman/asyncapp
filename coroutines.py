import asyncio
import time
from concurrent.futures import Future


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    tasks = [
        asyncio.create_task(say_after(2, 'hello')),
        asyncio.create_task(say_after(2, 'world')),
        asyncio.create_task(say_after(1, '!!!'))
    ]

    print(asyncio.all_tasks())

    print(f"started at {time.strftime('%X')}")

    [await task for task in tasks]

    print(f"finished at {time.strftime('%X')}")

print('start')
asyncio.run(main(), debug=True)
print('end')


async def nested():
    return 42


async def main():
    # Ничего не произойдет, если мы просто вызовем "nested()".
    # Объект корутины создан, но не await,
    # так что *не будет работать вообще*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())


