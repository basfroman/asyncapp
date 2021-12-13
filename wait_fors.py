import asyncio


async def eternity():
    # Спать в течение одного часа
    await asyncio.sleep(2)
    print('yay!')


async def main():
    # Подождите не более 1 секунды
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())


asyncio.as_completed()
