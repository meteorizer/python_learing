import asyncio

async def set_after(future, delay, value):
    print(f"Sleeping for {delay} seconds.")
    await asyncio.sleep(delay)
    print(f"Setting future result to {value}.")
    future.set_result(value)

async def main():

    loop = asyncio.get_running_loop()
    future = loop.create_future()

    loop.create_task(set_after(future, 2, "Hello, there!"))

    result = await future
    print(result)

asyncio.run(main())