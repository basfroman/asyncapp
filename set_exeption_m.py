import asyncio


async def bug():
    raise Exception("not consumed")


async def main():
    asyncio.create_task(bug())


# asyncio.run(main())
asyncio.run(main(), debug=True)
