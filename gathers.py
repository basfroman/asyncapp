import asyncio

z = None


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Запланировать дерево вызовов *конкурентно*:
    global z
    z = await asyncio.gather(
        factorial("A", -4),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

print(z)
