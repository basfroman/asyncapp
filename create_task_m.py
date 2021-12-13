import asyncio


async def test_func(string: str):
    print(string)
    return string


async def main():
    z = asyncio.create_task(test_func("test"))
    print(f'return {z}')

if __name__ == "__main__":
    asyncio.run(main())
