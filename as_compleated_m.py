import asyncio


async def counter(num: int):
    await asyncio.sleep(num)
    return f'number {num}'


async def main():
    cour_s = [counter(1), counter(2), counter(5)]

    for cour in asyncio.as_completed(cour_s):
        print(await cour)
        print(asyncio.current_task())


if __name__ == '__main__':
    asyncio.run(main())
